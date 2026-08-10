本页介绍张量初始化信息（init-info）类型，以及 SpatialML Kotlin API 中用到的各种枚举。关于概念模型，请阅读[张量与形状](concepts-tensors-and-shapes)；关于消费这些类型的算子，请参阅[算子目录](reference-operator-catalog)。
## 张量初始化信息（init-info）
你先用一个 init-info 对象描述一个张量，再通过 `session.newGlobalTensor(...)` 或 `pipeline.newLocalTensor(...)` 创建它。
### MultiDimensionalInitInfo
通用的 N 维张量类型。**它是唯一支持 [arithmetic](reference-operators-arithmetic) 的 init-info。**用于图像、矩阵以及大多数工作张量。
```text
Tensor.MultiDimensionalInitInfo(
    dataType: DataType,
    dimensions: IntArray,
    channel: Int = 1,
    dynamicTexture: Boolean = false,
)
```

| 参数 | 含义 |
| --- | --- |
| `dataType` | 元素类型——参见 [DataType](#tensor-datatype)。 |
| `dimensions` | 以 `IntArray` 表示的形状（至少 2 维；向量请使用 `[N, 1]` 或 `[1, N]`）。图像使用 `intArrayOf(height, width)`。 |
| `channel` | 每个元素的分量数（RGB 为 `3`），默认值为 `1`。**不建议显式设置**——对于多通道像素张量，优先使用下面的 `DataType.Image` 重载。 |
| `dynamicTexture` | 设为 `true` 会创建一个可实时渲染的[动态贴图](concepts-tensors-and-shapes#%E5%8A%A8%E6%80%81%E7%BA%B9%E7%90%86)（仅限全局张量）。更推荐直接使用 `*_DYNAMIC` 形式的 `DataType.Image` 取值。 |
还有一个重载版本接受 `DataType.Image`（例如 `R8G8B8_U` 或 `R8G8B8A8_U_DYNAMIC`）来代替基础的 `DataType` + `channel` 组合。它会自动为你设置通道数和动态贴图标志，因此是声明图像和贴图张量的推荐方式：
```text
// 1024x960 RGB image tensor
Tensor.MultiDimensionalInitInfo(Tensor.DataType.Image.R8G8B8_U, intArrayOf(1024, 960))

// 512x512 RGBA dynamic-texture tensor (renderable)
Tensor.MultiDimensionalInitInfo(Tensor.DataType.Image.R8G8B8A8_U_DYNAMIC, intArrayOf(512, 512))
```

对于 8 位色彩渲染目标，推荐使用 `R8G8B8A8_U_DYNAMIC`。在绑定或回读之前，请使用 `Pipeline.ColorConversion.RGB_TO_RGBA` 将三通道 RGB 结果转换到其中。
### 其他 init-info 类型
| Init-info | 描述内容 |
| --- | --- |
| `ScalarInitInfo` | 单个标量值。 |
| `ColorArrayInitInfo` | 颜色数组。 |
| `Point2ArrayInitInfo` | 2D 点数组（例如仿射变换的源点/目标点）。 |
| `Point3ArrayInitInfo` | 3D 点数组。 |
| `SliceInitInfo` | 供 [get](reference-operators-get) 切片算子使用的切片描述符。 |
| `StringInitInfo` | 字符串数据（例如文本内容）。 |
| `TimeStampInitInfo` | 时间戳张量（与 `rectifiedVSTAccess` 的时间戳结果相匹配）。 |
| `FloatArrayInitInfo` / `DoubleArrayInitInfo` / `IntArrayInitInfo` / `ShortArrayInitInfo` | 带类型的数值数组。 |
所有 init-info 类型产生的张量，其内容都可以通过 `tensorResource`（一个 [SharedMemory](reference-core-api#sharedmemory)）来设置。
## Tensor.DataType
元素数据类型。
| 取值 | 说明 |
| --- | --- |
| `UINT8` | 无符号字节——相机/显示图像。 |
| `INT8` | 有符号字节。 |
| `UINT16` | 无符号 16 位。 |
| `INT16` | 有符号 16 位。 |
| `INT32` | 32 位整数——类别索引、时间戳。 |
| `FLOAT32` | 32 位浮点数——模型输入/输出、矩阵。 |
| `FLOAT64` | 64 位浮点数。 |
| `GLTF_BINARY` | glTF 场景（由 `newSceneFromGLTF` 生成）。 |
`Tensor` 还定义了一个嵌套的 `Image` 类型，用于图像类型的数据；`Tensor.ColorType` 和 `Tensor.TensorUsage` 分别用于分类颜色排布方式和张量的用途。
## Pipeline.ModelInferenceType
为 [runModelInference](reference-operators-run-model-inference) 选择加速器。模型二进制文件始终是 TensorFlow Lite FlatBuffer（`.tflite`）；这个枚举只用于选择它运行在哪里。
| 取值 | 运行位置 |
| --- | --- |
| `LITE_RT_CPU` | 在 CPU 上运行 LiteRT。 |
| `LITE_RT_GPU` | 在 GPU 上运行 LiteRT。 |
| `LITE_RT_NPU` | 在 NPU 上运行 LiteRT。 |
请根据你的延迟和质量预算选择合适的加速器。
## 颜色、归一化、范数与排序相关枚举
| 枚举 | 使用者 | 取值 / 用途 |
| --- | --- | --- |
| `ColorConversion` | [convertColor](reference-operators-convert-color) | 选择要应用的颜色/排布转换（例如 RGB↔GRAY、RGB↔HSV）。 |
| `NormalizeType` | [normalize](reference-operators-normalize) | `L1`、`L2`、`INF`、`MINMAX`。 |
| `NormType` | [norm](reference-operators-norm) | `L1`、`L2`、`INF`。 |
| `SortType` | [sortMatrix](reference-operators-sort-matrix) | `BY_COLUMN`、`BY_ROW`。（[sortVec](reference-operators-sort-vec) 不需要排序类型。） |
## 文本对齐枚举
供文本场景图算子使用。
| 枚举 | 使用者 |
| --- | --- |
| `TextHorizontalAlignment` | [updateSceneGraphTextHorizontalAlignment](reference-operators-update-scene-graph-text-horizontal-alignment) |
| `TextVerticalAlignment` | [updateSceneGraphTextVerticalAlignment](reference-operators-update-scene-graph-text-vertical-alignment) |
## SceneGraphProperty
一个密封（sealed）层级结构，用于选择 [updateSceneGraphProperty](reference-operators-update-scene-graph-property)要写入的属性。
| 属性 | 选择内容 |
| --- | --- |
| `Transform` | 实体变换，例如 `Transform.LocalMatrix`、`Transform.Position`、`Transform.Rotation`、`Transform.Scale`。 |
| `CameraAnchor` | 将实体锚定在相机空间中：`CameraAnchor.Follow`（位姿跟随相机/某个被追踪的目标——需提供一个 4×4 矩阵）和 `CameraAnchor.Locked`（世界锁定）。当被追踪的内容必须在常规 Volume 的边界之外保持可见时，搭配 [Portal 容器](concepts-containers-and-portals) 使用。 |
| `Text` | 文本属性，包括 `Text.HorizontalAlignment` / `Text.VerticalAlignment`。 |
| `PBRMaterials` | 可索引的材质列表：`PBRMaterials[i].BaseColor`、`PBRMaterials[i].BaseColorTexture`。 |
```text
// bind a dynamic texture into the first material's base-color texture
updateSceneGraphProperty(scene, "/", PBRMaterials[0].BaseColorTexture, dynamicTexture)
```

参见[驱动场景图输出](workflows-drive-scene-graph-output)。
## 延伸阅读

* [张量与形状](concepts-tensors-and-shapes)——概念模型。
* [算子目录](reference-operator-catalog)——消费这些类型的算子。
* [核心 API](reference-core-api)——创建张量的相关类型。

