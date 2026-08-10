SideNavigation 是 PICO 设计规范下一种用于侧边栏的导航控件，由顶部 title 部分和多个 section 组成，常用于设置导航、侧边的菜单分栏等场景，形态上可分为头部和导航区。您可以自定义 title，分组显示多个类别。

* 头部：SideNavigation 的 header，位于顶部，可放置标题和搜索框等组合控件。
* 导航区：除 header 的区域，可在垂直方向滑动，放置 SideNavigationSection（分组显示导航） 和 SideNavigationItem（承载内容）。

## API Surface

* SideNavigation
   * `contentPadding`：内容的内边距， 默认水平方向 24 dp。
   * `header`：控件头部内容， 可选，通常放标题和搜索框。
   * `content`：控件的内容，可选放置 `SideNavigationSection`、`SideNavigationItem`。
* SideNavigationSection
   * `contentPadding`：组内容的内边距， 默认顶部 16 dp。
   * `titlePadding`：组的 title 的内边距，默认值 `DefaultSectionTitlePadding`。
   * `title`：组的头部内容。
   * `content`：组的内容，放置 `SideNavigationItem`。
* SideNavigationItem
   * `selected`：Item 是否被选中。
   * `horizontalArrangement`：item 中 `leading`、`content` 以及 `trailing` 三部分的水平布局。
   * `shape`：item 的形状，默认 `RoundedCornerShape`。
   * `contentPadding`：item 的内边距。
   * `colors`：item 的颜色，可通过 `SideNavigationItemColors` 方法进行自定义。
   * `leading`：item 中顶部的内容，可选， 常为 `Icon` 或者 `Image`。
   * `trailing`：item 中尾部的内容，可选，常搭配 `Icon`、`Button`、`Badge` 以及 `Switch`等组件使用。
   * `content`：item 的内容。

## 基础用法
在侧边分栏设置导航的分类，同步更新内容，常见于二级分栏的导航使用。
```Kotlin
@Composable
fun SideNavigationSample() {
    val pins =
        listOf(
            "Recents",
            "Favorites",
            "Applications",
            "Documents",
        )

    val currentSelectedText = remember { mutableStateOf("") }
    Row(
        verticalAlignment = Alignment.CenterVertically
    ) {
        SideNavigation(
            modifier = Modifier.fillMaxHeight().weight(0.3f),
            header = {
                Column {
                    Box(
                        modifier =
                        Modifier.padding(
                            start = 8.dp,
                            top = 26.dp,
                            bottom = 26.dp,
                        )
                    ) {
                        Text(
                            "Settings",
                            style = PicoTheme.typography.titleLarge,
                            maxLines = 1,
                        )
                    }
                }
            }
        ) {
            pins.forEach {
                //侧边栏的Item
                SideNavigationItem(
                    selected = currentSelectedText.value == it,
                    modifier = Modifier.clickable { currentSelectedText.value = it },
                ) {
                    Text(it, maxLines = 1)
                }
            }
        }
        Box (Modifier.weight(0.7f).fillMaxHeight().background(Color.DarkGray),
            contentAlignment = Alignment.Center
        ) {
            Text(currentSelectedText.value)
        }
    }
}
```


## 高阶用法
在侧边栏的导航中可能会有多个分组，header 内有搜索框的场景使用。
```Kotlin
@Composable
fun SideNavigationSample() {
    val pins =
        listOf(
            "Recents",
            "Favorites",
            "Applications",
            "Documents",
        )

    val tags =
        listOf(
            Color.Red to "Red",
            Color.Green to "Green",
            Color.Blue to "Blue",
            Color.Yellow to "Yellow",
            Color.Cyan to "Cyan",
            Color.Magenta to "Magenta",
            Color.White to "White",
        )

    val currentSelectedText = remember { mutableStateOf("") }

    SideNavigation(
        modifier = Modifier.fillMaxHeight(),
        //自定义头部
        header = {
            Column {
                Box(
                    modifier =
                        Modifier.padding(
                            start = 8.dp,
                            top = 26.dp,
                            bottom = 26.dp,
                        )
                ) {
                    Text(
                        "Settings",
                        style = PicoTheme.typography.titleLarge,
                        maxLines = 1,
                    )
                }
                Box(modifier = Modifier.padding(bottom = 24.dp)) { SimpleSearch() }
            }
        }
    ) {
        pins.forEach {
            SideNavigationItem(
                selected = currentSelectedText.value == it,
                modifier = Modifier.clickable { currentSelectedText.value = it },
                leading = { AnyIcon(iconSize = 20.dp) },
            ) {
                Text(it, maxLines = 1)
            }
        }
        //侧边栏分组
        SideNavigationSection(title = { Text("Tags") }) {
            tags.forEach {
                SideNavigationItem(
                    selected = currentSelectedText.value == it.second,
                    modifier = Modifier.clickable { currentSelectedText.value = it.second },
                    leading = {
                        Box(
                            modifier =
                                Modifier.padding(6.dp)
                                    .size(20.dp)
                                    .background(it.first, shape = CircleShape)
                                    .padding(4.dp)
                        )
                    },
                ) {
                    Text(it.second, maxLines = 1)
                }
            }
        }
    }
}
```


