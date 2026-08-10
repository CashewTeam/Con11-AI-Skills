计算一个 2×3 仿射矩阵，将一组源点映射到一组目标点。[applyAffine](zh-reference-operators-apply-affine) 使用该矩阵结果对图像进行裁剪、缩放、旋转或其他形式的变形处理。
## 签名
```text
Pipeline.getAffine(
    srcPoints: Tensor,
    affinedPoints: Tensor,
    affineMatrixResult: Tensor,
)
```

## 参数 / 结果
| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `srcPoints` | 输入 | 源点集合（通常为三个 2D 点）。 |
| `affinedPoints` | 输入 | 变换后这些点应落到的位置。 |
| `affineMatrixResult` | 结果 | 用于接收仿射矩阵的 `FLOAT32` 张量，形状为 `[2, 3]`。 |
## 示例
来自 SuperResolutionApp 的仿射管线示例——三个源点及其目标位置生成缩放矩阵，并存入一个全局张量：
```kotlin
zoomPoints = newLocalTensor(
    MultiDimensionalInitInfo(DataType.FLOAT32, intArrayOf(3, 1), 2)
)

val targetZoomPoints = newLocalTensor(zoomPoints.config).apply {
    // (0,0), (AFFINE_IMG_SIZE-1, 0), (0, AFFINE_IMG_SIZE-1) written into SharedMemory
    tensorResource = mem
}

getAffine(zoomPoints, targetZoomPoints, zoomAffine)   // zoomAffine is FLOAT32 [2,3]
```

每当放大比例发生变化时，应用都会重写 `zoomPoints` 并重新运行该管线，因此下一帧的 `applyAffine` 会裁剪出不同的区域。
## 空间模式说明

* 矩阵结果必须是形状为 `[2, 3]` 的 `FLOAT32`。
* 点张量遵循 API 中其他位置所使用的 Point2 约定——三组对应点即可完全确定一个 2D 仿射变换。
* 当变换很少发生变化时，应将仿射计算拆分到独立的管线中（参见[异步管线模式](zh-workflows-async-pipeline-patterns)）；每帧都重新计算是一种浪费。

## 相关算子

* [applyAffine](zh-reference-operators-apply-affine) — 将矩阵应用于图像。
* [applyAffinePoint](zh-reference-operators-apply-affine-point) — 将其应用于点坐标。
* [makeTransform](zh-reference-operators-make-transform) — 构造完整的变换矩阵。
* [为模型准备图像数据](zh-workflows-prepare-image-data)

