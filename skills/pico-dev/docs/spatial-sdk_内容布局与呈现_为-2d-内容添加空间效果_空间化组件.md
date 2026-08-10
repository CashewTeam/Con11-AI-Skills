你可以在 WindowContainer 中添加空间化组件，以增强应用的空间感。
### Augment
窗口功能区（Function Area）是针对 Planar 和 Volumetric 窗口的统一设计规范。通常将窗口所在平面划分为四个区域：顶部导航区、左侧导航区、底部操作区和右侧扩展区。在 PICO OS 6 中，还定义了一系列可超出主窗口范围的子窗口 Augment，它们环绕分布在这些区域内，与主窗口共同构成完整的应用窗口结构。

* Augment 会影响 WindowContainer 的包围盒大小。
* WindowContainer 的标题栏（Caption Bar）会对 Augment 进行动态避让。

详细使用说明参考《[Augment](./spatial-ui_空间窗口类_augment.md)》。
### Subwindow
Subwindow 是用于承载辅助操作和信息的控件。它位于 WindowContainer 之外，但依附于其存在。

Subwindow 内置 RTL 支持。在默认模式（`SubwindowPlacement.Default`）下，会根据 RTL 配置自动决定显示在 WindowContainer 的左侧或右侧。
详细使用说明参考《[Subwindow](./spatial-ui_空间窗口类_subwindow.md)》。
### ToolBar
ToolBar 是工具控件，固定在 WindowContainer 底部。当应用需要对当前 WindowContainer 的内容进行控制、修改、创建或删除等操作时，优先推荐使用系统提供的 ToolBar 控件。

详细使用说明参考《[ToolBar](./spatial-ui_空间窗口类_toolbar.md)》。
### TabBar
TabBar 是导航控件，用于帮助用户在应用的不同模块之间切换。根据实际需求，你可以将其放置在 WindowContainer 的顶部或左侧。

详细使用说明参考《[TabBar](/document/spatial-ui/tab-bar/)》。

