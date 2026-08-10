你可以为 WindowContainer 中的 view 添加毛玻璃背景效果。PICO Spatial SDK 提供 Thin、Regular、Thick 和 Thickest 四种类型的毛玻璃背景材质，分别对背景后的内容产生不同程度的模糊效果。

代码示例如下：
```Kotlin
@Composable
fun BackgroundMaterial(){
    Box(
        Modifier.size(100.dp).backgroundMaterial(
            enable = true,
            style = Material.Thickest
        )
    )
}
```


