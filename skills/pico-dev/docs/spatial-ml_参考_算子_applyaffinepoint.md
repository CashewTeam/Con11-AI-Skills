将 2×3 仿射矩阵应用于点的**坐标**，而非图像像素。可用于在不同坐标系之间移动检测关键点、边界框角点或特征点（例如，将裁剪后的模型空间坐标映射回完整的相机空间）。
## 签名
```text
Pipeline.applyAffinePoint(
    affineMatrix: Tensor,
    srcPoints: Tensor,
    affinedPoints: Tensor,
)
```

## 参数 / 结果
| 名称 | 类别 | 说明 |
| --- | --- | --- |
| `affineMatrix` | 输入 | `FLOAT32` `[2, 3]` 矩阵（通常是裁剪变换的逆矩阵）。 |
| `srcPoints` | 输入 | 待变换的点张量。 |
| `affinedPoints` | 结果 | 变换后的点张量。 |
## 空间模式说明

* 此算子变换的是坐标，而非图像内容——如需处理像素，请使用 [applyAffine](zh-reference-operators-apply-affine)。
* 常见做法是先对裁剪矩阵求逆（参见 [inversion](zh-reference-operators-inversion)），使模型空间中的检测结果映射回相机空间的 UV 坐标，以便传入 [uvTo3DInCameraSpace](zh-reference-operators-uv-to-3d-in-camera-space)。

## 相关算子

* [getAffine](zh-reference-operators-get-affine) / [applyAffine](zh-reference-operators-apply-affine)
* [inversion](zh-reference-operators-inversion) —— 对变换矩阵求逆。
* [uvTo3DInCameraSpace](zh-reference-operators-uv-to-3d-in-camera-space) —— 将二维点提升到三维。

