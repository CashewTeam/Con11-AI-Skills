网格（Mesh）是 3D 模型的基础构建单元，定义了 3D 模型的几何形状和表面细节。网格由顶点、边和面组成，是渲染管线中的核心几何数据结构，直接影响渲染性能和视觉质量。
## 加载 Mesh
你可以通过静态函数 `MeshResource.load` 从文件中加载网格，该函数直接返回一个 `MeshResource` 实例：
```Kotlin
fun load(path: String, loadType: LoadType = LoadType.FROM_ASSETS): MeshResource
```

调用该函数时，需要传入文件路径，并指定加载类型（`LoadType.FROM_ASSETS` 或 `LoadType.FROM_STORAGE`，默认为 `LoadType.FROM_ASSETS`）。
当前仅支持加载 OBJ 格式的文件中的网格数据。

需要注意的是，如果加载类型为 `LoadType.FROM_ASSETS`，文件路径必须是相对于 `assets` 目录的路径；如果加载类型为 `LoadType.FROM_STORAGE`，文件路径必须是文件在设备存储中的绝对路径。例如，要分别使用上述两种方式从 /assets/model/your_custom_mesh.obj 文件中加载网格，可以使用以下代码：
```Kotlin
fun loadMeshResourceExample(context: Context) {
    val subFolderName = "model"
    val fileName = "your_custom_mesh.obj"
    // 从 /assets 目录中加载网格数据
    val meshFromAssets =
        MeshResource.load(path = "${subFolderName}/${fileName}", loadType = LoadType.FROM_ASSETS)

    // 将文件从 /assets 目录复制至设备的存储
    val outFile = File(context.filesDir, fileName)
    context.assets.open("${subFolderName}/${fileName}").use { inputStream ->
        FileOutputStream(outFile).use { outputStream ->
            inputStream.copyTo(outputStream)
            outputStream.flush()
        }
    }
    // 从设备存储中加载网格数据
    val meshFromStorage = MeshResource(outFile.absolutePath, LoadType.FROM_STORAGE)
}
```

除了从文件中直接加载网格，你还可以使用以下三种方式加载网格：

* 成功加载了带有网格的模型之后，你可以通过 `modelComponent.mesh` 获取网格数据（`modelComponent` 为 `ModelComponent` 的实例）。详情参考《[模型](./spatial-sdk_资源管理_模型.md)》。
* 成功获取平面锚点之后，你可以通过 `MeshResource.loadFromPlaneAnchor` 从空间平面锚点加载网格。详情参考《[平面检测](./spatial-sdk_环境感知（混合现实）_平面检测.md)》。
* 成功获取网格锚点之后，你可以通过 `MeshResource.loadFromMeshAnchor` 从空间网格锚点加载网格。详情参考《[空间网格](./spatial-sdk_环境感知（混合现实）_空间网格.md)》。

## 创建 Mesh
PICO Spatial SDK 提供了一系列 `MeshResource` 的静态函数，让你可以快速创建基础几何网格，包括 Plane、Sphere、Cylinder、Cone、Capsule、Box、Torus、和 VideoPanel。示例代码如下：
```Kotlin
fun createMeshResourceExample() {
    // 创建 plane 网格
    val planeMesh = MeshResource.createPlane(width = 0.4f, height = 0.3f, cornerRadius = 0.02f)
    // 创建 video panel，建议在渲染视频材质时使用
    val videoPanelMesh =
        MeshResource.createVideoPanel(width = 0.4f, height = 0.3f, cornerRadius = 0.02f)
    // 创建 sphere 网格
    val sphereMesh = MeshResource.createSphere(radius = 0.5f)
    // 创建 cylinder 网格
    val cylinderMesh = MeshResource.createCylinder(radius = 0.5f, height = 1.0f)
    // 创建 cone 网格
    val coneMesh = MeshResource.createCone(radius = 0.5f, height = 1.0f)
    // 创建 capsule 网格
    val capsuleMesh = MeshResource.createCapsule(height = 0.3f, radius = 0.3f)
    // 创建 box 网格
    val boxMesh = MeshResource.createBox(size = Vector3(0.4f, 0.3f, 0.2f), cornerRadius = 0.02f)
    // 创建 torus 网格
    val torusMesh = MeshResource.createTorus(outerRingRadius = 0.5f, innerRingRadius = 0.3f)
}
```

## 使用 MeshInstance
PICO Spatial SDK 借助 GPU 实例化技术，通过 `MeshInstance` 实现高效的批量渲染。在复杂场景中，`MeshInstance` 支持在单次绘制调用中渲染大量重复的网格对象（如植被、粒子、建筑群），从而显著减少 CPU 与 GPU 之间的通信开销。
其实现原理是：对于拥有相同几何形状和材质的实例，共享同一份网格和材质数据，仅为每个实例传递必要的差异化属性（如变换矩阵、颜色等）。
这种机制带来以下优势：

*  **减少绘制调用**：由多次调用合并为一次，显著降低 CPU 负载。
*  **节省内存占用**：网格和材质数据只需存储一份即可。
*  **支持动态更新**：可实时增删实例或修改其属性，适用于动态场景（如粒子系统、人群模拟）。

以下代码模拟了一个大规模实例化渲染场景：创建 500 个重复网格实例，并通过 `MeshInstancesResource` 渲染。
```Kotlin
fun meshInstanceExample() {  
    // 准备 500 个实例，为其设置 id 和 transform
    val instances = mutableListOf<Instance>()  
    for (i in 0..500) {  
        instances.add(Instance("yourmesh_$i", randomTransformByPosition()))  
    }  
    // 创建 MeshInstanceResource 并添加实例
    val meshInstancesResource = MeshInstancesResource.create("yourmesh")  
    instances.forEach { meshInstancesResource.add(it) }  
    // 将 MeshInstanceResource 绑定到模型 entity
    val entity = ModelEntity(  
        mesh = MeshResource.createTorus(0.6f, 0.4f),  // 共享网格
        material = UnlitMaterial.create().apply { setBaseColor(Color4.GREEN) }  // 共享材质
    )  
    entity.components[ModelComponent::class.java]!!.meshInstances = meshInstancesResource  
}  

// 生成随机位置的变换矩阵  
fun randomTransformByPosition(): Transform {  
    val position = Vector3(  
        x = (Random.nextFloat() * 200) - 100,  // X 范围：[-100, 100]  
        y = Random.nextFloat(),                // Y 范围：[0, 1]  
        z = (Random.nextFloat() * 200) - 100   // Z 范围：[-100, 100]  
    )  
    return Transform(position, EulerAngles(0F, 0F, 0F), Vector3(1F, 1F, 1F))  
}  
```

如果实例之间只有少量浮点数据不同，例如颜色、透明度或动画参数，不需要为每个实例创建不同材质。可以在创建 `MeshInstancesResource` 时指定 `customDataCount`，再通过 `Instance` 的 `customFloatData` 传入每个实例自己的数据。
下面的示例代码演示如何为 `MeshInstance`传入自定义颜色数据。示例中的数据索引需要与 Shader 或 ShaderGraph 中的读取逻辑保持一致；普通 PBR 材质会忽略这些自定义数据。
```Kotlin
import com.pico.spatial.core.ecs.Entity
import com.pico.spatial.core.ecs.ModelComponent
import com.pico.spatial.core.ecs.ModelEntity
import com.pico.spatial.core.ecs.TransformComponent
import com.pico.spatial.core.ecs.resource.AssetBundle
import com.pico.spatial.core.ecs.resource.MeshInstancesResource
import com.pico.spatial.core.ecs.resource.MeshInstancesResource.Instance
import com.pico.spatial.core.ecs.resource.MeshResource
import com.pico.spatial.core.ecs.resource.PhysicallyBasedMaterial
import com.pico.spatial.core.ecs.resource.ShaderGraphMaterial
import com.pico.spatial.core.math.Color4
import com.pico.spatial.core.math.EulerAngles
import com.pico.spatial.core.math.Transform
import com.pico.spatial.core.math.Vector3
import kotlin.random.Random

class MeshInstancesCustomDataSample : Entity() {
    init {
        setUp()
    }

    private fun setUp() {
        // 网格参数：5x5x5 的立方体网格，间距 0.11m
        val gridWidth = 5
        val gridHeight = 5
        val gridDepth = 5
        val spacing = 0.11f
        // 每个实例预留 16 个浮点数的自定义数据
        val customDataCount = 16

        // 生成网格变换列表
        val gridTransforms = buildGridTransforms(gridWidth, gridHeight, gridDepth, spacing)

        // 为每个实例构建自定义数据（此处将随机颜色存放在自定义数据的第1、5、9位，与 Shader 约定的布局一致）
        val instances = gridTransforms.mapIndexed { index, transform ->
            Instance("inst_$index", transform, buildColorCustomData())
        }

        // 创建 MeshInstancesResource，指定自定义数据长度和初始实例列表
        val meshInstancesResource = MeshInstancesResource.create(
            "customDataGrid", 
            customDataCount, 
            instances
        )

        // 创建立方体网格资源
        val mesh = MeshResource.createBox(Vector3(0.1f, 0.1f, 0.1f))

        // 加载支持读取自定义数据的 ShaderGraph 材质
        val bundle = AssetBundle.load("asset://Bundle/shadergraph_parms.bundle")
        val shaderGraphMaterial = ShaderGraphMaterial.loadFromAssetBundle(
            bundle,
            "custominstance/Root/CustomInstanceMaterial"
        )

        // 使用 ShaderGraph 材质的实体：会读取自定义数据渲染不同颜色的实例
        val shaderGraphEntity = ModelEntity(mesh, shaderGraphMaterial)
        shaderGraphEntity.components[ModelComponent::class.java]!!.meshInstances = meshInstancesResource
        shaderGraphEntity.components[TransformComponent::class.java]?.apply {
            setPosition(Vector3(0.5f, 0f, 0f))
        }
        addChild(shaderGraphEntity)

        // 使用普通 PBR 材质的实体：忽略自定义数据，所有实例显示为蓝色
        val pbrMaterial = PhysicallyBasedMaterial.create()
        pbrMaterial.setBaseColor(Color4(0f, 0f, 1f, 1f))
        val pbrEntity = ModelEntity(mesh, pbrMaterial)
        pbrEntity.components[ModelComponent::class.java]!!.meshInstances = meshInstancesResource
        pbrEntity.components[TransformComponent::class.java]?.apply {
            setPosition(Vector3(-0.5f, 0f, 0f))
        }
        addChild(pbrEntity)

        // 示例：更新第一个实例的自定义数据
        val newCustomData = FloatArray(customDataCount)
        newCustomData[1] = 1f // R = 1
        newCustomData[5] = 0f // G = 0
        newCustomData[9] = 0f // B = 0
        meshInstancesResource.update(
            "inst_0", 
            gridTransforms[0], 
            newCustomData
        )

        bundle.close()
    }

    companion object {
        /**
         * 构建 16 位浮点自定义数据，存储随机颜色值
         * 布局约定（与 Shader 保持一致）：
         * index 1: R 通道值
         * index 5: G 通道值
         * index 9: B 通道值
         */
        private fun buildColorCustomData(): FloatArray {
            val data = FloatArray(16)
            data[1] = Random.nextFloat() // 随机 R 值
            data[5] = Random.nextFloat() // 随机 G 值
            data[9] = Random.nextFloat() // 随机 B 值
            return data
        }

        /**
         * 生成网格变换列表
         */
        private fun buildGridTransforms(
            width: Int, 
            height: Int, 
            depth: Int, 
            spacing: Float
        ): List<Transform> {
            val transforms = mutableListOf<Transform>()
            for (z in 0 until depth) {
                for (y in 0 until height) {
                    for (x in 0 until width) {
                        val position = Vector3(
                            x * spacing - (width - 1) * spacing / 2,
                            y * spacing - (height - 1) * spacing / 2,
                            z * spacing - (depth - 1) * spacing / 2
                        )
                        transforms.add(
                            Transform(
                                position, 
                                EulerAngles(0f, 0f, 0f), 
                                Vector3(1f, 1f, 1f)
                            )
                        )
                    }
                }
            }
            return transforms
        }
    }
}
```

## 使用建议
网格的使用建议如下：

* 控制模型的三角形数量以获得最佳性能。
* 合并静态网格或使用 `MeshInstance`，以减少绘制调用。
* 使用 LOD 技术，根据物体距离相机的远近动态调整网格复杂度。PICO Spatial SDK 暂不支持 LOD 相关的 API，你可以根据项目需要，自行实现 LOD 功能。

`MeshInstance` 的使用建议如下：

* 优先批量创建：通过 `MeshInstancesResource.create(name, list)` 一次性添加大量实例，避免循环调用 `add` 导致的性能损耗。
* 减少属性差异：实例之间仅保留必要的差异（如变换或少量属性：颜色等），尽量避免网格或材质的多样化，以提升渲染效率。如果差异只体现在 Shader 可读取的少量 Float 数据上，优先使用 `customFloatData`，不要为每个实例创建不同材质。
* 合理选择批处理方式：完全静态的场景（如建筑物）优先使用静态批处理； 动态场景（如移动的敌人）采用 GPU 实例化。
* 控制自定义数据长度：`customDataCount` 最大取值为 `16`，超过 `16` 会抛出 `ResourceLoadingException` 异常。
* 保持数据长度匹配：调用 `add()` 或 `update()` 方法时，传入的 `customFloatData` 数组长度必须小于等于创建资源时指定的 `customDataCount`，否则会抛出 `IllegalArgumentException` 异常。
* 约定 Shader 数据布局：自定义数据每个索引的含义需要和 Shader 实现保持一致，Shader 侧按约定索引读取后才会生效。
* 减少不必要的更新：自定义数据会占用额外 GPU 显存，频繁更新大量实例的自定义数据也会产生 CPU 开销。建议根据实际需求设置最小必要的 `customDataCount`，并控制更新频率。

绘制调用优化方案的对比如下：
| **优化方式** | **适用场景** | **优点** | **缺点** |
| --- | --- | --- | --- |
| 网格合并 | 静态场景（如地形） | 彻底减少绘制调用 | 不支持动态更新 |
| 静态批处理 | 静态对象（如建筑） | 简单易用 | 不支持移动，内存占用高 |
| GPU 实例化 | 动态重复对象（如粒子、NPC） | 支持动态更新，内存占用低 | 需共享网格/材质 |
## API 参考
`MeshResource` 类提供网格相关的函数，`MeshInstancesResource` 和 `MeshInstancesResource.Instance` 提供 GPU 实例化及逐实例自定义数据相关能力。详情参阅 API 参考。根据你所处的地理位置选择合适的文档链接：

* 中国大陆：[https://developer-cn.picoxr.com/spatial-api/index.html](https://developer-cn.picoxr.com/spatial-api/index.html)
* 非中国大陆：[https://developer.picoxr.com/spatial-api/index.html](https://developer.picoxr.com/spatial-api/index.html)

