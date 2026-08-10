Subwindow 是在 PICO 设计规范下，一种显示在窗口容器左侧或右侧的容器，其高度始终与窗口容器的高度相同。

## API Surface

* `rotation3D`：SubWindow 的 3D 旋转角度，Rotation3D 的 pivot 中的 z 参数将被忽略。
* `followViewpoints`：SubWindow 要跟随的视点。
* `placement`：确定 SubWindow 的放置位置，默认由 `SubwindowPlacement.Default` 方法提供。
* `offset`：SubWindow 的偏移量，根据 `placement` 的设置会在距离主窗口侧设置间距，默认为 24 dp。
* `content`：SubWindow 的内容。

## 使用限制
当前 SubWindow 的宽度固定为 360 dp，高度跟随主窗口高度，由 `LocalConfiguration.current.screenHeightDp.dp` 方法提供。
## 基础用法
```Kotlin
@Composable
fun SubwindowSample() {
    Subwindow() {
        LazyColumn(Modifier.fillMaxSize()) {
            items(count = 100) { Text("messageItem-${it}") }
        }
    }
}
```


## **高阶用法**

* 可修改 `placement`，设置 SubWindow 在场景中的展示位置。
* 可修改 `rotation3D` 从而让 SubWindow 实现 3D 旋转的效果。

```Kotlin
@Composable
fun SubwindowSample() {
    // a message list alongside the main window with a little rotation
    val axis =
        when (LocalLayoutDirection.current) {
            LayoutDirection.Ltr -> -RotationAxis3D.Y
            LayoutDirection.Rtl -> RotationAxis3D.Y
        }

    val pivot =
        when (LocalLayoutDirection.current) {
            LayoutDirection.Ltr -> NormalizedPoint3D.Left
            LayoutDirection.Rtl -> NormalizedPoint3D.Right
        }
    Subwindow(rotation3D = Rotation3D(degree = 45f, axis, pivot)) {
        LazyColumn(Modifier.fillMaxSize()) {
            items(count = 100) { Text("messageItem-${it}") }
        }
    }
}
```


