本文介绍 Divider、HorizontalDivider 以及 VerticalDivider 组件的能力和用法。
## Divider
Divider 是 PICO 设计规范下，用于划分界面区域的组件，外观通常是线性组件。

### API Surface

* `color`：Divider 的颜色值
* `thickness`：当前 Divider 的厚度。如果 `orientation` 为 `Horizontal` 则代表其竖向的厚度；如果 `orientation` 为 `Vertical` 则代表其横向的厚度。
* `orientation`：设置 Divider 的布局方向，默认为 `Orientation.Horizontal` 水平方向摆放。

### 基础用法
```Kotlin
@Composable
fun DividersDemo(){
    Box(contentAlignment = Alignment.Center, modifier = Modifier.fillMaxSize()) {
        Column {
            Text("Horizontal Divider Start")
            Divider()
            Text("Horizontal Divider End")
        }
    }
}
```


### **高阶用法**
可以通过设定 `orientation`、`color`、`thickness`，配合上 `Modifier` 实现自定义的展示效果。
```Kotlin
@Composable
fun DividersDemo(){
    Box(contentAlignment = Alignment.Center, modifier = Modifier.fillMaxSize()) {
        Row (modifier = Modifier.height(IntrinsicSize.Max)) {
            Text("Divider Start")
            Divider(modifier = Modifier.padding(horizontal = 20.dp).fillMaxHeight(), thickness = 2.dp, orientation = Orientation.Vertical, color = Color.Red)
            Text("Divider End")
        }
    }
}
```


## HorizontalDivider
HorizontalDivider 是 PICO 设计规范下，专门用于水平方向划分界面区域的组件。
### API Surface

* `color` : HorizontalDivider 的颜色值。
* `thickness` :当前 Divider 的厚度，默认为 1 dp。

### 基础用法
```Kotlin
@Composable
fun DividersDemo(){
    Box(contentAlignment = Alignment.Center, modifier = Modifier.fillMaxSize()) {
        Row (modifier = Modifier.height(IntrinsicSize.Max)) {
            Text("Horizontal Divider Start")
            HorizontalDivider()
            Text("Horizontal Divider End")
        }
    }
}
```


### **高阶用法**
可以通过设定 `thickness` 与 `color`，配合上 `Modifier` 实现更加自定义的展示效果。
```Kotlin
@Composable
fun DividersDemo(){
    Box(contentAlignment = Alignment.Center, modifier = Modifier.fillMaxSize()) {
        Column (modifier = Modifier.height(IntrinsicSize.Max)) {
            Text("Horizontal Divider Start")
            // 添加thickness为5dp，修改颜色为red
            HorizontalDivider(color = Color.Red, thickness = 10.dp, modifier = Modifier.padding(5.dp))
            Text("Horizontal Divider End")
        }
    }
}
```


## VerticalDivider
VerticalDivider 是 PICO 设计规范下，专门用于垂直方向划分界面区域的组件。
### API Surface

* `color` : VerticalDivider 的颜色值。
* `thickness` :当前 Divider 的厚度，默认为 1 dp。

### 基础用法
```Kotlin
@Composable
fun DividersDemo(){
    Box(contentAlignment = Alignment.Center, modifier = Modifier.fillMaxSize()) {
        Row (modifier = Modifier.height(IntrinsicSize.Max)) {
            Text("Vertical Divider Start")
            VerticalDivider()
            Text("Vertical Divider End")
        }
    }
}
```


### **高阶用法**
可以通过设定 `thickness` 与 `color`，配合上 `Modifier` 实现更加自定义的展示效果。
```Kotlin
@Composable
fun DividersDemo(){
    Box(contentAlignment = Alignment.Center, modifier = Modifier.fillMaxSize()) {
        Row (modifier = Modifier.height(IntrinsicSize.Max)) {
            Text("分割线开始")
            VerticalDivider(color = Color.Red, thickness = 10.dp, modifier = Modifier.padding(horizontal = 5.dp))
            Text("分割线结束")
        }
    }
}
```


