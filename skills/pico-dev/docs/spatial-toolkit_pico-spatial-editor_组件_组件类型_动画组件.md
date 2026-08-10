本文介绍 Spatial Editor 中的动画组件。
动画组件可以被添加到实体或从实体中删除。在 .usda 文件中，动画组件的类型为 `SpatialComponent`。这是一种由 Spatial Editor 定义的、非 USD 原生的组件类型。
## Animation Resource Library

该组件用于向 Timeline 中的 **Play Animation** 动画模板提供动画。绑定了动画的实体会自动内置该组件。你无法自行添加或删除该组件。详情参阅 [预制动画模板](./spatial-toolkit_pico-spatial-editor_动画_timelines_timelines-支持的动作.md)。
目前 Animation Resource Library 仅支持骨骼动画。

你可以通过该组件管理实体的动画：

* 单击下方的加号按钮为实体添加动画。

* 单击骨骼动画右侧的加号按钮创建一个动画的副本并通过调整开始时间和结束时间进行裁剪。右击副本可以在下拉菜单中选择重命名或删除副本。

