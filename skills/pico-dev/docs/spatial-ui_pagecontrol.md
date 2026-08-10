本文介绍 PageControl、ProgressPageControl 组件的功能与用法。
## PageControl
PageControl 是 PICO 设计规范下的显示一系列水平点来表示翻页进度的控件。您可通过设置页面总数，当前索引值来控制进度变化，可以限制最大的显示点的数量，超过了会有逐渐缩小的引导。

### API Surface

* `currentIndex`：当前选中索引值。
* `onClickAction`：当点击改变当前索引时，触发该回调。
* `totalDots`：代表总页数。该值必须大于或等于 0。
* `selectIcon`：自定义选中的图标， `@Composable` 回调函数，可选，通常放置 `Icon`。
* `colors`：设置控件中点的高亮选中和常态颜色。 默认通过 `PageControlDefaults` 设置默认的颜色，也可通过 `PageControlDefaults` 实例自定义颜色。
* `enabled`：设置控件是否可交互。
* `maxDisplayCount`：设置控件最多可显示多少点，目前默认最多显示 9 个，超过后当前后端有没显示的点，圆点会逐渐缩小显示。
* `pageControlSpec`：设置控件的布局。可通过自定义 `PageControlSpec` 实例设置圆点的半径、圆点间的间距， 圆点竖直方向是的间距。

#### 基础用法
简单作为分页指示器使用，设置总共的点数和当前索引，在点击时可切换到不同的索引处。
```Kotlin
@Composable
fun TestPageControlChangeIndex() {
    Column(modifier = Modifier.background(BackGroundColor)) {
        var currentIndex by remember { mutableStateOf(0) }
        PageControl(
            currentIndex = currentIndex,
            onClickAction = { index ->
                currentIndex = index
                if (currentIndex > MaxDots) {
                    currentIndex = 0
                }
            },
            totalDots = MaxDots,
            colors =
                PageControlDefaults.pageControlColors(
                    highLightColor = Color.White,
                    normalColor = Color.Black
                ),
            enabled = true,
            pageControlSpec =
                PageControlDefaults.pageControlSpec(
                    dotRadius = 20.dp,
                    dotSpace = 20.dp,
                    verticalPadding = 20.dp,
                )
        )
        Text(text = "currentIndex: $currentIndex")
    }
}
```


### 高阶用法

* 自定义选中 item 的显示样式
   ```Kotlin
   @Preview
   @Composable
   fun CustomPageControlSample() {
       var current by remember { mutableIntStateOf(0) }
       Column(horizontalAlignment = Alignment.CenterHorizontally) {
           Text("Index value: $current")
           PageControl(
               currentIndex = current,
               onClickAction = {
                   current = it
               },
               totalDots = 16,
               colors = PageControlDefaults.pageControlColors(),
               selectIcon = {
                   Icon(
                       painter = painterResource(id = R.drawable.ic_sample_love),
                       contentDescription = "love",
                       modifier = Modifier.size(14.dp),
                   )
               },
               enabled = true,
               maxDisplayCount = PageControlDefaults.NormalMax,
               pageControlSpec = PageControlDefaults.Spec
           )
       }
   }
   ```


* 在常见的分页浏览中，切换时 PageControl 能同步指示，点击更新到不同的对应页面
   ```Kotlin
   @Composable
   fun HorizontalPagerWithScrollableContent() {
       val pagerState = rememberPagerState { 12 }
       val currentInTotal = "${pagerState.currentPage + 1}/${pagerState.pageCount}"
       Box(
           modifier = Modifier
               .fillMaxWidth()
               .height(300.dp),
           contentAlignment = Alignment.Center
       ) {
           // 水平分页Pager
           HorizontalPager(
               modifier = Modifier.fillMaxSize(),
               state = pagerState,
               contentPadding = PaddingValues(20.dp),
               pageSpacing = 10.dp
           ) {
               Box(
                   modifier = Modifier
                       .fillMaxSize()
                       .padding(4.dp)
                       .background(if (it % 2 == 0) Color.Black else Color.Yellow),
                   contentAlignment = Alignment.Center
               ) {
                   Text(
                       text = currentInTotal,
                       color = if (it % 2 != 0) Color.Black else Color.Yellow
                   )
               }
           }
           PageControl(
               //同步索引
               currentIndex = pagerState.currentPage,
               onClickAction = { },
               modifier = Modifier
                   .offset(y = 60.dp)
                   .background(Color.LightGray),
               numberOfDots = pagerState.pageCount,
           )
       }
   }
   ```


## ProgressPageControl
ProgressPageControl 是 PICO 设计规范下的控件 PageControl 的扩展，给予每个选中点都有进度值。您可通过当前选中索引和它的进度值来控制控件更新变化。

### API Surface

* `currentIndex`：当前选中索引值。
* `onClickAction`：当点击改变当前索引时，触发该回调。
* `numberOfDots`：当选中状态变化时，会触发此回调。例如用户点击了 Option。
* `currentProgress`：设置控件的当前进度。
* `colors`： 设置控件中点的高亮选中和常态颜色。通过 `PageControlDefaults` 设置默认的颜色，也可通过`PageControlDefaults` 实例自定义颜色。
* `enabled`：设置控件是否可交互。
* `maxDisplayCount`：设置控件最多可显示多少点，目前默认最多显示 16 个，超过后当前后端有没显示的点，圆点会逐渐缩小显示。
* `pageControlSpec`：设置控件的布局。可通过自定义 `PageControlSpec` 实例设置圆点的半径、圆点间的间距， 圆点竖直方向的间距。

### 基础用法
可用在循环自动更新进度的场景。
```Kotlin
@Composable
fun ProgressPageControlSample() {
    var count by remember { mutableStateOf(CurrentValue) }
    var currentIndex by remember { mutableStateOf(4) }
    var progress by remember { mutableFloatStateOf(0.0f) }

    LaunchedEffect(true) {
        while (true) {
            delay(1000L) // 每隔1秒执行一次
            progress += 0.1f
            if (progress >= 1.0f) {
                //进度变化时同步更新索引
                currentIndex += 1
                if (currentIndex >= MaxDots) {
                    currentIndex = 0
                }
                progress = 0.0f
            }
        }
    }
    Column(modifier = Modifier.background(BackGroundColor)) {
        ProgressPageControl(
            currentIndex = currentIndex,
            onClickAction = {
                count = it
            },
            currentProgress = { progress },
            numberOfDots = MaxDots
        )
        Text(text = "current index:$currentIndex Progress: $progress}")
    }
}
```


### 高阶用法
在自动轮播翻页的场景中，根据进度自动翻页或者点击翻页，可定义最多显示的点个数。
```Kotlin
@Composable
fun AutoScrollPagerWithContent() {
    val pageTotal = 12
    var currentIndex by remember { mutableStateOf(4) }
    var progress by remember { mutableFloatStateOf(0.0f) }
    val pagerState = rememberPagerState { pageTotal }
    val currentInTotal = "${pagerState.currentPage + 1}/${pagerState.pageCount}"
    val coroutine = rememberCoroutineScope()
    var clickChange by remember { mutableStateOf(false)  }
    LaunchedEffect(true) {
        launch {
            //执行翻页
            pagerState.animateScrollToPage(currentIndex)
        }
        while (true) {
            delay(1000L) // 每隔1秒执行一次
            if (clickChange) continue
            progress += 0.1f
            if (progress >= 1.0f) {
                currentIndex += 1
                if (currentIndex >= pageTotal) {
                    currentIndex = 0
                }
                progress = 0.0f
                delay(250)
                launch {
                    //执行翻页
                    pagerState.animateScrollToPage(currentIndex)
                }
            }
        }
    }

    Box(
        modifier = Modifier
            .fillMaxWidth()
            .height(300.dp),
        contentAlignment = Alignment.Center
    ) {
        HorizontalPager(
            modifier = Modifier.fillMaxSize(),
            state = pagerState,
            contentPadding = PaddingValues(20.dp),
            pageSpacing = 10.dp
        ) {
            Box(
                modifier = Modifier
                    .fillMaxSize()
                    .padding(4.dp)
                    .background(if (it % 2 == 0) Color.Black else Color.Yellow),
                contentAlignment = Alignment.Center
            ) {
                Text(
                    text = currentInTotal,
                    color = if (it % 2 != 0) Color.Black else Color.Yellow
                )
            }
        }
        ProgressPageControl(
             //当前进度
            currentIndex = pagerState.currentPage,
            onClickAction = {
                //更新当前页
                clickChange = true
                currentIndex = it
                progress = 0f
                coroutine.launch {
                    //更新调到点击的索引对应的分页
                    pagerState.animateScrollToPage(it)
                    clickChange = false
                }
            },
            //当前进度
            currentProgress = {
                progress
            },
            modifier = Modifier
                .offset(y = 60.dp)
                .background(Color.LightGray),
             //总共的点数
            numberOfDots = pagerState.pageCount,
            //最多显示点数
            maxDisplayCount = 7
        )
    }
}
```


