张量是在管线中的算子之间流动的、带类型的多维数据。正确设置张量模型——数据类型、形状、通道和作用域——是让 SpatialML 图正常工作的关键所在。本页是概念性参考；完整的类型列表见[张量类型与枚举](reference-tensor-types-and-enums)。
## 张量的构成
一个 SpatialML 张量具有：

* 一个**数据类型**（[Tensor.DataType](reference-tensor-types-and-enums#tensor-datatype)）—— 例如 `UINT8`、`FLOAT32`、`INT32`；
* 一个**形状**—— 以 `IntArray` 给出的各维度；以及
* 一个**通道数**—— 每个元素持有多少个值（例如 RGB 为 `3`）。

你永远不会直接构造张量，而是用一个 **init-info** 对象来描述它，并请求会话或管线创建它。
## Init-info：描述一个张量
最常用的 init-info，也是唯一支持[算术运算](reference-operators-arithmetic)的，是 `MultiDimensionalInitInfo`：
```text
// a 512 x 512 RGB image of unsigned bytes
MultiDimensionalInitInfo(
    dataType = DataType.UINT8,
    dimensions = intArrayOf(512, 512),
    channel = 3,
)

// a 2 x 3 float affine matrix (single channel)
MultiDimensionalInitInfo(DataType.FLOAT32, intArrayOf(2, 3))
```

其他 init-info 类型用于描述标量、颜色数组、点数组、切片、字符串、时间戳，以及带类型的数字数组。完整列表及各自的使用场景见[张量类型与枚举](reference-tensor-types-and-enums#%E5%BC%A0%E9%87%8F%E5%88%9D%E5%A7%8B%E5%8C%96%E4%BF%A1%E6%81%AF-init-info)。
**图像张量是 (H, W) 加通道**
图像形状的张量使用 `dimensions = intArrayOf(height, width)`，像素分量由 `channel` 承载。一帧 512×512 的 RGB 图像是 `intArrayOf(512, 512)` 配合 `channel = 3`，而不是 `intArrayOf(512, 512, 3)`。
## 全局张量与本地张量
作用域决定了张量的生命周期以及它能做什么。
|  | 本地张量 | 全局张量 |
| --- | --- | --- |
| 创建方式 | [pipeline.newLocalTensor(...)](reference-operators-new-local-tensor)、[pipeline.newPlaceholder(...)](reference-operators-new-placeholder) | [session.newGlobalTensor(...)](reference-core-api#spatialmlsession)、`session.newSceneFromGLTF(...)` |
| 生命周期 | 单个管线 | 整个 session |
| 能否跨管线共享？ | 不能 | 能（通过[占位符](concepts-execution-model#%E5%8D%A0%E4%BD%8D%E7%AC%A6%E4%B8%8E%E7%BB%91%E5%AE%9A)绑定） |
| 能否回读？ | 不能 | 能（[回读 API](workflows-read-back-results)） |
| 典型用途 | 图内的中间值 | 在管线、场景、回读目标之间共享的输入/输出 |
管线通过**占位符**来消费全局张量：你在图中创建一个 [PipelineTensorPlaceholder](concepts-execution-model#%E5%8D%A0%E4%BD%8D%E7%AC%A6%E4%B8%8E%E7%BB%91%E5%AE%9A)，并在[提交时](concepts-execution-model)将一个具体的 `GlobalTensor` 绑定给它。这就是同一个管线能够在不同运行之间操作不同全局张量的方式。
## 设置张量内容
要向张量中放入常量数据（例如仿射变换的源点），需要写入它的 `tensorResource`，这是一个 Android [SharedMemory](reference-core-api#sharedmemory)：
```kotlin
SharedMemory.create("affine_src_points", 6 * Float.SIZE_BYTES).use { mem ->
    val buf = mem.mapReadWrite()
    buf.order(ByteOrder.nativeOrder())
    buf.putFloat(0f); buf.putFloat(0f)
    buf.putFloat(127f); buf.putFloat(0f)
    buf.putFloat(0f); buf.putFloat(127f)
    SharedMemory.unmap(buf)
    tensor.tensorResource = mem
}
```

模型字节也用同样的方式加载到 `SharedMemory` 中——参见 [loadAssetToSharedMemory](workflows-run-model-inference#%E5%8A%A0%E8%BD%BD%E6%A8%A1%E5%9E%8B)。
## 动态纹理
动态纹理张量是一种全局图像张量，运行时可以将其渲染为实时纹理。推荐使用动态 [DataType.Image](reference-tensor-types-and-enums#multidimensionalinitinfo)，它同时涵盖了像素布局和可渲染纹理标志：
```kotlin
val dynamicTexture = session.newGlobalTensor(
    MultiDimensionalInitInfo(
        DataType.Image.R8G8B8A8_U_DYNAMIC,
        intArrayOf(512, 512),
    )
)
```

对于 8 位色彩渲染，请使用 `R8G8B8A8_U_DYNAMIC`。如果模型或相机处理链产生的是 RGB，在写入动态纹理之前需要先将其转换为 RGBA：
```kotlin
convertColor(Pipeline.ColorConversion.RGB_TO_RGBA, rgbOutput, dynamicTexture)
```

动态纹理是从管线的图像输出通往可见输出之间的桥梁。在[安全模式](concepts-secure-and-readback-modes)下，你用 [updateSceneGraphProperty](reference-operators-update-scene-graph-property) 把它绑定到场景材质中；在[回读模式](concepts-secure-and-readback-modes)下，你用 [readbackAsTextureResource](workflows-read-back-results) 把它取出来。
## 数据类型速查表
| 任务 | 典型类型 |
| --- | --- |
| 相机图像 | `DataType.Image.R8G8B8_U` |
| 可渲染的显示纹理 | `DataType.Image.R8G8B8A8_U_DYNAMIC` |
| 归一化后的模型输入 | `FLOAT32` |
| 仿射 / 变换矩阵 | `FLOAT32` |
| 类别索引（argmax 输出） | `INT32` |
| 时间戳 | `INT32`，4 通道（通过时间戳 init-info） |
| 从 glTF 加载的场景 | `GLTF_BINARY`（由 `newSceneFromGLTF` 创建） |
完整的枚举列表见[张量类型与枚举](reference-tensor-types-and-enums)。
## 延伸阅读

* [张量类型与枚举](reference-tensor-types-and-enums) —— 每一个 init-info 和枚举。
* [执行模型](concepts-execution-model) —— 占位符、绑定与提交。
* [为模型准备图像数据](workflows-prepare-image-data) —— 在真实预处理链路中的张量。

