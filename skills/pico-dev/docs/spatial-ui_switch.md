Switch 是 PICO 设计规范下用于可以在两种状态之间切换的基础控件，可用于开启或关闭某项设置、启用或停用某个功能、 选择一个选项等场景中。该控件由滑块和滑道两部分组成。滑块（thumb）是可以拖动的部分，轨道（track）是背景，用户可以拖动滑块以更改开关状态。

### API Surface

* `checked`：控件当前状态。
* `onCheckedChange`：改变状态时的回调函数， 每次状态改变时执行。
* `enabled`：控件是否可用。
* `colors`：控件颜色， 用户可自定义控件的 `checkedThumbColor`、`checkedTrackColor`、`checkedTrackShadowColor`、`uncheckedThumbColor`、`uncheckedTrackColor`、`uncheckedTrackShadowColor`。

## 基础用法
```Kotlin
@Composable
fun SwitchSample() {
    var checked by remember { mutableStateOf(true) }
    Switch(
        checked = checked,
        onCheckedChange = { checked = it }
    )
}
```


## 高阶用法
自定义 Swith 的颜色、控件所占尺寸大小，比如在录制场景下控制声音打开或关闭。以下演示如何自定义使用颜色参数及所占尺寸大小。
```Kotlin
@Composable
fun SwitchSample() {
    var recordVoice by remember { mutableStateOf(true) }
    Row(verticalAlignment = Alignment.CenterVertically) {
        Text( if (recordVoice)"AudioOn" else "AudioOff")
        Switch(
            checked = recordVoice,
            onCheckedChange = {
                recordVoice = it
            },
            //自定义所占尺寸大小
            modifier = Modifier.size(60.dp, 60.dp),
            //自定义颜色
            colors = SwitchColors.switchColors(
                checkedThumbColor = Color.White,
                checkedTrackColor= Color(0xFF3377FF),
                checkedTrackShadowColor = Color.LightGray,
                uncheckedThumbColor = Color.White,
                uncheckedTrackColor = Color(0x1F3D3D3D),
                uncheckedTrackShadowColor= Color(0x0A7F7F7F)
            )
        )
    }
}
```


