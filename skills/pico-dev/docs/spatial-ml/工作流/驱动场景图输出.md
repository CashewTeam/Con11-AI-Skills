在 [安全模式](concepts-secure-and-readback-modes)下，管线通过直接驱动一个由 SpatialML 拥有的场景来展示结果——不需要回读、不需要相机权限，源自相机的像素数据永远不会离开运行时。本页介绍用于从图中更新 SpatialEngine 内容的场景图相关算子。
## 选择容器如何裁剪内容
场景图输出被渲染在会话的 [SpatialML 容器](concepts-containers-and-portals)内：

* 常规 `VOLUMETRIC` 容器会裁剪其 3D 盒子外的场景内容。
* `VOLUMETRIC` 加上 `addPortal()` 让超出边界的内容通过体积背面的隐藏面板保持可见。适用于由被追踪的相机空间位姿驱动的 `CameraAnchor.Follow` 输出。
* `PLANAR` 适用于 Z 范围有限的平面受保护输出。

portal 仅改变容器的可见性；场景更新仍然使用下面相同的算子。
## 场景就是一个全局张量
你可以用 [session.newSceneFromGLTF](reference-core-api#spatialmlsession)（或其 `suspend` 版本）从 glTF 资源加载场景。它会返回一个代表该场景的 [GlobalTensor](concepts-tensors-and-shapes#%E5%85%A8%E5%B1%80%E5%BC%A0%E9%87%8F%E4%B8%8E%E6%9C%AC%E5%9C%B0%E5%BC%A0%E9%87%8F)；场景图相关算子会接收这个张量，再加上要更新的**实体路径**和**属性**。
```kotlin
val displayScene = session.newSceneFromGLTFSuspend("Display512.glb")
```

## 场景图相关算子
| 算子 | 更新内容 |
| --- | --- |
| [updateSceneGraphProperty](reference-operators-update-scene-graph-property) | 实体上的某个属性：变换、材质颜色/贴图等。 |
| [switchSceneVisibility](reference-operators-switch-scene-visibility) | 某个场景/实体是否显示。 |
| [updateSceneGraphTextContent](reference-operators-update-scene-graph-text-content) | 文本实体的字符串内容。 |
| [updateSceneGraphTextHorizontalAlignment](reference-operators-update-scene-graph-text-horizontal-alignment) | 文本水平对齐方式。 |
| [updateSceneGraphTextVerticalAlignment](reference-operators-update-scene-graph-text-vertical-alignment) | 文本垂直对齐方式。 |
要更新哪个属性，是通过 [SceneGraphProperty](reference-tensor-types-and-enums#scenegraphproperty) 这个密封层级结构来选择的——包括 `Transform`、`PBRMaterials[i].BaseColor` / `.BaseColorTexture`、`CameraAnchor`，以及 `Text` 对齐相关属性。
## 在场景中显示管线的图像
最常见的模式：把一个[动态贴图](concepts-tensors-and-shapes#%E5%8A%A8%E6%80%81%E7%BA%B9%E7%90%86)全局张量绑定到某个材质的基础色贴图上，然后让场景可见。这是一次性的接线工作，所以示例把它放在了一条专门的初始化管线里：
```text
session.newPipeline().run {
    // replace the panel material's base-color texture with the pipeline's output texture
    updateSceneGraphProperty(
        displayScene,                       // scene entity (GlobalTensor)
        "/",                                // entity path within the scene
        PBRMaterials[0].BaseColorTexture,   // which property
        dynamicTexture,                     // data (the live texture)
    )
    // make it visible
    switchSceneVisibility(displayScene, displayScene)
    submit(mapOf(), null, null)
}
```

这段代码运行一次之后，逐帧管线只需要持续向 `dynamicTexture` 写入新的像素（例如将 RGB 结果转换为 RGBA 纹理），运行时就会自动重新渲染面板——不再需要每帧调用场景相关算子。

对于 8 位色彩渲染目标，推荐使用 RGBA 动态纹理并显式转换 RGB 输出：
```kotlin
val dynamicTexture = session.newGlobalTensor(
    MultiDimensionalInitInfo(
        DataType.Image.R8G8B8A8_U_DYNAMIC,
        intArrayOf(512, 512),
    )
)

// `rgbOutput` is an R8G8B8_U tensor with matching dimensions.
convertColor(Pipeline.ColorConversion.RGB_TO_RGBA, rgbOutput, dynamicTexture)
```

这是 SuperResolution 示例当前使用的模式。三通道 RGB 动态纹理可能在渲染路径上失败；RGBA 也为回读提供了一致的四字节像素布局。
## 更新变换与文本
同样的 `updateSceneGraphProperty` 调用，只要选择不同的 `SceneGraphProperty`，就能驱动其他属性：
```text
// move/rotate/scale an entity via its local matrix
updateSceneGraphProperty(scene, "/Anchor", Transform.LocalMatrix, matrixTensor)

// set a base color (not a texture)
updateSceneGraphProperty(scene, "/Panel", PBRMaterials[0].BaseColor, colorTensor)
```

对于文本实体，可以用专门的文本算子来设置字符串和对齐方式——参见 [updateSceneGraphTextContent](reference-operators-update-scene-graph-text-content)。
## 只绑定一次，而不是每帧都绑定
优先把持久性的属性（贴图绑定、可见性）在初始化管线中**只接线一次**，让运行时随着底层张量的变化自动重新渲染。把逐帧场景算子留给那些确实每帧都会变化的值（例如一个持续移动的变换）。这与示例中把初始化管线和 10 Hz 的主管线分开是一致的思路。
## 延伸阅读

* [容器与传送门](concepts-containers-and-portals) —— 比较常规 Volume 与 Portal 行为。
* [updateSceneGraphProperty](reference-operators-update-scene-graph-property)[ 算子卡片](reference-operators-update-scene-graph-property)
* [switchSceneVisibility](reference-operators-switch-scene-visibility)[ 算子卡片](reference-operators-switch-scene-visibility)
* [张量类型与枚举：SceneGraphProperty](reference-tensor-types-and-enums#scenegraphproperty)
* [安全模式与回读模式](concepts-secure-and-readback-modes)

