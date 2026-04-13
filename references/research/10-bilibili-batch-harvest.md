# 王心凌 - Bilibili 批量语料采集

> 调研时间：2026-04-11 16:01:20 UTC
> 搜索词：王心凌 看板人物, 王心凌 记者会, 王心凌 演唱会 幕后, 王心凌 演唱会 庆功, 王心凌 talking, 王心凌 专访
> 策略说明：本轮按新策略跳过已确认无字幕的 `BV1HeYizrEyu` 与 `BV1C44y1975q`，集中搜索新的发言型 `ai-zh` 命中。

## 本轮结果摘要

- 新增可直接消费的 transcript：
  - `BV1za411A7Js_transcript.txt`
  - `BV1df4y1Z7EB_transcript.txt`
  - `BV1qkMezcEys_transcript.txt`
  - `BV1U8N9zFE56_transcript.txt`
  - `BV1PU4y1q7Bc_transcript.txt`
- 这轮命中的高价值方向比上一轮更集中在：
  - `记者会`
  - `talking`
  - `专访`
- 说明脚本的窄搜策略是有效的，下一轮应优先消费这批新 transcript，而不是回头重复试无字幕旧目标。

| BVID | 标题 | 搜索词 | 字幕 | Transcript |
|---|---|---|---|---|
| `BV1My4y1F7iD` | 【王心凌 看板人物 完整版】 | `王心凌 看板人物` | `ai-zh, danmaku` | `BV1My4y1F7iD_transcript.txt` |
| `BV1i341167kX` | 王心凌2012年记者会回应小三传闻 | `王心凌 记者会` | `ai-zh, danmaku` | `BV1i341167kX_transcript.txt` |
| `BV1za411A7Js` | 【王心凌】《CYNDILOVES2SING 爱。心凌巡回演唱会 2021旗舰版》记者会全程直播 | `王心凌 记者会` | `ai-zh, danmaku` | `BV1za411A7Js_transcript.txt` |
| `BV1df4y1Z7EB` | 【王心凌】王心凌《「私·心」线上音乐会》高清完整版 | `王心凌 记者会` | `ai-zh, danmaku` | `BV1df4y1Z7EB_transcript.txt` |
| `BV1o7DYB2ESW` | 【A-Lin X 王心凌】《爱你》歌迹Journey世界巡回演唱会-上海站丨官摄 | `王心凌 演唱会 幕后` | `ai-zh, danmaku` | `BV1o7DYB2ESW_transcript.txt` |
| `BV1Ps411b7dc` | 王心凌2016演唱會与明道 张栋梁 辰亦儒 孙协志 坤达五位男主合唱  20160107 完全娛樂 | `王心凌 演唱会 幕后` | `ai-zh, danmaku` | `BV1Ps411b7dc_transcript.txt` |
| `BV1hf9AYBEy4` | 【DVD】【台湾】原生60fps \| 王心凌 - 2006 No.1 庆功演唱会 - 6.49GB | `王心凌 演唱会 庆功` | `ai-zh, danmaku` | `BV1hf9AYBEy4_transcript.txt` |
| `BV19B4y1M7qQ` | 【1080p】王心凌 - 2006 Cyndi with U No.1庆功演唱会 甜心教主的巅峰表演 | `王心凌 演唱会 庆功` | `ai-zh, danmaku` | `BV19B4y1M7qQ_transcript.txt` |
| `BV1ktVhzrEjy` | 王心凌：其实里面好多层，你们其实是看不到的！但也要保护我哦！ | `王心凌 talking` | `danmaku` | `` |
| `BV1qkMezcEys` | 王心凌郑州DAy2小品天后 talking | `王心凌 talking` | `ai-zh, danmaku` | `BV1qkMezcEys_transcript.txt` |
| `BV1U8N9zFE56` | 王心凌｜2.0杭州站Day2 Talking｜翻牌子根本念不完～ | `王心凌 talking` | `ai-zh, danmaku` | `BV1U8N9zFE56_transcript.txt` |
| `BV18z4y1L71H` | 方念华专访王心凌：从容自在地乘风破浪 2023.09.17 | `王心凌 专访` | `ai-zh, danmaku` | `BV18z4y1L71H_transcript.txt` |
| `BV1PU4y1q7Bc` | 【王心凌】《风芒娱乐》王心凌采访高清完整版 | `王心凌 专访` | `ai-zh, danmaku` | `BV1PU4y1q7Bc_transcript.txt` |

## 工作室主页定点探测补记

> 更新：2026-04-12
> 来源：`https://space.bilibili.com/3546644630997630`
> 说明：本轮不是再跑广搜，而是直接对工作室首页第一梯队 5 条视频做 `--list-subs` 和落盘。

### 结果摘要

- 第一梯队 5 条工作室视频全部命中 `ai-zh`
- 说明工作室主页当前是命中率很高的可用素材池
- 这 5 条不应再留到“下一轮再消费”
- 下一轮应该直接前推第二梯队，而不是回头重试这 5 条

| BVID | 标题 | 来源 | 字幕 | Transcript |
|---|---|---|---|---|
| `BV17mZ7B4EyA` | 【王心凌】来自Sugar Land的最后一封情书💌 \| SUGAR HIGH2.0 世界巡回演唱会最终章 | `王心凌工作室首页` | `ai-zh, danmaku` | `BV17mZ7B4EyA_transcript.txt` |
| `BV1JNkeBKEfM` | 【王心凌】这视频加了催泪弹吗🥹 \| SUGAR HIGH2.0 世界巡回演唱会上海站 vlog | `王心凌工作室首页` | `ai-zh, danmaku` | `BV1JNkeBKEfM_transcript.txt` |
| `BV1mNixBrECT` | 【王心凌】重生之在演唱会帮人求婚😏 \| SUGAR HIGH2.0世界巡回演唱会武汉站vlog | `王心凌工作室首页` | `ai-zh, danmaku` | `BV1mNixBrECT_transcript.txt` |
| `BV1SkTkzuE4Q` | 【王心凌】送给你们「不匿名」的安慰 \| SUGAR HIGH2.0世界巡回演唱会苏州站vlog | `王心凌工作室首页` | `ai-zh, danmaku` | `BV1SkTkzuE4Q_transcript.txt` |
| `BV1uXEEzvEJA` | 【王心凌】演唱会舞台爆改魔术现场🪄 \| SUGAR HIGH2.0世界巡回演唱会南昌站vlog | `王心凌工作室首页` | `ai-zh, danmaku` | `BV1uXEEzvEJA_transcript.txt` |

### 当前价值判断

- `BV17mZ7B4EyA`：最高优先，兼具 backstage 口语、事故处理、团队默契和最终章定义
- `BV1SkTkzuE4Q`：最高优先，补到当前歌迷关系表述和“双向奔赴”
- `BV1JNkeBKEfM`：高优先，补到巡演收尾的轻安抚口气
- `BV1mNixBrECT`：中高优先，补到求婚和临场共享人生节点
- `BV1uXEEzvEJA`：中等优先，补到舞台惊喜和轻 backstage 口语
