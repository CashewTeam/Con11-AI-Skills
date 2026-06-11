---
name: yutto-downloader
description: 使用 yutto 下载哔哩哔哩视频。当你需要下载 B 站视频、番剧、课程、音频、弹幕、字幕时调用此 skill。支持单集下载、批量下载、清晰度选择、仅音频、弹幕/字幕提取等。
allowed-tools:
  - Bash
  - Read
  - Write
---

# yutto 哔哩哔哩视频下载

## 命令入口

`yutto download` 是本 skill 的核心命令，所有下载操作都由此子命令完成。

## 使用前确认

调用本 skill 时，首先从用户输入中提取以下信息：

1. **URL**（必填）：B 站视频/番剧/课程页面链接
2. **下载内容**：完整视频（默认）| 仅音频 | 仅视频 | 仅弹幕 | 仅字幕
3. **画质偏好**：如果用户提到"高画质""1080P""4K"等，映射为对应质量码
4. **输出目录**：用户指定则用 `-d`，未指定则默认 `~/Downloads`
5. **认证**：用户是否提供了 Cookie/SESSDATA

## 画质码速查

### 视频画质 `-q`

| 码值 | 含义 |
|------|------|
| 127 | 8K |
| 126 | Dolby Vision |
| 125 | 4K HDR10 |
| 120 | 4K |
| 116 | 1080P60 |
| 112 | 1080P+（高码率） |
| 100 | 智能修复 |
| 80 | 1080P |
| 74 | 720P60 |
| 64 | 720P |
| 32 | 480P |
| 16 | 360P |

### 音频码率 `-aq`

| 码值 | 含义 |
|------|------|
| 30251 | Hi-Res |
| 30255 | Dolby Audio |
| 30250 | Dolby Atmos |
| 30280 | 320kbps |
| 30232 | 128kbps |
| 30216 | 64kbps |

### 输出格式 `--output-format`

`infer`（自动推断，默认）、`mp4`、`mkv`、`mov`

纯音频时使用 `--output-format-audio-only`：`infer`、`m4a`、`aac`、`mp3`、`flac`、`mp4`、`mkv`、`mov`

## 常见场景及命令模板

### 场景 1：下载单个视频（默认画质）

```bash
yutto download "<URL>" -d ~/Downloads
```

用户未提画质时直接用此命令，yutto 会选最优可用画质。**默认不下弹幕和字幕**，只有用户明确要求时才加 `-df ass`。

### 场景 2：指定画质下载

```bash
yutto download "<URL>" -q 80
```

根据用户提到的画质描述，从速查表选对应码值。例如"1080P"→80，"4K"→120。

### 场景 3：仅下载音频（如提取 BGM / 播客）

```bash
yutto download "<URL>" --audio-only --output-format-audio-only m4a
```

### 场景 4：仅下载视频流（不含音频）

```bash
yutto download "<URL>" --video-only
```

### 场景 5：下载视频 + 弹幕 + 字幕（用户明确要求时）

```bash
yutto download "<URL>" -d ~/Downloads -df ass
```

弹幕格式：`xml` | `ass` | `protobuf`。推荐 `ass` 可直接在播放器中渲染。
**注意：默认不下载弹幕和字幕**，只有用户明确说"要弹幕""带字幕"等才加 `-df ass`。

### 场景 6：下载指定目录

```bash
yutto download "<URL>" -d "/path/to/output"
```

### 场景 7：批量下载番剧/合集/课程

```bash
yutto download "<URL>" -b
```

用户提供的 URL 是番剧/合集主页时，加 `-b` 批量下载所有分集。

#### 只下载指定集数

```bash
yutto download "<URL>" -b -p "1-5,8,10"
```

`-p` 支持范围（`1-5`）和逗号分隔（`1,3,5`），可混用（`1-5,8,10`）。

#### 包含 PV/预告/特别篇

```bash
yutto download "<URL>" -b -s
```

### 场景 8：使用 Cookie 认证（下载大会员/高画质内容）

两种方式：

**方式 A**：命令行直接传入
```bash
yutto download "<URL>" --auth "SESSDATA=xxxxx; bili_jct=yyyyy"
```

**方式 B**：使用认证文件
```bash
yutto download "<URL>" --auth-file /path/to/auth.txt
```

### 场景 9：设置代理

```bash
yutto download "<URL>" -x auto
```

`auto`=系统代理，`no`=不使用代理，或直接写代理地址如 `http://127.0.0.1:7890`。

### 场景 10：并发下载加速

```bash
yutto download "<URL>" -n 4
```

`-n` 设置同时下载的最大 Worker 数，默认较低，可提高至 4-8 以加速。

### 场景 11：覆盖已下载文件

```bash
yutto download "<URL>" -w
```

### 场景 12：生成元数据文件

```bash
yutto download "<URL>" --with-metadata
```

生成包含标题、简介、发布时间等信息的 `.metadata` 文件。

### 场景 13：仅下载封面

```bash
yutto download "<URL>" --cover-only
```

### 场景 14：高画质 + 音频 + 弹幕全量下载

```bash
yutto download "<URL>" -d ~/Downloads -q 120 -aq 30280 -df ass --with-metadata
```

## 多级目录存储

用 `-tp` 自定义输出子目录结构：

```bash
yutto download "<URL>" -tp "{title}/{name}"
```

可用变量：`{title}`（系列标题）、`{name}`（分集标题）、`{id}`、`{bvid}`、`{owner}` 等。

## 视频编码选择

```bash
yutto download "<URL>" --vcodec hevc:hevc
```

`<下载编码>:<保存编码>`，常用编码：`hevc`、`avc`（H.264）、`av1`。

## 下载间隔

批量下载时，可在每集之间添加间隔以避免触发风控：

```bash
yutto download "<URL>" -b --download-interval 5
```

单位为秒。

## 命令构建原则

1. **默认下载到 `~/Downloads`**：用户不指定目录时统一加 `-d ~/Downloads`
2. **默认不下载弹幕和字幕**：只有用户明确提"要弹幕""带字幕""下载 ass"等才加 `-df ass`
3. **先确认 URL 来源**：是单个视频还是番剧/合集页面，后者自动加 `-b`
4. **从用户描述映射画质**：映射表见上文。未明确提画质则不指定 `-q`，让 yutto 自动选择
5. **音频下载默认用 m4a**：兼容性好
6. **路径含空格要加引号**
7. **Cookie 中的 SESSDATA 是敏感信息**，提醒用户不要分享

## 错误处理

| 现象 | 处理方式 |
|------|---------|
| 下载失败/403 | 添加 `--auth` 提供 Cookie |
| 画质不可用 | 降低 `-q` 值重试（如 80→64→32） |
| 批量下载风控 | 加 `--download-interval 3` |
| 覆盖提示 | 加 `-w` 强制覆盖 |
| 代理不通 | 用 `-x no` 关闭代理或 `-x <正确地址>` |
| 下载速度慢 | 加 `-n 8` 提高并发 |
