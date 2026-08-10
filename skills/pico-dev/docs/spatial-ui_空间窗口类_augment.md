Augment 是在 PICO 设计规范下，用于放置在主窗口之外的容器，可以由它实现弹窗的效果。

## API Surface

* `anchor`：Augment 的锚点，这是一个相对于窗口容器左上角的归一化点。(0, 0, 0) 表示左上角且 z 轴为 0 的点，而 (1, 1, 1) 表示右下角且 z 轴为 1 的点。
* `alignment`：一个归一化的二维点，表示相对于 Augment 自身的一个点，该点将与 `anchor` 对齐。`0,0` 表示挂件左上角与锚点对齐， `1,1` 表示右下角。
* `offset`：在应用 `anchor` 和对齐之后要应用的绝对偏移量。
* `rotation3D`：Augment 相对于自身的三维旋转。
* `followViewpoints`：Augment 要跟随的视点。默认由 `ViewPoint.All` 提供。
* `content`：Augment 的内容。

## 基础用法
```Kotlin
@Composable
private fun AugmentDemo() {
    val anchor by remember { mutableStateOf(NormalizedPoint3D(0f, 0f, 0f)) }
    var showAugment by remember {
        mutableStateOf(false)
    }
    Column(modifier = Modifier.size(500.dp)) {
        Button({
            showAugment = !showAugment
        }) {
            Text("Show/Hide Augment")
        }

        if (showAugment){
            // 设置anchor为左上角，alignment为TopLeft，即Augment的左上角会对齐主窗口的坐上角
            Augment(
                anchor = anchor,
                alignment = AugmentContentAlignment.Center,
            ) {
                Box(modifier = Modifier.size(100.dp)) {
                    Text("Augment Content")
                }

            }
        }
    }
}
```


## **高阶用法**

* 可修改 `alignment`，搭配 `anchor` 可以实现把 Augment 放在主窗口的任意位置。
* 可修改 `rotation3D` 从而让 Augment 实现 3D 旋转的效果。

```Kotlin
@Composable
private fun AugmentDemo() {
    val anchor by remember { mutableStateOf(NormalizedPoint3D(0f, 0f, 0f)) }
    var showAugment by remember {
        mutableStateOf(false)
    }
    Column(modifier = Modifier.size(500.dp)) {
        Button({
            showAugment = !showAugment
        }) {
            Text("Show/Hide Augment")
        }

        if (showAugment){
            Augment(
                anchor = anchor,
                // 设置center，即当前augment的中心点会对齐着anchor当前主窗口的左上角
                alignment = AugmentContentAlignment.Center,

                // 围绕x轴旋转60度
                rotation3D = Rotation3D(degree = 60f, axis = RotationAxis3D.X)
            ) {
                Box(modifier = Modifier.size(100.dp)) {
                    Text("Augment Content")
                }
            }
        }
    }
}
```


