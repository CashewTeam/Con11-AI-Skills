SpatialML 允许你按功能逐项选择：源自相机的结果是留在受保护的运行时内部，还是回流到你的应用中。这个选择是 SpatialML 应用中最核心的隐私决策。本页介绍这两种模式，以及 [SuperResolutionApp](samples-super-resolution) 是如何实现它们的。
**命名说明**
在本文档中，安全模式（Secure Mode）指的是受保护路径，即你的应用无法读取源自相机的输出；回读模式（Readback Mode）**指的是应用*可以*读取这些输出的路径（在用户授予所需权限之后）。在示例源码中，二者分别对应 `useSecureMr = true` 和 `useSecureMr = false` 代码路径。
## 两种模式
|  | 安全模式 | 回读模式 |
| --- | --- | --- |
| 应用能读取结果吗？ | 不能——输出只在运行时内部生效 | 能——通过[回读 API](workflows-read-back-results) |
| 需要相机权限吗？ | 不需要 | 需要（`android.permission.CAMERA`） |
| 典型输出路径 | [场景图算子](workflows-drive-scene-graph-output)驱动一个由 SpatialML 拥有的场景 | 应用读取一个全局张量并将其应用到自己的实体上 |
| 隐私姿态 | 透视像素永远不会离开运行时 | 应用会接收到处理后的像素；应将其视为敏感数据 |
| 适用场景 | 你只需要在空间场景中*展示*结果 | 你需要在应用代码中使用这些像素（上传、保存、进一步处理） |
## 安全模式
在安全模式下，运行时处理相机帧，并将结果渲染到它自己拥有的场景中。你的应用只描述图和场景的连接方式，但永远不会收到像素数据。由于没有任何敏感数据回流到应用内存中，**因此不需要相机权限**。
session 创建时使用非零的 [SpatialML 容器](concepts-containers-and-portals)，管线驱动的是运行时从 glTF 加载的场景：
```kotlin
val session = SpatialMLInstance.create(appContext)
    .also { while (!it.ready) delay(100) }
    .createSession(
        InitInfo(
            imageWidth = 512, imageHeight = 512,
            containerWidth = 1200, containerHeight = 1200, containerDepth = 200,
        )
    )!!

val displayScene = session.newSceneFromGLTFSuspend("Display512.glb")

session.newPipeline().run {
    // bind the pipeline's output texture into the scene's material, then show it
    updateSceneGraphProperty(displayScene, "/", PBRMaterials[0].BaseColorTexture, dynamicTexture)
    switchSceneVisibility(displayScene, displayScene)
    submit(mapOf(), null, null)
}
```

这里，放大后的图像保存在 `dynamicTexture` 中（一个[动态纹理全局张量](concepts-tensors-and-shapes#%E5%8A%A8%E6%80%81%E7%BA%B9%E7%90%86)），并由运行时负责展示。应用从不调用回读。
### 选择安全模式容器
安全模式并不局限于单一容器形状：

* 对有界 3D 内容使用常规 `VOLUMETRIC` 容器。超出其盒子范围的内容会被裁剪。
* 当相机锚定或被追踪的内容可能超出体积但需要保持可见时，使用 `VOLUMETRIC` 加上 [addPortal()](concepts-containers-and-portals#%E5%B8%B8%E8%A7%84-volume-%E4%B8%8E-portal)。
* 对 Z 范围有限的平面受保护输出，使用 `PLANAR`。

Portal 不会削弱安全模式的边界。它改变的是受保护场景内容在哪里可见，而不是应用能否读取它。
## 回读模式
在回读模式下，管线将结果写入一个[全局张量](concepts-tensors-and-shapes#%E5%85%A8%E5%B1%80%E5%BC%A0%E9%87%8F%E4%B8%8E%E6%9C%AC%E5%9C%B0%E5%BC%A0%E9%87%8F)，应用通过[回读扩展函数](workflows-read-back-results)把结果取出来。由于处理后的相机数据会回到你的应用，用户必须先授予相机权限。
```kotlin
// container size is 0 in Readback Mode — no runtime-owned scene is needed
val session = instance.createSession(
    InitInfo(imageWidth = 512, imageHeight = 512,
             containerWidth = 0, containerHeight = 0, containerDepth = 0)
)!!

// ... build and run the pipeline that fills `dynamicTexture` ...

// later, in app code (requires CAMERA permission):
val texture = dynamicTexture.readbackAsTextureResourceSuspend()   // apply to your own entity
val content = dynamicTexture.readbackContentSuspend()             // or get raw bytes
```

示例代码把回读得到的纹理应用到自己的 `display512` 实体的基础色材质上，同时也读取原始字节来发起一次视觉问答（visual-question-answer）请求。
**回读仅支持全局张量**
你只能回读 [GlobalTensor](reference-core-api#tensor-%E4%B8%8E-globaltensor) 的值，管线本地张量无法回读。[TensorContent](reference-core-api#tensorcontent) 是 `AutoCloseable` 的，内部持有一个 `SharedMemory` 缓冲区——请及时关闭它（使用 `use { ... }`），以避免泄漏本地（native）内存。
## 选择合适的模式

只要你只需要*展示*结果，就优先使用安全模式：它更简单、不需要权限，还能让用户数据始终受到保护。只有当应用确实需要处理后的数据时，才使用回读模式——并且要像示例那样，妥善处理权限被拒绝的情况。
## 延伸阅读

* [容器与传送门](concepts-containers-and-portals) —— 选择 Planar、常规 Volume、Portal 或 Disabled。
* [将数据回读到应用](workflows-read-back-results) —— 详细介绍回读 API。
* [驱动场景图输出](workflows-drive-scene-graph-output) —— 安全模式的输出路径。
* [SuperResolutionApp](samples-super-resolution) —— 一个应用中同时使用两种模式。

