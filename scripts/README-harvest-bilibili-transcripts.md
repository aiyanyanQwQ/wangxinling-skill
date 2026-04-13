# Bilibili 批量字幕采集脚本说明

Updated: 2026-04-11

Script path:

- `scripts/harvest_bilibili_transcripts.py`

Related helper:

- `scripts/srt_to_transcript.py`

Important packaging note:

- 分发版 skill 不包含 `cookies.txt`
- 下文统一用示例变量：
  - `SKILL_DIR=/path/to/cyndiwang.skill`
  - `COOKIE_FILE=/path/to/cookies.txt`
  - `YT_DLP=/path/to/yt-dlp`（如果 `yt-dlp` 已在 `PATH` 中，可直接写 `yt-dlp`）

## 1. 这是什么

这个脚本用于批量搜索 B 站王心凌相关视频，检查视频是否有可下载的 `ai-zh` 字幕，如果有，就自动：

1. 下载字幕
2. 转成纯文本 transcript
3. 更新视频卡片
4. 写批量采集报告

它适合做：

- 新一轮广搜
- 按主题重跑一轮候选池
- 验证某批视频现在是否新放出了 AI 字幕

它不适合做：

- 逐字级人工校对
- 只看网页播放页、不落任何文件的临时试探
- 复杂人工筛选后的精读分析

## 2. 依赖与前提

### 必需前提

- 有可用的 B 站登录态 cookie
- `yt-dlp` 可用
- Python 可用

### 推荐约定

- `SKILL_DIR=/path/to/cyndiwang.skill`
- `COOKIE_FILE=/path/to/cookies.txt`
- `YT_DLP=yt-dlp`

### 重要提醒

- 不要默认系统全局就有 `yt-dlp`
- 如果你是通过虚拟环境安装的 `yt-dlp`，先激活对应环境；否则确保 `yt-dlp` 已在 `PATH` 中

```bash
export SKILL_DIR=/path/to/cyndiwang.skill
export COOKIE_FILE=/path/to/cookies.txt
export YT_DLP=yt-dlp
```

## 3. 脚本现在的真实行为

当前逻辑是：

1. 用 B 站搜索页 HTML 抓取 `BV` 号
2. 用 `x/web-interface/view` 补标题、作者、时长、描述
3. 用 `yt-dlp --list-subs` 探测字幕语言
4. 如果命中 `ai-zh`，则下载 `.srt`
5. 用 `scripts/srt_to_transcript.py` 转成 `*_transcript.txt`
6. 更新：
   - `sources/video_notes/`
   - `sources/transcripts/`
   - `references/research/10-bilibili-batch-harvest.md`

## 4. 为什么不用旧逻辑

之前脚本用的是：

- `yt-dlp -j`
- 再读取返回 JSON 里的 `subtitles` / `automatic_captions`

这个逻辑在 B 站上不稳定，实测会出现：

- `--list-subs` 明明能看到 `ai-zh`
- `-j` 返回却是空字幕字段

所以会误判成 `none`。

现在已经改成优先用：

```bash
yt-dlp --list-subs
```

来判定字幕语言，这和手动看到的 B 站结果更一致。

## 5. 另一个已修复的问题

旧脚本里 `--download-limit` 曾经按“已记录条目数”截断，而不是按“已下载条目数”截断。

结果会导致：

- 前面候选很多
- 即使前面大多没字幕
- 后面真正有 `ai-zh` 的视频也可能被跳过

现在已经修成按“成功下载并转写的条目数”计数。

## 6. 基本用法

### 查看帮助

```bash
python "$SKILL_DIR/scripts/harvest_bilibili_transcripts.py" --help
```

### 用默认搜索词跑一轮

```bash
python "$SKILL_DIR/scripts/harvest_bilibili_transcripts.py" \
  --skill-dir "$SKILL_DIR" \
  --cookies "$COOKIE_FILE"
```

### 跑“发言类素材” focused batch

```bash
python "$SKILL_DIR/scripts/harvest_bilibili_transcripts.py" \
  --skill-dir "$SKILL_DIR" \
  --cookies "$COOKIE_FILE" \
  --queries \
    '王心凌 方念华 专访' \
    '王心凌 新京报 专访' \
    '王心凌 台北 媒体群访' \
    '王心凌 北京 talking' \
    '王心凌 看板人物' \
    '王心凌 记者会' \
  --pages 1 \
  --per-query-limit 5 \
  --download-limit 8
```

### 跑某一个窄主题

```bash
python "$SKILL_DIR/scripts/harvest_bilibili_transcripts.py" \
  --skill-dir "$SKILL_DIR" \
  --cookies "$COOKIE_FILE" \
  --queries '王心凌 方念华 专访' '王心凌 新京报 专访' \
  --pages 1 \
  --per-query-limit 2 \
  --download-limit 2
```

## 7. 参数说明

### `--skill-dir`

项目根目录。

传 skill 根目录，例如：

- `/path/to/cyndiwang.skill`

### `--cookies`

B 站 cookies 文件。

传你的 B 站 cookies 文件，例如：

- `/path/to/cookies.txt`

### `--queries`

搜索词列表。建议优先用：

- 明确内容类型
- 明确场景
- 明确媒体名

比方说：

- `王心凌 方念华 专访`
- `王心凌 台北 媒体群访`
- `王心凌 记者会`
- `王心凌 talking`

不建议太泛的词：

- `王心凌`
- `王心凌 广州站`
- `王心凌 Sugar High`

太泛容易把：

- 饭拍
- MV
- 切片
- AI 二创
- 其他艺人同节目视频

一起带进来。

### `--pages`

搜索页页数。默认 `1`。

建议：

- 先 `1`
- 真不够再加

### `--per-query-limit`

每个搜索词最多保留多少候选。

建议：

- 发言类精搜：`3-6`
- 广搜：`8-12`

### `--download-limit`

最多成功下载多少条带 `ai-zh` 的视频。

当前已经修复为：

- 按“成功转写的条目数”计数
- 不是按“记录条目数”计数

## 8. 输出文件在哪里

### 1. 批量报告

- `references/research/10-bilibili-batch-harvest.md`

### 2. 视频卡片

- `sources/video_notes/*.md`

### 3. 字幕

- `sources/transcripts/*.ai-zh.srt`

### 4. 转写文本

- `sources/transcripts/*_transcript.txt`

## 9. 如何判断这轮有没有真正命中

不要只看脚本跑完，要看三个地方：

### A. 批量报告

看：

- `字幕` 列是否出现 `ai-zh`
- `Transcript` 列是否有文件名

### B. `sources/transcripts/`

看是否新增：

- `*.ai-zh.srt`
- `*_transcript.txt`

### C. 对应视频卡片

看 `Subtitle Status` 是否被更新为：

- `ai-zh, danmaku`
- 或至少包含 `ai-zh`

## 10. 如何做最小验证

如果怀疑脚本又错了，不要直接信报告，先手工对照：

### 已知有 `ai-zh` 的例子

- `BV18z4y1L71H`
- `BV1xD4y1L7pS`
- `BV1e9muYyEzA`
- `BV18iVnzxEiz`

### 已知当前只有 `danmaku` 的例子

- `BV1C44y1975q`

### 对照命令

```bash
yt-dlp --cookies "$COOKIE_FILE" --list-subs https://www.bilibili.com/video/BV18z4y1L71H/
yt-dlp --cookies "$COOKIE_FILE" --list-subs https://www.bilibili.com/video/BV1C44y1975q/
```

如果这里和脚本报告不一致，先修脚本，不要继续基于错误结果分析。

## 11. 当前已知限制

### 1. 搜索结果会混入噪音

即使查询写得比较准，也可能混入：

- 同主持人采访别的艺人
- 同节目不同期
- AI 二创
- 饭拍切片
- 标题碰词但内容不值钱的条目

所以批量报告只是“候选池”，不是“已验证高价值池”。

### 2. `--list-subs` 本身也慢

脚本现在更准确了，但会更慢，因为每条候选都要额外跑一次字幕探测。

所以实际建议是：

- 先缩查询
- 再提高精准度

不要一上来就跑很大的词池。

### 3. B 站字幕状态会变化

有些视频一开始没有 `ai-zh`，后面会出现。

所以：

- 老候选值得重跑
- 旧报告不是最终真相

### 4. 会拉到非王心凌视频

比如查 `王心凌 方念华 专访` 时，可能同时命中同一主持人的其他专访。

这是正常现象，需要后续人工筛掉。

## 12. 推荐跑法

### 跑法 A：精搜发言素材

适合下一轮继续补：

- 专访
- 看板人物
- 群访
- 记者会
- talking

建议参数：

- `--pages 1`
- `--per-query-limit 3-5`
- `--download-limit 4-8`

### 跑法 B：周期性复查旧候选

适合验证之前没字幕的视频现在有没有新放出 `ai-zh`。

建议重点复查：

- `BV1C44y1975q`
- `BV1HeYizrEyu`
- `BV1My4y1F7iD`
- `BV1i341167kX`

### 跑法 C：大范围扩池

只在你明确想扩候选池时才做。

做完后一定要：

- 手工筛一遍 `video_notes`
- 重新整理 `11-bilibili-followup-targets.md`

## 13. 下一轮 Codex 应该怎么做

下一轮如果要继续用这个脚本，建议顺序是：

1. 先读本文件
2. 再看当前批量报告
3. 再看 `sources/transcripts/` 是否已有新增
4. 然后决定：
   - 是继续扩池
   - 还是优先消费已有 transcript

不要一上来就盲跑广搜。

## 14. 这份说明和正式 skill 的关系

本文件是：

- 脚本操作说明
- 故障排查说明
- 下一轮重跑指南

如果后续 Codex 需要再次运行批量脚本，应该在执行前先读本文件，再决定：

- 是继续扩池
- 还是优先消费已有 transcript
