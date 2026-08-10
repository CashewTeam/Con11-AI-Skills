本文介绍 CheckBox、TriStateCheckbox 组件的功能和用法。
## CheckBox
CheckBox 是 PICO 设计规范下，提供给用户用于从列表中选择一个或多个选项的基础控件。通过复选框可以开启或关闭某项功能；通过列表中的多个选项，可以进行自主选择（例如协议的同意与接受）。

### API Surface

* `checked`：当前是否选中。
* `onCheckedChange`：选中状态改变的回调，当 checked 变化时，回调执行。
* `enabled`：是否有效。
* `contentSize`：尺寸， 可通过 `CheckboxContentSize` 方法进行自定义。
* `colors`：颜色， 可通过 `CheckboxColor` 方法进行自定义。

### 基础用法
```Kotlin
@Composable
fun CheckBoxSample() {
    var checked by remember { mutableStateOf(true) }
    Checkbox(
        checked = checked,
        onCheckedChange = { checked = !checked }
    )
}
```


### 高阶用法
可自定义颜色，在多选单个选项的场景中使用，比如奶茶中加奶油、加椰肉或者加冰块等可分别选择。
```Kotlin
@Composable
fun CheckboxesExample33() {
    // 初始化状态
    val childCheckedStates = remember {
        mutableStateListOf(
            false,
            false,
            false,
            false
        )
    }
    val names = listOf(
        "option 1",
        "option 2",
        "option 3",
        "option 4"
    )
    Column {
        childCheckedStates.forEachIndexed { index, checked ->
            Row(verticalAlignment = Alignment.CenterVertically) {
                Text(names[index])
                Checkbox(
                    checked = checked,
                    //自定义颜色
                    colors = CheckboxColor(
                        backgroundColor = Color.Gray,
                        contentColor = Color.White,
                        borderColor = Color.Black
                    ),
                    onCheckedChange = { isChecked ->
                        // 更新单个子项的状态
                        childCheckedStates[index] = isChecked
                    }
                )
            }
        }
    }
}
```


## TriStateCheckbox
TriStateCheckbox 是一种具有三种状态的 Checkbox，适用于全选/非全选/未选中的场景。

### API Surface

* `state`：当前状态，可选 `ToggleableState` 的 On、Off 或者 ** Indeterminate。
* `onCheckedChange`：选中状态改变的回调，当 checked 变化时，回调执行。
* `enabled`：是否有效。
* `contentSize`：尺寸，可通过 `CheckboxContentSize` 自定义。
* `colors`：颜色，可通过 `CheckboxColor` 自定义。

### 基础用法
```Kotlin
@Composable
fun TriStateCheckboxSample() {
    var state by remember { mutableStateOf(ToggleableState.Indeterminate) }
    TriStateCheckbox(state = state, onClick = {
    //不同状态的下一个状态
        state = when (state) {
            ToggleableState.On -> ToggleableState.Off
            ToggleableState.Off -> ToggleableState.Indeterminate
            ToggleableState.Indeterminate -> ToggleableState.On
        }
    })
}
```


### 高阶用法
使用于需要多个条件同时满足才可以实现某一条件的场景。
```Kotlin
@Composable
fun CheckboxExample() {
    val childCheckedStates = remember { mutableStateListOf(false, false, false) }
    //通过多个子控件状态，更新状态
    val parentState = when {
        childCheckedStates.all { it } -> ToggleableState.On
        childCheckedStates.none { it } -> ToggleableState.Off
        else -> ToggleableState.Indeterminate
    }

    Column {
        Row(
            verticalAlignment = Alignment.CenterVertically,
        ) {
            Text("All")
            TriStateCheckbox(
                state = parentState,
                onClick = {
                    val newState = parentState != ToggleableState.On
                    childCheckedStates.forEachIndexed { index, _ ->
                        childCheckedStates[index] = newState
                    }
                }
            )
        }
        childCheckedStates.forEachIndexed { index, checked ->
            Row(
                verticalAlignment = Alignment.CenterVertically,
            ) {
                Text("Option ${index + 1}")
                Checkbox(
                    checked = checked,
                    onCheckedChange = { isChecked ->
                        // Update the individual child state
                        childCheckedStates[index] = isChecked
                    }
                )
            }
        }
    }
}
```


