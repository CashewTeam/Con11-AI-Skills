菜单组件，在空间中以浮窗的的形式展示可选列表项，列表内容一般搭配 MenuItem 使用，也可以完全自定义列表内容。
形态上可分为主菜单、子菜单。

* 主菜单：Menu
* 子菜单：SubMenu，在 Menu 下的二级菜单

菜单内容通常使用 MenuItem 承载，您也可以自由定义菜单中的选项 UI 样式。

菜单背景颜色跟随系统材质。不支持自定义。
## 使用限制

* 宽度： 最小 `DimensionTokens.WidthMin`， 最大 `DimensionTokens.WidthExtraLarge`
* 高度：最大 `DimensionTokens.HeightExtraLarge`

## API Surface

* Menu & SubMenu:
   * `content`： 菜单内容，通常为 MenuItem，也可以是自定义 View。
   * `onDismissRequest`： Menu 隐藏的回调，例如点击菜单外的空白处，通常需要在此处更新菜单的显示&隐藏状态。
   * `position`：相对锚点的 View 的位置。
   * `padding`：Menu 内边距。
   * `cornerRadius`：圆角尺寸。
* MenuItem
   * `title`：标题区域，一般为`Text`。
   * subtitle：子标题区域，可选，一般为`Text`。
   * subMenu：为 SubMenu 提供的槽位。
   * onClick：点击回调，可选，与 `modifier.clickable{}` 一致。
   * leadingIcon：左侧内容区，一般为`Icon`。
   * trailingIcon：右侧内容区，一般为`Icon`。
   * contentColors：可自定义 MenuItem 的颜色。
   * paddings：MenuItem 的内边距。
   * cornerSize：圆角尺寸。

## 基础用法
Menu 的例子如下：
```Kotlin
@Composable
private fun ButtonWithMenu() {
    var showPopup by remember { mutableStateOf(false) }
    Box {
        // 锚点 View
        Button(onClick = { showPopup = true }) {
            // 文字
            Text(text = "Show Menu")
        }
        // 下拉菜单
        if (showPopup) {
            Menu(onDismissRequest = { showPopup = false }) {
                MenuItem(title = { 
                    Text("Option 1")
                })
                MenuItem(title = { 
                    Text("Option 2")
                })
                MenuItem(title = { 
                    Text("Option 3")
                })
            }
        }
    }
}
```


SubMenu 的使用例子如下：
```Kotlin
@Composable
private fun ButtonWithMenu() {
    var showPopup by remember { mutableStateOf(false) }
    Box {
        Button(onClick = { showPopup = true }) {
            // 文字
            Text(text = "Show Menu")
        }
        // 下拉菜单
        if (showPopup) {
            // 主菜单
            Menu(onDismissRequest = { showPopup = false }) {
                // 
                repeat(4) { index ->
                    var showSubMenu by remember { mutableStateOf(false) }
                    MenuItem(title = {
                        Text("Option $index")
                    }, onClick = {
                        showSubMenu = true
                    }, subMenu = {
                        if (showSubMenu) {
                            SubMenu(onDismissRequest = {showSubMenu = false}) {
                                MenuItem(
                                    title = { Text("Option") },
                                    onClick = { showSubMenu = false }
                                )
                            }
                        }
                    })
                }

            }
        }
    }
}
```


## 高阶用法
### 锚点 View 规则

* 菜单是基于 View 的位置弹出，锚点 View 为 Menu 的直接父 View。例如下面代码，Column 是 Menu 的锚点 View。
   ```Kotlin
   Row {
       Column {
           Menu()
       }
   }
   ```

* 锚点 View 的 Padding 会影响 Menu 的对齐逻辑。如下代码，Box 的实际尺寸为 100 dp，但是作为 Menu 的锚点为黄色区块的 60 dp，而不是基于红色区域对齐。
   组件库里的大部分组件，如 Button、IconButton，都有 Padding 存在，因此使用这些组件作为 Menu 的锚点时，会出现视觉上无法对齐的情况，解决此问题的最佳实践是将 Button 和 Menu 放置在同一个 Box 里。

   ```Kotlin
   Box(modifier = Modifier
       .size(100.dp)
       .background(Color.Red)
       .padding(20.dp)
       .background(Color.Yellow)
   ) {
       Menu()
   }
   ```


* 锚点 View 的子 View 会影响锚点区域，在锚点 View 内摆放其它 View 时，需慎重。如下代码，因为 CustomView 导致 Box 撑满空间，导致 Menu 无法和 Button 对齐。
   ```Kotlin
   Box {
       CustomView(modifier = Modifier.fillMaxSize)
       var showMenu by remember {mutableStateOf(false)}
       Button() {
           Text("show Menu")
       }
       if(showMenu) {
           Menu()
       }
   }
   ```


**最佳实践**
使用 Box 承载目标 View（如 Button） 和 Menu。Box 内除了目标 View、Menu，不要放置其它 View。如下：
```Kotlin
// Box 上不要使用任何关于Size的Modifier
// Box 内部只放锚点View和 Menu，不要放其它的View
Box {
    // 可以是Button，或者是其他组件
    Button() {}
    // 相对于Button的位置弹出菜单
    Menu()
   
}
```

### 自定义菜单弹出位置
Spatial UI 为菜单的的排布方式定义了一组位置排布定义。

* 围绕着锚点 View，例如 Button，水平方向的排布如下：

* 竖直方向的排布规则如下：

* 理论上，您可以通过 `rememberMenuPositionProvider` 和 `rememberSubMenuPositionProvider` 组合出多种位置定义。
* Offset 符合 View 坐标系定义。
   例如，当你需要做出如下效果时，就得使用：
   ```Kotlin
   positionProvider = rememberMenuPositionProvider(
       horizontalPlacement = HorizontalPlacement.toStartOf(offset = -8.dp),
       verticalPlacement = VerticalPlacement.alignBottom
   )
   ```


   示例如下：
   ```Kotlin
   @Composable
   private fun ButtonWithMenu() {
       var showPopup by remember { mutableStateOf(false) }
       Box {
           Button(onClick = { showPopup = true }) {
               // text
               Text(text = "Show Menu")
           }
           // drop down menu
           if (showPopup) {
               Menu(
                   positionProvider =
                       rememberMenuPositionProvider(
                           horizontalPlacement = HorizontalPlacement.alignEnd(),
                           verticalPlacement = VerticalPlacement.above(offset = 10.dp)
                       ),
                   onDismissRequest = { showPopup = false }) {
                   repeat(4) { index ->
                       MenuItem(title = {
                           Text("Option $index")
                       })
                   }
   
               }
           }
       }
   }
   ```


### 搭配 DropDown 使用的例子
```Kotlin
@Composable
private fun ButtonWithMenu() {
    var showPopup by remember { mutableStateOf(false) }
    // 记录选中的索引
    var selectedIndex by remember { mutableStateOf(-1) }
    // 菜单数据列表
    val itemData = remember {
        listOf(
            "Option 1", "Option 2", "Option 3", "Option 4", "Option 5",
        )
    }
    Column {
        Text("You've chosen: ${itemData.getOrNull(selectedIndex)}")
        Box {
            Button(onClick = { showPopup = true }, trailingIcon = {
                Icon(
                    painter = painterResource(.R.drawable.ic_arrow),
                )
            }, colors = ButtonDefaults.buttonColors(containerColor = Color.LightGray)) {
                // 文字
                Text(text = "Choose from")
            }
            // 下拉菜单
            if (showPopup) {
                Menu(
                    onDismissRequest = { showPopup = false }) {
                    itemData.forEachIndexed { index, item ->
                        MenuItem(title = {
                            Text(item)
                        }, trailingIcon = {
                            // 显示展示状态
                            if (selectedIndex == index) {
                                Icon(painter = painterResource(id = R.drawable.ic_sample_listitem_check),null)
                            }
                        }, onClick = {
                            // 更新选中的索引
                            selectedIndex = index
                            // 隐藏菜单
                            showPopup = false
                        })
                    }

                }
            }
        }
    }
}
```


