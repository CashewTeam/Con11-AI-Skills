ScrollIndicator 通常用于长内容页面滚动进度的可视化，帮助用户感知内容长度及当前位置，提升导航效率与用户体验。它的功能点总结如下：

* 可随滚动实时更新
* 适配横向/纵向滚动场景

## API Surface
 当前 Scrollindicator 适配的组件包括：

* Row
* LazyRow
* Column
* LazyColumn
* Menu
* 适配 Row & Column **** 的 ScrollIndicator
   * state：绑定在 Row & Column 上的 ScrollState。
   * orientation：滚动指示器方向。Column 是 Vertical、Row 是 Horizontal。
   * alignment： 自定义在 Box 中的摆放位置。
   * dismissAfter：无交互后延迟多久消失。
   * paddingForInteraction：额外的交互热区大小。
* 适配 LazyRow & LazyColumn 的 ScrollIndicator
   * state：绑定在 Row & Column 上的 ScrollState。
   * alignment： 自定义在 Box 中的摆放位置。
   * dismissAfter：无交互后延迟多久消失。
   * paddingForInteraction：额外的交互热区大小。
* 适配 Menu & SubMenu
   * hasScrollIndicator：当内容超出 Menu 尺寸限制后，滚动过程是否出现 ScrollIndicator

## 基础用法
### Column 搭配 ScrollIndicator
```Kotlin
@Composable
fun ColumnWithScrollIndicatorDemo() {
    Box {
        // 1. define a scroll state
        val state = rememberScrollState()
        Column(
            modifier =
                Modifier.fillMaxSize()
                    // 2. apply the scroll state to the column
                    .verticalScroll(state)
        ) {
            repeat(times = 100) {
                Box(
                    modifier = Modifier.fillMaxWidth().height(50.dp),
                    contentAlignment = Alignment.Center
                ) {
                    Text("Item $it")
                }
                Divider()
            }
        }
        // 3. apply the scroll state to the scroll indicator
        ScrollIndicator(state = state, orientation = Orientation.Vertical)
    }
}
```


### Row 搭配 ScrollIndicator
```Kotlin
@Composable
fun RowWithScrollIndicatorDemo() {
    Box {
        // 1. define a scroll state
        val state = rememberScrollState()
        Row(
            modifier =
                Modifier.fillMaxSize()
                    // 2. apply the scroll state to the Row
                    .horizontalScroll(state)
        ) {
            repeat(times = 100) {
                // add your content here
                Text("item $it")
                Divider(orientation = Orientation.Vertical)
            }
        }
        // 3. apply the scroll state to the scroll indicator
        ScrollIndicator(state = state, orientation = Orientation.Horizontal)
    }
}
```


### LazyColumn 搭配 ScrollIndicator
```Kotlin
@Composable
fun LazyColumnWithScrollIndicatorDemo() {
    Box {
        // 1. define a scroll state
        val state = rememberLazyListState()
        LazyColumn(
            modifier = Modifier.fillMaxSize(),
            // 2. apply the scroll state to the LazyColumn
            state = state
        ) {
            items(count = 100) {
                Box(modifier = Modifier.fillMaxWidth().height(50.dp)) { Text("Item $it") }
                Divider()
            }
        }
        // 3. apply the scroll state to the scroll indicator
        ScrollIndicator(state = state)
    }
}
```


### LazyRow 搭配 ScrollIndicator
```Kotlin
@Composable
fun LazyRowWithScrollIndicatorDemo() {
    Box {
        // 1. define a scroll state
        val state = rememberLazyListState()
        LazyRow(
            modifier = Modifier.fillMaxSize(),
            // 2. apply the scroll state to the LazyRow
            state = state
        ) {
            items(count = 100) {
                // add your content here
                Text("item $it")
                Divider(orientation = Orientation.Vertical)
            }
        }
        // 3. apply the scroll state to the scroll indicator
        ScrollIndicator(state = state)
    }
}
```


### Menu 搭配ScrollIndicator
```Kotlin
Box {
    Button(onClick = {
        // show menu
        showMenu = true
    }) {
        Text(text = "ShowMenu")
    }
    if (showMenu) {
        Menu(
            onDismissRequest = {
                // dismiss menu
                showMenu = false
            },
            hasScrollIndicator = true
        ) {
            
            // 自定义items
        }
    }
```


