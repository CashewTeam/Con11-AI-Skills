Snack 和 Android Toast 类似，可用作显示在 WindowContainer 底部的简短信息通知。它通常显示几秒后自动消失。除了展示主体信息之外，它还提供了可交互槽位，允许自定义交互行为。

Snack 的背景色跟随应用主题变化。

## API Surface
提供两种类型的 API：

* 简单版，自定义程度低：
   * `message`：需要展示的信息，String 类型。
   * `description`：信息补充描述，String 类型，可选。
   * `leadingIcon`：左侧的图标，Composable function 类型，可选，通常搭配 `Icon` 使用。
   * `action`：信息展示时长，默认为 3 秒。
* 灵活定制版，自定义程度高：
   * `message`： 需要展示的信息，Composable UI 类型，通常搭配 `Text` 使用。
   * `description`：信息补充描述，Composable UI 类型，通常搭配`Text`使用
   * `leadingIcon`：左侧的图标，Composable UI 类型，可选，通常搭配 `Icon` 使用 。
   * `trailingActions`：右侧区域，Composable UI 类型，可选，可摆放一到多个组件，通常为 IconButton、Button 等。
   * `duration`：信息展示时长，默认为 3 秒。

## 基础用法

1. `SnackHost`:
   * 承载 LocalSnackHostState，通过 LocalComposition 机制向下级 View 节点提供 LocalSnackHostState，一般只需要在 WindowContainer 的根节点添加即可。
   * PicoTheme 内置了 SnackHost，如果 WindowContainer 使用了 PicoTheme，就无需再设置 SnackHost。
2. LocalSnackHostState：在 SnackHost 或者 PicoTheme 的任意子节点均可获取。
3. 展示信息，默认 3 秒后隐藏。

```Kotlin
@Composable
fun SimpleSnack() {
    // 1. 承载LocalSnackHostState，在Button的任意父View节点设置都行
    SnackHost {
        // 2.SnackHost的任意子节点都能获取到LocalSnackHostState
        val snackState = LocalSnackHostState.current
        val scope = rememberCoroutineScope()
        Button(onClick = { 
            scope.launch { 
                // 3. 展示信息
                snackState.show(message = "This is a Snack") 
            }
        }) {
            Text("SimpleSnack")
        }
    }
}
```


## 高阶用法

* 展示 Icon、辅助描述文案
   ```Kotlin
   @Composable
   fun SnackWithLeftIcon() {
       // 1. 承载LocalSnackHostState，在Button的任意父View节点设置都行
       SnackHost {
           // 2.SnackHost的任意子节点都能获取到LocalSnackHostState
           val snackState = LocalSnackHostState.current
           val scope = rememberCoroutineScope()
           Button(
               onClick = {
                   scope.launch {
                       snackState.show(
                           message = "SnackWithLeftIcon", // 信息
                           description = "Snack demo",  // 描述文案
                           leadingIcon = {
                               Icon(painter = painterResource(R.drawable.ic_sample_listitem_leading),contentDescription = null)
                           }
                       )
                   }
               }
           ) {
               Text("SnackWithLeftIcon")
           }
       }
   }
   ```


* 支持交互，并且根据交互结果自定义业务逻辑
   * 简单的交互例子如下：
      ```Kotlin
      val snackState = LocalSnackHostState.current
      val scope = rememberCoroutineScope()
      Button(
          onClick = {
              scope.launch {
                  val result = snackState.show(
                       message = "Leaving current site. Continue to external page?", 
                       action = "OK"
                  )
                  when(result) {
                      SnackResult.ActionPerformed -> {
                          // 点击按钮后的操作
                      }
                      SnackResult.Dismissed -> {
                          // Snack自动关闭，
                      }       
                  }
              }
          }
      ) {
          Text("SnackWithAction")
      }
      ```

   * 当你需要提供用户更复杂的交互逻辑时，请参考下面的例子：
      ```Kotlin
      val snackState = LocalSnackHostState.current
      val scope = rememberCoroutineScope()
      Button(
          onClick = {
              scope.launch {
                  snackState.show(
                      message = {
                          Text( "Important info" )
                      },
                      description = { Text("brief description") },
                      leadingIcon = {
                          CircularProgressIndicator(modifier = Modifier.size(13.dp))
                      },
                      trailingActions = {
                          // 按钮1
                          Button(onClick = { 
                              // 交互后隐藏Snack，对应 SnackResult.ActionPerformed
                              this.performAction()
                          }, size = ButtonDefaults.Min) {
                              Text("OK")
                          }
                          // 按钮2，关闭按钮
                          IconButton(onClick = { 
                              // 交互后立刻隐藏Snack，对应SnackResult.Dismissed
                              this.dismiss() 
                          }, size = IconButtonDefaults.Min) {
                              CloseIcon()
                          }
                      }
                  )
              }
          }
      ) {
          Text("SnackWithMultiAction")
      }
      ```

