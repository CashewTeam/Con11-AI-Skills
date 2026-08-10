---
name: pico-dev
description: "PICO OS 6 / Spatial SDK 6.0 空间应用开发知识库（Kotlin/Android）。开发 PICO 空间应用时使用：空间容器与空间状态（WindowContainer/Stage、Shared/Full Space）、Spatial UI、ECS 场景、资源与 AssetBundle、渲染/动画/物理、追踪与交互、空间音视频、混合现实环境感知、SpatialML、性能调试、迁移与升级。内置官方中文文档库（docs/ 525 篇）+ Kotlin API 参考（docs/api/ 4409 页，含签名/参数/返回/异常），并整合官方 PICO Intelligent Plugins 工作流 skill（official/：16 个 spatial + 3 个 unity，含 pico-cli/MCP 实操流程）。"
---

<!-- argument-hint: [话题，如 ECS / WindowContainer / 手部追踪 / SpatialML / 性能，或 docs/ 文档文件名] -->

# PICO Dev — PICO OS 6 / Spatial SDK 6.0 开发者知识库

**语料版本**: 中文 PICO OS 6 / Spatial SDK 6.0（官方 llmstxt 导出，2025-08 抓取）
**文档**: `docs/` 525 篇原文 | **API 参考**: `docs/api/` 4409 页 | **全量索引**: `INDEX.md`（566 条，含 tags 与一句话摘要） | **官方工作流**: `official/`（16 spatial + 3 unity skill）

## 使用方式

- **无参数** — 加载本文件，获得平台心智模型与问题路由
- **带话题** — 如"如何创建 Volumetric WindowContainer"、"手部追踪 API"、"AssetBundle 加载"：按下方路由定位文档族，再读取 `docs/` 中对应文件原文。`docs/` 按 **族/一级分类** 组织（如 `docs/spatial-sdk/空间容器/`），文件名为原 URL slug 去掉族/分类前缀；完整 slug 见 `INDEX.md`
- **带文档名** — 如 `pico-dev 读取 spatial-sdk_空间容器_管理-stage_管理-stage-的生命周期和状态`：文件位于 `docs/spatial-sdk/空间容器/管理-stage_管理-stage-的生命周期和状态.md`，直接读取
- **浏览/检索** — "列出文档"或"有哪些文档"：读 `INDEX.md`；每个条目带 tags 可 grep
- **需要 API 细节时** — 文档正文多为说明式；签名级细节以文档内代码块为准，超出语料范围的设备差异/外部 Android API 需回官方权威来源核验
- **执行/实操任务** — 如"创建项目"、"迁移 Android 应用"、"性能诊断"、"Figma/截图转 app"、"Spatial Editor 创作"：走 `official/` 下对应工作流 skill（见下方"官方 Agentic 工作流 skill"章节），知识细节回 `docs/` 检索
- **查 API 签名/参数** — 如"WindowContainer 的 API"、"loadSuspend 的参数与返回"：grep 定位 `docs/api/`（见"API 参考"章节），签名/参数/返回/异常以 API 页为准

## 核心心智模型

### 1. 空间应用 = Android 应用 + 空间承载模型
PICO Spatial SDK 基于 Android 体系（Kotlin + Compose）。SDK 的设计目标是**弱化对 Activity 的直接依赖**：常规开发无需管理 Activity 生命周期，只需声明空间容器并编写容器内的 Composable content。Activity 只是空间容器内部的 UI 载体（默认 Activity 由模板生成，也可自定义）。

### 2. 空间容器三选一（先决定承载，再选 API）
| 容器 | 呈现方式 | 边界 | 适用 |
|---|---|---|---|
| **Planar WindowContainer** | 2D 平面窗口 | 有边界，内容被裁切 | 常见 UI、2D 面板（窗口内也可放 3D 内容） |
| **Volumetric WindowContainer** | 3D 立体窗口 | 有边界 | 3D 物体与立体内容，固定区域 |
| **Stage** | 沉浸式场景 | 无边界 | Full Space 沉浸体验 |

默认打开时 WindowContainer 出现在用户前方约 **1.75 米** 处，中心对齐头显朝向。**决策规则**：先问"内容是 2D 平面 / 有边界 3D / 无边界沉浸"，再选容器；生命周期与状态管理进入对应细页（见常见用例 2）。

### 3. 空间状态：Shared Space vs Full Space
`context.getSelfSpaceState()` 返回 `SpaceState` 枚举：`UNKNOWN` / `SHAREDSPACE` / `FULLSPACE`。Shared Space 与系统多窗口共存；Full Space 独占沉浸。**先分清当前空间状态，再推荐行为**。

### 4. 3D 运行时场景 = ECS（实体-组件-系统）
- **Entity**：场景节点，本身无业务逻辑，只是数据与能力的承载者
- **Component**：能力与数据的最小单元（变换、渲染、光照、交互、物理、音频、视频、传送门等内置组件），通过 `entity.components` 挂载/查询/获取/移除
- **System**：逐帧更新逻辑；自定义组件 + 自定义系统实现复杂交互/动画
- 实体以树维护层级；场景用 Scene / SpatialViewContent 订阅实体事件

### 5. 2D UI = Spatial UI（Compose 风格）
`PicoTheme` 定义外观；控件族覆盖 Button/IconButton/ToggleButton/Chip/Badge/CheckBox/Switch/Slider/ListItem/TextField/SearchField/NumberField/DatePicker 等，浮层族含 Alert Dialog/Toolbar/Sheet/Snack/Menu/Coachmark/Subwindow/SpatialPopup/Augment。
**空间化效果**（为 2D 内容加空间感）：毛玻璃（Thin/Regular/Thick/Thickest）、空间浮起（z 偏移）、空间旋转（`rotation3D`）、空间缩放、空间悬停（CustomHover/SpatialHoverEffectGroup）、ToolTip、深度与布局、Vibrant Style（动态混色）。
**单位**：支持物理长度单位（米/厘米）与 dp 互转；`dmm`（与距离无关的毫米）是设计规范中的角度单位。

### 6. 资源模型与所有权
类型链：**网格 Mesh → 纹理 → 材质 → 模型 → AssetBundle**；另有音频/视频资源。注意资源所有权、引用计数、释放与持久化。动态 3D 模型用 `MeshModel` 创建/更新。ShaderGraphMaterial 是 Spatial Editor 可视化材质在运行时的实例，存储 Shader 暴露的可调参数与资源绑定。

### 7. 功能能力族（按需进入）
- **交互**：3D 物体基础交互（碰撞体、输入目标、悬停/选中事件、操控与反馈）→ 空间手势（`SpatialTapGesture`/`SpatialDragGesture`）→ 3D 悬停高亮 → 与实体交互（`targetedToEntity`）→ 自定义空间交互事件 → 手柄振动反馈
- **追踪**：`DataProvider` 是通用访问/订阅模式 → 头显 / 手柄（ControllerTrackingProvider）/ 手部 / 全身动捕 / 独立追踪（体感追踪器 6DoF）/ 视线
- **渲染**：ShaderGraphMaterial、IBL 基于图像光照、动态光照/投影、透明度（OpacityControllerComponent）、传送门、粒子、实体渲染顺序（默认按与相机距离，透明规则不同；SortAsUIElementComponent 统一管理实体与 2D UI 顺序）、3D 高斯泼溅
- **动画**：骨骼 / 补间 / 轨道 / Timeline（Spatial Editor 创建）/ Blend Shape → 动画组合与播放控制（AnimationPlaybackController、AnimationPlayConfig）→ 动画事件
- **物理**：碰撞体 + 刚体 + 外力 + 物理世界参数（重力、模拟时钟、迭代次数）→ 基于射线/投射几何体的命中检测
- **音频**：三组件分工——ChannelAudioComponent（声道直通，无空间化）、AmbientAudioComponent（感知朝向、无距离与混响）、ObjectAudioComponent（感知位置/朝向/距离，全空间化）→ 音频混合组、音频事件、SpatialAudioTrackExtension（第三方播放器）
- **视频**：VideoMaterial（视频纹理材质，透明/单双面/平面立体布局）→ VideoPlayerComponent（CypressMediaPlayer）/ VideoComponent（适配第三方播放器）→ 投影方式（Planar 平面 / Spherical 球面）
- **MR 环境感知**：空间锚点（创建/定位/持久化）、空间网格（环境几何→模型）、平面检测、PICO 键盘追踪
- **SpatialML**：受保护相机 + 图式执行（Pipeline/算子/张量），独立 spatial-ml 文档族
- **性能**：统一渲染（Unified Rendering）流程分析、场景复杂度、性能优化、高清 UI 渲染（系统服务统一渲染 2D UI）、System Trace、Metrics HUD

## 问题路由（官方给 LLM 的导航指引）

- **承载与生命周期** → 先区分 Planar/Volumetric WindowContainer、Stage、Shared/Full Space，再推荐 API；默认入口是"了解空间容器 & 空间状态"
- **2D UI** → Spatial UI 概览 + 设计规范；**3D 运行时** → ECS、资源、渲染、交互、动画、物理文档
- **Spatial Editor / Shader Graph / Timelines / Plugin / Emulator** → 界面或工具工作流，**若无运行时文档佐证，不要据此推断 Kotlin SDK 行为**
- **SpatialML** → 先读 spatial-ml 概览与"运行时模型"，明确管线阶段与张量契约后再查算子叶子页
- **升级/兼容** → 同时使用"升级 SDK" + "迁移 Android 应用" + "更新说明"（更新说明是变更记录，不是概念入口）
- **性能** → 先走"性能与调试 概览"路由；**模拟器现象需结合"Emulator 与真机差异"文档或真机验证**
- **版本** → 默认使用本文库代表的 6.0 语料版本，除非用户明确指定其他版本

## 学习路线图

**通用路径**：① 基础与承载模型（"了解 PICO Spatial SDK 和空间应用" + "了解空间容器 & 空间状态"）→ ② 首个可运行项目（"第二步：创建并运行 Spatial 项目" + "项目结构与依赖配置"）→ ③ UI 与场景架构（Spatial UI 概览 / ECS 架构 + 资源概览）→ ④ 交互与功能系统（"3D 物体的基础交互" 起步，按需进入追踪/渲染/动画/物理/音视频/环境感知/SpatialML）→ ⑤ 工具与交付（Plugin/Editor/Emulator + 性能概览 + 迁移兼容更新说明）。

**按背景分支**：
- **传统 Android 开发者**：平台心智模型 → 空间容器 → 项目结构 → "迁移 Android 应用" → Spatial UI；仅需要 3D 时继续 Volumetric、Stage 与 ECS
- **游戏 / 3D 开发者**：平台与容器 → ECS → 资源/AssetBundle → 渲染材质 → 交互 → 动画/物理/音视频 → Spatial Editor 资产管线 → 性能
- **空间计算 / visionOS 开发者**：把空间应用映射到 WindowContainer/Stage 与 Shared/Full Space → 对比 2D 面板与 3D 实体 → 交互与追踪 → 锚点/网格/平面检测/音视频/环境感知

## 常见用例 → 文档入口（docs/ 内）

| 用例 | 入口文档（docs/） |
|---|---|
| 构建第一个空间应用 | `docs/spatial-sdk/了解-pico-spatial-sdk-和空间应用.md`、`docs/spatial-sdk/快速开始_第二步：创建并运行-spatial-项目.md`、`docs/spatial-tutorial/从模板开始搭建空间应用/教程介绍.md` |
| 选择容器并管理生命周期 | `docs/spatial-sdk/空间容器/了解空间容器-&-空间状态.md`、`docs/spatial-sdk/空间容器/管理-windowcontainer_管理-windowcontainer-的生命周期和状态.md`、`docs/spatial-sdk/空间容器/管理-stage_管理-stage-的生命周期和状态.md` |
| Spatial UI 与空间化 2D | `docs/spatial-ui/spatial-ui-概览.md`、`docs/spatial-sdk/内容布局与呈现/spatial-ui-主题和组件.md`、`docs/spatial-sdk/内容布局与呈现/为-2d-内容添加空间效果_深度与布局.md` |
| 交互与手势 | `docs/spatial-sdk/交互/3d-物体的基础交互.md`、`docs/spatial-sdk/交互/空间手势.md`、`docs/spatial-tutorial/在空间应用中实现-3d-物体的交互/教程介绍.md` |
| ECS 实体/组件/系统 | `docs/spatial-sdk/实体-组件-系统（ecs）/了解-ecs-架构.md`、`docs/spatial-sdk/实体-组件-系统（ecs）/实体概览.md`、`docs/spatial-sdk/实体-组件-系统（ecs）/自定义系统和组件.md` |
| 资源与 AssetBundle | `docs/spatial-sdk/资源管理/资源概览.md`、`docs/spatial-sdk/资源管理/assetbundle.md`、`docs/spatial-sdk/资源管理/动态创建和更新模型.md` |
| 渲染与材质 | `docs/spatial-sdk/渲染/shadergraphmaterial.md`、`docs/spatial-sdk/渲染/基于图像的光照.md`、`docs/spatial-toolkit/pico-spatial-editor/材质_shader-graph_shader-graph-快速入门.md` |
| 动画 | `docs/spatial-sdk/动画/动画系统.md`、`docs/spatial-sdk/动画/动画组合与播放控制.md`、`docs/spatial-toolkit/pico-spatial-editor/动画_timelines_什么是-timelines.md` |
| 物理 | `docs/spatial-sdk/物理/物理模拟的流程.md`、`docs/spatial-sdk/物理/添加碰撞和外部作用.md`、`docs/spatial-sdk/物理/基于射线的物体命中检测.md` |
| 空间音频 | `docs/spatial-sdk/音频/空间音频概览.md`、`docs/spatial-sdk/音频/使用-objectaudiocomponent.md`、`docs/spatial-sdk/音频/使用音频混合组.md` |
| 空间视频 | `docs/spatial-sdk/视频/视频概览.md`、`docs/spatial-sdk/视频/投影方式.md`、`docs/spatial-sdk/视频/使用-videoplayercomponent.md` |
| MR 环境感知 | `docs/spatial-sdk/环境感知（混合现实）/空间锚点.md`、`docs/spatial-sdk/环境感知（混合现实）/空间网格.md`、`docs/spatial-sdk/环境感知（混合现实）/平面检测.md` |
| 追踪 | `docs/spatial-sdk/追踪/dataprovider-使用说明.md`、`docs/spatial-sdk/追踪/手部追踪.md`、`docs/spatial-sdk/追踪/视线追踪.md` |
| SpatialML | `docs/spatial-ml/spatialml-for-the-pico-spatial-sdk.md`、`docs/spatial-ml/快速上手/第一个-spatialml-场景.md`、`docs/spatial-ml/参考/算子目录.md` |
| 工具链（Plugin/Emulator/Editor） | `docs/spatial-toolkit/pico-spatial-plugin/什么是-pico-spatial-plugin.md`、`docs/spatial-toolkit/pico-emulator/什么是-pico-emulator.md`、`docs/spatial-toolkit/pico-spatial-editor/什么是-pico-spatial-editor.md` |
| 性能与调试 | `docs/spatial-sdk/性能与调试/概览.md`、`docs/spatial-sdk/性能与调试/获取并分析-trace-记录.md`、`docs/spatial-toolkit/pico-emulator/了解-pico-emulator-与真机的差异.md` |
| 迁移 / 升级 | `docs/spatial-sdk/迁移-android-应用.md`、`docs/spatial-sdk/升级-sdk.md`、`docs/spatial-sdk/更新说明.md` |

## 文档族索引（docs/ 按 族/一级分类 组织；完整 566 条见 INDEX.md）

### spatial-sdk（139 篇）— 核心 SDK
- 总览/入门：`docs/spatial-sdk/了解-pico-spatial-sdk-和空间应用.md`、`docs/spatial-sdk/快速开始_第二步：创建并运行-spatial-项目.md`、`docs/spatial-sdk/项目结构与依赖配置.md`
- 空间容器：`docs/spatial-sdk/空间容器/了解空间容器-&-空间状态.md`、`docs/spatial-sdk/空间容器/管理应用的空间状态.md`、`docs/spatial-sdk/空间容器/管理-windowcontainer_声明-windowcontainer.md`、`docs/spatial-sdk/空间容器/管理-windowcontainer_打开或关闭-windowcontainer.md`、`docs/spatial-sdk/空间容器/管理-windowcontainer_管理-windowcontainer-的生命周期和状态.md`、`docs/spatial-sdk/空间容器/管理-stage_声明-stage.md`、`docs/spatial-sdk/空间容器/管理-stage_打开或关闭-stage.md`、`docs/spatial-sdk/空间容器/管理-stage_管理-stage-的生命周期和状态.md`、`docs/spatial-sdk/空间容器/关于默认空间容器和默认-activity.md`、`docs/spatial-sdk/空间容器/自定义空间容器的-activity.md`、`docs/spatial-sdk/空间容器/示例：欢迎来到-pico-os-6！.md`
- 内容布局与呈现：`docs/spatial-sdk/内容布局与呈现/spatial-ui-主题和组件.md`、`docs/spatial-sdk/内容布局与呈现/在-spatialmodelview-和-spatialview-中添加-3d-内容.md`、`docs/spatial-sdk/内容布局与呈现/将-2d-面板挂载至-3d-实体.md`、`docs/spatial-sdk/内容布局与呈现/长度单位转换.md`、`docs/spatial-sdk/内容布局与呈现/vibrant-style.md`、`docs/spatial-sdk/内容布局与呈现/上肢可见性.md`、`docs/spatial-sdk/内容布局与呈现/`（毛玻璃/空间浮起/空间旋转/空间悬停/空间缩放/深度与布局/ToolTip/空间化组件）、`docs/spatial-sdk/内容布局与呈现/示例：创建空间-ui-应用.md`
- ECS：`docs/spatial-sdk/实体-组件-系统（ecs）/了解-ecs-架构.md` + 实体概览/创建实体/查询实体/管理实体的生命周期/管理实体层级/为实体挂载组件/控制实体的朝向/获取实体的包围盒/克隆实体/实体事件/内置组件/自定义系统和组件
- 资源：`docs/spatial-sdk/资源管理/资源概览.md` + 网格/纹理/材质/模型/音频资源/视频文件/assetbundle/动态创建和更新模型
- 事件系统：`docs/spatial-sdk/事件系统.md`
- 交互：`docs/spatial-sdk/交互/3d-物体的基础交互.md`、`docs/spatial-sdk/交互/空间手势.md`、`docs/spatial-sdk/交互/3d-悬停高亮.md`、`docs/spatial-sdk/交互/与实体交互.md`、`docs/spatial-sdk/交互/自定义空间交互事件.md`、`docs/spatial-sdk/交互/交互音效.md`、`docs/spatial-sdk/交互/拖放-ui-组件.md`、`docs/spatial-sdk/交互/手柄振动反馈.md`
- 追踪：`docs/spatial-sdk/追踪/dataprovider-使用说明.md` + 头显/手柄/手部/全身动捕/独立追踪/视线追踪
- 渲染：`docs/spatial-sdk/渲染/shadergraphmaterial.md`、`docs/spatial-sdk/渲染/基于图像的光照.md`、`docs/spatial-sdk/渲染/动态光照.md`、`docs/spatial-sdk/渲染/动态投影.md`、`docs/spatial-sdk/渲染/透明度.md`、`docs/spatial-sdk/渲染/传送门.md`、`docs/spatial-sdk/渲染/粒子.md`、`docs/spatial-sdk/渲染/实体渲染顺序.md`、`docs/spatial-sdk/渲染/实体与-2d-ui-的渲染顺序.md`、`docs/spatial-sdk/渲染/3d-高斯泼溅.md`
- 动画：`docs/spatial-sdk/动画/动画系统.md` + 骨骼/补间/轨道/timeline-动画/blend-shape-动画/动画组合与播放控制/动画事件/示例：为-3d-模型添加动画
- 物理：`docs/spatial-sdk/物理/物理模拟的流程.md` + 添加碰撞和外部作用/设置物理世界的参数/基于射线的物体命中检测/示例：为应用添加物理效果
- SpatialML 概览（sdk 族）：`docs/spatial-sdk/spatialml/`（概览/隐私声明/基本概念/快速上手/最佳实践/示例：超级分辨率相机）— 细节见 spatial-ml 族
- MR 环境感知：`docs/spatial-sdk/环境感知（混合现实）/空间锚点.md`、`docs/spatial-sdk/环境感知（混合现实）/空间网格.md`、`docs/spatial-sdk/环境感知（混合现实）/平面检测.md`、`docs/spatial-sdk/环境感知（混合现实）/pico-键盘追踪.md`、`docs/spatial-sdk/环境感知（混合现实）/示例：利用空间网格创建射击游戏.md`
- 音频：`docs/spatial-sdk/音频/空间音频概览.md` + 使用-channelaudiocomponent/使用-ambientaudiocomponent/使用-objectaudiocomponent/使用-spatialaudiotrackextension/使用音频事件/使用音频混合组/使用音频组资源/示例：创建沉浸式空间音频
- 视频：`docs/spatial-sdk/视频/视频概览.md` + 投影方式/使用-videomaterial/使用-videoplayercomponent/使用-videocomponent/示例：在应用中播放空间视频/视频常见问题_*
- 空间数学：`docs/spatial-sdk/空间数学/坐标空间转换.md`、`docs/spatial-sdk/空间数学/长度单位转换.md`
- 性能与调试：`docs/spatial-sdk/性能与调试/概览.md` + 3d-渲染流程与性能分析/场景复杂度与应用性能/性能优化/开启高清-ui-渲染/获取并分析-trace-记录/头戴端性能监测工具-(metrics-hud)
- 迁移/兼容：`docs/spatial-sdk/迁移-android-应用.md`、`docs/spatial-sdk/升级-sdk.md`、`docs/spatial-sdk/更新说明.md`、`docs/spatial-sdk/实验性-api-的使用注意事项.md`、`docs/spatial-sdk/已知问题.md`、`docs/spatial-sdk/面向-ai-的大语言模型资源.md`

### spatial-ui（36 篇）— Compose 组件参考
- 入口：`docs/spatial-ui/spatial-ui-概览.md`、`docs/spatial-ui/主题.md`
- 标准控件：button/iconbutton/togglebutton/toggleiconbutton/link/divider/chip/badge/checkbox/switch/option/slider/listitem/titlebar/progressindicator/pagecontrol/segmentcontrol/sidenavigation/textfield/searchfield/numberfield/textselectionandtoolbarprovider/scrollindicator
- 空间窗口类：`docs/spatial-ui/空间窗口类/alert-dialog.md`、`docs/spatial-ui/空间窗口类/toolbar.md`、`docs/spatial-ui/空间窗口类/sheet.md`、`docs/spatial-ui/空间窗口类/snack.md`、`docs/spatial-ui/空间窗口类/menu.md`、`docs/spatial-ui/空间窗口类/coachmark.md`、`docs/spatial-ui/空间窗口类/datepicker.md`、`docs/spatial-ui/空间窗口类/timepicker.md`、`docs/spatial-ui/空间窗口类/augment.md`、`docs/spatial-ui/空间窗口类/subwindow.md`、`docs/spatial-ui/空间窗口类/spatialpopup.md`

### spatial-ml（70 篇）— 受保护相机 + 机器学习管线
- 入口：`docs/spatial-ml/spatialml-for-the-pico-spatial-sdk.md`
- 快速上手：`docs/spatial-ml/快速上手/前置条件.md`、`docs/spatial-ml/快速上手/第一个-spatialml-场景.md`
- 核心概念：`docs/spatial-ml/核心概念/运行时模型.md`、`docs/spatial-ml/核心概念/空间模式.md`、`docs/spatial-ml/核心概念/安全模式与回读模式.md`、`docs/spatial-ml/核心概念/容器与传送门.md`、`docs/spatial-ml/核心概念/张量与形状.md`、`docs/spatial-ml/核心概念/执行模型.md`
- 工作流：`docs/spatial-ml/工作流/使用管线包（pipeline-zoo）.md`、`docs/spatial-ml/工作流/访问-vst-相机图像.md`、`docs/spatial-ml/工作流/为模型准备图像数据.md`、`docs/spatial-ml/工作流/运行模型推理.md`、`docs/spatial-ml/工作流/将数据回读到应用.md`、`docs/spatial-ml/工作流/驱动场景图输出.md`、`docs/spatial-ml/工作流/异步管线模式.md`
- 参考：`docs/spatial-ml/参考/算子目录.md`、`docs/spatial-ml/参考/核心-api.md`、`docs/spatial-ml/参考/管线包格式.md`、`docs/spatial-ml/参考/张量类型与枚举.md`、`docs/spatial-ml/参考/`（rectifiedVSTAccess/getDepthMap/getAffine/applyAffine/runModelInference/normalize/convertColor/switchCHWAndHWC/copy/argmax/nonMaximumSuppression/arithmetic/uvTo3DInCameraSpace/solvePnP/makeTransform/updateSceneGraphProperty/switchSceneVisibility/newSceneFromGLTF/captureMicrophone/outputSounds/submit/newLocalTensor/newPlaceholder/newPlaceholderLike/get（张量切片）/elementwiseMultiply/inversion/norm/sortMatrix/singularValueDecomposition/比较与位运算系列/applyAffinePoint/updateSceneGraphTextContent/updateSceneGraphTextHorizontalAlignment/updateSceneGraphTextVerticalAlignment 等）
- 示例/排查：`docs/spatial-ml/示例_superresolutionapp-演练.md`、`docs/spatial-ml/疑难排查.md`（图"悄无声息"失败：面板空白或回读全零而非异常）

### spatial-toolkit（216 篇）— 工具链（界面/编辑器文档，不单独支撑运行时结论）
- Plugin：`docs/spatial-toolkit/pico-spatial-plugin/什么是-pico-spatial-plugin.md`、`docs/spatial-toolkit/pico-spatial-plugin/管理-spatial-项目.md`
- Emulator：`docs/spatial-toolkit/pico-emulator/什么是-pico-emulator.md`、`docs/spatial-toolkit/pico-emulator/了解-pico-emulator-与真机的差异.md`、`docs/spatial-toolkit/pico-emulator/ui-调试.md`
- Spatial Editor：`docs/spatial-toolkit/pico-spatial-editor/什么是-pico-spatial-editor.md` + 支持的-3d-模型格式/资源_*/场景_*/组件_*/组件类型_*/音频_audio-mixer_*/材质_*（含 shader-graph 全部节点参考 ~180 篇，仅用于编辑器节点选型）
- Timelines：`docs/spatial-toolkit/pico-spatial-editor/动画_timelines_什么是-timelines.md`、`docs/spatial-toolkit/pico-spatial-editor/动画_timelines_为实体添加动画效果.md`、`docs/spatial-toolkit/pico-spatial-editor/动画_timelines_timelines-支持的动作.md`

### spatial-design（56 篇）— 设计规范（体验决策，非运行时 API）
- `docs/spatial-design/pico-design-设计原则.md`、`docs/spatial-design/安全防护.md`
- 基础：`docs/spatial-design/基础/单位.md`（dmm/dp）、`docs/spatial-design/基础/排版.md`、`docs/spatial-design/基础/窗口.md`、`docs/spatial-design/基础/动效.md`、`docs/spatial-design/基础/声音.md`、`docs/spatial-design/基础/`
- 组件规范：`docs/spatial-design/基础/`（Action & Menu / Selection & Input / Navigation & Search / Surface Content / Status / Presentation 各组件）
- 输入与交互：`docs/spatial-design/输入与交互/概览.md`、`docs/spatial-design/输入与交互/体感交互.md`、`docs/spatial-design/输入与交互/外接设备.md`、`docs/spatial-design/输入与交互/交互方式的切换.md`、`docs/spatial-design/输入与交互/系统指令-系统手势.md`、`docs/spatial-design/输入与交互/通用事件设计.md`
- 美术：`docs/spatial-design/美术设计/模型.md`、`docs/spatial-design/美术设计/动画.md`、`docs/spatial-design/美术设计/spatial-editor-与-usd.md`、`docs/spatial-design/美术设计/美术规范.md`（Shared/Full Space）、`docs/spatial-design/美术设计/性能建议.md`、`docs/spatial-design/美术设计/资产制作.md`
- 资源：`docs/spatial-design/资源_字体.md`

### spatial-tutorial（8 篇）— 分阶段教程
- 从模板开始搭建空间应用：`docs/spatial-tutorial/从模板开始搭建空间应用/教程介绍.md` + 第一阶段（Planar 2D）/第二阶段（Volumetric 3D）/第三阶段（Stage Full Space）
- 在空间应用中实现 3D 物体的交互：`docs/spatial-tutorial/在空间应用中实现-3d-物体的交互/教程介绍.md` + 第一阶段（基础交互）/第二阶段（复合交互）/第三阶段（自然交互）

## API 参考（docs/api/）

Kotlin **Dokka API 文档全量离线镜像**（PICO Spatial SDK 6.0.0，4409 页，抓自官方 https://developer-cn.picoxr.com/spatial-api/6.0.0/）。与 `docs/` 的说明性文档互补：**查签名/参数/返回类型/异常 → `docs/api/`**。结构 `docs/api/<模块>/<包>/<类或成员>.md`，完整模块/包索引见 `docs/api/README.md`。

| 模块 | 路径 | 页面数 |
|---|---|---|
| core | `docs/api/spatialpack/core/` | 1737 |
| ui:design | `docs/api/spatialui/design/` | 666 |
| ui:foundation | `docs/api/spatialui/foundation/` | 490 |
| foundation | `docs/api/spatialfoundation/foundation/` | 370 |
| tracking | `docs/api/trackingpack/tracking/` | 364 |
| spatialml:securemr | `docs/api/spatialml/securemr/` | 347 |
| sense | `docs/api/sensepack/sense/` | 148 |
| spatialml:readback | `docs/api/spatialml/readback/` | 22 |
| ui:platform | `docs/api/spatialui/platform/` | 264 |

**检索方式**：
- 已知类/方法名：`grep -rl "<符号>" docs/api/` 定位页面，再读取
- 已知包：直接读 `docs/api/<模块>/<包路径>/index.md`（如 `docs/api/spatialpack/core/com.pico.spatial.core.container/index.md`）
- 成员页面含完整 Kotlin 签名（```kotlin 代码块）、说明、Parameters、Return、Throws
- **优先级**：API 签名/参数/异常以 `docs/api/` 为准（权威）；用法模式、最佳实践与版本差异仍以 `docs/` 说明文档与 `official/` references 为准

## 官方 Agentic 工作流 skill（official/）

官方 **PICO Intelligent Plugins**（Apache-2.0）原样打包在此：`official/pico-spatial-agentic-tools/` 与 `official/pico-unity-agentic-tools/`。它们提供**可执行工作流**（如何跑 `pico-cli`、如何从模板建 app、如何迁移、如何诊断性能），与 `docs/` 知识库互补：**知识/API 问题先查 `docs/`；执行/实操任务走 `official/` 对应 skill**。完整协调规则、角色模型（Planner/Generator/Evaluator）与知识源选择顺序见 `official/pico-spatial-agentic-tools/AGENTS.md`。

**依赖**：多数工作流 skill 需要 `pico-cli`（`npm install -g @picoxr/pico-cli`）与可选 `pico-dev-knowledge` MCP（`official/**/.mcp.json` 经 `npx @picoxr/pico-cli mcp:dev-knowledge` 启动）。未安装时相关命令步骤无法执行，但 skill 内的流程与参考仍可读。官方激活规则：环境相关任务（pico-cli/MCP/模拟器/设备）先跑 `pico-env-doctor` 预检并复用健康结果；`pico-env-doctor` 不是纯本地代码工作的通用门槛。

### spatial（Kotlin/Android，16 个）

| Skill | 用途（何时用） |
|---|---|
| `pico-cli` | `pico-cli` 命令族选择、help/version/setup 发现、输出格式、设备目标、故障排查 |
| `pico-env-doctor` | 执行 pico-cli/MCP/模拟器工作流前的环境预检（verify-first，修复需授权） |
| `spatial-sdk-guideline` | 日常 3D 开发指南：容器/ECS/资源/材质/动画/物理/交互/坐标单位/性能预算；`reference/` 为 curated 最佳实践（与 docs/ 互补） |
| `spatial-app-onboarding` | 从模板创建/继续第一个可运行空间应用（空目录快速上手、新 app、3D 模型 demo） |
| `spatial-app-dev-workflow` | 项目 `AGENTS.md` 之后的按需求迭代实现工作流（构建→模拟器/真机→证据→logcat 修崩溃） |
| `spatial-design-to-app` | 从 Figma/截图/PRD/意图/混合输入生成或补丁空间应用（含容器/窗口模型/面板层级/布局区域决策，带检查脚本） |
| `pico-spatial-app-designer` | 设计交付物工作流：意图→研究→空间结构→组合→设计系统→预览→交付就绪（engines/critics/roles） |
| `porting-android-app` | Android 应用迁移到 PICO Spatial（代码重构、SDK 集成、依赖解析、UI 适配） |
| `spatial-sdk-update` | Spatial SDK 版本升级/迁移助手（含风险与约束） |
| `spatial-editor` | Spatial Editor 场景/实体/资产/材质/效果创作、视觉检查与打包交接 |
| `spatial-sdk-scene-builder` | 根据 3D 资产包围盒推导空间变换、生成结构化场景配置（带 scripts/） |
| `spatial-emulator-usage` | 模拟器/真机工作流：生命周期、APK 安装/启动、文件传输、截图/录屏/logcat |
| `spatial-app-perf-diagnose` | 真机性能诊断：`pico-cli perf` + Perfetto Trace 分析卡顿/掉帧/CPU/GPU/场景复杂度 |
| `spatial-ui-ability` | SpatialUI 能力速查与 Kotlin 片段：手势/Vibrant/悬停/窗口约束/深度/毛玻璃/z 偏移/3D 变换/Augment |
| `spatial-ui-design-style` | SpatialUI 设计系统指南：PicoTheme、token、排版角色、内置组件优先、自定义 Compose（带 verify 脚本） |
| `plugin-audit` | 插件可见性审计，生成本地支持包（默认仅元数据，不含会话内容） |

### unity（Unity 引擎，3 个）

| Skill | 用途 |
|---|---|
| `pico-unity-init` | 初始化 PICO Unity 项目（探空/收集偏好、拷贝模板、装 SDK、写配置；手动触发命令 `/pico-unity-init`） |
| `pico-unity-buildingblocks` | 通过 `pico_xr_*` MCP 工具编排 PICO XR 构建块（XR Origin、VST/Passthrough、Controller、Locomotion、Spatial Mesh、Hand tracking） |
| `pico-unity-package-manager` | 通过 `pico_xr_package` MCP 工具管理 Unity 包与 sample（install/remove/update/query/import-sample） |

**强制规则（官方）**：生成的 app 必须用 SpatialUI（`com.pico.spatial.ui.*`）包裹 `PicoTheme`，禁用 Material/Material3（`androidx.compose.material` / `material3` / `MaterialTheme`）。

## 边界与注意事项

- 本文库仅覆盖**中文 6.0 语料**（llmstxt 导出快照）。版本差异、设备差异、外部 Android API 与政策事项应回到 PICO 官方权威来源（developer-cn.picoxr.com）核验
- `spatial-toolkit`（Editor/Shader Graph/Timelines/Plugin/Emulator）与 `spatial-design` 是工具/设计文档：**不能单独支撑运行时 SDK 结论**
- SpatialML 隐私：部署的算法可能使用双目/深度相机等空间数据，应用必须先获得用户相机、空间数据授权，才能读取算法输出
- 实验性 API 有稳定性与生产使用风险，使用前读 `docs/spatial-sdk/实验性-api-的使用注意事项.md` 并结合更新说明核对状态
- 性能结论先经"性能与调试 概览"路由；模拟器现象需结合"Emulator 与真机差异"或真机验证
- `official/` 为官方 PICO Intelligent Plugins 原样打包（Apache-2.0，见 `official/` 内 LICENSE/SECURITY/PRIVACY）；多数工作流依赖 `pico-cli` 与可选 `pico-dev-knowledge` MCP，未安装时命令步骤不可执行、流程与参考仍可读
- 官方推荐：非平凡 SDK/API 事实优先 `pico-dev-knowledge` MCP 检索；本 skill 的 `docs/`、`docs/api/` 与 official 内 references 可作离线知识源，均不得覆盖项目本地已验证证据
- `docs/api/` 为 6.0.0 版本 Dokka 快照；其他版本（0.13.3 等）或未覆盖的符号需回在线站点核对
