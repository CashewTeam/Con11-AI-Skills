提取张量的一个切片或区域。切片操作通过在管线张量上使用 Kotlin 的方括号（`get`）运算符表示，返回一个 `PipelineTensorSlice`。之后可使用 [copy](zh-reference-operators-copy) 来读写该切片。
## 签名
```kotlin
// bracket operators on a PipelineTensor produce a PipelineTensorSlice
operator fun PipelineTensor.get(vararg indices: IntRange): PipelineTensorSlice
operator fun PipelineTensor.get(vararg indexAndSkips: IntProgression): PipelineTensorSlice
operator fun PipelineTensor.get(indices: PipelineTensor): PipelineTensorSlice

// a slice is read/written with copy(...)
Pipeline.copy(src: PipelineTensorSlice, dst: Tensor)
Pipeline.copy(src: Tensor, dst: PipelineTensorSlice)
```

## 用法
```text
// static slice: take rows 0..5 and columns 0..1
copy(source[0..5, 0..1], regionOut)

// strided slice via IntProgression (start, end, step)
copy(source[0..127 step 2, 0..127], halfResRows)

// dynamic slice: use a SliceInitInfo tensor computed at run time
copy(source[sliceTensor], regionOut)
```

对于动态切片，`sliceTensor` 是通过 [SliceInitInfo](zh-reference-tensor-types-and-enums#%E5%85%B6%E4%BB%96-init-info-%E7%B1%BB%E5%9E%8B) 创建的张量。
## 空间模式说明

* 可用它来提取某个子区域或特定的行/列，供后续处理使用。
* 分配目标张量时，需使其大小与所选区域内的元素数量一致。
* 切片操作不能应用于场景图张量。

## 相关算子

* [copy](zh-reference-operators-copy) — 移动整个张量或转换类型。
* [switchCHWAndHWC](zh-reference-operators-switch-chw-and-hwc) — 重新排列图像布局。
* [张量与形状](zh-concepts-tensors-and-shapes)

