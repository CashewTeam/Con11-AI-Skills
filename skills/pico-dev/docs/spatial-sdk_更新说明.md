本文记录 PICO Spatial SDK 在各个版本中的变更。
## 6.0.0 - 2026-08-04
6.0.0 版本的变更如下。若要将你项目中的 0.13.3 版本的 SDK 升级为 6.0.0 版本，参考《[升级 SDK](./spatial-sdk_升级-sdk.md)》。
**新增**
**SpatialUI**

* `SpatialModelView(...)` 新增以回调形式暴露模型加载状态的重载。你可通过 `onLoad`、`onError`、`onSuccess` 分别处理加载中、失败与成功状态，而无需自行判断 `ModelLoadingState`。
* 弹窗类组件支持 JetPack Compose 的 [DialogWindowProvider](https://developer.android.com/reference/kotlin/androidx/compose/ui/window/DialogWindowProvider)，你可通过 JetPack Compose API 获取弹窗组件的 `Window`。

**SpatialML**

* Secure MR 模式现已支持传送门（Portal），可帮助你实现更好的虚实空间融合。

**变更**
**SpatialUI**

* `detectSpatialDragGesture`、`detectSpatialRotateGesture` 和 `detectSpatialScaleGesture` 的 `onStart` 、`onEnd` 和 `onCancel` 回调现在会携带对应的手势数据对象（`SpatialDragValue` 、`SpatialRotateValue` 和`SpatialScaleValue`）。其中 ：
   * `detectSpatialRotateGesture`和 `detectSpatialScaleGesture` 的`onStart` 、`onEnd` 和 `onCancel` 回调由原先的无参数 lambda 变更为接收手势值的 lambda。
   * `detectSpatialDragGesture` 的 `onDragStart`回调在原有的 `Offset3D` 参数之外额外增加手势值参数，`onDragEnd` 和 `onDragCancel` 由无参数变更为接收手势值。此改动涉及接口签名变更，因此你在升级 SDK 时需要手动解决编译问题，详见《[升级 SDK](upgrade-sdk)》。
* `windowConstraints(...)` 的默认值语义调整：最小值默认由 `Dp.Unspecified` 变更为 `Dp.Hairline`，最大值默认变更为 `Dp.Infinity`。此前在仅设置 `minWidth` / `minHeight` 时，窗口实际尺寸可能被误当作最终尺寸（例如根 view 设置 `windowConstraints(minWidth = 800.dp, minHeight = 800.dp)` 时窗口被固定为 800 × 800 dp）；调整后仅作为下界约束生效。
* 展开态透明度动画的延迟时间重新调优：`ExpandedAlphaShowDelayMillis` 由 680 ms 调整为 1200 ms，`ExpandedAlphaHideDelayMillis` 由 280 ms 调整为 800 ms；同时优化了 TabBar 展开动画效果。
* TabBar 的玻璃材质由 `Thickest` 调整为 `Regular`。
* Subwindow 圆角由 16 dp 调整为 32 dp。
* 调整了 Snackbar 的显示底部偏移位置。

**移除**
**SpatialML**

* 移除 `Pipeline.ModelInferenceType.QNN_HTP` 及 QNN 相关 API。SpatialML 系统层推理后端已切换为 TFLite / LiteRT，请改用 `LITE_RT_CPU`、`LITE_RT_GPU`、`LITE_RT_NPU` 等推理类型。

**修复**
**SpatialUI**

* 修复 `Switch` 组件的 hover 问题。
* 修复 `LinearProgressIndicator` 更新进度时圆角显示异常的问题。
* 修复部分组件音效覆盖不生效的问题，优化组件内音频特效播放，并更新 `TimePicker` 默认步进的手柄震动与 recompose 时的播放器行为。
* 稳定 `Slider` 布局，并修复 `Slider` 点击与拖拽时的交互音效反馈问题。
* 修复 Compose 版本升级导致的 scroll 类组件边缘模糊（羽化）失效问题。
* 修复混合 ComposeView / AndroidView 场景下接收 cancel 事件时 `PointerInputFilter` 数据丢失的问题。
* 修复 `TextField` 在 `Disabled` 状态下仍触发音效与手柄震动的问题；调整 `TextField` 默认 handle 颜色，规避 Vibrant 导致的选择手柄颜色分层。
* 修复点击时出现坐标偏移的问题。
* 修复旋转手势在指针恢复后重新捏合时旋转突变的问题。

**SpatialPack**

* 修复 attachment 通过 2D（Compose）navigation 进入时偶现不显示的问题；修复 navigation pop 页面后 3D 内容短暂残留的问题。
* 修复 `DrawOrderGroupComponent` 的 draw order 同步时机问题，将同步推迟至实体绑定完成后执行。
* 为资源引用增加缓存以支持弱引用清理，修复高频使用资源场景中部分资源可能被提前回收导致使用时无效的问题。
* 增强 `SpatialContainer` 容器注册阶段的健壮性：读取到不识别的容器时会继续扫描，不影响后续容器内容的读取。

**SpatialML**

* 修复 SpatialML Demo 的 ANR 问题（将推理协程指定运行在 IO 线程）。

---

## 0.13.3 - 2026-06-05
0.13.3 版本的变更如下。若要将你项目中的 0.12.2 版本的 SDK 升级为 0.13.3 版本，参考 0.13.x 版本的《升级 SDK》文档。
**新增**

* **SpatialUI**
   * **TabBar**
      * TabBar 接入玻璃纸效果，支持二级菜单，优化 badge 样式，并在无展开内容时不浮起。
      * `TabBar(...)` 新增 `extraContentHeight` 参数；`TabBarScope.item(...)` 新增 `extraContent` 内容槽。默认 padding 与 `extraContent` 区域范围也进行了调整。
   * **Sheet**
      * `Sheet(...)` 与 `HeadImageSheet(...)` 新增 `contentPadding` 与 `contentSpace` 参数，用于更精细地控制内容区域布局。
   * **Augment**
      * `Augment(...)` 新增 `windowSizeBehaviors` 参数，用于控制窗口挂件尺寸策略。
      * 新增 `WindowSizeBehaviors`，默认自适应内容尺寸，并支持与容器主区同宽或同高。
   * 新增 `enableSpatialHittestProvider(...)`，支持 View 级别屏蔽 / 管理空间交互事件。
   * `HandControllerHapticType` 新增 `coerceToValidRange()`，用于将震动类型约束到有效范围。
* **SpatialPack**
   * 新增 `GaussianSplattingResource` 与 `GaussianSplattingComponent`，支持加载和挂载 3D Gaussian Splatting 资源。
   * `PortalComponent` 新增 `panelColor` 与 `backgroundMode`，并新增 `PortalBackgroundMode`，支持 `SOLID_COLOR` 与 `PASSTHROUGH` 等 Portal 背景模式。
   * `VideoComponent` 与 `VideoPlayerComponent` 新增 `stereoDisparity` 访问接口，用于调节 3D 片源瞳距。
   * `AttachmentPanelComponent` 支持加载来自 Spatial Editor 的 `AttachmentPanel` 布局信息（宽、高与对齐方式）。
   * 新增 `SortAsUIElementComponent`，用于让 3D 实体与 2D UI 一起参与渲染排序。详情参阅《[实体与 2D UI 的渲染顺序](./spatial-sdk_渲染_实体与-2d-ui-的渲染顺序.md)》。
   * `MeshInstancesResource` 新增 `customDataCount` 与带 `customFloatData` 的创建 / 更新接口，便于与 ShaderGraph 参数联动。

**变更**

* **SpatialUI**
   * `SubMenu` 不再阻断父级 Menu 交互，父级 Menu 仍可响应 Hover 与 Touch。

**移除**

* **SpatialUI**
   * 移除 `com.pico.spatial.ui.foundation.annotation.ExperimentalVibrantApi`。Vibrant 相关能力已进入稳定 API 阶段。
   * 移除不包含 `windowSizeBehaviors` 参数的旧版 `Augment(...)` 重载。
   * 移除不包含 `extraContentHeight` 参数的旧版 `TabBar(...)` 重载。
   * 移除不包含 `extraContent` 内容槽的旧版 `TabBarScope.item(...)` 重载。
   * 移除不包含 `contentPadding` 与 `contentSpace` 参数的旧版 `Sheet(...)` 与 `HeadImageSheet(...)` 重载。

**修复**

* **SpatialUI**
   * 修复 `ButtonSize.copy(...)` 默认参数映射，`minWidth` 默认值不再错误沿用 `width`。
   * 修复 `RemovableChip` 在 `enable = false` 时点击仍触发手柄震动的问题。
   * `TextField` `trailingContent` 改为仅限制最小尺寸；输入框光标位置变化和选择范围变化时支持音效与手柄震动。
   * 修复 `SnackBar` 被父窗口裁切的问题。
   * 修复组件 `chips` 宽度从固定限制改为最小宽度限制。
* **SpatialPack**
   * 修复 Drag and Drop 时复制的 3D Collision 设置导致无法判定 drop 区域的问题。
   * 修复 `StageProperties` 拷贝数据错误问题。
* **文档**
   * 修复 API 文档搜索栏中部分搜索结果（如 `SpatialModelView`）无法点击跳转的问题。

---

## 0.12.2 - 2026-05-14
0.12.2 版本的变更如下。若要将你项目中的 0.11.7 版本的 SDK 升级为 0.12.2 版本，参考 0.12.x 版本的《升级 SDK》文档。
**新增**

* **SpatialUI：**
   * 新增控制器振动反馈 API，支持在 UI 交互时触发手柄振动。相关接口包括 `ControllerHapticConfiguration`、`HandController`、`HandControllerHapticType`、`SpatialHandControllerHaptic`。详情参阅《[手柄振动反馈](./spatial-sdk_交互_手柄振动反馈.md)》。
   * `Toolbar` 新增 `supportingContent`，用于实现分段式工具栏。
* **SpatialPack：**
   * 2D Drag and Drop 现支持拖拽 3D 内容。当拖动目标为 `SpatialView` 时，其关联的 3D 模型可随之拖动。
   * 新增 `AnimationBindTarget.bindBlendShapeWeights()` 方法，可用于绑定目标以驱动 Blend Shape 动画。详情参阅 《[Blend Shape 动画](./spatial-sdk_动画_blend-shape-动画.md)》。
   * 新增 `MeshModel` API，支持通过自定义顶点、索引、UV、法线等数据动态创建 `MeshResource`。
   * 新增动画更新事件，在底层动画系统结算前后分别抛出全局事件，开发者可在对应节点处理动画数据。
   * 新增 `SpatialAudioTrackExtension`，便于基于原生 `AudioTrack` 接入 PICO 空间音频能力。详情参阅《[使用 SpatialAudioTrackExtension](./spatial-sdk_音频_使用-spatialaudiotrackextension.md)》。
   * `AudioResource` 新增 `getConfig()` 接口，`AudioGroupResource` 新增 `getPlayMode()` 接口，用于查询配置参数。
   * 为多个枚举类型（如 `AnchorUpdate.Event`、`TrackingState`）新增 `UNKNOWN` 预留值，用于未来版本兼容。
* **SpatialML：**
   * `Pipeline.ModelInferenceType` 新增 `LITE_RT_CPU`、`LITE_RT_GPU`、`LITE_RT_NPU` 选项，提供更多推理硬件路径。
   * `Pipeline` 新增 `getDepthMap(...)` 方法，用于获取深度图信息。

**变更**

* **SpatialUI：**
   * **TabBar：**
      * `TabBar(...)` 构造函数新增 `followViewpoints` 和 `focusable` 参数。
      * `TabBarScope.item(...)` 由原有的 `text` / `icon` 重载形式调整为 `content` 内容块形式。
   * **Toolbar 和 Subwindow：**
      * `Toolbar(...)` 和 `Subwindow(...)` 的构造函数签名已调整，请按新签名更新调用代码。
   * **Augment：**
      * `Augment(...)` 构造函数新增 `focusable` 参数，用于控制窗口挂件是否可获取焦点。
   * **SegmentControl：**
      * `SegmentItem(...)` 新增 `onClick` 回调参数，用于处理点击事件。
   * **Snackbar：**
      * `SnackbarHostState.show(...)` 的重载方法签名已调整。
      * `Snackbar` 新增背景颜色和背景玻璃材质控制参数，并支持程序化取消。
   * **TextToolbar：**
      * `TextToolbar` 的布局逻辑调整为基于文本选中区域水平居中。
* **SpatialPack：**
   * 自定义 Component 现在必须提供 `public` 无参构造函数。此前该约束仅作为 Lint 警告提示；现在会在运行时的 register 阶段进行强制校验，缺失默认构造函数时将抛出异常。
   * `AmbientAudioComponent` 构造函数新增 `AmbientOrientationMode` 参数，用于指定音频朝向的计算模式，可选值为 `ORIENTATION_ONLY` 或 `POSITION_AND_ORIENTATION`。未显式传入时，默认使用 `ORIENTATION_ONLY`。
   * 为部分核心枚举类型（如 `ShadowFaceCullingMode`）新增 `UNKNOWN` 或 `AUTO` 枚举值，以增强兼容性。

**移除**

* **SpatialUI：**
   * 移除 `com.pico.spatial.ui.design.windows.TabBarPlacement` 类，相关能力已整合。
   * 移除不含 `focusable` 参数的旧版 `Augment(...)` 构造函数。

**修复**

* **SpatialPack：**
   * 修复通过 `ContentResolver` + `Uri` 从 SAF 文件选择器加载模型时可能出现的 `format not supported` 错误。
* **SpatialUI：**
   * 修复 `PageControl` 在 `disable` 状态下不可见的问题。
   * 修复超出主窗口区域的 `Menu`、`SpatialPopup` 在点击外部区域时无法自动消失的问题。
   * 调整点击交互时短音效的播放时机，由 `PressUp` 改为 `PressDown`。
   * 修正 `backgroundMaterial` 默认携带 `back = 1` 的问题。

---

## 0.11.7 - 2026-04-23
0.11.7 版本的变更如下。若要将你项目中的旧 SDK 升级为 0.11.7 版本，参考 0.11.7 版本的《升级 SDK》文档。
**新增**

* **SpatialPack：**
   * 新增 `AudioGroupResource` 用于管理音频组，组内支持以不同的模式（`FORWARD`、`BACKWARD`、`RANDOM`）播放音频。
   * 支持加载 `.obj` 和 `.stl` 格式的模型文件。
   * 射线检测和凸体投射的结果 `CollisionCastResult` 中新增 `uv` 和 `materialIndex` 属性，以获取碰撞点的纹理坐标和材质索引（仅限使用 static mesh 创建 collider 时可获取此信息）。
   * `UnlitMaterial` 新增 `toneMappingEnabled` 属性，用于控制是否启用色调映射。
* **TrackingPack：**
   * 新增手柄按键事件，可通过 `ControllerAction` 和 `ControllerActionData` 监听特定按键的按压、触摸状态以及扳机键/握持键的数值。
* **SpatialML：**
   * 引入 `PipelineArithmeticScope`，以结构化方式执行张量运算，替代基于字符串的 `arithmetic(expression, ...)` API。
   * 新增 `Pipeline.JavaScriptIO`，支持以 JavaScript 为机器学习算法增加自定义的预处理、后处理算子。
   * 新增音频 I/O，支持在管线内直接采集麦克风输入并输出生成音频。

**变更**

* **构建工具链升级：**
   * **Kotlin**: 版本升级至 2.0，并默认启用 K2 编译器。
   * **Compose Compiler**: 已集成至 Kotlin 插件，遵循[官方迁移指南](https://kotlinlang.org/docs/compose-compiler-migration-guide.html)进行配置。
   * **Android Gradle Plugin (AGP)**: 推荐将项目基线版本提升至 8.8.0，Kotlin 2.0 官方最低支持版本为 AGP 8.5，但实际构建验证表明，低版本在 release 构建阶段存在兼容性问题。
* **SpatialUI：**
   * 色彩系统重构：由 accent/onAccent + Vibrant 迁移至语义化的 ColorScheme / *Colors（如 fillPrimary、labelPrimary），组件颜色统一由语义角色驱动；自定义主题需迁移至新体系。
   * `Menu` 相关的 `HorizontalPlacement` 和 `VerticalPlacement` 类包路径变更：`com.pico.spatial.ui.design.menu` → `com.pico.spatial.ui.design.windows.popup` (请更新 import 语句)。
* **SpatialPack：**
   * `ObjectAudioComponent` 现在包含 `soundRadiusLevel` 属性，用于控制声源的感知半径。
   * `AudioResourceConfig` 现已支持 `randomStart` 和 `loopEnable` 标志，以提供对音频播放的更多控制。
   * 加载 `MeshResource` 失败时，现在仅抛出 `ResourceLoadingException`，简化了异常处理逻辑。

**废弃**

* **SpatialML：**
   * 基于字符串的 `Pipeline.arithmetic(expression: String, ...)` 方法已废弃。请迁移到新的 `Pipeline.arithmetic(result: Tensor, operations: PipelineArithmeticScope.() -> ...)` 方法，它提供了更好的类型安全性和更具表达力的 DSL。

**移除**

* **SpatialUI：**
   * 移除所有 `*Vibrants` 数据类（例如 `ButtonVibrants`, `SliderVibrants`, `ChipVibrants`）及相关的 `*Defaults` 方法；移除`IconKt`、`TextKt`、`ButtonKt` 等组件中的所有 `vibrant*` 参数和相关的重载方法；移除用于耦合颜色和视觉动效的 `ColorStyle` 类。此外，`Vibrant` 枚举进行了简化，移除了 `LightenHover` 和 `Termination`。原有颜色与 vibrant 能力已收敛至 ColorScheme / *Colors，相关逻辑需按语义角色重新映射。
* **SpatialPack：**
   * `VideoMaterial` 移除 `setHardwareBuffer`；`VideoComponent` 移除 `getTransformMode`、`setCropRect`。使用 `VideoComponent` 播放空间视频改为使用 `SurfaceRenderTexture` 管线，不再提供 `setHardwareBuffer` 方案；裁剪行为已内置，无需再调用 `setCropRect`。

**修复**

* **SpatialPack：**
   * 修复了通过 `ContentResolver` + `Uri`（例如，从 SAF 文件选择器）加载模型时会报“format not supported”错误的问题。
   * 修复多个 Attachment 存在父子关系时的渲染异常。
* **SpatialUI：**
   * 修正了 `Checkbox` 的混合模式，以确保其显示正确。
   * 修复了在 `TextField` 等文本输入组件上移动光标时可能产生的抖动问题。

---

## 0.10.7 - 2026-03-02
PICO Spatial SDK 首个正式版本现已上线，面向搭载 PICO OS 6 的设备，帮助开发者构建空间应用。

* **3D 场景 / 实体 / 资源体系：**覆盖资源加载、场景编排、动画播放、物理模拟与碰撞检测等核心 3D 能力，为空间体验提供基础支撑。
* **Spatial UI 框架：**提供窗口管理、2D UI 布局与组件库以及基础空间手势，将 2D 内容衔接至 3D 场景。
* **空间音视频：**通过空间音频渲染与空间视频播放，还原立体声场和画面，为应用构建沉浸式视听体验。
* **环境感知：**依托系统环境网格扫描能力，使应用能够感知和利用真实空间信息。
* **SpatialML：**面向混合现实场景的 ML 推理运行时框架，支持在 PICO 设备本地运行基于主流框架训练的自定义模型，并结合相机与空间定位数据增强环境理解能力。
* **开发工具链与示例工程：**提供 Spatial Editor、Spatial Plugin、PICO Emulator 等配套开发工具，以及模板项目和示例项目，帮助开发者快速搭建与调试空间应用。
