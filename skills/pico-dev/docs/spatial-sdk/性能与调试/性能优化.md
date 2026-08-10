性能优化是空间应用的开发中重要的一环，并且会贯穿整个应用开发周期。它不仅决定了用户的沉浸感和交互流畅度，也直接关系到设备的续航、可扩展性等方面。通过合理的性能优化，应用才能保持高帧率和低延迟运行，兼顾流畅体验、能效和可扩展性，从而提升用户体验。
## 性能优化工作流
在实际的性能优化工作中，往往会分为这样几个步骤：

1. **检查性能问题**：通过各种性能调试工具或其他手段，发现应用中存在的性能问题并分析，从而找到影响性能的瓶颈。
2. **优化性能表现**：针对发现的性能瓶颈进行修改，优化性能表现。
3. **持续监控性能**：为对用户体验有明确影响的部分以及已经发现了的性能问题制定基准指标，在研发流程中和线上持续进行监控。

### 检查性能问题
发现性能问题有多种手段，可以通过人工分析来发现新的性能问题，也可以通过性能基准测试来发现已有性能指标的变化，还可以通过测试、用户反馈等渠道来收集性能相关反馈。
| **方式** | **描述** |
| --- | --- |
| 人工分析 | 通过 Android Studio Profiler 和 Prefetto 等工具来分析空间应用，可以通过多个方向来进行分析： ;; * 通过记录 System Trace 或者更详细的 Callstack Sample 或者 Method Recording，分析应用卡顿时程序的执行状况，找到相应瓶颈所在。 ;  * 通过 Heap Dump 和内存分配记录，分析应用内存占用情况和发现内存泄露。 ;  * 通过 PICO 在 Trace 记录中提供的空间应用性能数据，分析应用的空间应用特性使用情况。 ;  * 甚至可以通过 Android 提供的 Trace API，添加自己的 Trace 记录，来分析自己应用中重要流程的运行时长和状态。 |
| 性能基准测试 | 可以通过 Androidx Benchmark 来编写性能基准测试，并定期运行（比如在 CI 流程中）来持续对这部分性能指标做监控。关于 Androidx Benchmark 详情请参阅[官方文档](https://developer.android.com/topic/performance/benchmarking/benchmarking-overview)。 |
### 优化性能表现
在分析出性能瓶颈之后，就可以针对瓶颈进行优化，从而提升性能表现。对于空间应用，常见且有效的优化方式如下：
| **方式** | **描述** |
| --- | --- |
| 资产优化 | 降低场景复杂度、压缩贴图、烘焙光照等合理的优化可以在几乎不影响表现的情况下明显降低渲染场景的开销。 |
| 资源懒加载 | 不要在初始化时就加载好所有所需资源，这样只会减慢应用的启动速度，并增加应用运行时的内存开销。 |
| 资源预加载 | 在用户操作之前，提前加载好下一步场景所需的资源，就可以有效降低用户操作后的等待时间。良好结合懒加载和预加载可以平衡运行时资源占用和用户等待时间。 |
| 异步、多线程计算 | 将繁重的计算从主线程转移到其他线程中，避免长时间占用主线程导致卡顿。 |
在完成优化之后，可以再次进行分析以验证优化的效果。同时也需要留意，在优化一处性能表现后，要避免引入其他的性能问题。
### 持续监控性能
完成性能优化之后，可以将这处问题编写成性能测试的用例，并加入到定期执行的性能测试中，来避免相同的问题再次发生。同时对于已经上线的空间应用，也要持续关注用户反馈和线上监控发现的性能问题，并对其进行分析和优化。
## 常见问题排查
而在实际的空间应用开发中，往往会有很多因素影响空间应用的性能，针对已经发现的和潜在的性能问题，可以采用各种工具来进行排查。
### 冷启动慢
冷启动时长，在用户感知上表现为点击应用图标后，到应用内容显示完全、应用可以正常使用的时间。对于空间应用来说，冷启动这段时间除了常规应用会做的 2D 视图布局和绘制、核心模块初始化以外，往往还会进行 3D 资产的加载或创建。
对于空间应用的冷启动，除了传统应用的注意事项外，还有以下值得注意的事项：

* 在启动时仅加载默认容器所需的资产，以避免不必要的资产加载。
* 对资产进行优化，比如压缩纹理、降低模型面数等，以降低资产加载耗时。
* 如果你的应用需要在进入应用后展示复杂的场景，可以考虑在加载完成之前展示 splash screen，而不是一片空白/漆黑。

当你开始排查冷启动问题时，可以通过 Android Studio Profiler 的 System Trace 或者 Perfetto，抓取应用启动阶段的 Trace 记录，并进行分析。除了查看 Android 应用的常规冷启动信息之外，也请关注在冷启动阶段，是否有资产加载的 Slice 信息。
比如如下代码在运行时就会由于在主线程加载了 AssetBundle 和 Entity 而导致卡顿：
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

Trace 中就会出现：

经过分析 Trace 记录，如果发现其他 Slice 有预期外的耗时，可以通过 Android Studio Profiler 的 Find CPU Hotspots 功能，记录并分析冷启动阶段耗时较长的方法，并进行针对性优化：

资产加载相关的 Trace 信息如下：
| **Trace 名称** | **描述** |
| --- | --- |
| LoadEntity: {name} | 在 UI 线程中，从 Path 创建 Entity 对象。 |
| LoadEntity_Asset: {name} | 在 UI 线程中，从 Bundle 创建 Entity 对象。 |
| LoadAsset: {name} | 在 UI 线程中，创建 AssetBundle 对象。 |
| LoadMesh: {name} | 在 UI 线程中，从 Path 创建 MeshResource 对象。 |
| LoadTexture: {name} | 在 UI 线程中，从 Path 创建 TextureResource 对象。 |
### 响应慢和 ANR
当应用长时间占用主线程时，就会发生卡顿，甚至是 ANR。通常来讲，超过 100ms 就会让用户有明显感知，超过 5s 就会触发 ANR。
对于空间应用，要特别注意在 `System.update` 和 `SpatialView` 的 `initial` 和 `update` 块中，避免长时间阻塞，因为这些方法都是运行在主线程之中的。对此有如下注意事项：

* 避免在 `System.update` 和 `SpatialView` 的 `initial` 和 `update` 块中同步加载 3D 资产，加载 3D 资产往往需要数十毫秒以上的时间。
* 在 `SpatialView` 中，如果可以，通过 `remember` 块来提前获取到所需的 Entity 对象，而不是在每次 update 中查找。
* 在 `System.update` 中，通过 `EntityQueryCondition.hasComponent()` 来查找所需的 Entity 对象。
* 在 `System.update` 和 `SpatialView` 的 `update` 块中，减少对象分配次数，由于这两个方法会频繁执行，在其中分配对象会显著增加内存压力和 GC 频率。

在排查卡顿问题时，可以通过 Android Studio Profiler 的 System Trace 或者 Perfetto，抓取应用运行过程中的 Trace 记录，并进行分析。在 Trace 记录中，你可以在主线程找到每一个 System 的 Slice：

对于每个被注册过的 System，每次运行时都会在 Trace 记录中留下 “System_update: {name}” 命名的 Slice。这里 System 的名字会是运行时的 System 类名，也就是说如果 System 类名被混淆，这里显示的也会是混淆后的名字。

对于 SpatialView 的 `initial` 和 `update` 块，可以使用 Android Studio Profiler 的 Find CPU Hotspots 功能，在其中搜索 “SpatialView”，就可以找到在重组时 SpatialView 中的执行状况：

又或者，你可以使用 Compose UI 提供的 [Composition tracing](https://developer.android.com/develop/ui/compose/tooling/tracing) 工具来排查 SpatialView 重组引发的卡顿。
### 渲染掉帧
如果一个空间应用的 3D 场景过于复杂，就会带来较大的渲染压力，甚至会掉帧。用户感受为整个画面卡顿，转头或者移动时画面不流畅。对于 3D 场景的复杂度，参阅《[场景复杂度](./spatial-sdk_性能与调试_场景复杂度与应用性能.md)》。
在排查渲染掉帧问题时，可以通过 Android Studio Profiler 的 System Trace 或者 Perfetto，抓取应用运行过程中的 Trace 记录。在 [Perfetto UI](https://ui.perfetto.dev/) 中打开 Trace 记录并分析，在 Trace 记录中你可以找到运行时 3D 资源和特性的使用情况。你可以着重关注光照、物理、粒子、PBR 材质等消耗较大的特性。

Profiler 不会展示 Trace 记录中的 Counter 信息，这部分计数信息需要在 Perfetto UI 中查看。

这里需要着重关注的特性和 Trace 信息有：

* **物理模拟**
   使用物理相关组件均会在 Trace 记录中留下 Counter 信息，包括：
   | **Trace 名称** | **描述** |
   | --- | --- |
   | collisionComponentCount | 当前已加载的 `CollisionComponent` 的数量。 |
   | rigidBodyComponentCount | 当前已加载的 `RigidBodyComponent` 实例的数量。 |
   | physicsVelocityComponentCount | 当前已加载的 `PhysicsVelocityComponent` 实例的数量。 |
   | physicsForceComponentCount | 当前已加载的 `PhysicsForceComponent` 实例的数量。 |
   | physicsWorldComponentCount | 当前已加载的 `PhysicsWorldComponent` 实例的数量。 |
   当为较多物体添加了物理特性后，会显著增加 CPU 运算开销，这时可以考虑这些方式来降低开销：
   * 减少不必要的参与物理模拟的物体。
   * 为碰撞体设置合适的碰撞模式和碰撞分组。
   * 为物理刚体设置合适的连续碰撞检测模式，平衡精度和性能。
   * 通过添加 `PhysicsWorldComponent`：
      * 将环境中不会发生交互的部分分成不同的物理世界。
      * 在合理的范围降低迭代次数、提高物理更新时间间隔。
* **动态光照**
   当场景中存在动态光照时，会显著增加渲染压力。在大多数情况下，使用烘焙光照或者 IBL 都可以获得良好的效果，并且不会有显著的性能开销。如果你的场景需要使用动态光照来实现效果，请尽量控制光源数量。
   使用动态光照相关组件均会在 Trace 记录中留下 Counter 信息，包括：
   | **Trace 名称** | **描述** |
   | --- | --- |
   | pointLightComponentCount | 当前已加载的 `PointLightComponent` 实例的数量。 |
   | spotLightComponentCount | 当前已加载的 `SpotLightComponent` 实例的数量。 |
   | directionalLightComponentCount | 当前已加载的 `DirectionalLightComponent` 实例的数量。 |

若想分析当前在渲染的模型面数、绘制调用数量等数据，需要使用 Perfetto UI 查看 `com.pico.spatial.runtime` 进程的 Trace 记录：

对于在该进程中的每帧的模型面数、绘制调用数量等数据，都是当前系统中正在运行的所有进程的总和。在 Shared Space 下，可以通过对比容器启动前后的数量差来得出当前容器的数量。

对于模型面数和绘制调用数量，可以简单的理解为数量越低，渲染压力越小。整个场景中建议的模型面数和 DrawCall 数量如下：

* **模型面数**：不超过 350000
* **DrawCall 数量**：Shared Space 中不超过 80 个；Full Space 中不超过 90 个

当模型面数过多时，需要在合理的范围内降低模型面数，通过法线贴图等方式弥补模型显示效果。
当绘制调用过多时，可以通过合并多个模型来减少模型数从而降低绘制调用数量，或者使用 `MeshInstance` 来展示多个相同物体。
## Trace 列表
关于空间应用独有的 Trace 信息，参阅《[获取并分析 Trace 记录](./spatial-sdk_性能与调试_获取并分析-trace-记录.md)》。

