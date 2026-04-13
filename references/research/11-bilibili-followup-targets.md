# 王心凌 - Bilibili 后续优先目标

> 调研时间：2026-04-11
> 来源：`references/research/10-bilibili-batch-harvest.md`

## 这轮广搜之后的判断

批量脚本已经把一批 B 站候选视频跑过了，结果很明确：

- 和王心凌相关的视频很多
- 但真正带 `ai-zh` 字幕、能直接自动转 transcript 的并不多
- 旧思路里最优先的两条无字幕目标已经验证过多次，继续复查收益很低
- 新一轮更有效的做法，是跳过已确认无字幕的旧目标，把搜索火力集中到新的发言型候选上

## 状态更新

- 2026-04-11 复查后，`BV18z4y1L71H` 已经可以通过 `yt-dlp + cookies.txt` 拉到 `ai-zh`。
- 已新增：
  - `sources/transcripts/BV18z4y1L71H.ai-zh.srt`
  - `sources/transcripts/BV18z4y1L71H_transcript.txt`
- 因此它不再属于“高价值无字幕待处理”清单，后续重点应转向其余仍无字幕的视频。
- 同日继续按 `yt-dlp --list-subs` 逐条复查 4 个指定目标后，状态更新为：
  - `BV1HeYizrEyu`：仍为 `danmaku`
  - `BV1C44y1975q`：仍为 `danmaku`
  - `BV1My4y1F7iD`：已出现 `ai-zh`，并新增 `sources/transcripts/BV1My4y1F7iD.ai-zh.srt` 与 `sources/transcripts/BV1My4y1F7iD_transcript.txt`
  - `BV1i341167kX`：已出现 `ai-zh`，并新增 `sources/transcripts/BV1i341167kX.ai-zh.srt` 与 `sources/transcripts/BV1i341167kX_transcript.txt`
- 在按新策略跑窄搜后，又新增了以下 `ai-zh` transcript：
  - `BV1za411A7Js`
  - `BV1df4y1Z7EB`
  - `BV1qkMezcEys`
  - `BV1U8N9zFE56`
  - `BV1PU4y1q7Bc`
- 用户已明确判断 `BV1C44y1975q` 与 `BV1HeYizrEyu` 对当前项目“完全没有价值”。
- 因此这两条不再是“冻结待观察”，而是直接从候选池中移除：
  - 不再复查字幕
  - 不再进入优先列表
  - 不再作为下一轮参考目标

## 弃用目标：从当前项目候选池移除

### 1. 2023 新京报专访：王心凌的甜美进化论

- BVID: `BV1C44y1975q`
- 当前状态：弃用
- 说明：
  - 已有 `references/research/13-round5-bjnews-video-text-crosscheck.md` 作为文本替身
  - 当前项目不再需要这条视频补层

### 2. 北京站 D2 完整版 Talking

- BVID: `BV1HeYizrEyu`
- 当前状态：弃用
- 说明：
  - 当前项目不再把它视为值得投入的现场口语素材
  - 后续不再为它安排自动或人工转写

## 第一优先级：本轮已命中的新 transcript

### 1. 风芒娱乐专访

- BVID: `BV1PU4y1q7Bc`
- 当前状态：已拿到 `ai-zh` 与 transcript
- 价值：
  - 访谈时长长，发言密度高
  - 适合补公开自我解释、宣传期表达与采访口语层

### 2. 郑州 Day2 talking

- BVID: `BV1qkMezcEys`
- 当前状态：已拿到 `ai-zh` 与 transcript
- 价值：
  - 纯现场说话感更强
  - 适合补演唱会 talking 的接梗、翻牌、现场互动节奏

### 3. 杭州 Day2 talking

- BVID: `BV1U8N9zFE56`
- 当前状态：已拿到 `ai-zh` 与 transcript
- 价值：
  - 也是直接的现场口语材料
  - 可以和郑州 talking 互相对照，看哪些互动方式是稳定的

### 4. 2021 记者会全程直播

- BVID: `BV1za411A7Js`
- 当前状态：已拿到 `ai-zh` 与 transcript
- 价值：
  - 记者会型长视频
  - 适合补“公开答问”和较完整的活动口语组织方式

### 5. 私心线上音乐会完整版

- BVID: `BV1df4y1Z7EB`
- 当前状态：已拿到 `ai-zh` 与 transcript
- 价值：
  - 适合补唱段之间的说话方式和公开陪伴感

### 6. 2016 演唱会五位男主合唱片段

- BVID: `BV1Ps411b7dc`
- 当前状态：已拿到 `ai-zh` 与 transcript
- 价值：
  - 有现场感谢、嘉宾互动和演唱会收尾口气
  - 对“舞台上怎么谢人、怎么接嘉宾话头”有补充价值
  - 但整体仍偏节目段落，不如专访和 talking 密度高

### 7. 2006 No.1 庆功演唱会完整版

- BVID: `BV1hf9AYBEy4`
- 当前状态：已拿到 `ai-zh` 与 transcript
- 价值：
  - 能补早年舞台口气、早期感谢方式和公开脆弱表达
  - 适合做纵向时间线对照
  - 但歌唱段落占比很高，消费时要重点抓说话段和收尾感言

### 8. 2006 No.1 庆功演唱会另一版

- BVID: `BV19B4y1M7qQ`
- 当前状态：已拿到 `ai-zh` 与 transcript
- 价值：
  - 与 `BV1hf9AYBEy4` 高度重合
  - 更适合作为互相校对版本，而不是单独高优先主素材

### 9. A-Lin 合唱官摄

- BVID: `BV1o7DYB2ESW`
- 当前状态：已拿到 `ai-zh` 与 transcript
- 价值：
  - 主要是歌曲和短开场
  - 几乎不提供新的访谈层或 talking 层信息
  - 归档即可，当前研究优先级低

## 第二优先级：仍可继续尝试的新候选

### 1. 其他 talking / 幕后候选

- `BV1ktVhzrEjy`
- `BV1YfcsbMEm8`

价值：

- 仍可保留作补池
- 但优先级低于已经落地并确认有内容的 transcript

## 推荐顺序

1. `BV1PU4y1q7Bc`
2. `BV1qkMezcEys`
3. `BV1U8N9zFE56`
4. `BV1za411A7Js`
5. `BV1df4y1Z7EB`
6. `BV1Ps411b7dc`
7. `BV1hf9AYBEy4`
8. `BV19B4y1M7qQ`

## 结论

本轮已经验证了新的策略更有效：

- 不再围绕已被用户判定无价值的旧目标内耗
- 可用的 B 站素材仍然存在，而且已经继续扩出 4 条新 transcript
- 但它们的价值并不平均：
  - `BV1Ps411b7dc`、`BV1hf9AYBEy4` 还有继续消费的空间
  - `BV19B4y1M7qQ` 更像校对版本
  - `BV1o7DYB2ESW` 当前更适合归档，而不是重点深挖

## 工作室主页状态更新

2026-04-12 继续推进王心凌工作室主页后，状态已经进一步变化：

- 第一梯队 5 条已全部命中 `ai-zh`
- 并且都已经新增 `.ai-zh.srt` 与 `*_transcript.txt`
- 因此它们不再属于“follow-up 待验证”目标

已完成的第一梯队：

- `BV17mZ7B4EyA`
- `BV1JNkeBKEfM`
- `BV1mNixBrECT`
- `BV1SkTkzuE4Q`
- `BV1uXEEzvEJA`

下一轮如果继续深挖工作室主页，应直接前推第二梯队：

- `BV1Sc2vBaEyp`
- `BV1MpqhBbEqg`
- `BV17Sgrz4EfJ`
- `BV1niKczuEBp`
- `BV1XML1zBEHf`

也就是说，当前项目里的 follow-up 逻辑已经变成：

- 不回头试旧无字幕废目标
- 不重复验证已命中的工作室第一梯队
- 直接把工作室第二梯队当作新的字幕探测主战场
