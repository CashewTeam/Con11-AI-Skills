利用当前帧的时间戳、相机矩阵和立体图像，将图像空间中的 UV 坐标转换为相机空间中的 3D 点。这是从 2D 检测结果通往 3D 放置的桥梁。
## 签名
```text
Pipeline.uvTo3DInCameraSpace(
    uv: Tensor,
    timestamp: Tensor,
    camMatrix: Tensor,
    leftImage: Tensor,
    rightImage: Tensor,
    point3Result: Tensor,
)
```

## 参数 / 结果
| 参数 | 说明 |
| --- | --- |
| `uv` | 要投影的图像空间 UV / 像素坐标。 |
| `timestamp` | 帧时间戳（来自 [rectifiedVSTAccess](zh-reference-operators-rectified-vst-access)）。 |
| `camMatrix` | 相机内参矩阵（来自 `rectifiedVSTAccess`）。 |
| `leftImage`、`rightImage` | 该帧的立体（左右目）VST 图像。 |
| `point3Result` | 用相机空间 3D 点填充的结果张量。 |
## 空间模式说明

* 请传入来自**同一次** `rectifiedVSTAccess` 调用的时间戳、相机矩阵和左右目图像，以确保投影结果一致。
* `uv` 的典型来源是检测模型经过后处理的输出（如框中心点、关键点）。

## 相关算子

* [rectifiedVSTAccess](zh-reference-operators-rectified-vst-access) —— 提供时间戳、矩阵和图像。
* [solvePnP](zh-reference-operators-solve-pnp) —— 根据 2D/3D 对应关系求解位姿。
* [makeTransform](zh-reference-operators-make-transform) —— 根据得到的点构建变换。

