#!/usr/bin/env python3
"""
将 SRT/VTT 字幕文件清洗为干净的纯文本 transcript。

用法:
    python3 srt_to_transcript.py input.srt [output.txt]
    python3 srt_to_transcript.py input.vtt [output.txt]
"""

from __future__ import annotations

import re
import sys
from pathlib import Path


def clean_srt(content: str) -> str:
    lines = content.strip().split("\n")
    texts: list[str] = []

    for line in lines:
        line = line.strip()
        if re.match(r"^\d+$", line):
            continue
        if re.match(r"\d{2}:\d{2}:\d{2}", line):
            continue
        if not line:
            continue
        line = re.sub(r"<[^>]+>", "", line)
        line = re.sub(r"align:.*$|position:.*$", "", line).strip()
        if line:
            texts.append(line)

    deduped: list[str] = []
    for text in texts:
        if not deduped or text != deduped[-1]:
            deduped.append(text)

    result: list[str] = []
    current: list[str] = []
    for text in deduped:
        current.append(text)
        joined = " ".join(current)
        if len(joined) > 200 or re.search(r"[。！？.!?]$", text):
            result.append(joined)
            current = []

    if current:
        result.append(" ".join(current))

    return "\n\n".join(result)


def clean_vtt(content: str) -> str:
    content = re.sub(r"^WEBVTT.*?\n\n", "", content, flags=re.DOTALL)
    content = re.sub(r"NOTE.*?\n\n", "", content, flags=re.DOTALL)
    return clean_srt(content)


def main() -> int:
    if len(sys.argv) < 2:
        print("用法: python3 srt_to_transcript.py <input.srt|input.vtt> [output.txt]")
        return 1

    input_path = Path(sys.argv[1])
    if not input_path.exists():
        print(f"❌ 文件不存在: {input_path}")
        return 1

    if len(sys.argv) >= 3:
        output_path = Path(sys.argv[2])
    else:
        output_path = input_path.parent / f"{input_path.stem}_transcript.txt"

    content = input_path.read_text(encoding="utf-8")
    if input_path.suffix.lower() == ".vtt" or content.startswith("WEBVTT"):
        transcript = clean_vtt(content)
    else:
        transcript = clean_srt(content)

    output_path.write_text(transcript, encoding="utf-8")
    print(f"✅ 转换完成: {output_path}")
    print(f"   字数: {len(transcript)}  段落数: {transcript.count(chr(10)) + 1}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
