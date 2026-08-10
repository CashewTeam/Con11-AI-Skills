Trace 记录是定位和分析性能问题的重要信息。System Trace 可在一段时间内记录设备运行情况并生成报告，帮助你了解和排查应用的性能。
在 PICO OS 6 中，空间应用的运行流程与传统 Android 应用有所不同，因此 PICO 提供了一系列专用的 Trace 记录类型，帮助你更高效地诊断空间应用的性能问题。
## 获取 Trace 记录
在 Android 平台上获取 Trace 记录的方式有多种，这里主要介绍如何通过 Profiler 和 Perfetto 获取 Trace 记录。

* Profiler 是 Android Studio 内置工具，用于实时监控和分析应用运行时的性能。
* Perfetto 是一个独立的性能分析工具，用于采集、查看和分析系统级 Trace 数据。

### 使用 Profiler
你可以在 Profiler 中查看应用的 Slice 信息（即一段有开始时间和结束时间的事件记录，对应一个持续的操作或状态）。步骤如下：

1. 在 Android Studio 中，打开 Profiler。
2. 选择 **Capture System Activities** 和你要调试的进程。
3. 在 **Start profiler task from** 处，选择你所需的启动模式，
4. 点击右下角的 **Start anyway** 按钮。

   Profiler 开始获取 Trace 记录。
5. 获取 Trace 记录后，在应用中进行你想要了解和排查性能的操作。
6. 操作完成后，点击 **Stop recording and show results** 按钮。

   Trace 记录已获取。等待片刻后，你将看到已获取的 Trace 记录。

### 使用 Perfetto
Profiler 中只会显示应用的 Slice 信息，如果需要查看 Counter 信息（即数值随时间的变化趋势），则可以使用 Perfetto 来打开刚才获取的 Trace 记录。用 Perfetto 打开 Trace 记录后，你将同时看到 Slice 和 Counter 信息。步骤如下：

1. 在 **Profiler** 面板中，切换到 **Past Recordings** 页签。
2. 在 **Recordings name** 列表中，选中先前获取的 Trace 记录。
3. 点击 **Export recording** 按钮，将 Trace 记录文件导出至本地。

4. 在 [Perfetto UI](https://ui.perfetto.dev/) 中，打开 Trace 记录文件，然后选择需要分析的进程。

## 分析 Trace 记录
获取 Trace 记录后，你可以对其进行分析，以详细了解应用的性能状况并作针对性优化。
### 空间应用初始化
空间应用启动时会初始化其独有的逻辑。若要分析空间应用的初始化耗时，必须确保 Trace 捕获到了应用启动阶段的完整过程。
名为 Spatial_App_Initialize 的 Slice 记录了 PICO Spatial SDK 的初始化流程，其中完成了空间应用启动时的必要操作，随后是应用第一帧的回调。如果你的应用启动较慢，可以从 Spatial_App_Initialize 入手来进行排查。

### 帧循环
空间应用启动后，便进入了帧循环。除了 Android 帧循环的回调外，空间应用中会有如下的独特回调的 Trace 记录，其中每一个被注册的系统的 `update()` 的执行时长都会被记录下来。帧循环相关的 Trace 信息见 “附录：Trace 列表” 部分。

若在空间应用中注册了 `CustomSystem`。
```Kotlin
fun mainApp(scope: SpatialAppScope) = with(scope) {
    DefaultWindowContainer {
        HomeScreen(Modifier.windowConstraints(width = 1600.dp, height = 1000.dp))
    }
    System.register(CustomSystem::class.java)
}

class CustomSystem: System() {

    override fun update(context: SceneUpdateContext) {
        super.update(context)
        Log.d("CustomSystem", "update")
    }

}
```

在 Trace 记录中就可以看到名为 `System_Update: CustomSystem` 的 Slice。

如果应用出现掉帧，会在 `frameDrop` 计数器中累加一次（记录为 1）。

Profiler 不会展示 Trace 记录中的 Counter 信息，这部分计数信息需要在 Perfetto UI 中查看。详见上文中的 “使用 Perfetto“ 部分。

### 资源加载
3D 资源是空间应用的重要组成部分，但加载过程往往会消耗一定时间。若在主线程执行加载操作，Trace 记录中会留下对应的 Slice，这有助于定位和优化加载性能瓶颈。在主线程加载的各类资源均会以 `Load{resource_type}: {name}` 格式的 Slice 记录在 Trace 记录中。资源加载相关的 Trace 信息见 “附录：Trace 列表” 部分。
若在主线程加载 `AssetBundle` 中的名称为 `"Hi"` 的`Entity`。
```Kotlin
@Composable
fun HomeScreen(modifier: Modifier) {
    Column(modifier = modifier.fillMaxSize()) {
        SpatialView { content, _ ->
            val bundle = AssetBundle.load("asset://hi.bundle")
            val entity = Entity.load(modelName = "Hi", bundle = bundle)
            bundle.close()
            
            entity?.let {
                content.addEntity(it)
            }
        }
    }
}
```

在 Trace 记录中就可以看到名为 “LoadEntity_Asset: Hi” 的 Slice。通过这些记录，你可以得知哪些资源加载阻塞了主线程，从而做出优化，比如：将这些加载放到 IO 线程。

### 资源计数
空间应用运行过程中，会产生数个 3D 资源，比如材质、模型。各类资源的数量都会以 Counter 的形式记录在 Trace 记录中。资源计数相关的 Trace 信息见 “附录：Trace 列表” 部分。
以下代码在 `SpatialView` 中异步从 `AssetBundle` 加载一个名为 `"Hi"` 的 `Entity` 并将其添加到场景中，以避免阻塞主线程。
```Kotlin
@Composable
fun HomeScreen(modifier: Modifier) {
    Column(modifier = modifier.fillMaxSize()) {
        SpatialView { content, _ ->
            val entity = withContext(Dispatchers.IO) {
                val bundle = AssetBundle.load("asset://hi.bundle")
                val entity = Entity.load(modelName = "Hi", bundle = bundle)
                bundle.close()
                entity
            }

            entity.let {
                content.addEntity(it)
            }
        }
    }
}
```

加载完模型后，关闭 AssetBundle，在 Trace 中就可以看到名为 `assetBundleCount` 的 Counter 数值变化。

Profiler 不会展示 Trace 记录中的 Counter 信息，这部分计数信息需要在 Perfetto UI 中查看。详见上文中的 “使用 Perfetto“ 部分。

### 特性使用
空间应用中也会使用到各种 3D 特性，比如物理和光照，Trace 记录中会记录下各种特性的使用情况。特性使用相关的 Trace 信息见 “附录：Trace 列表” 部分。
例如，在 hi.bundle 中添加了一个模型和一个聚光灯：

再加载并运行以下代码：
```Kotlin
@Composable
fun HomeScreen(modifier: Modifier) {
    Column(modifier = modifier.fillMaxSize()) {
        SpatialView { content, _ ->
            val entity = withContext(Dispatchers.IO) {
                val bundle = AssetBundle.load("asset://hi.bundle")
                val entity = Entity.load(modelName = "Hi", bundle = bundle)
                bundle.close()
                entity
            }

            entity.let {
                content.addEntity(it)
            }
        }
    }
}
```

可以看到 Trace 记录中出现了名为 `modelComponentCount` 和 `spotLightComponentCount` 的 Counter 记录。

### 场景渲染
每一帧场景渲染，由 PICO 空间引擎内置的统一渲染服务完成，PICO 空间引擎相关的 Trace 位于 `com.pico.spatial.runtime` 进程，该进程的 Trace 记录中会包含该帧的各类渲染数据统计。具体的 Trace 信息见 “附录：Trace 列表” 部分。

## 附录：Trace 列表
### 应用进程中的 Trace

* 空间应用初始化：
   | **Trace 名称** |  **描述** |
   | --- | --- |
   | Spatial_App_Initialize | 空间应用的基础功能初始化。 |
* 帧循环：
   | **Trace 名称** |  **描述** | **备注** |
   | --- | --- | --- |
   | Choreographer#beginSpatialFrame | 开始一帧。 | - |
   | 3d_ec | 3D 内容的刷新。 | - |
   | Choreographer#endSpatialFrame | 结束一帧。 | - |
   | System_Update | 更新 3D 数据，执行所有自定义系统的 `update()`。 | - |
   | System_Update: {name} | 指定某个自定义系统的 `update()`。 | Trace 名称后会跟随自定义系统的名称（若应用开启了混淆，则名称为混淆后的名字）。 |
   | frameRate | 空间应用最近一秒的帧率。 | - |
* 资源加载：
   | **Trace 名称** |  **描述** | **备注** |
   | --- | --- | --- |
   | LoadEntity: {name} | 在 UI 线程中，从 Path 创建实体对象。 | 只有在 UI 线程加载资源才会输出此类 Trace 数据，Trace 名称后会跟加载的资源路径或者名称。 |
   | LoadEntity_Asset: {name} | 在 UI 线程中，从 Bundle 创建实体对象。 |  |
   | LoadAsset: {name} | 在 UI 线程中，创建 AssetBundle 对象。 |  |
   | LoadMesh: {name} | 在 UI 线程中，从 Path 创建 MeshResource 对象。 |  |
   | LoadTexture: {name} | 在 UI 线程中，从 Path 创建 TextureResource 对象。 |  |
* 资源计数：
   | **Trace 名称** |  **描述** | **备注** |
   | --- | --- | --- |
   | assetBundleCount | 当前已加载的 AssetBundle 的数量。 | 当对应数量变化时，会打印 Counter 的值，在 Trace 上以数值的形式显示。 |
   | meshResourceCount | 当前已加载的 MeshResource 的数量。 |  |
   | textureResourceCount | 当前已加载的 TextureResource 的数量。 |  |
   | animationResourceCount | 当前已加载的 AnimationResource 的数量。 |  |
   | physicsMaterialResourceCount | 当前已加载的 PhysicsMaterialResource 的数量。 |  |
   | shapeResourceCount | 当前已加载的 ShapeResource 的数量。 |  |
   | videoMaterialCount | 当前已加载的 VideoMaterial 的数量。 |  |
   | shaderGraphMaterialCount | 当前已加载的 ShaderGraphMaterial 的数量。 |  |
* 特性使用：
   | **特性** | **Trace 名称** |  **描述** | **备注** |
   | --- | --- | --- | --- |
   | 模型 | transformComponentCount | 当前已加载的 TransformComponent 的数量。 | 当对应数量变化时会打印 Counter 的值，在 Trace 上以数值的形式显示。 |
   |  | modelComponentCount | 当前已加载的 ModelComponent 的数量。 |  |
   | 物理模拟 | collisionComponentCount | 当前已加载的 CollisionComponent 的数量。 |  |
   |  | rigidBodyComponentCount | 当前已加载的 RigidBodyComponent 的数量。 |  |
   |  | physicsVelocityComponentCount | 当前已加载的 PhysicsVelocityComponent 的数量。 |  |
   |  | physicsForceComponentCount | 当前已加载的 PhysicsForceComponent 的数量。 |  |
   |  | physicsWorldComponentCount | 当前已加载的 PhysicsWorldComponent 的数量。 |  |
   | 空间视频 | videoComponentCount | 当前已加载的 VideoComponent 的数量。 |  |
   |  | videoPlayerComponentCount | 当前已加载的 VideoPlayerComponent 的数量。 |  |
   |  | videoMaterialCount | 当前已加载的 VideoMaterial 的数量。 |  |
   | 空间音频 | objectAudioComponentCount | 当前已加载的 ObjectAudioComponent 的数量。 |  |
   |  | ambientAudioComponentCount | 当前已加载的 AmbientAudioComponent 的数量。 |  |
   | View Attachment | viewAttachmentCount | 当前在显示的 ViewAttachment 的数量。 |  |
   | 粒子 | particleComponentCount | 当前已加载的 ParticleComponent 的数量。 |  |
   | 传送门 | portalComponentCount | 当前已加载的 PortalComponent 的数量。 |  |
   |  | portalWorldComponentCount | 当前已加载的 PortalWorldComponent 的数量。 |  |
   |  | portalCrossingComponentCount | 当前已加载的 PortalCrossingComponent 的数量。 |  |
   | Shader Graph | shaderGraphMaterialCount | 当前已加载的 ShaderGraphMaterial 的数量。 |  |
   | 动态光照 | pointLightComponentCount | 当前已加载的 PointLightComponent 的数量。 |  |
   |  | spotLightComponentCount | 当前已加载的 SpotLightComponent 的数量。 |  |
   |  | directionalLightComponentCount | 当前已加载的 DirectionalLightComponent 的数量。 |  |
   | 动态投影 | groundingShadowComponentCount | 当前已加载的 GroundingShadowComponent 的数量。 |  |

### PICO 空间引擎的 Trace
场景渲染相关的 Trace 位于 `com.pico.spatial.runtime` 进程中，如下表所示。
| **Trace 名称** | **描述** |
| --- | --- |
| frameRate | PICO 空间引擎的渲染帧率。 |
| 3D Mesh Draw Call Count | 由 ModelComponent 产生的绘制调用数量。 |
| Particle Draw Call Count | 由 ParticleComponent 所产生的绘制调用数量。 |
| Shadow Draw Call Count | 由 ShadowComponent 所产生的绘制调用数量。 |
| Draw Call Count | PICO 空间引擎当前渲染的绘制调用总量。 |
| 3D Mesh Triangle Count | 由 ModelComponent 所产生的三角面数量。 |
| Particle Triangle Count | 由 ParticleComponent 所产生的三角面数量。 |
| Shadow Triangle Count | 由 ShadowComponent 所产生的三角面数量。 |
| Triangle Count | PICO 空间引擎当前渲染的三角面总量。 |
| 3D Mesh Vertex Count | 由 ModelComponent 所产生的顶点数量。 |
| Particle Vertex Count | 由 ParticleComponent 所产生的顶点数量。 |
| Shadow Vertex Count | 由 ShadowComponent 所产生的顶点数量。 |
| Vertex Count | PICO 空间引擎当前渲染的顶点总量。 |
| Visible Directional Lights | 当前可见的平行光源数量。 |
| Visible Point Lights | 当前可见的点光源数量。 |
| Visible Spot Lights | 当前可见的聚光灯光源数量。 |
| Visible Lights | 当前可见的光源总量。 |
| Skeletal Animation Count | PICO 空间引擎中当前正在播放的骨骼动画数量。 |
| Mesh Memory | PICO 空间引擎中网格当前所占用的内存量。 |
| Scene Graph Memory | PICO 空间引擎中 Scene Graph 当前所占用的内存量。 |
| Texture2D Memory | PICO 空间引擎中 Texture2D 当前所占用的内存量。 |
## 了解更多
更多 Profiler 的使用技巧可以参考其[官方文档](https://developer.android.google.cn/studio/profile)。此外，你也可以通过 Perfetto UI 或者 adb 命令来抓取 Trace 记录，Perfetto 使用说明参阅其[官方文档](https://perfetto.dev/docs/quickstart/android-tracing)。

