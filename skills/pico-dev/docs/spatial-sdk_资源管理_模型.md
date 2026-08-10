模型是包含网格、材质、动画等数据的完整 3D 资产包，是空间应用中的核心视觉元素。
## 支持的模型格式
### USD 格式
USD（Universal Scene Description）是由 Pixar 开发的开源 3D 场景描述格式，支持复杂的层级结构和丰富的特性集，是空间应用开发的首选格式。
PICO Spatial SDK 支持的 USD 格式的变体包括：

* **.usd**：文本格式，适合编辑和版本控制；
* **.usda**：ASCII 编码的文本格式，可直接阅读；
* **.usdc**：二进制格式，加载速度快，占用空间小；
* **.usdz**：压缩包格式，包含模型和所有依赖资源。

PICO Spatial SDK 支持的 USD 格式的特性包括：

* **基础几何**
   * 基本形状（Primitive Shapes）：支持 box、sphere 等标准几何体。
   * 多边形网格（Polygon Mesh）：支持子网格（Submesh）划分。
* **动画系统**
   * 骨骼系统（Skeleton）：完整的骨骼绑定和蒙皮支持。
   * 时间采样动画（Timesampled Animation）：基于关键帧的动画数据。
* **着色器与材质**
   * 着色器图（Shader Graph）：支持节点化的着色器编辑。
   * 材质系统：支持 USD Preview Surface 标准材质，可定义金属度、粗糙度等 PBR 属性

### glTF 格式
glTF（GL Transmission Format）是 Khronos Group 推出的 3D 模型格式，专为实时渲染设计，文件体积小，加载速度快。若你想详细了解 glTF，请参考[官方文档](https://github.khronos.org/glTF-Tutorials/gltfTutorial/)。
glTF 格式的模型通常包含三个部分：

* **.gltf**：JSON 描述文件，储存核心数据，包括模型结构、材质信息、动画定义等，可直接阅读且易于编辑；
* **.bin**：二进制文件，包含顶点数据、索引数据、动画关键帧等；
* **图像文件**：纹理贴图，包括 .png, .jpg 等格式。

.glb 文件是 glTF 的二进制容器格式，它将 JSON 描述文件、二进制文件、图像文件打包为一个二进制文件，包括：

* **头部信息（Header）**：包含文件类型、版本和长度信息；
* **JSON 块**：包含模型结构描述信息，可使用 gzip 工具对其进行压缩；
* **二进制块**：包含几何数据、动画和嵌入式纹理。

PICO Spatial SDK 支持 glTF 格式模型的大部分基本属性，包括网格、材质、纹理和基本动画等，但存在以下使用限制：

* **场景组件限制**：不支持导入相机和光源节点；
* **网格限制**：Mesh Primitive 的模式不支持 `POINT`、`LINES`、`LINE_LOOP` 和 `LINE_STRIP`；
* **动画限制**：`animation.sampler.interpolation` 不支持 STEP 插值方式。

PICO Spatial SDK 支持的 glTF extension 包括：
| **扩展名称** | **功能描述** | **备注** |
| --- | --- | --- |
| KHR_materials_pbrSpecularGlossiness | 支持高光光泽度 PBR 工作流。 | 与金属粗糙度工作流二选一。 |
| KHR_materials_unlit | 支持无光照材质。 | 适用于 UI 元素和特效。 |
| KHR_materials_sheen | 支持织物光泽效果。 | 暂不支持 sheenRoughness 输入。 |
| KHR_materials_clearcoat | 支持清漆效果。 | 可模拟车漆、水面等透明涂层。 |
| KHR_materials_ior | 支持折射率控制。 | 影响透明物体的光线折射效果。 |
| KHR_materials_emissive_strength | 支持自发光强度控制。 | 出于性能考虑，不推荐开启 BLOOM 效果。 |
| KHR_texture_transform | 支持纹理坐标变换。 | 可实现纹理平移、旋转和缩放。 |
| KHR_texture_basisu | 支持 Basis Universal 纹理压缩。 | 显著降低内存占用。 |
| EXT_texture_webp | 支持 WebP 格式作为纹理源。 | 相比 JPEG/PNG 通常有更小的文件大小。 |
| KHR_draco_mesh_compression | 支持 Draco 几何压缩库的模式（支持流式传输压缩几何数据而非原始数据）。 | 对于几何数据占重要比例的模型（>1 MB），Draco 可以在许多情况下将文件大小减少约 95%。 |
| KHR_mesh_quantization | 支持使用 8 位 或 16 位存储替代 32 位浮点数。 | 较低位数存储会带来精度损失，需要评估对模型质量的影响。 |
| EXT_meshopt_compression | 支持 meshoptimizer 库，提供轻量级解码器和快速的运行时解压缩。 ;   | 虽然解码快速，但仍需要 CPU 时间进行解压缩；解压后的数据需要额外内存空间。 |
| EXT_mesh_gpu_instancing | 支持 GPU 实例化渲染。 | 允许高效绘制大量相同几何体的实例，共享几何数据，减少内存占用，充分利用 GPU 并行处理能力，大幅减少 draw call 数量。 |
| KHR_animation_pointer | 支持动画属性指针。 ;; * 节点变换：支持 node transform 动画。 ;  * 材质属性：支持 PBR 金属粗糙度工作流的以下属性动画： ;     * baseColorFactor（基础颜色系数） ;     * metallicFactor（金属度系数） ;     * roughnessFactor（粗糙度系数） ;     * emissiveFactor（自发光系数） | 需要注意性能方面的影响： ;; * 运行时开销; * JSON 指针解析需要额外的 CPU 时间 ;     * 大量属性动画可能影响整体性能 ;     * 建议对关键属性进行优化和缓存 ;  * 内存使用; * 额外的动画数据增加文件大小 ;     * 运行时需要更多内存存储动画状态 ;     * 需合理规划动画的数量和复杂度 |
## 加载模型
PICO Spatial SDK 支持 USD 和 glTF 格式的 3D 模型，并且支持以下途径加载模型并创建 entity 实例：
各加载方法均有对应的 suspend 异步版本。你可以通过 `Entity.loadSuspend` 方法来加载模型，建议在主线程中调用该方法。

### **方式一**：通过 URI String 加载
支持以下 Scheme：

* `"asset://"` 或 `"assets://"`：加载 src/main/assets 目录下的指定模型。
   ```Kotlin
   // 通过 scheme 为 "asset://" 的 URI String 加载 /assets 目录下的指定模型：
   suspend fun loadEntityFromAsset() {
       val subFolderName = "model"
       val fileName = "your_custom_model.usdz"
       val entity =
           withContext(Dispatchers.IO) {
               Entity.load(uriString = "asset://${subFolderName}/${fileName}")
           }
   }
   ```

* `"file://"`：加载设备存储中的指定模型文件，URI String 中的路径必须为文件的绝对路径。
   ```Kotlin
   // 通过 scheme 为 "file://" 的 URI String 或者 File Object 加载设备存储中的指定模型文件：
   suspend fun loadEntityFromStorageViaFileUri(context: Context) {
       // 从文件 URI 加载 entity
       val entityFromFileUri =
           withContext(Dispatchers.IO) { Entity.load("file://your_file_path") }
   }
   ```


### **方式二**：通过 File 对象加载
```Kotlin
suspend fun loadEntityFromStorageViaFileObject(context: Context) {
    // 从文件对象加载 entity
    val entityFromFileObject = withContext(Dispatchers.IO) { Entity.load(yourFile) }
}
```

### **方式三**：通过 ContentResolver 和 URI 对象加载
加载 scheme 为 `"content://"` 的 URI 所指向的模型。
```Kotlin
suspend fun loadEntityFromContentUri(context: Context) {
    // 创建 content 的 URI
    val contentUri = Uri.parse("content://${context.packageName}.yourmodelprovider/$fileName")
    // 从 ContentResolver 和 content 的 URI 加载 entity
    val entityFromContentUri =
        withContext(Dispatchers.IO) { Entity.load(context.contentResolver, contentUri) }
}
```

### **方式四**：通过 InputStream 和 ModelFormat 加载
加载已经转换为 `InputStream` 的模型文件。其中 `ModelFormat` 用于补充原始文件的格式信息，当前支持 `ModelFormat.USDZ` 与 `ModelFormat.GLTF` 两种。
```Kotlin
suspend fun loadEntityFromInputStream(context: Context) {
    // 从 InputStream 加载 entity
    val entityFromInputStream =
        withContext(Dispatchers.IO) { Entity.load(inputStream, ModelFormat.USD) }
}
```

### **方式五**：通过 Entity.load() 加载 AssetBundle
向 `Entity.load()` 传入 AssetBundle 实例的路径和 USDA 文件名称，将 Spatial Editor 中的目标场景加载为模型，并返回对应的 entity 实例。
```Kotlin
suspend fun loadEntityFromBundle() {
    val entity =
        withContext(Dispatchers.IO) {
            Entity.load(
                modelName = "YourCustomSceneName",
                bundle = AssetBundle.load("asset://your_custom_asset_bundle.bundle")
            )
        }
}
```

### **方式六**：通过 AssetBundle.load() 加载 AssetBundle
通过 `AssetBundle.load()` 将 Spatial Editor 项目中的场景加载为模型，并获取场景中的子实体。详情参考《[AssetBundle](./spatial-sdk_资源管理_assetbundle.md)》。
```Kotlin
val bundle = AssetBundle.load("asset://path/to/bundle/YourCustomBundleName.bundle")
bundle.preloadModel("Hi")
val rootEntity = bundle.loadModel("Hi")
```

## 创建 ModelEntity
模型由网格和材质组成。当你通过加载或创建方式获得网格与材质后，可以按以下方式创建 `ModelEntity`：
```Kotlin
fun createModelEntityExample(mesh: MeshResource, material1: Material, material2: Material) {
    val modelEntityWithSingleMaterial = ModelEntity(mesh, material1)
    val modelEntityWithMultiMaterials = ModelEntity(mesh, arrayOf(material1, material2))
}
```

关于如何加载或创建网格和材质，参考《[网格](./spatial-sdk_资源管理_网格.md)》和《[材质](./spatial-sdk_资源管理_材质.md)》。
## 动态创建和更新模型
除了从外部加载模型资源外，你还可以通过 `MeshModel` 动态创建和更新 3D 模型。详情参阅《[动态创建和更新模型](./spatial-sdk_资源管理_动态创建和更新模型.md)》。
## 访问和控制模型相关属性
成功加载模型后，你可以通过 ModelComponent 的属性来控制模型的各项特征。需要注意的是，只有包含模型网格的节点才能获取到 ModelComponent，否则将无法访问相关属性。
### 控制渲染状态
你可以通过 `entity.components[ModelComponent::class.java]?.isRendererEnabled` 控制 `ModelComponent` 的渲染状态，默认值为 `true`。该参数仅影响模型的视觉显示，不影响 entity 的其他组件或系统功能。当 `isRendererEnabled` 为 `true` 时，模型被正常渲染和显示；当 `isRendererEnabled` 为 `false` 时，模型组件将不会被渲染，但 entity 的其他组件和功能仍会正常工作。
```Kotlin
// 隐藏 entity 的模型的渲染效果，保留其他组件和功能
entity.components[ModelComponent::class.java]?.isRendererEnabled = false
// 重新开启 entity 的模型的渲染效果
entity.components[ModelComponent::class.java]?.isRendererEnabled = true
```

`entity.components[ModelComponent::class.java]?.isRendererEnabled` 需要和 `entity.enabled` 进行区分。前者仅影响模型的渲染效果；而后者控制整个 entity 的启用状态，影响 entity 的所有行为和功能。
`entity.enabled` 默认值为 `true`（启用状态）。如果子 entity 被启用但其父 entity 被禁用，则该属性返回 `false`。当 `entity.enabled` 为 `false` 时，entity 不会被渲染，且它的所有组件、系统功能和子级 entity 都将被禁用，但仍会被保留在 `scene.queryEntity(EntityQueryCondition)` 的查询结果中。
因此，在需要保持逻辑功能正常但隐藏视觉效果时（如调试时临时隐藏），可以选择将 `isRendererEnabled` 置为` false`；而如果需要隐藏整个 entity 层级并且停用该层级的所有功能，可以选择将 `entity.enabled` 置为 `false`，以停止所有相关计算，节省更多性能。
## 线程使用注意事项
在进行模型加载和 entity/component 相关操作时，需要根据接口类型选择合适的线程：

* 同步加载接口（如 `Entity.load`） 的加载过程耗时较长，建议在后台线程调用。推荐使用 `withContext(Dispatchers.IO)` 将加载操作切换到 IO 线程中执行，避免因阻塞主线程而导致界面卡顿。
* 异步加载接口（如 `Entity.loadSuspend`） 可以直接在主线程调用，底层会自动管理加载协程，无需关心线程调度问题，更加便捷高效。
* 模型加载完成并创建 entity 实例后，所有 entity/component 相关操作必须在主线程执行，包括：
   * **场景操作**：获取 scene、修改 enabled 状态等；
   * **组件管理**：修改或添加各种组件等；
   * **层级遍历**：遍历 entity 层级树以访问子节点等；
   * **坐标空间转换**：将 entity 的位置、旋转、缩放等转换到不同坐标空间中；
   * **动画控制**：播放/停止骨骼动画（需要模型文件包含动画资源）等；
   * **音频处理**：准备或播放音频资源等；

## API 参考
`Entity`、`ModelEntity` 和 `ModelComponent` 类提供模型相关的函数，详情参阅 API 参考。根据你所处的地理位置选择合适的文档链接：

* 中国大陆：[https://developer-cn.picoxr.com/spatial-api/index.html](https://developer-cn.picoxr.com/spatial-api/index.html)
* 非中国大陆：[https://developer.picoxr.com/spatial-api/index.html](https://developer.picoxr.com/spatial-api/index.html)

