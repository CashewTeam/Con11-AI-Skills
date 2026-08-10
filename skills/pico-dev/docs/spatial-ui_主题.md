主题（PicoTheme）用于定义空间应用（Spatial App）的外观风格，包括影响各组件的默认表现。
## 主题介绍
主题包含颜色、文字排版、通用以及系统材质四项配置。
### 主题颜色
主题颜色（ColorTheme）包含以下几类：

* **Semantic color** 定义惯用且带通俗语义的色彩，比如警示、报错等。

* **Accent color** 定义系统或应用的主题色。

* **Background color** 定义容器（window、sheet、dialog 等）的背景色。

* **Forecolor** 定义前景色（字体或元素填充）。

* **Sub color** 定义系统视觉辅助色彩，如标签、图标等颜色。

**角色 Role**
可供您修改的两个角色：Accent、On Accent。修改对应角色参数后，系统会将颜色同步修改到使用该角色的所有组件，受影响组件包括 Snack、TabBar、Button 以及光标等。
| **角色名称** | **说明** |
| --- | --- |
| Accent | 用于小面积且重要元素的背景色，例如 Button、Snack 的背景色。 |
| On Accent | 使用在 Accent 上的前景色，需要保证其识别性。 |

### 文字排版
针对不同的内容展示诉求，主题中定义了一系列文本排版规则（Typography），应用于对应的组件。定义说明如下：
| **样式名称** | **使用场景** |
| --- | --- |
| **DisplayLarge**; **DisplayMedium**; **DisplaySmall**  | 装饰性标题 ;   |
| **HeadlineLarge**; **HeadlineMedium**; **HeadlineSmall** | 容器页面标题 |
| **TitleLarge** ;  **TitleMedium** ;  **TitleSmall** | 模块标题 ;   |
| **LabelLarge** ;  **LabelMedium** ;  **LabelSmall** | 常用于 Action，如 Button 中的文字 ;   |
| **BodyLarge** | 常用于输入文案、以及行数不多（不超过 5 行）的正文 |
| **BodyMedium** | 单行正文 |
| **BodySmall** | 常用于辅助文案，补充信息或解释功能 |
### 通用
对于可交互的组件，例如 Buttons 等，通过通用（State）配置为用户提供统一的交互视觉体验。基础样式上可叠加通用配置，配置包括的状态有：
| **状态** | **描述** |
| --- | --- |
| Hover | 当手柄射线移到组件内，高亮图层，提示此组件是可交互的 ;   |
| Pressed | 当用户按下手柄等交互器时，沟通过另一种高亮颜色图层提示 Press 状态，提示用户“正在发生交互” ;   |
| Enable & Disabled | 提示用户，该组件无法交互。 ;   |
### 系统材质
系统材质主要应用于 Dialog、Menu、ToolBar 等空间浮窗中，以呈现统一的视觉效果。
目前系统层的效果比较简单（即白色背景），Menu 组件已接入材质效果。

| **材质名称** | **使用场景** |
| --- | --- |
| MaterialRegular | 最底层的容器背景色。例如：Subwindow、Augment、TabBar、ToolBar 组件 |
| MaterialThick | 浮起的大面积容器背景色。例如：Alert Dialog、Sheet、Menus 组件 |
| MaterialThickest | 浮起的小面积容器背景色。例如：TextSelectionAndToolbarProvider 组件 |
场景示例：

## 使用主题
推荐在 `WindowContainer` 内容根节点添加 `PicoTheme` 函数，`WindowContainer` 内的 UI 将会生效主题相关配置。
```Kotlin
WindowContainer(id = "Window1") {
    // 在 WindowContainer DSL 中使用 PicoTheme
    PicoTheme {
        Content()
    }
}
```

`PicoTheme` 借助 Compose 的 [CompositionLocal](https://developer.android.com/reference/kotlin/androidx/compose/runtime/CompositionLocal) 机制，将主题配置向下透传给 Compose View Tree。
在 `PicoTheme` 的任意子节点，可以通过`PicoTheme` 对象快速获取到主题系统重定义的颜色、文字排版。

### 使用主题颜色与文字排版
默认情况下 SpatialUI 组件库内置的组件已覆盖主题配置。您的自定义 UI 需要保持和主题一致时，可以参考下列用法：
```Kotlin
@Composable
fun Demo() {
    Box(modifier = Modifier.size(200.dp)
        // 使用主题色作为背景，当主题变更时，它会跟着刷新
        .background(PicoTheme.colorScheme.accent)
    ) {
        Text(
            "Text For Theme",
            // 使用主题色作为内容颜色，当主题变更时，它会跟着刷新
            color = PicoTheme.colorScheme.onAccent,
            // 使用主题的文本样式，当主题变更时，它会跟着刷新
            style = PicoTheme.typography.bodyMedium
        )
    }
}
```

### 使用通用状态
SpatialUI 使用 Compose [Indication](https://developer.android.com/develop/ui/compose/touch-input/user-interactions/handling-interactions?hl=zh-cn#consume-emit) 机制处理交互状态，利用[ CompositionLocal](https://developer.android.com/reference/kotlin/androidx/compose/runtime/CompositionLocal) 机制确保 PicoTheme 内所有组件的交互状态一致性。

* SpatialUI 组件库已适配交互状态，您无需关注。
* Compose 默认情况下，`Modifier.clickable` 修饰符通过 `LocalIndication` 自动适配交互状态。您的自定义组件具有背景形状时，请组合 [clip](https://developer.android.com/reference/kotlin/androidx/compose/ui/Modifier#(androidx.compose.ui.Modifier).clip(androidx.compose.ui.graphics.Shape)) 使用。

```Kotlin
@Composable
fun Demo() {
    Box(modifier = Modifier
        // 可选，如果需要定义背景形状的话。
        .clip(RoundedCornerShape(10.dp))
        .background(Color.White)
        // 不要使用这种方式订定义形状
        // .background(Color.White, RoundedCornerShape(10.dp))
        .clickable {  }
    ) {
    }
}
```

### 使用通用 Disable 状态
PICO 标准的组件 Disable 状态是给组件设置透明度。当自定义组件需要使用 PICO 标准规范时，可参考下列代码：
```Kotlin
@Composable
fun Demo(enable: Boolean = true) {
    // 根据状态获取透明度
    val alpha = if(enable) {
        1f
    } else {
        // 从CompositionLocal中获取
        LocalDisableAlpha.current
    }
    Box(modifier = Modifier
        .graphicsLayer {
            // 设置透明度
            this.alpha = alpha
        }
        .background(Color.Red)
    ) {
    }
}
```

## 自定义主题
### 自定义主题颜色与文字排版
在保持设计规范的前提下，PicoTheme 为您的自定义主题保留一定的自由度。
```Kotlin
WindowContainer(id = "Window1") {
    // 在 WindowContainer DSL 中使用 PicoTheme
    PicoTheme(
        // 自定义主题色
        colorScheme = PicoTheme.colorScheme.copy(
            accent = xx,
        ),
        // 自定义文本排版
        typography = PicoTheme.typography.copy(
            displayMedium = xxx
        )
    ) {  }
}
```

### 自定义交互状态
您可以通过[自定义 Indication](https://developer.android.com/develop/ui/compose/touch-input/user-interactions/handling-interactions?hl=zh-cn#replace-effect)，实现自己的交互状态，然后使用 `CompositionLocalProvider` 替换节点之后的 Indication。
```Kotlin
// 自定义Indication
object MyIndication : IndicationNodeFactory {
    override fun create(interactionSource: InteractionSource): DelegatableNode {
        return xxx
    }
}

@Composable
fun Demo() {
    // 替换成自定义Indication
    CompositionLocalProvider(LocalIndication provides MyIndication) {
        // content
    }
}
```

### 自定义 Disable 透明度
```Kotlin
@Composable
fun Demo() {
    CompositionLocalProvider(LocalDisableAlpha provides 0.5f) {
        // content
    }
}
```


