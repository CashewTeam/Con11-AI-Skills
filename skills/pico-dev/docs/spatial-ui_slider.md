本文介绍 Slider、SegmentSlider 以及 SymbolSlider 组件的功能与用法。
## Slider
Slider 是 PICO 设计规范下让用户以拖拽的方式确定属性值，例如可以用于屏幕亮度调节、音量调节等场景。它包含轨迹、滑块，用户在轨迹上滑动滑块能得到当前滑块所在的值。

### API Surface

* `value`：当前值， 传入的值在 `valueRange` 的最大、最小值之间。
* `valueRange`：值的范围，默认 0f ~ 1f
* `onValueChange`：值改变的回调函数，每次值发生变化时都会执行的回调。
* `onValueChangeFinished`：值改变结束的回调函数，当拖拽滑动停止时执行的回调。
* `enabled`：设置控件是否生效。
* `sliderSpec`：定义所占空间的参数，可定义 `thumbAreaSize`、`thumbSize`、`thumbPressedSize` 以及 `trackHeight`。
* `colors`：控件颜色，可通过 `SliderDefaults` 自定义 `trackColor`、`progressColor`、`progressHighColor`、`thumbColor` 以及 `thumbHighColor`。

### 基础用法
```Kotlin
@Composable
fun SliderRegularSample() {
    Column {
        var sliderValue by remember { mutableStateOf(0f) }
        Slider(
            value = sliderValue,
            onValueChange = { sliderValue = it },
            onValueChangeFinished = { },
            sliderSpec = SliderDefaults.Regular
        )
        Text(text = "$sliderValue")
    }
}
```


### 高阶用法
自定义 slider 中的当前值及值范围和尺寸、颜色大小。
```Kotlin
@Composable
fun SliderRegularSample() {
    Column {
        var sliderValue by remember { mutableStateOf(50f) }
        Slider(
            value = sliderValue,
            //自定义值范围
            valueRange = 0f..100f,
            onValueChange = { sliderValue = it },
            onValueChangeFinished = { },
            //自定义尺寸
            sliderSpec = SliderDefaults.sliderSpec(
                thumbAreaSize = 60.dp,
                thumbSize = 20.dp,
                thumbPressedSize = 20.dp,
                thumbHoverSize = 20.dp,
                trackHeight = 40.dp
            ),
            //自定义颜色
            colors = SliderDefaults.sliderColors(
                thumbColor = Color.Red,
                trackColor = Color.Blue,
                progressColor = Color.White,
                segmentDotColor = Color.Yellow
            )
        )
        Text(text = "$sliderValue")
    }
}
```


## SegmentSlider
SegmentSlider 是 PICO 设计规范下，让用户以拖拽的方式确定属性值的分段式拖拽条，可以用于分步骤或者含有几个结点的场景。用户在轨迹上滑动滑块时会吸附到离它最近的节点。

### API Surface

* `initialStep`：当前初始值，传入的值在 0 到 `segmentCount` 之间。
* `segmentCount`：总共的段数。
* `onStepChange`：step 变化的回调函数。
* `enabled`：设置控件是否生效。
* `sliderSpec`：定义所占空间的参数，可定义 `thumbAreaSize`、`thumbSize`、`thumbPressedSize`、`trackHeight` 以及 `segmentDotSize`。
* `colors`：控件颜色，可通过 SliderDefaults 自定义 `trackColor`、`progressColor`、`progressHighColor`、`thumbColor`、`thumbHighColor`、`segmentDotColor` 以及 `segmentDotHighColor`。

### 基础用法
```Kotlin
@Composable
fun SegmentSliderSmallSample() {
    Column {
        var step by remember { mutableStateOf(2) }
        SegmentSlider(initialStep = step, segmentCount = 5, onStepChange = { step = it })
        Text(text = "$step")
    }
}
```


### 高阶用法
自定义 SegmentSlider 的分段数、颜色、所占尺寸的大小。
```Kotlin
@Composable
fun SegmentSliderSmallSample() {
    Column {
        var step by remember { mutableStateOf(2) }
        SegmentSlider(
            initialStep = step,
            modifier = Modifier.size(600.dp, 60.dp),
            //自定义分段数
            segmentCount = 5,
            onStepChange = {
                step = it
            },
            //自定义滑块尺寸相关参数
            sliderSpec = SliderDefaults.sliderSpec(
                thumbAreaSize = 50.dp,
                thumbSize = 40.dp,
                thumbPressedSize = 40.dp,
                thumbHoverSize = 40.dp,
                trackHeight = 60.dp,
                segmentDotSize = 16.dp
            ),
            //自定义颜色
            colors = SliderDefaults.sliderColors(
                thumbColor = Color.White,
                trackColor = Color(0x3D919191),
                progressColor = Color.White,
                segmentDotColor = Color.DarkGray,
                thumbHighColor = Color.White,
                segmentDotHighColor = Color.White
            )
        )
        Text(text = "$step")
    }
}
```


## SymbolSlider
SymbolSlider 是 PICO 设计规范下让用户以拖拽的方式确定属性值并带有符号的拖拽条，例如可以用于屏幕亮度调节、音量调节等场景，并可以在首部自定义符号显示。用户在轨迹上滑动滑块时可根据不同的值进行更新显示的符号。

### API Surface

* `value`：当前值，传入的值在 `valueRange` 的最大、最小值之间。
* `valueRange`：值的范围，默认 0f ～ 1f ，可自定义范围。
* `onValueChange`：值改变的回调函数，每次值发生变化时都会执行的回调。
* `icon`：顶部符号，用户可自定义。
* `onValueChangeFinished`：值改变结束的回调函数，当拖拽滑动停止时执行的回调。
* `enabled`：设置控件是否生效。
* `sliderSpec`：定义所占空间的参数，可定义 `thumbAreaSize`、`thumbSize`、`thumbPressedSize` 以及 `trackHeight`。
* `colors`：控件颜色，可通过 SliderDefaults 自定义 `trackColor`、`progressColor`、`progressHighColor`、`thumbColor` 以及 `thumbHighColor`。

### 基础用法
添加自定义图标显示。
```Kotlin
@Composable
fun SymbolSliderSimple() {
    var sliderValue by remember { mutableStateOf(0f) }
    SymbolSlider(
        value = sliderValue,
        onValueChange = { sliderValue = it },
        //添加图标
        icon = {
            Icon(
                painter =
                painterResource(
                    id = R.drawable.sample_circle
                ),
                contentDescription = null
            )
        },
        onValueChangeFinished = {},
        sliderSpec = SliderDefaults.Regular
    )
}
```


### 高阶用法
自定义颜色、尺寸、动态切换图标，可以用在音量、光照等可以使用 SymbolSlider 控制的场景。
```Kotlin
@Composable
fun SymbolSliderRegularSample() {
    var sliderValue by remember { mutableStateOf(0f) }
    SymbolSlider(
        value = sliderValue,
        onValueChange = { sliderValue = it },
        //自定义图标
        icon = {
            Icon(
                painter =
                painterResource(
                    id =
                    if (sliderValue > 0) R.drawable.sample_open_voice
                    else R.drawable.sample_close_voice
                ),
                contentDescription = null
            )
        },
        onValueChangeFinished = {},
        //自定义尺寸
        sliderSpec = SliderDefaults.sliderSpec(
            thumbAreaSize = 60.dp,
            thumbSize = 20.dp,
            thumbPressedSize = 20.dp,
            thumbHoverSize = 20.dp,
            trackHeight = 40.dp
        ),
        //自定义颜色
        colors = SliderDefaults.sliderColors(
    thumbColor = Color.White,
    trackColor = Color.LightGray,
    progressColor = Color(0x1FFFFFFF),
    segmentDotColor = Color.White
)
        )
    )
}
```


