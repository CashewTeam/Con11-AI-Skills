3D 高斯泼溅（3D Gaussian Splatting, 3DGS）是一种 3D 重建与渲染技术。它通过使用大量高斯分布来表示 3D 场景，能够实现高质量的实时渲染效果，尤其适合展示复杂的场景和精细的物体。
## 基础概念
| 概念 | **说明** |
| --- | --- |
| SPZ 文件 | PICO Spatial SDK 加载 3DGS 资源所使用的标准压缩文件格式，其中包含高斯分布的全部参数信息。 |
| `GaussianSplattingComponent` | PICO Spatial SDK 中的 ECS 组件，用于实现 3DGS 渲染，并负责管理 3DGS 资源与渲染配置。 |
| `GaussianSplattingResource` | 用于加载和管理 SPZ 格式的 3DGS 模型文件的资源类。 |
| `LoadType` | 用于指定资源加载来源路径类型的枚举。 |
## 应用场景
3DGS 功能可帮助你在 PICO 设备上高效渲染高质量的 3D 高斯模型，适用于以下场景：

* **高精度模型展示**：适用于需要高保真展示的场景，如文物、艺术品、工业零件等。
* **真实感场景渲染**：对室内外环境或数字孪生等场景进行实时渲染。
* **混合现实应用**：将高真实感的 3D 内容叠加到现实世界中。
* **内容创作工具**：支持你导入并查看自己创建的 3DGS 模型。

## 示例代码
### 把 3DGS 模型加载到实体
下面的代码演示了 3DGS 模型的加载流程。

1. 在 `Dispatchers.IO` 线程中通过 `GaussianSplattingResource(path, loadType)` 创建资源对象，传入资源路径和 `LoadType.FROM_ASSETS`，表示从应用资源目录加载 SPZ 文件。
2. 资源加载完成后，先检查当前 `Entity` 是否仍然有效。如果对象已经销毁，就立即调用 `close()` 释放资源，避免内存泄漏。
3. 在主线程创建 `GaussianSplattingComponent()`，将资源赋值给 `gaussianSplattingResource` 属性，再把组件挂载到实体上，实体就具备了 3DGS 渲染能力。
4. 通过 `TransformComponent` 设置模型的位置和缩放。

示例里的 `destroy()` 也补充了资源回收逻辑，确保实体销毁时同步释放 3DGS 资源。
```Kotlin
import com.pico.spatial.core.ecs.Entity
import com.pico.spatial.core.ecs.GaussianSplattingComponent
import com.pico.spatial.core.ecs.LoadType
import com.pico.spatial.core.ecs.TransformComponent
import com.pico.spatial.core.ecs.resource.GaussianSplattingResource
import com.pico.spatial.core.math.Vector3
import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.launch
import kotlinx.coroutines.withContext

// 创建一个包含 3DGS 组件的 Entity
class GaussianSplattingEntity(private val assetPath: String) : Entity() {
    init {
        CoroutineScope(Dispatchers.Main).launch { 
            setupGaussianSplatting() 
        }
    }

    private suspend fun setupGaussianSplatting() {
        // 1. 加载 3DGS 资源（在IO线程执行）
        val gsResource = withContext(Dispatchers.IO) {
            GaussianSplattingResource(assetPath, LoadType.FROM_ASSETS)
        }
        
        // 检查 Entity 是否有效（防止在加载完成前 Entity 被销毁）
        if (!valid) {
            gsResource.close()
            return
        }
        
        // 2. 创建并配置 GaussianSplattingComponent
        val gsComponent = GaussianSplattingComponent()
        gsComponent.gaussianSplattingResource = gsResource
        
        // 3. 将组件添加到 Entity
        components[GaussianSplattingComponent::class.java] = gsComponent
        
        // 4. 配置 Transform 组件设置位置和缩放
        components[TransformComponent::class.java]?.apply {
            setPosition(Vector3(0f, 0f, -2f)) // 放置在前方2米位置
            setScaleVector(Vector3(1f)) // 保持原始大小
        }
    }

    // 销毁时释放资源
    override fun destroy(destroyChildren: Boolean) {
        components[GaussianSplattingComponent::class.java]?.gaussianSplattingResource?.close()
        super.destroy(destroyChildren)
    }
}
```

### 在已有实体上替换 3DGS 模型
这段代码演示了如何在已有实体上替换 3DGS 模型。

1. 在 `Dispatchers.IO` 线程中创建新的 `GaussianSplattingResource`，避免阻塞主线程。
2. 切回主线程更新 `GaussianSplattingComponent`。由于 `GaussianSplattingComponent` 标记为 `@MainThread`，对 `gaussianSplattingResource` 属性的修改必须在主线程执行。
3. 通过 `component?.gaussianSplattingResource = newResource` 绑定新资源后，实体会切换为新模型。

示例里也处理了实体失效的情况：如果切换时 `entity` 已被销毁，就主动调用 `newResource.close()` 释放刚加载的资源。旧资源不需要手动释放，替换 `gaussianSplattingResource` 时会自动回收。
```Kotlin
// 切换模型的方法
fun switchGaussianSplattingModel(entity: Entity, newAssetPath: String) {
    CoroutineScope(Dispatchers.IO).launch {
        val component = entity.components[GaussianSplattingComponent::class.java]
        
        // 加载新资源
        val newResource = GaussianSplattingResource(newAssetPath, LoadType.FROM_ASSETS)
        
        // 在主线程更新组件
        withContext(Dispatchers.Main) {
            if (entity.valid) {
                component?.gaussianSplattingResource = newResource
            } else {
                newResource.close()
            }
        }
    }
}
```

## 注意事项
为了避免性能问题和资源泄漏，你需要在使用 3DGS 功能时遵循以下建议：
### **资源管理**

* 3DGS 资源会占用大量内存。当你不再需要时，请及时调用 `close()` 方法释放资源。
* 避免同时加载过多的 3DGS 资源。建议同一时间最多加载 1-2 个复杂模型。
* 当 `Entity` 被销毁时，确保其关联的 `GaussianSplattingResource` 也被一同释放，以防止内存泄漏。

### **线程安全**

* 由于 `GaussianSplattingResource` 的加载是耗时操作，建议你在 IO 线程中执行，以避免阻塞主线程。
* 所有对 `GaussianSplattingComponent` 的操作都必须在主线程中完成。
* 在异步加载资源后，务必检查 `Entity` 的有效性。这样做可以避免在 `Entity` 已被销毁的情况下进行操作，从而防止内存泄漏。

## API 参考
`GaussianSplattingComponent` 类和 `GaussianSplattingResource` 类提供了 3DGS 相关的属性和函数，详情参阅 API 参考。根据你所处的地理位置选择合适的文档链接：

* 中国大陆：[https://developer-cn.picoxr.com/spatial-api/index.html](https://developer-cn.picoxr.com/spatial-api/index.html)
* 非中国大陆：[https://developer.picoxr.com/spatial-api/index.html](https://developer.picoxr.com/spatial-api/index.html)
