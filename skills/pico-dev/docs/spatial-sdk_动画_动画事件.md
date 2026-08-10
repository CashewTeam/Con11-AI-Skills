动画事件用于在动画播放的特定时间点执行自定义逻辑。为此，你需要订阅目标事件，并定义该事件被触发时的回调。在动画播放过程中，当系统检测到对应事件被触发时，将自动调用你定义的回调函数。
## 动画事件概览
PICO Spatial SDK 的 `AnimationEvents` 类定义了以下动画事件：
| **动画事件** | **触发条件** |
| --- | --- |
| `AnimationEvents.Started` | 动画开始播放。 |
| `AnimationEvents.Paused` | 动画暂停播放。 |
| `AnimationEvents.Resumed` | 动画由暂停恢复播放。 |
| `AnimationEvents.Looped` | 动画完成了一个循环。 |
| `AnimationEvents.Terminated` | 动画被终止播放。调用 `stop()` 方法时被触发。 |
| `AnimationEvents.Completed` | 动画完成播放并停止。调用 `stop()` 方法时不会被触发。 |
## 订阅动画事件
你可以通过有效的 Scene（适用于通过 entity 订阅）或 SpatialViewContent（适用于通过 SpatialView 的 content 订阅）订阅动画事件，并在函数体中定义该事件被触发时所需执行的逻辑，如播放音效、切换技能、展示特效等。不需要监听事件时，你可以通过 `cancel` 取消订阅。
```Kotlin
@Composable
fun AnimationStartedEventExample() {
    val subscription = remember { mutableStateOf<Cancellable?>(null) }
    // DisposableEffect 用于在 Composable 生命周期内注册和注销事件
    DisposableEffect(Unit) {
        onDispose {
            // 当该 Composable 被移除时，自动取消事件订阅
            subscription.value?.cancel()
            subscription.value = null
        }
    }
    SpatialView(
        initial = { content, _ ->
            val entity = Entity().apply { setName("Entity for AnimationStartedEvent") }
            content.addEntity(entity)
            // 订阅 AnimationEvents.Started 事件，并在动画开始事件触发时，输出 log
            content.subscribe(AnimationEvents.Started::class.java) {
                val controller = it.playbackController
                Log.d("AnimationStartedEvent", "Animation Started on entity: ${controller.entity}")
            }
        },
    )
}
```

## 管理动画事件
当你需要处理大量事件时，你可以自定义一个 `EventManager` 来管理事件的订阅和取消订阅，以及事件被触发时的回调。
```Kotlin
// 该对象用于统一管理动画事件的订阅与取消订阅
object EventManager {
    private var subscription: Cancellable? = null

    fun <T : Event> subscribeAnimationEvent(content: SpatialViewContent, animEvent: Class<T>) {
        when (animEvent) {
            // 订阅动画开始事件
            AnimationEvents.Started::class.java -> {
                subscription =
                    content.subscribe(animEvent) {
                        Log.d("EventManager", "Animation Started!")
                        // Implement your logic here
                    }
            }
            // 订阅动画终止事件
            AnimationEvents.Terminated::class.java -> {
                subscription =
                    content.subscribe(animEvent) {
                        Log.d("EventManager", "Animation Terminated!")
                        // Implement your logic here
                    }
            }
            else -> {
                Log.e("EventManager", "No Matching Animation Event Found!")
            }
        }
    }

    // 取消订阅所有动画事件
    fun unsubscribeAllAnimationEvents() {
        subscription?.cancel()
    }
}
```

## API 参考
`AnimationEvents` 对象提供了动画相关的事件，详情参阅 API 参考。根据你所处的地理位置选择合适的文档链接：

* 中国大陆：[https://developer-cn.picoxr.com/spatial-api/index.html](https://developer-cn.picoxr.com/spatial-api/index.html)
* 非中国大陆：[https://developer.picoxr.com/spatial-api/index.html](https://developer.picoxr.com/spatial-api/index.html)

