[安全模式](concepts-secure-and-readback-modes)的会话会将其受保护的场景渲染在一个由运行时拥有的 SpatialML 容器内。容器控制该可见场景的形状，以及当场景内容超出其边界时会发生什么。
当前 SDK 支持三种容器类型：
| `SpatialMLSession.ContainerType` | 行为 | 典型用途 |
| --- | --- | --- |
| `VOLUMETRIC` | 一个有界的 3D 盒子。超出其宽、高或深的内容会被裁剪。 | 面板、固定显示以及设计为保持在已知体积内的 3D 内容。 |
| `PLANAR` | 一个 2D 平面。它可以渲染 3D 对象，但有效 Z 范围有限。`containerDepth` 会被忽略。 | 平面受保护输出，如图像、状态表面或仪表盘。 |
| `DISABLED` | 没有 SpatialML 拥有的容器。 | [回读模式](concepts-secure-and-readback-modes)，应用接收结果并在应用自有的内容中渲染。 |
`VOLUMETRIC` 是默认值。
## 常规 Volume 与 Portal
调用 [SpatialMLSession.InitInfo.addPortal()](reference-core-api#addportal) 会在立体（volumetric）SpatialML 容器的背面添加一个隐藏的 portal 面板。
**Portal 不是第四种容器类型**
API 没有定义 `PORTAL` 这种 `ContainerType`。Portal 容器是一个通过 `addPortal()` 配置了 `InitInfo` 的 `VOLUMETRIC` 容器。
|  | 常规立体容器 | 带 `addPortal()` 的立体容器 |
| --- | --- | --- |
| 基本形状 | 有界 3D 盒子 | 同样的有界 3D 盒子，加上背面的 portal 面板 |
| 超出体积的内容 | 在容器边界处被裁剪 | 可以**通过 portal 面板**保持可见 |
| 最适合 | 有意限制在盒子内的内容 | 可以移出盒子的相机锚定或被追踪内容 |
| 主要优势 | 可预测的合成与裁剪 | 在不让受保护数据被应用读取的前提下保持可见性 |
| 配置方式 | `ContainerType.VOLUMETRIC` 且尺寸为正值 | 相同配置后加上 `.addPortal()` |
常规 Volume 容器适用于裁剪本身就是表现形式一部分的场景：面板上的处理后图像、有界的模型预览，或内容布局在已知盒子内的场景。其边界可以防止内容在视觉上逃逸到用户的周围环境中。
Portal 容器适用于内容的位置来自相机而非固定布局的场景。例如，一个对象检测器可以为数字孪生体生成相机空间变换。如果被追踪的对象移动到超出配置的体积深度，常规 Volume 会裁剪掉数字孪生体——即使追踪仍然成功。有了 portal，用户可以继续通过背面面板看到数字孪生体。

## 创建 Portal 容器
创建一个普通的立体 `InitInfo`，然后在传给 `createSession` 之前链式调用 `addPortal()`：
```kotlin
val initInfo =
    SpatialMLSession.InitInfo(
        imageWidth = 580,
        imageHeight = 326,
        containerWidth = 1000,
        containerHeight = 1000,
        containerDepth = 10,
        containerType = SpatialMLSession.ContainerType.VOLUMETRIC,
    ).addPortal()

val session = instance.createSession(initInfo)
    ?: error("SpatialML session creation returned null")
```

`addPortal()` 返回同一个 `InitInfo`，因此链式调用是常规用法。
## 要求与限制

* `containerType` 必须是 `ContainerType.VOLUMETRIC`。
* `containerWidth`、`containerHeight` 和 `containerDepth` 必须全部为正值。
* 对 `PLANAR`、`DISABLED` 或非正尺寸调用 `addPortal()` 会抛出 `SpatialMLException`。
* portal 改变了通过容器的可见性；它**不会**启用回读或将受保护的相机数据移入应用内存。
* portal 不能替代场景锚定。请使用诸如 [CameraAnchor.Follow](reference-tensor-types-and-enums#scenegraphproperty) 之类的场景图属性来提供被追踪的相机空间变换。

## 选择容器

对于有界 3D 输出，默认使用**常规 Volume**。仅当体验需要为相机空间位置可能超出该体积的内容保持可见性时——尤其是被追踪对象的叠加层和数字孪生体——才添加 **Portal**。
## 示例：FaceDetection
[FaceDetection 示例](samples-face-detection)是 Portal 的参考用例：

1. 一个 Pipeline 包检测到一张人脸。
2. `uvTo3DInCameraSpace` 将检测结果转换为相机空间中的点。
3. 应用将变换写入 `CameraAnchor.Follow`。
4. 当该变换超出正常体积边界时，portal 使人脸框架保持可见。

## 延伸阅读

* [安全模式与回读模式](concepts-secure-and-readback-modes) —— 选择隐私与输出路径。
* [驱动场景图输出](workflows-drive-scene-graph-output) —— 从管线更新受保护场景。
* [FaceDetection 示例](samples-face-detection) —— 查看 Portal 与相机锚定的配合使用。
* [核心 API：](reference-core-api#spatialmlsession-initinfo)[SpatialMLSession.InitInfo](reference-core-api#spatialmlsession-initinfo) —— 确切的容器 API。

