根据一组 2D 图像点及其对应的 3D 模型点估算 3D 位姿（旋转 + 平移）——即经典的 Perspective-n-Point（PnP）问题。可用于将已知的 3D 物体锚定到相机所看到的位置上。
## 签名
```text
Pipeline.solvePnP(
    objPoints: Tensor,
    imgPoints: Tensor,
    camMatrix: Tensor,
    rotationVecResult: Tensor? = null,
    translationVecResult: Tensor? = null,
)
```

## 参数 / 结果
| 名称 | 类型 | 说明 |
| --- | --- | --- |
| `objPoints` | 输入 | 模型空间中的 3D 点。 |
| `imgPoints` | 输入 | 图像中与之对应的 2D 点。 |
| `camMatrix` | 输入 | 相机内参（例如来自 [rectifiedVSTAccess](zh-reference-operators-rectified-vst-access)）。 |
| `rotationVecResult` | 结果 | 可选的 `FLOAT64` 旋转向量（`1x3` / `3x1`）。 |
| `translationVecResult` | 结果 | 可选的 `FLOAT64` 平移向量（`1x3` / `3x1`）。 |
## 空间模式说明

* 相机矩阵应来自产生这些 2D 点检测所用图像的同一次 VST access 调用。
* `solvePnP` 输出的是一个**旋转向量**和一个**平移向量**（而非单一的位姿矩阵）。将它们传入 [makeTransform](zh-reference-operators-make-transform) 构建 `[4, 4]` 矩阵，再传入 [updateSceneGraphProperty](zh-reference-operators-update-scene-graph-property)，即可将 glTF 实体放置到物体所在的位置。
* 可以只提供 `rotationVecResult`、只提供 `translationVecResult`，或两者都提供。

## 相关算子

* [rectifiedVSTAccess](zh-reference-operators-rectified-vst-access) —— 相机矩阵的来源。
* [makeTransform](zh-reference-operators-make-transform) / [updateSceneGraphProperty](zh-reference-operators-update-scene-graph-property)
* [uvTo3DInCameraSpace](zh-reference-operators-uv-to-3d-in-camera-space) —— 另一种 2D→3D 提升方式。

