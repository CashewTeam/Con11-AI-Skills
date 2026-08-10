本文介绍 Badge、DotBadge 以及 NumberBadge 组件的功能和用法。
## Badge
Badge 是 PICO 设计规范下，通常用于展示动态信息的足迹，它可以以小图标或者数字的形式叠加在其他组件上，达到提示用户的目的。

### API Surface

* `badgeColor`：用于设置 Badge 颜色。
* `badgeSize`：设置 Badge 的大小，默认为 `BadgeDefaults.Small`。
* `radius`：设置 Badge 圆角，默认情况下为 `BadgeDefaults.Small` 提供圆角大小。
* `contentPadding`：设置 Badge 的内边距。
* `textStyle`：用于设置 Badge 内部的文本样式。
* `content`：Badge 控件下的内容，可以选择添加自定义展示内容。

### 基础用法
```Kotlin
@Composable
fun BadgeDemo(){
    Box(contentAlignment = Alignment.Center, modifier = Modifier.fillMaxSize()) {
        Badge {
            Text("Badge Content")
        }
    }
}
```


### **高阶用法**
通过配置 Badge 的 `badgeColor`、`radius` 以及 `contentPadding` 等参数，可以实现更加自定义化的内容。
```Kotlin
@Composable
fun BadgeDemo(){
    Box(contentAlignment = Alignment.Center, modifier = Modifier.fillMaxSize()) {
       // 设置Badge背景色为红色，内容文字颜色为白色，圆角为6dp，内边距为6dp
        Badge(badgeColor = BadgeDefaults.badgeColors(Color.Red,Color.White), radius = 16.dp, contentPadding = PaddingValues(6.dp)){
            Text("Badge Content")
        }
    }
}
```


## DotBadge
DotBadge 是 PICO 设计规范下，用于原点提示的 Badge，通常用于简单的消息提醒。

### API Surface
`color`：用于设置 DotBadge 颜色。
### 基础用法
```Kotlin
@Composable
fun BadgeDemo(){
    Box(contentAlignment = Alignment.Center, modifier = Modifier.fillMaxSize()) {
        DotBadge()
    }
}
```


### **高阶用法**
DotBadge 通过与其他控件一起配合，实现更多丰富的提醒功能。
```Kotlin
@Composable
fun BadgeDemo(){
    Box(contentAlignment = Alignment.Center, modifier = Modifier.fillMaxSize()) {
        Box {
            Text("A simple message")
            DotBadge(modifier = Modifier.align(Alignment.TopEnd).offset(x= 10.dp), color = Color.Yellow)
        }
    }
}
```


## NumberBadge
NumberBadge 是 PICO 设计规范下，用于展示数字类型的 Badge。

### API Surface

* `number`：NumberBadge 展示的数字大小。
* `threshold`：设置 NumberBadge 的最大展示值，如果 `number` 大于 `threshold` 就会出现 `overflow` 指定的效果。
* `overflow`：当 `number` 超过 `threshold` 时展示的样式，默认为 `Overflow.Plus`。
* `contentPadding`：设置 Badge 的内边距。
* `textStyle`：用于设置 `number` 的文本样式。
* `badgeSize`：设置 NumberBadge 的大小，可以通过传入 `BadgeSize` 对象设置自定义大小。
* `badgeColor`：用于设置 NumberBadge 颜色。
* `contentPadding`：设置 NumberBadge 的内边距。

### 基础用法
```Kotlin
@Composable
fun BadgeDemo(){
    Box(contentAlignment = Alignment.Center, modifier = Modifier.fillMaxSize()) {
        NumberBadge(number = 1)
    }
}
```


### **高阶用法**
通过配合 NumberBadge 的`threshold`、`overflow`，可以实现不同的展示效果。
```Kotlin
@Composable
fun BadgeDemo(){
    Box(contentAlignment = Alignment.Center, modifier = Modifier.fillMaxSize()) {
        Row(horizontalArrangement = Arrangement.spacedBy(10.dp)) {
            NumberBadge(number = 1, badgeColor = BadgeDefaults.badgeColors())
            NumberBadge(number = 10, badgeColor = BadgeDefaults.badgeColors())
            // 默认的Overflow.Plus效果
            NumberBadge(number = 100, threshold = 9, badgeColor = BadgeDefaults.badgeColors())
            NumberBadge(number = 100, threshold = 99, badgeColor = BadgeDefaults.badgeColors())
            // Overflow.Ellipsis效果
            NumberBadge(
                number = 100,
                threshold = 99,
                overflow = Overflow.Ellipsis,
                badgeColor = BadgeDefaults.badgeColors(),
            )
        }
    }
}
```


