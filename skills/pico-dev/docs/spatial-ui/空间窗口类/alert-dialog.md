AlertDialog 是在 PICO 设计规范下，用于阻断提示用户目的的组件，可包含图标、标题、自定义内容以及按钮。

## API Surface

* `onDismissRequest`：当用户尝试通过点击 Alert Dialog 外部或按下返回按钮关闭 Alert Dialog 时，调用的回调函数。
* `icon`：显示在标题上方的图标，通常为 `Icon`。
* `title`：标题组件，用于解释对话框的目的。
* `content`：自定义内容区域，显示在标题下方。
* `buttons`：按钮区域，常用于 “确定” 或 “取消” 等操作。
* `orientation`：AlertDialog 的方向，默认为横向（`Orientation.Horizontal`）。
* `padding`：整个 AlertDialog 的内边距，默认为（`AlertDialogDefaults`）的 DialogPadding。
* `cornerRadius`：对话框的圆角半径，默认由 `AlertDialogDefaults.DialogCornerRadius` 方法提供。
* `properties`：用于进一步配置对话框的特定平台属性，默认由 `AlertDialogDefaults.DefaultAlertDialogProperties` 方法提供，可配置 Alert Dialog 的行为。

## 基础用法
```Kotlin
@Preview
@Composable
fun NoticeDialogWithoutButton() {
    Box(modifier = Modifier.size(600.dp)) {
        AlertDialog(
            onDismissRequest = { },
            title = {
                Text(text = "DP Firmware upgrading")
            },
            icon = {
                Icon(
                    painter = painterResource(id = R.drawable.ic_toast_warning),
                    contentDescription = "",
                    modifier = Modifier.size(48.dp),
                )
            },
            content = {
                Text(text = "Regular Dialog")
            },
        )
    }

}
```


## **高阶用法**
`orientation` 可以决定内容的摆放顺序，`cornerRadius` 可以决定 AlertDialog 的圆角，也可以通过添加 `properties` 属性修改 Alert Dialog 的本身属性。
```Kotlin
@Preview
@Composable
fun NoticeDialogWithoutButton() {
    Box(modifier = Modifier.size(600.dp)) {
        var show by remember {
            mutableStateOf(true)
        }
        if (show){
            AlertDialog(
                onDismissRequest = {
                    show = false
                },
                title = {
                    Text(text = "DP Firmware upgrading")
                },
                icon = {
                    Icon(
                        painter = painterResource(id = R.drawable.ic_toast_warning),
                        contentDescription = "",
                        modifier = Modifier.size(48.dp),
                    )
                },
                content = {
                    Text(text = "Content")
                },
                cornerRadius = 0.dp,
                orientation = Orientation.Vertical
            )
        }

    }
}
```


