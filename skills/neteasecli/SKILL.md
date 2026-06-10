---
name: neteasecli
description: 在终端中使用网易云音乐。当你需要搜索歌曲、播放音乐、下载歌曲、管理歌单、查看歌词、控制播放器时调用此 skill。基于 neteasecli 命令行工具，支持 JSON 输出用于脚本集成和 AI 代理。
allowed-tools:
  - Bash
  - Read
  - Write
---

# neteasecli 网易云音乐命令行工具

## 命令入口

`neteasecli` 是本 skill 的核心命令。通过浏览器 Cookie 完成认证，无需处理验证码或短信。

## 环境要求

- Node.js >= 24
- [mpv](https://mpv.io/)（可选，用于播放）
- Chrome / Edge / Firefox / Safari（用于 Cookie 导入）

## 安装

```bash
npx neteasecli <command>        # 免安装运行
npm install -g neteasecli        # 全局安装
```

调用 skill 时先 `which neteasecli` 或 `npx neteasecli` 检查可用性，未安装则使用 `npx` 运行。

## 使用前确认

从用户输入中提取以下信息：

1. **操作类型**：搜索 | 播放 | 下载 | 歌词 | 歌单 | 收藏 | 控制
2. **搜索关键词/ID**：歌曲名、歌手名、专辑名或数字 ID
3. **画质/音质偏好**：用户提到的音质等级
4. **账号**：是否需要指定 profile 切换账号
5. **输出格式**：是否明确要求 JSON 输出

## 认证

### 登录（导入浏览器 Cookie）

```bash
neteasecli auth login                    # 自动检测浏览器导入 Cookie
neteasecli auth login --profile work      # 多账号登录
neteasecli auth login --profile "Chrome Profile 1"  # 指定 Chrome Profile
```

### 检查状态

```bash
neteasecli auth check
```

### 登出

```bash
neteasecli auth logout
neteasecli auth logout --profile work
```

## 全局选项

| 选项 | 说明 |
|------|------|
| `--json` | 强制 JSON 输出（管道时默认启用） |
| `--plain` | 纯文本输出（制表符分隔） |
| `--pretty` | 格式化 JSON |
| `--quiet` | 静默模式 |
| `--no-color` | 禁用颜色 |
| `--profile <name>` | 指定账号配置（默认 "default"） |
| `-v, --verbose` | 详细输出 |
| `-d, --debug` | 调试输出 |
| `--timeout <seconds>` | 请求超时秒数（默认 30） |

## 常见场景及命令模板

### 场景 1：搜索歌曲

```bash
neteasecli search track "关键词"
neteasecli search track "周杰伦" -l 10    # 限制结果数
neteasecli --json search track "晴天"     # JSON 输出
```

### 场景 2：搜索专辑

```bash
neteasecli search album "关键词"
```

### 场景 3：搜索歌单

```bash
neteasecli search playlist "关键词"
neteasecli search playlist "华语" -l 5
```

### 场景 4：搜索歌手

```bash
neteasecli search artist "关键词"
```

### 场景 5：查看歌曲详情

```bash
neteasecli track detail <id>
```

返回歌曲元数据：标题、歌手、专辑、时长等。

### 场景 6：获取播放链接

```bash
neteasecli track url <id>
neteasecli track url <id> -q lossless    # 指定音质
```

音质选项：`standard` | `higher` | `exhigh`（默认）| `lossless` | `hires`

### 场景 7：获取歌词

```bash
neteasecli track lyric <id>
```

### 场景 8：下载歌曲

```bash
neteasecli track download <id>
neteasecli track download <id> -q lossless    # 无损下载
```

### 场景 9：播放歌曲

```bash
neteasecli track play <id>
neteasecli track play <id> -q hires
```

需要安装 mpv。

### 场景 10：播放器控制

```bash
neteasecli player status           # 查看播放状态
neteasecli player pause            # 暂停/继续
neteasecli player stop             # 停止
neteasecli player seek 10          # 快进 10 秒
neteasecli player seek -10         # 快退 10 秒
neteasecli player seek 60 --absolute  # 跳转到第 60 秒
neteasecli player volume 80        # 设置音量 80
neteasecli player volume           # 查看当前音量
neteasecli player repeat on        # 开启单曲循环
neteasecli player repeat off       # 关闭单曲循环
```

音量范围：0-150。

### 场景 11：查看我喜欢的音乐

```bash
neteasecli library liked
neteasecli --json library liked
```

### 场景 12：收藏/取消收藏

```bash
neteasecli library like <id>
neteasecli library unlike <id>
```

### 场景 13：最近播放

```bash
neteasecli library recent
```

### 场景 14：我的歌单

```bash
neteasecli playlist list
```

### 场景 15：歌单详情

```bash
neteasecli playlist detail <id>
```

## JSON 输出格式

所有命令都返回结构化 JSON：

```json
{
  "success": true,
  "data": { ... },
  "error": null
}
```

退出码：`0` 成功，`1` 通用错误，`2` 认证错误，`3` 网络错误。

## 多账号管理

```bash
neteasecli --profile work auth login    # 用 work 账号登录
neteasecli --profile work library liked  # 查看 work 账号的喜欢
neteasecli --profile work track download <id>  # 用 work 账号下载
```

配置存储在 `~/.config/neteasecli/profiles/<name>/`。

## 命令构建原则

1. **未安装先检查**：`npx neteasecli` 免安装也能运行
2. **搜索优先给 ID**：搜索结果中的 ID 用于后续播放/下载/歌词操作
3. **需要用户交互时优先 JSON**：`--json` 输出便于解析，特别是需要从搜索结果提取 ID 时
4. **mpv 未安装提示**：播放命令需 mpv，未安装时提示用户
5. **认证优先**：未登录时大部分接口返回受限数据，提醒用户先 `auth login`
6. **音质按需选择**：默认 exhigh（320kbps），用户提"无损"用 lossless，提"Hi-Res"用 hires

## 错误处理

| 现象 | 处理方式 |
|------|---------|
| auth error (退出码 2) | 引导用户执行 `neteasecli auth login` 登录 |
| network error (退出码 3) | 检查网络，可加 `--timeout 60` 增加超时 |
| 播放无声音 | 检查 mpv 是否安装：`which mpv` |
| 下载的画质不满足 | 尝试更高音质 `-q lossless` 或 `-q hires` |
| 搜索结果为空 | 尝试更短的关键词或不同的搜索类型 |
| Node.js 版本过低 | 需要 Node.js >= 24 |
