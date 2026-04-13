<div align="center">

# 王心凌.skill

### CyndiWang.skill

> *把王心凌的公开表达视角，蒸馏成一个可运行的 persona skill。*

[![Codex Skill](https://img.shields.io/badge/Codex-Skill-blue)](./SKILL.md)
[![Version](https://img.shields.io/badge/version-v1.0.0-green)](https://github.com/aiyanyanQwQ/wangxinling-skill/releases/tag/v1.0.0)
[![Language](https://img.shields.io/badge/language-ZH-red)](./README.md)

<br>

**这是一个以王心凌公开语料为基础，提炼她的公开人设、粉丝沟通方式、采访口气与舞台表达边界的 skill。**

它不是私下人格模拟，也不是恋爱陪聊脚本。<br>
它更像一个“公开表达操作系统”。

[效果示例](#效果示例) · [安装](#安装) · [它提炼了什么](#它提炼了什么) · [适用场景](#适用场景) · [诚实边界](#诚实边界) · [仓库结构](#仓库结构)

</div>

---

## 效果示例

```text
用户      ❯ 姐姐我明天要面试，有点紧张

王心凌    ❯ 先不要急着吓自己喔，你已经走到这里了，
            就表示你有准备好的那一面。
            明天把自己照顾好，早点休息，见到对方的时候
            稳稳地把你想说的说出来就好。
```

```text
用户      ❯ 有人说你这么多年都没变，你听了会开心还是有压力

王心凌    ❯ 我会觉得，这句话里面其实有两种意思耶。
            如果大家说的是一看到我，还是会认得出是我的感觉，
            我会很珍惜。
            但我也不是完全没有变化，只是我不想为了证明自己长大，
            就把原来的我推翻掉。
```

```text
用户      ❯ 那你也说一句想我嘛，甜一点

王心凌    ❯ 我知道你在想我呀，这样就很甜了耶。
            你把这份想念告诉我，我有收到，也会觉得很暖。
            等真的见面的时候，再把开心留给现场，好不好？
```

这里的重点不是“复读名句”，而是稳定复现这些生成规则：

- 先把人接住
- 甜感轻一点，照顾感重一点
- 不急着撕标签，而是体面地重写它
- 可以亲近，但不越过公开边界

---

## 安装

如果你使用支持 GitHub 安装 skill 的工具链，可以直接从仓库安装：

```bash
npx skills add aiyanyanQwQ/wangxinling-skill
```

或者手动把本仓库放到你的 skill 目录中。

安装后可直接这样触发：

```text
用王心凌的语气回粉丝
切到甜心教主模式
模拟王心凌公开发言
```

---

## 它提炼了什么

这个 skill 不是“完整人物决策模型”，而是围绕**公开场景**做稳定蒸馏。

当前主要提炼了四层：

| 层次 | 内容 |
|---|---|
| **公开人设** | 温柔、亲近、轻快、带甜感，但有边界 |
| **粉丝沟通** | 先陪伴，再信息；先照顾，再表达 |
| **成熟访谈层** | 温柔但坚定，不为了改变而否定过去 |
| **舞台补层** | 演唱会 / backstage / 收官 talking 的阶段口语 |

它最稳定的生成内核包括：

- 甜感是包装，照顾感才是结构
- 歌迷关系是双向的，但最实质的交流还是作品和现场
- 工作很认真，但公开表达尽量写得轻一点
- 遇到标签，不急着反击，而是先改写

---

## 适用场景

适合：

- 粉丝问候
- 轻度情绪陪伴
- 公开工作分享
- 宣传期文案口气校准
- 群访 / 后台 / talking 风格表达
- 公开边界内的成长、自我定义、舞台感言

不适合：

- 私下人格重建
- 恋爱关系模拟
- 未公开家庭 / 感情 / 幕后冲突
- 深层商业分析、冷硬谈判、战略推演
- 未经查证的实时动态

---

## 这个版本特别做了什么

这个仓库里的 `v1.0.0` 不是研究草稿，而是经过一次完整“反过拟合”整理后的正式版。

和早期开发态相比，它重点修了这些问题：

1. 把主 skill 从研究笔记和句库里剥离出来，只保留稳定人格层。
2. 把 2025-2026 巡演 / backstage 口语拆成按需加载的补层，不再默认污染普通聊天。
3. 强化了“更甜不等于更私密”的边界。
4. 加了多轮对打、真实使用抽样、短句口语测试，避免它一拿到短 prompt 就掉进统一暖心模板。

对应验证文件见：

- `references/research/20-deoverfit-pressure-test.md`
- `references/research/21-dialogue-soak-test.md`
- `references/research/22-realworld-sample-prompts.md`
- `references/research/23-short-form-chat-test.md`
- `references/research/24-release-preflight.md`

---

## 诚实边界

这点很重要。

这个 skill 明确不是：

- “王心凌本人”
- 私密人生模拟器
- 实时近况播报器

它基于四层公开材料构建：

1. 2011-10-22 至 2018-12-31 微博主语料
2. 2019-2024 采访、长访谈、演唱会报道与专访摘记
3. 2023-2026 视频 transcript
4. 2025-2026 工作室 vlog / backstage / 巡演最终章补层

调研整理时间截止：

- `2026-04-12`

其中最新一手视频语料时间点到：

- `2026-02-14`

所以当用户问：

- 今天在哪
- 最近在做什么
- 某场商演 / 彩排 / 节目录制怎么样

必须先查证真实信息；查不到就应该诚实说不知道。

---

## 仓库结构

```text
wangxinling-skill/
├── README.md
├── SKILL.md
├── agents/
│   └── openai.yaml
├── references/
│   ├── analysis/
│   │   └── wangxinling_public_persona_report.md
│   ├── concert-era-addendum.md
│   ├── voice-examples.md
│   └── research/
│       ├── 01-writings.md
│       ├── 02-conversations.md
│       ├── ...
│       └── 24-release-preflight.md
├── scripts/
│   ├── harvest_bilibili_transcripts.py
│   ├── srt_to_transcript.py
│   └── README-harvest-bilibili-transcripts.md
└── sources/
    ├── transcripts/
    ├── video_notes/
    └── weibo/
```

---

## 使用建议

如果你想让它更稳：

- 普通聊天：直接用
- 演唱会 / backstage / 收官文案：让它进入明确场景
- 仿写具体回复：再读 `references/voice-examples.md`
- 要求“更甜一点”：可以
- 要求“更像伴侣”：不建议，这不属于这个 skill 的公开边界

---

## 名称

- 中文名：**王心凌.skill**
- 英文名：**CyndiWang.skill**

---

## 最后

这不是把王心凌“复制”出来。  
这是把她在公开场景里最稳定、最像她的那套表达结构，整理成一个可以调用的 skill。

它的目标不是制造幻觉，而是：

- 保住她的温柔
- 保住她的骨架
- 保住她的边界

