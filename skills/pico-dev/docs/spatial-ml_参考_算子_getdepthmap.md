获取当前帧的深度图，用于深度感知放置、过滤或遮挡类逻辑。
## 签名
```text
Pipeline.getDepthMap(depthMapResult: Tensor)
```

## 参数 / 结果
| 参数 | 描述 |
| --- | --- |
| `depthMapResult` | 由调用方分配的结果张量；算子会将深度图写入其中。 |
## 空间模式说明

* 深度视场角固定为**垂直 90°、水平 109°**。请据此设置结果尺寸并解释坐标。
* 与 [rectifiedVSTAccess](zh-reference-operators-rectified-vst-access) 类似，该算子只产生结果，不接受操作数。
* 当需要在同一帧中同时获取彩色图像和深度信息时，可与相机访问算子搭配使用。

## 示例
```kotlin
val depth = newLocalTensor(
    MultiDimensionalInitInfo(DataType.FLOAT32, intArrayOf(512, 512))
)
getDepthMap(depthMapResult = depth)
```

## 相关算子

* [rectifiedVSTAccess](zh-reference-operators-rectified-vst-access) — 彩色图像与相机矩阵。
* [uvTo3DInCameraSpace](zh-reference-operators-uv-to-3d-in-camera-space) — 与深度信息结合进行 3D 定位。
* [访问 VST 相机图像](zh-workflows-access-camera-vst)

