Spatial UI 内包含主题和组件。主题用于定义空间应用（Spatial App）的外观风格，同时也会影响各组件的默认表现。组件用于灵活构建一个完整的空间应用。

* 了解主题请参见《[主题](./spatial-ui_主题.md)》。
* 了解组件请参见：

| **组件名称** | **描述** |
| --- | --- |
| [Button](./spatial-ui_button.md) | Button 用来响应用户的点击行为。 |
| [IconButton](./spatial-ui_iconbutton.md) | IconButton 是用于响应用户点击交互的控件，和 Button 不同的是，IconButton 的内容区域通常使用 `Icon` 填充（也支持填充 `Text`），而 Button 的内容区域通常为 `Text`。 |
| [ToggleButton](./spatial-ui_togglebutton.md) | ToggleButton 是一种带有二级“状态”的用于响应用户点击交互的的控件，内容区域通常为 `Text`， 或其他可组合项，常用于新建、添加等场景，可设置 leading、trailing 的图标。 |
| [ToggleIconButton](./spatial-ui_toggleiconbutton.md) | ToggleIconButton 是一种带有二级“状态”的用于响应用户点击交互的的控件，内容区域通常为 Icon， 或其他可组合项。 |
| [Link](./spatial-ui_link.md) | Link 是一种没有背景或边框的用于响应用户点击交互的的控件，内容区域通常为文本 `Text` 或其他可组合项，常用于导航链接、了解或查看详情等场景。 |
| [Divider](./spatial-ui_divider.md) | * Divider 是用于划分界面区域的组件，外观通常是线性组件。 ;  * HorizontalDivider 是 PICO 设计规范下，专门用于水平方向划分界面区域的组件。 ;  * VerticalDivider 是 PICO 设计规范下，专门用于垂直方向划分界面区域的组件。 |
| [Chip](./spatial-ui_chip.md) | Chip 是常用于标签展示场景下的控件，根据样式与功能不同，包含了 ButtonChip、ToggleableChip 以及 RemovableChip。 |
| [Badge](./spatial-ui_badge.md) | * Badge 通常用于展示动态信息的足迹，它可以以小图标或者数字的形式叠加在其他组件上，达到提示用户的目的。 ;  * DotBadge 用于原点提示，通常用于简单的消息提醒。 ;  * NumberBadge 用于展示数字类型。 |
| [CheckBox](./spatial-ui_checkbox.md) | * CheckBox 是提供给用户用于从列表中选择一个或多个选项的基础控件。 ;  * TriStateCheckbox 是一种具有三种状态的 Checkbox，适用于全选/非全选/未选中的场景。 |
| [Switch](./spatial-ui_switch.md) | Switch 是用于在两种状态之间切换的基础控件，可用于开启或关闭某项设置、启用或停用某个功能、 选择一个选项等场景中。 |
| [Option](./spatial-ui_option.md) | Option 是一种具有“选中”状态的基础组件。您可以组合多个 Option，自由实现“多选”、“单选”场景。 |
| [Slider](./spatial-ui_slider.md) | * Slider 用于让用户以拖拽的方式确定属性值，例如可以用于屏幕亮度调节、音量调节等场景。 ;  * SegmentSlider 是用于让用户以拖拽的方式确定属性值的分段式拖拽条，可以用于分步骤或者含有几个结点的场景。 ;  * SymbolSlider 是用于让用户以拖拽的方式确定属性值并带有符号的拖拽条，例如可以用于屏幕亮度调节、音量调节等场景，并可以在首部自定义符号显示。 |
| [ListItem](./spatial-ui_listitem.md) | ListItem 是用于承载竖直列表中通用的信息展示组件，常作为 Column、LazyColumn 的内容。 |
| [TitleBar](./spatial-ui_titlebar.md) | TitleBar 是对一行内左、中、右三部分用户自定义样式进行布局的标题栏控件，提供了标题内容绝对居中和相对居中两种模式。 |
| [ProgressIndicator](./spatial-ui_progressindicator.md) | * LinearProgressIndicator 是一种线性的表示进度的基础控件，它的进度是确定的，由背景和前景两部分组成， 不可交互，常使用在“加载内容”、“文件上传”等场景中。 ;  * CircularProgressIndicator 是一种圆形的表示进度的基础控件，常使用在“加载内容”、“文件上传”等场景中。 ;  * SymbolicCircularProgressIndicator 是一种圆形的表示进度的基础控件，常使用在“加载内容”、“文件上传”等场景中，它可以添加自定义图标，来表示当前进度的状态。 |
| [PageControl](./spatial-ui_pagecontrol.md) | * PageControl 是显示一系列水平点来表示翻页进度的控件。 ;  * ProgressPageControl 是 PageControl 的扩展，给予每个选中点都有进度值。 |
| [SegmentControl](./spatial-ui_segmentcontrol.md) | SegmentControl 是一种用于在多个互斥选项中进行切换的组件，它通常由一系列并排的图标或者文本选项组成，用户通过点击选择其中一项可修改展示效果。 |
| [SideNavigation](./spatial-ui_sidenavigation.md) | SideNavigation 是一种用于侧边栏的导航控件，由顶部 title 部分和多个 section 组成，常用于设置导航、侧边的菜单分栏等场景，形态上可分为头部和导航区。 |
| [TextField](./spatial-ui_textfield.md) | TextField 是常用于文本输入的组件。 |
| [SearchField](./spatial-ui_searchfield.md) | SearchField 允许用户输入文本，并通过按下键盘上的搜索按钮或其他方式触发搜索操作。 |
| [NumberField](./spatial-ui_numberfield.md) | NumberField 允许用户创建一个带有增减按钮的数字输入框。 |
| [TextSelectionAndToolbarProvider ](./spatial-ui_textselectionandtoolbarprovider.md) | TextSelectionAndToolbarProvider 提供文本选择与 toolbar 颜色配置，常见于 TextField 的光标、选中颜色更改或者展示 toolbar 等场景。 |
| [Scroll Indicator](./spatial-ui_scrollindicator.md) | Scroll Indicator 通常用于长内容页面滚动进度的可视化，帮助用户感知内容长度及当前位置，提升导航效率与用户体验。 |
| [Coachmark](./spatial-ui_空间窗口类_coachmark.md) | Coachmark 是以锚点为基础进行内容展示的组件。Coachmark 分为锚点与内容，CoachmarkBox 提供基础的展示锚点，配合 SimpleCoachmark、RichCoachmark 以及 ImageCoachmark 等完成最终的内容展示。 |
| [DatePicker](./spatial-ui_空间窗口类_datepicker.md) | * DatePicker 是用于进行日期选择的控件。 ;  * DateRangePicker 是用于选中一段时间的组件。 |
| [TimePicker](./spatial-ui_空间窗口类_timepicker.md) | TimePicker 是用于时间纬度（时、分、秒）选择的控件。 |
| [ToolBar](./spatial-ui_空间窗口类_toolbar.md) | ToolBar 是一种被放置在 WindowContainer 的底部中央位置的容器，可以用于展示额外的提示控件。 |
| [TabBar](/tab-bar) | TabBar 基于系统挂件 Augment 容器扩展而来的导航控件，协助用户在应用的不同模块之间切换跳转。 |
| [AlertDialog](./spatial-ui_空间窗口类_alert-dialog.md) | AlertDialog 是用于阻断提示用户目的的组件，可包含图标、标题、自定义内容以及按钮。 |
| [Sheet](./spatial-ui_空间窗口类_sheet.md) | Sheet 是用于呈现弹出内容的组件，可以承担弹窗相关的任务。 |
| [Augment](./spatial-ui_空间窗口类_augment.md) | Augment 是用于放置在主窗口之外的容器，可以由它实现弹窗的效果。 |
| [Subwindow](./spatial-ui_空间窗口类_subwindow.md) | Subwindow 是一种显示在窗口容器左侧或右侧的容器，其高度始终与窗口容器的高度相同。 |
| [Snack](./spatial-ui_空间窗口类_snack.md) | Snack 和 Android Toast 类似，可用作显示在 WindowContainer 底部的简短信息通知。它通常显示几秒后自动消失。除了展示主体信息之外，它还提供了可交互槽位，允许自定义交互行为。 |
| [Menu](./spatial-ui_空间窗口类_menu.md) | 菜单组件，在空间中以浮窗的的形式展示可选列表项，列表内容一般搭配 MenuItem 使用，也可以完全自定义列表内容。 |

