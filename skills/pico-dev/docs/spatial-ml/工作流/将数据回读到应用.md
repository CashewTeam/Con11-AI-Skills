[回读模式](concepts-secure-and-readback-modes)允许你的应用把管线的结果从运行时中取出，并在应用代码里使用它——应用到你自己的实体上、上传它，或做进一步处理。回读功能由 `com.pico.spatial.ml.readback` 包中的扩展函数提供。
**回读需要回读模式和相机权限**
把源自相机的结果回读到你的应用中，只有在 [回读模式](concepts-secure-and-readback-modes)下才可用。由于处理过的相机数据会回到应用内存中，用户必须先授予 `android.permission.CAMERA` 权限。[安全模式](concepts-secure-and-readback-modes)永远不会暴露回读能力。
## 回读只针对全局张量
你只能回读 [GlobalTensor](reference-core-api#tensor-%E4%B8%8E-globaltensor)——也就是用 `session.newGlobalTensor(...)` 创建的、持久存在且作用域为整个会话的张量。管线局部张量无法被回读。因此常见的模式是：让你的管线把结果写入一个全局张量，然后再读取那个张量。
```kotlin
val dynamicTexture = session.newGlobalTensor(
    MultiDimensionalInitInfo(
        DataType.Image.R8G8B8A8_U_DYNAMIC,
        intArrayOf(512, 512),
    )
)
// ... pipeline runs:
// copy(rgbFloatResult, rgbUint8Result)
// convertColor(Pipeline.ColorConversion.RGB_TO_RGBA, rgbUint8Result, dynamicTexture)
```

## 两种读取方式
`readback` 包在 `GlobalTensor` 上添加了四个扩展函数——每种读取方式各有一个阻塞版本和一个 `suspend` 版本：
| 扩展函数 | 返回值 | 用途 |
| --- | --- | --- |
| `readbackContent()` / `readbackContentSuspend()` | [TensorContent](reference-core-api#tensorcontent) | 原始字节（上传、转换为 `Bitmap`、自定义处理） |
| `readbackAsTextureResource()` / `readbackAsTextureResourceSuspend()` | `TextureResource` | 直接应用到 SpatialEngine 材质上 |
在协程中优先使用 `suspend` 版本。
### 作为贴图资源
最直接的方式：把张量读取为一个 `TextureResource`，并将其设为你自己某个实体上材质的基础色贴图。
```kotlin
fun imageReadbackAsTexture() = scope.async {
    sessionDeferred.await()
    dynamicTexture.readbackAsTextureResourceSuspend()
}

// apply it to an app-owned entity's material
material.setBaseColorTexture(superResolution.imageReadbackAsTexture().await())
```

### 作为原始内容
需要原始字节时，读取 `TensorContent`。`TensorContent` 是 `AutoCloseable` 的，内部封装了一个 `SharedMemory` 缓冲区——请始终使用 `use { ... }`，以便及时释放原生内存。
```kotlin
fun imageReadBack(): Deferred<TensorContent> =
    scope.async { dynamicTexture.readbackContentSuspend() }

// copy the RGBA bytes out into an ARGB bitmap buffer
superResolution.imageReadBack().await().use { content ->
    content.buffer.rewind()
    while (content.buffer.hasRemaining()) {
        argb.put(content.buffer.get())   // R
        argb.put(content.buffer.get())   // G
        argb.put(content.buffer.get())   // B
        argb.put(content.buffer.get())   // A
    }
}   // content closed here — SharedMemory released
```

当前的 SuperResolution 路径使用 RGBA 动态纹理。因此其原始回读包含每像素四个字节；请消费 alpha 字节，而不是假设三通道 RGB。
**务必关闭 TensorContent**
缓冲区存在于 `SharedMemory` 中。如果你让 `TensorContent` 保持打开状态（或者拷贝出了缓冲区引用而不是字节数据），就会造成原生内存泄漏。请在 `use` 代码块内部拷贝出你需要的数据，然后让它关闭。
## 端到端全貌

## 延伸阅读

* [安全模式与回读模式](concepts-secure-and-readback-modes)——什么时候允许回读。
* [核心 API：回读相关类型](reference-core-api#%E5%9B%9E%E8%AF%BB)——`TensorContent` 及其扩展函数。
* [驱动场景图输出](workflows-drive-scene-graph-output)——无需回读的安全模式替代方案。

