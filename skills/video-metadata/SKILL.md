---
name: video-metadata
description: 根据 SRT 字幕和当前达芬奇工程，一次性生成视频简介、分段章节、BGM 列表。当你说"生成简介"时输出三件套全集。
allowed-tools:
  - Bash
  - Read
  - Write
  - Edit
---

# 视频元信息生成

## 触发词

生成简介 → 输出全集（简介 + 分段 + BGM），不单出

## 行为

用户说"生成简介"时，**一次性输出三个内容**，不要只出简介：

1. 简介（50字以内）
2. 分段章节（带时间戳）
3. BGM 列表（纯曲名，逗号间隔）

## 工作流

### 1. 读取 SRT 字幕

从 ASR 字幕目录读取，路径模式：

```
/Users/con11/Documents/asr/<项目名>/<项目名>_subtitles_asr_remote_raw.srt
```

直接用 Read 工具读取然后分析内容。

### 2. 从达芬奇获取 BGM 信息

用达芬奇 MCP 获取当前时间线的音频轨道信息：

```
timeline probe_timeline_structure track_types=["audio"] include_clip_properties=true
timeline get_track_count track_type=audio
```

然后用 jq 提取音频轨道中非同期声的素材名（排除 Track 1 的相机音频，以及 Track 4 的纯音效）：

```
jq '[.result.tracks.audio.tracks[] | {track_index, item_count, clip_names: [.items[] | .media_pool_item_name] | unique}]'
```

### 3. 输出格式（必须全部输出）

**简介**（50字以内，概括视频核心内容）

**分段章节**（分行）：
```
00:00 章节名
00:26 章节名
```

**BGM 列表**（纯歌曲名，去歌手、序号，逗号间隔）：
```
曲名1, 曲名2, 曲名3
```

### 4. 关键字幕时间节点定位

分析字幕内容中的转折词来确定分段节点：
- "首先"、"第一" → 章节开始
- "然后"、换话题 → 新章节
- "回到开头的问题"、"所以"、"总的来说" → 结尾章节
- "以上就是"、"我们下期" → 结尾

### 项目路径映射

| 项目 | ASR 字幕路径 |
|------|-------------|
| macai工作流 | /Users/con11/Documents/asr/macai工作流/macai工作流_subtitles_asr_remote_raw.srt |
