创建一个仅存在于单个管线内部的张量，用于在算子之间流转数据时保存中间值。
## 签名
```text
// create from an init-info describing the tensor
Pipeline.newLocalTensor(config: Tensor.InitInfo): PipelineTensor
```

`newLocalTensor`提供多个重载，可接受不同的[初始化信息（init-info）类型](zh-reference-tensor-types-and-enums#%E5%BC%A0%E9%87%8F%E5%88%9D%E5%A7%8B%E5%8C%96%E4%BF%A1%E6%81%AF-init-info)（多维、标量、点数组等）。
## 参数
| 参数 | 描述 |
| --- | --- |
| `config` | 描述类型、形状与通道数的[初始化信息](zh-reference-tensor-types-and-enums#%E5%BC%A0%E9%87%8F%E5%88%9D%E5%A7%8B%E5%8C%96%E4%BF%A1%E6%81%AF-init-info)。 |
## 示例
来自 SuperResolutionApp 的示例：
```kotlin
val rightEye = newLocalTensor(
    MultiDimensionalInitInfo(DataType.UINT8, intArrayOf(512, 512), channel = 3)
)

// reuse an existing tensor's config to make a matching one
val targetPoints = newLocalTensor(zoomPoints.config)
```

## 空间模式说明

* 局部张量归属于单个管线，无法被[回读](zh-workflows-read-back-results)——如需可共享/可回读的数据，请使用 [session.newGlobalTensor](zh-reference-core-api#spatialmlsession)。
* 可通过写入 `tensorResource`（一块 [SharedMemory](zh-reference-core-api#sharedmemory)）来设置常量内容。
* 只有 [MultiDimensionalInitInfo](zh-reference-tensor-types-and-enums#multidimensionalinitinfo) 类型的张量支持 [arithmetic](zh-reference-operators-arithmetic)。

## 相关算子

* [newPlaceholder](zh-reference-operators-new-placeholder) — 接受在提交时绑定的全局张量。
* [copy](zh-reference-operators-copy) — 在张量之间移动/转换数据。
* [张量与形状](zh-concepts-tensors-and-shapes)

