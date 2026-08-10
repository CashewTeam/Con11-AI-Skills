手部追踪 （Hand Tracking） 可以获得用户手部的位姿信息，包括手掌、手腕以及各手指关节的位置和旋转。你可用这些数据来识别用户当前的手势，并根据手势或手部位置与虚拟场景中的对象进行交互。
## 推荐阅读
建议阅读《[DataProvider 使用说明](./spatial-sdk_追踪_dataprovider-使用说明.md)》一文，了解如何使用 `DataProvider` 获取追踪数据、判断数据的可用性以及 `DataProvider` 的状态。
## 使用限制
仅当应用的模式为 Full Space 时，才可以获取手部追踪数据。
## 开发流程
通过手部追踪可以实时获取用户手部的位姿数据，并将其设置给虚拟场景中的实体，实现真实手部与虚拟手部之间的运动的同步。整个开发流程如下：

1. 创建 `HandTrackingProvider` 实例。
   ```Kotlin
   @Composable
   fun HandTrackingSample() {
       val handTrackingProvider = remember { HandTrackingProvider() }
       // ...
   }
   ```

2. 调用 `start()` 启动 `HandTrackingProvider`，并在不再需要时调用 `stop()`。
   ```Kotlin
   @Composable
   fun HandTrackingSample() {
       // ...
       DisposableEffect(handTrackingProvider) {
           handTrackingProvider.start()
           onDispose { handTrackingProvider.stop() }
       }
       // ...
   }
   ```

3. 使用 `dataFlow` 获取手部的位姿数据。
   你可以根据具体场景选择不同的获取方式。此处，在 Composable 函数中，可以使用 `dataFlow` 获取数据；在 ECS 中，可以通过 `latestData` 获取最新数据。

   ```Kotlin
   @Composable
   fun HandTrackingSample() {
       // ...
       val handTrackingData by
           handTrackingProvider.dataFlow.collectAsState(initial = HandTrackingData(null, null, 0L))
       // ...
   }
   ```

4. 读取右手食指指尖的位姿数据，转换数据的坐标系，然后将结果设置给实体。
   ```Kotlin
   @Composable
   fun HandTrackingSample() {
       // ...
       val rootEntity: Entity = remember { Entity() }
       val rightIndexTipEntity: Entity = remember { Entity() }
       
       SpatialView(
           update = { _, _ ->
               handTrackingData.right?.let { right ->
                   val indexTipJoint = right[Index.INDEX_TIP]
                   val transformComponent = rightIndexTipEntity.components[TransformComponent::class.java]
                   transformComponent?.apply {
                       val position = rootEntity.convertPositionFrom(indexTipJoint.position, null)
                       val rotation = rootEntity.convertRotationFrom(indexTipJoint.rotation, null)
                       setPosition(position)
                       setQuaternion(rotation)
                   }
               }
           }
       ) { content, _ ->
           rootEntity.addChild(rightIndexTipEntity)
           content.addEntity(rootEntity)
       }
       // ...
   }
   ```


## 完整代码示例
以下代码展示了如何将右手食指尖的实时手部追踪数据设置给虚拟场景中的 `rightIndexTipEntity`，使 `rightIndexTipEntity` 在每帧的渲染中与真实手指尖同步移动和旋转。
```Kotlin
@Composable
fun HandTrackingSample() {
    // 创建 HandTrackingProvider
    val handTrackingProvider = remember { HandTrackingProvider() }

    // 从 dataFlow 中获得实时追踪数据
    val handTrackingData by
        handTrackingProvider.dataFlow.collectAsState(initial = HandTrackingData(null, null, 0L))

    // 在 Composable 生命周期内使用追踪数据
    DisposableEffect(handTrackingProvider) {
        handTrackingProvider.start()
        onDispose { handTrackingProvider.stop() }
    }
    
    // 创建场景中的两个实体：根节点和右手食指尖节点
    val rootEntity: Entity = remember { Entity() }
    val rightIndexTipEntity: Entity = remember { Entity() }

    SpatialView(
        update = { _, _ ->
            handTrackingData.right?.let { right ->
                // 获取右手食指尖关节的数据
                val indexTipJoint = right[Index.INDEX_TIP]
                val transformComponent = rightIndexTipEntity.components[TransformComponent::class.java]
                transformComponent?.apply {
                    // 将追踪数据的数据转换到根节点坐标系下，并设置给右手食指尖节点
                    val position = rootEntity.convertPositionFrom(indexTipJoint.position, null)
                    val rotation = rootEntity.convertRotationFrom(indexTipJoint.rotation, null)
                    setPosition(position)
                    setQuaternion(rotation)
                }
            }
        }
    ) { content, _ ->
        rootEntity.addChild(rightIndexTipEntity)
        content.addEntity(rootEntity)
    }
}
```

## 手部关节参考图
手部追踪功能支持追踪两只手的 26 个关节，如下图所示：

## API 参考
`HandTrackingProvider` 类提供手部追踪的相关接口，详情参阅 API 参考。根据你所处的地理位置选择合适的文档链接：

* 中国大陆：[https://developer-cn.picoxr.com/spatial-api/index.html](https://developer-cn.picoxr.com/spatial-api/index.html)
* 非中国大陆：[https://developer.picoxr.com/spatial-api/index.html](https://developer.picoxr.com/spatial-api/index.html)

