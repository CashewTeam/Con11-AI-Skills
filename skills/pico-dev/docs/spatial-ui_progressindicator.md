本文介绍 LinearProgressIndicator、CircularProgressIndicator 以及 SymbolicCircularProgressIndicator 组件的能力和用法。
## LinearProgressIndicator
LinearProgressIndicator 是 PICO 设计规范下一种线性的表示进度的基础控件，它的进度是确定的，由背景和前景两部分组成， 不可交互，常使用在“加载内容”、“文件上传”等场景中。

### API Surface

* `progress`：进度的回调函数，返回 float 类型的进度值。
* `colors`：进度条的颜色， 可自定义当前进度颜色 `indicatorColor` 和背景颜色 `backgroundColor`。
* `edgeStyle`：控件进度线两端的边缘样式，提供有 `RoundCorner` 和 `Flat` ** 两种样式，默认为 ** `RoundCorner`。
* `height`：进度条的高度。

### 基础用法
线性进度条的简单使用。
```Kotlin
@Composable
fun SimpleLinearProgressIndicatorSample() {
    var progress by remember { mutableStateOf(0f) }
    Column {
        LinearProgressIndicator({
            progress
        })
        Spacer(modifier = Modifier.size(10.dp))
        Button(
            onClick = {
                progress += 0.1f
                if (progress > 1f) {
                    progress = 0f
                }
            }
        ) {
            Text(text = "Click to Update")
        }
    }
}
```


### 高阶用法
自定义进度条的 colors 和 height、edgeStyle，常用于网络资源的加载进度等场景。
```Kotlin
@Composable
private fun LinearProgressExample() {
    val progressAnimatable = remember { androidx.compose.animation.core.Animatable(0f, 0.03f) }
    val scope = rememberCoroutineScope()
    var isLoading by remember { mutableStateOf(false) }
    val title = when (progressAnimatable.value) {
        0f -> "Download"
        in 0f ..< 1f -> "Loading"
        else -> "Download Complete"
    }
    LaunchedEffect(isLoading) {
        while (progressAnimatable.value <= 1f && isLoading) {
            scope.launch {
                progressAnimatable.animateTo(progressAnimatable.value + 0.02f)
            }
            delay(16)
        }
        if (progressAnimatable.value > 1f) {
            isLoading = false
        }
    }
    Column(modifier = Modifier.fillMaxWidth(), horizontalAlignment = Alignment.CenterHorizontally) {
        Button(onClick = {
            isLoading = !isLoading
            if (progressAnimatable.value >= 1f) {
                scope.launch{
                    progressAnimatable.animateTo(0f)
                }
            }
        }) {
            Text(text = title)
        }
        Spacer(modifier = Modifier.size(10.dp))
        LinearProgressIndicator(
            progress = { progressAnimatable.value },
            //自定义尺寸
            modifier = Modifier.size(width = 300.dp, height = 10.dp),
            //自定义颜色
            colors = LinearProgressDefaults.linearProgressColors(
                indicatorColor = Color(0xFF3377FF),
                backgroundColor = Color(0x1F3D3D3D)
            ),
            //自定义边缘形状
            edgeStyle = ProgressIndicatorEdgeStyle.RoundCorner,
            //自定义高度
            height = LinearProgressDefaults.linearProgressHeight(10.dp)
        )
    }
}
```


## CircularProgressIndicator

CircularProgressIndicator 是 PICO 设计规范下一种圆形的表示进度的基础控件，常使用在“加载内容”、“文件上传”等场景中，目前它有以下两种形态：

* **不确定进度**： 持续旋转播放，不考虑进度

* **确定进度**： 显示具体进度

### API Surface

* `progress`：当前进度。
* `colors`：进度条的颜色。
* `edgeStyle`：控件进度线端的边缘样式，提供有 `RoundCorner` 和 `Flat` ** 两种样式，默认为 ** `RoundCorner`。
* `progressSize`：控件尺寸，PICO 提供了三种样式 `Small`、`Regular` 以及 `Max`， 默认为 `Small`，用户可通过 `CircularProgressDefaults` 自定义尺寸。
* `strokeWidth`：进度线的宽度值，默认为控件尺寸的 0.1 倍，最小为 2 dp，可自定义。

### 基础用法

* 不确定进度的简单使用
   ```Kotlin
   @Composable
   fun CircularIndicatorSample() {        
       CircularProgressIndicator()
   }
   ```


* 确定进度的简单使用
   ```Kotlin
   @Composable
   fun CircularIndicatorSample() {
       var progress by remember { mutableStateOf(0f) }
       Column(horizontalAlignment = Alignment.CenterHorizontally) {
           CircularProgressIndicator(
               progress = { progress })
           Spacer(modifier = Modifier.size(10.dp))
           Button(
               onClick = {
                   progress += 0.1f
                   if (progress > 1f) {
                       progress = 0f
                   }
               }
           ) {
               Text(text = "Click to Update")
           }
       }
   }
   ```


### 高阶用法
在不同的场景下，对控件的样式可能不同，您可自定义颜色、尺寸、进度线的边缘风格和宽度大小。
```Kotlin
@Composable
fun DownloadCircularProgressSample() {
    val interactionSource = remember { MutableInteractionSource() }
    var isDownloading by remember { mutableStateOf(false) }
    var isFinish by remember { mutableStateOf(false) }
    var downloadProgress by remember { mutableFloatStateOf(0f) }

    LaunchedEffect(key1 = isDownloading) {
        if (isDownloading) {
            while (downloadProgress < 1f) {
                downloadProgress += 0.02f
                delay(16)
            }
            isFinish = downloadProgress >= 1f
        }
    }

    Column(horizontalAlignment = Alignment.CenterHorizontally) {
        Text(
            text = "Download Progress ${downloadProgress.coerceAtMost(1.0f) * 100}%",
            style = PicoTheme.typography.titleLarge,
            color = Color.White
        )
        CircularProgressIndicator(
            modifier =
            Modifier.clickable(
                interactionSource = interactionSource,
                indication = null,
                enabled = true
            ) {
                isDownloading = !isDownloading
            },
            //自定义边缘
            edgeStyle = ProgressIndicatorEdgeStyle.Flat,
            //自定义填充宽度
            strokeWidth = 10.dp,
            progress = { downloadProgress },
            //自定义尺寸
            progressSize = CircularProgressDefaults.circleProgressSize(
                size = 100.dp
            ),
            //自定义颜色
            colors = CircularProgressDefaults.circleProgressColors(
                backgroundColor = Color(0xFF292929),
                indicatorColor = Color(0xFF007AFF)
            )
        )
    }
}
```


## SymbolicCircularProgressIndicator
SymbolicCircularProgressIndicator 是 PICO 设计规范下一种圆形的表示进度的基础控件，常使用在“加载内容”、“文件上传”等场景中，它可以添加自定义图标，来表示当前进度的状态。如下所示：

### API Surface

* `progress`：当前进度。
* `progressSymbol`：`@Composable` 回调函数，通常放置 `Icon` 显示，可选。
* `colors`：进度条的颜色。
* `edgeStyle`：控件进度线端的边缘样式，提供有 `RoundCorner` 和 `Flat` ** 两种样式，默认为 ** `RoundCorner`。
* `progressSize`：控件尺寸，PICO 提供了三种样式 `Small`、`Regular` 以及 `Max`， 默认为 `Small`，用户可通过 `CircularProgressDefaults` 自定义尺寸。
* `strokeWidth`：进度线的宽度值，默认为控件尺寸的 0.1 倍，最小为 2 dp，可自定义。

### 基础用法
```Kotlin
@Composable
fun SimpleSymbolicCircularIndicatorSample() {
    var progress by remember { mutableStateOf(0f) }
    Column(horizontalAlignment = Alignment.CenterHorizontally) {
        SymbolicCircularProgressIndicator(
            progress = { progress },
            progressSize = CircularProgressDefaults.Regular,
            //自定义符号
            progressSymbol = {
                Icon(
                    painter = painterResource(id = R.drawable.ic_sample_download),
                    contentDescription = null
                )
            }
        )
        Spacer(modifier = Modifier.size(10.dp))
        Button(
            onClick = {
                progress += 0.1f
                if (progress > 1f) {
                    progress = 0f
                }
            }
        ) {
            Text(text = "Click to Update")
        }
    }
}
```


### 高阶用法
支持自定义颜色、尺寸、进度线的边缘风格和宽度大小，还支持在不同的进度阶段切换图标提示用户进度状态。
```Kotlin
@Composable
fun DownloadCircularProgressSample() {
    val interactionSource = remember { MutableInteractionSource() }
    var isDownloading by remember { mutableStateOf(false) }
    var isFinish by remember { mutableStateOf(false) }
    var downloadProgress by remember { mutableFloatStateOf(0f) }

    LaunchedEffect(key1 = isDownloading) {
        if (isDownloading) {
            while (downloadProgress < 1f) {
                downloadProgress += 0.02f
                delay(16)
            }
            isFinish = downloadProgress >= 1f
        }
    }

     //不同状态下的图标
    val resId = when {
        isFinish -> R.drawable.ic_sample_finish
        isDownloading -> R.drawable.ic_sample_pause
        else -> R.drawable.ic_sample_download
    }

    Column(horizontalAlignment = Alignment.CenterHorizontally) {
        Text(
            text = "Download Progress ${downloadProgress.coerceAtMost(1.0f) * 100}%",
            style = PicoTheme.typography.titleLarge,
            color = Color.White
        )
        SymbolicCircularProgressIndicator(modifier = Modifier.clickable(
            interactionSource = interactionSource, indication = null, enabled = true
        ) {
            isDownloading = !isDownloading
        },
            //自定义边缘
            edgeStyle = ProgressIndicatorEdgeStyle.Flat,
            //自定义填充宽度
            strokeWidth = 10.dp,
            progress = { downloadProgress },
            //自定义尺寸
            progressSize = CircularProgressDefaults.circleProgressSize(
                size = 100.dp
            ),
            //自定义颜色
            colors = CircularProgressDefaults.circleProgressColors(
                backgroundColor = Color(0xFF292929), indicatorColor = Color(0xFF007AFF)
            ),
            //自定义符号
            progressSymbol = {
                Icon(
                    modifier = Modifier.size(50.dp),
                    painter = painterResource(id = resId),
                    contentDescription = null
                )
            })
    }
}
```


