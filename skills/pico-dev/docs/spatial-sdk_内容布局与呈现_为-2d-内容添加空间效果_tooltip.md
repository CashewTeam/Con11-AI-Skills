ToolTip 是 Spatial UI 提供的一种信息提示 Modifier，用于在用户悬停时展示额外文本，包括标题和描述。同时，它还支持配置显示方向。
代码示例如下：
```Kotlin
@Composable
fun Demo(){
    Box(
        modifier = Modifier
            .tooltip(
                text = "标题",
                description = "描述信息",
                direction = it // 方向
            )
            .background(Color.Green)
            .clickable { }
            .size(80.dp)
    ) 
}
```

