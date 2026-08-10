原始的 VST 图像帧很少能直接匹配模型的输入约定。在[相机访问](workflows-access-camera-vst)和[推理](workflows-run-model-inference)之间，你通常需要裁剪/缩放、转换数据类型、归一化，有时还要重排通道顺序。本页以 [SuperResolutionApp](samples-super-resolution) 的处理链路为例，介绍这些预处理算子。
## 示例的预处理链路
SuperResolution 模型需要一张较小的、经过归一化的 `FLOAT32` 图像。示例把一帧 512×512 的 `UINT8` 相机图像转换成一张 `[0, 1]` 范围内的 128×128 `FLOAT32` 图像：
```kotlin
// 1. crop/scale with an affine transform (512x512 UINT8 -> 128x128 UINT8)
val affinedUint8 = newLocalTensor(
    MultiDimensionalInitInfo(DataType.UINT8, intArrayOf(128, 128), channel = 3)
)
applyAffine(zoomAffine, rightEyeImg, affinedUint8)

// 2. convert integer pixels to float
val affinedFloat = newLocalTensor(
    MultiDimensionalInitInfo(DataType.FLOAT32, intArrayOf(128, 128), channel = 3)
)
copy(affinedUint8, affinedFloat)

// 3. scale into the model's expected [0, 1] range
arithmetic(affinedFloat) { affinedFloat / 255.0 }
```


## 按任务分类的算子
| 任务 | 算子 | 说明 |
| --- | --- | --- |
| 裁剪 / 缩放 / 变焦 | [applyAffine](reference-operators-apply-affine) | 通过一个 2×3 仿射矩阵对图像做重采样。用 [getAffine](reference-operators-get-affine) 构建该矩阵。 |
| 转换数据类型 | [copy](reference-operators-copy) | 在不同 `DataType` 的张量之间拷贝会自动转换数值（例如 `UINT8` → `FLOAT32`）。 |
| 缩放 / 归一化 | [arithmetic](reference-operators-arithmetic) 或 [normalize](reference-operators-normalize) | `arithmetic` 运行一个像 `{ t / 255.0 }` 这样的闭包表达式；`normalize` 则应用配置好的归一化方式。 |
| 转换色彩排布 | [convertColor](reference-operators-convert-color) | RGB 与其他排布之间的转换 / 通道数变化。 |
| 重排通道 | [switchCHWAndHWC](reference-operators-switch-chw-and-hwc) | 在图像风格的 HWC 与模型风格的 CHW 之间切换。 |
## 构建仿射矩阵
`applyAffine` 需要一个 2×3 矩阵。可以用 [getAffine](reference-operators-get-affine) 根据源点→目标点的对应关系计算出它。示例把这一步放在一条**独立的管线**中运行，这样它只在缩放级别变化时才重新计算，而不是每帧都算：
```text
// source points (in the camera image) and destination points (in the cropped image)
getAffine(zoomPoints, targetZoomPoints, zoomAffine)   // writes the 2x3 matrix into zoomAffine
```

`zoomAffine` 是一个[全局张量](concepts-tensors-and-shapes#%E5%85%A8%E5%B1%80%E5%BC%A0%E9%87%8F%E4%B8%8E%E6%9C%AC%E5%9C%B0%E5%BC%A0%E9%87%8F)，所以逐帧管线读取到的，是仿射管线产生的最新矩阵。这两条管线之间如何排序，请参见[执行模型](concepts-execution-model#%E7%AE%A1%E7%BA%BF%E6%8E%92%E5%BA%8F)。
## 设置点数据
点类型的张量通过 `tensorResource` 获取数值。示例把裁剪区域的目标角点写入一个 `SharedMemory` 缓冲区：
```kotlin
SharedMemory.create("affine_dst_points", 6 * Float.SIZE_BYTES).use { mem ->
    val buf = mem.mapReadWrite().order(ByteOrder.nativeOrder())
    buf.putFloat(0f);   buf.putFloat(0f)      // top-left
    buf.putFloat(127f); buf.putFloat(0f)      // top-right
    buf.putFloat(0f);   buf.putFloat(127f)    // bottom-left
    SharedMemory.unmap(buf)
    targetZoomPoints.tensorResource = mem
}
```

## 精确匹配模型约定
在接入推理之前，请对照你的模型逐项确认以下内容：

* **形状**——输入张量的宽度、高度和通道数。
* **类型**——归一化之后通常是 `FLOAT32`。
* **范围**——`[0, 1]`、`[-1, 1]`，或原始范围；应用对应的 `arithmetic`/`normalize` 步骤。
* **数据排布**——HWC 还是 CHW；如有需要，插入 [switchCHWAndHWC](reference-operators-switch-chw-and-hwc)。

这里的不匹配是模型输出错误或为空最常见的原因——参见[疑难排查](troubleshooting)。
## 延伸阅读

* [运行模型推理](workflows-run-model-inference)——把准备好的张量喂给模型。
* [applyAffine](reference-operators-apply-affine) / [getAffine](reference-operators-get-affine)——变换类算子。
* [arithmetic](reference-operators-arithmetic)——基于表达式的张量运算。

