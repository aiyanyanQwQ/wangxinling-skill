#!/usr/bin/env python3
"""
Search Bilibili for Wang Xinling related videos, detect ai-zh subtitles via yt-dlp,
download subtitle files, convert them to transcripts, and write a markdown harvest report.

Usage:
  python3 scripts/harvest_bilibili_transcripts.py \
    --skill-dir /path/to/cyndiwang.skill \
    --cookies /path/to/cookies.txt
"""

from __future__ import annotations

import argparse
import html
import json
import re
import shutil
import subprocess
import sys
import time
import urllib.parse
import urllib.request
from dataclasses import dataclass
from datetime import datetime, UTC
from pathlib import Path


DEFAULT_QUERIES = [
    "王心凌 采访 完整版",
    "王心凌 专访",
    "王心凌 演唱会 talking",
    "王心凌 演唱会 庆功",
    "王心凌 演唱会 幕后",
    "王心凌 纪录片",
    "王心凌 乘风 采访",
    "王心凌 Sugar High",
]


def clean_html(text: str) -> str:
    return re.sub(r"<[^>]+>", "", html.unescape(text or "")).strip()


def fetch_json(url: str) -> dict:
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": "Mozilla/5.0",
            "Referer": "https://www.bilibili.com/",
        },
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode("utf-8", errors="ignore"))


def fetch_text(url: str) -> str:
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": "Mozilla/5.0",
            "Referer": "https://www.bilibili.com/",
        },
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        return resp.read().decode("utf-8", errors="ignore")


@dataclass
class Candidate:
    bvid: str
    title: str
    author: str
    duration: str
    pubdate: int
    description: str
    query: str


def search_bilibili(query: str, page: int = 1) -> list[Candidate]:
    params = urllib.parse.urlencode({"keyword": query, "page": page})
    page_html = fetch_text(f"https://search.bilibili.com/all?{params}")
    bvids = []
    seen = set()
    for bvid in re.findall(r"BV[0-9A-Za-z]{10}", page_html):
        if bvid in seen:
            continue
        seen.add(bvid)
        bvids.append(bvid)
    candidates = []
    for bvid in bvids:
        item = view_metadata(bvid)
        if not item:
            continue
        candidates.append(
            Candidate(
                bvid=bvid,
                title=clean_html(item.get("title", "")),
                author=item.get("owner", {}).get("name", ""),
                duration=str(item.get("duration", "")),
                pubdate=int(item.get("pubdate") or 0),
                description=clean_html(item.get("desc", "")),
                query=query,
            )
        )
    return candidates


def view_metadata(bvid: str) -> dict | None:
    data = fetch_json(f"https://api.bilibili.com/x/web-interface/view?bvid={bvid}")
    return data.get("data")


def run_cmd(args: list[str], cwd: Path | None = None) -> subprocess.CompletedProcess:
    try:
        return subprocess.run(
            args,
            cwd=str(cwd) if cwd else None,
            text=True,
            capture_output=True,
            check=False,
            timeout=45,
        )
    except subprocess.TimeoutExpired:
        return subprocess.CompletedProcess(args=args, returncode=124, stdout="", stderr="timeout")


def yt_metadata(yt_dlp: Path, cookies: Path, url: str) -> dict | None:
    proc = run_cmd(
        [str(yt_dlp), "--cookies", str(cookies), "--socket-timeout", "20", "-j", url]
    )
    if proc.returncode != 0 or not proc.stdout.strip():
        return None
    try:
        return json.loads(proc.stdout)
    except json.JSONDecodeError:
        return None


def subtitle_langs(meta: dict) -> list[str]:
    langs = set()
    for source in (meta.get("subtitles") or {}, meta.get("automatic_captions") or {}):
        langs.update(source.keys())
    return sorted(langs)


def probe_subtitle_langs(yt_dlp: Path, cookies: Path, url: str) -> list[str]:
    proc = run_cmd(
        [str(yt_dlp), "--cookies", str(cookies), "--socket-timeout", "20", "--list-subs", url]
    )
    if proc.returncode != 0:
        return []

    langs: list[str] = []
    for line in proc.stdout.splitlines():
        line = line.strip()
        if not line or line.startswith("["):
            continue
        if line.startswith("Language ") or line.startswith("Formats"):
            continue
        match = re.match(r"^([A-Za-z0-9-]+)\s+\S+", line)
        if match:
            langs.append(match.group(1))
    return sorted(set(langs))


def download_subtitle(yt_dlp: Path, cookies: Path, url: str, out_dir: Path) -> Path | None:
    before = {p.name for p in out_dir.glob("*.srt")}
    proc = run_cmd(
        [
            str(yt_dlp),
            "--cookies",
            str(cookies),
            "--socket-timeout",
            "20",
            "--write-subs",
            "--sub-langs",
            "ai-zh",
            "--sub-format",
            "srt",
            "--skip-download",
            "-o",
            str(out_dir / "%(id)s.%(ext)s"),
            url,
        ]
    )
    if proc.returncode != 0:
        return None
    after = {p.name for p in out_dir.glob("*.srt")}
    new_files = sorted(after - before)
    if new_files:
        return out_dir / new_files[-1]
    # fallback if file existed already
    match = sorted(out_dir.glob("*.ai-zh.srt"), key=lambda p: p.stat().st_mtime, reverse=True)
    return match[0] if match else None


def convert_transcript(py: str, converter: Path, srt_path: Path, transcript_path: Path) -> bool:
    proc = run_cmd([py, str(converter), str(srt_path), str(transcript_path)])
    return proc.returncode == 0 and transcript_path.exists()


def update_video_note(
    skill_dir: Path,
    candidate: Candidate,
    meta: dict,
    transcript_path: Path | None,
    subtitle_languages: list[str],
) -> None:
    notes_dir = skill_dir / "sources" / "video_notes"
    notes_dir.mkdir(parents=True, exist_ok=True)
    slug = re.sub(r"[^a-z0-9-]+", "-", f"bilibili-{candidate.bvid.lower()}-{candidate.title.lower()}").strip("-")
    slug = re.sub(r"-{2,}", "-", slug)[:120]
    note_path = notes_dir / f"{slug}.md"
    published = (
        datetime.fromtimestamp(candidate.pubdate, UTC).strftime("%Y-%m-%d %H:%M:%S UTC")
        if candidate.pubdate
        else "unknown"
    )
    title = meta.get("title") or candidate.title
    duration = meta.get("duration") or candidate.duration
    owner = (meta.get("uploader") or candidate.author or "").strip()
    langs = ", ".join(subtitle_languages) or "none"
    transcript_line = f"- Transcript: `{transcript_path.name}`\n" if transcript_path else ""
    content = f"""# Video Note: {candidate.bvid}

## Basic Info

- Platform: Bilibili
- URL: `https://www.bilibili.com/video/{candidate.bvid}/`
- Title: `{title}`
- Uploader: `{owner}`
- Published: `{published}`
- Duration: `{duration}`
- Search Query: `{candidate.query}`

## Subtitle Status

- Subtitle languages: `{langs}`
{transcript_line}## Search Description

{candidate.description or 'No description available.'}
"""
    note_path.write_text(content, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--skill-dir", required=True)
    parser.add_argument("--cookies", required=True)
    parser.add_argument("--queries", nargs="*", default=DEFAULT_QUERIES)
    parser.add_argument("--pages", type=int, default=1)
    parser.add_argument("--per-query-limit", type=int, default=12)
    parser.add_argument("--download-limit", type=int, default=8)
    args = parser.parse_args()

    skill_dir = Path(args.skill_dir)
    cookies = Path(args.cookies)
    if not skill_dir.exists():
        parser.error(f"--skill-dir does not exist: {skill_dir}")
    if not cookies.is_file():
        parser.error(f"--cookies file not found: {cookies}")
    yt_dlp_bin = shutil.which("yt-dlp")
    if yt_dlp_bin:
        yt_dlp = Path(yt_dlp_bin)
    else:
        parser.error("yt-dlp not found in PATH")
    py = sys.executable
    converter = Path(__file__).with_name("srt_to_transcript.py")
    transcripts_dir = skill_dir / "sources" / "transcripts"
    transcripts_dir.mkdir(parents=True, exist_ok=True)

    seen: set[str] = set()
    candidates: list[Candidate] = []
    for query in args.queries:
        for page in range(1, args.pages + 1):
            for item in search_bilibili(query, page=page)[: args.per_query_limit]:
                if item.bvid in seen:
                    continue
                seen.add(item.bvid)
                candidates.append(item)
        time.sleep(0.2)

    harvested = []
    downloaded_count = 0
    for candidate in candidates:
        url = f"https://www.bilibili.com/video/{candidate.bvid}/"
        meta = yt_metadata(yt_dlp, cookies, url)
        if not meta:
            continue
        langs = probe_subtitle_langs(yt_dlp, cookies, url)
        if not langs:
            langs = subtitle_langs(meta)
        transcript_path = None
        if "ai-zh" in langs and downloaded_count < args.download_limit:
            srt_path = download_subtitle(yt_dlp, cookies, url, transcripts_dir)
            if srt_path:
                transcript_path = transcripts_dir / f"{candidate.bvid}_transcript.txt"
                if convert_transcript(py, converter, srt_path, transcript_path):
                    downloaded_count += 1
        update_video_note(skill_dir, candidate, meta, transcript_path, langs)
        harvested.append(
            {
                "bvid": candidate.bvid,
                "title": meta.get("title") or candidate.title,
                "query": candidate.query,
                "author": meta.get("uploader") or candidate.author,
                "duration": meta.get("duration") or candidate.duration,
                "pubdate": candidate.pubdate,
                "subtitle_langs": langs,
                "transcript": transcript_path.name if transcript_path and transcript_path.exists() else "",
            }
        )
        time.sleep(0.2)

    report_path = skill_dir / "references" / "research" / "10-bilibili-batch-harvest.md"
    lines = [
        "# 王心凌 - Bilibili 批量语料采集",
        "",
        f"> 调研时间：{datetime.now(UTC).strftime('%Y-%m-%d %H:%M:%S UTC')}",
        f"> 搜索词：{', '.join(args.queries)}",
        "",
        "| BVID | 标题 | 搜索词 | 字幕 | Transcript |",
        "|---|---|---|---|---|",
    ]
    for item in harvested:
        title = item["title"].replace("|", "\\|")
        langs = ", ".join(item["subtitle_langs"]) or "none"
        transcript = item["transcript"] or ""
        lines.append(
            f"| `{item['bvid']}` | {title} | `{item['query']}` | `{langs}` | `{transcript}` |"
        )
    report_path.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(f"Wrote report: {report_path}")
    print(f"Candidates checked: {len(candidates)}")
    print(f"Entries recorded: {len(harvested)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
