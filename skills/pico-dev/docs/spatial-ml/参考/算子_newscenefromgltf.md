将 glTF 资产加载为场景图张量，后续算子可以通过实体路径来寻址它。在空间模式下，这是将可渲染内容（面板、模型、控制器）引入计算图的方式，以便管线对其进行变换和展示。
## 签名
```kotlin
// Session-level (outside a pipeline) — returns a GlobalTensor
SpatialMLSession.newSceneFromGLTF(assetName: String): GlobalTensor
suspend fun SpatialMLSession.newSceneFromGLTFSuspend(assetName: String): GlobalTensor
```

场景图全局张量在 **会话** 上创建，随后由管线内部的场景图算子引用。
## 参数 / 结果
| 名称 | 类型 | 说明 |
| --- | --- | --- |
| `assetName` | 输入 | 随应用打包的 glTF/GLB 资产文件名。 |
| return | 结果 | 指向已加载场景的 `GlobalTensor` 句柄。 |
## 示例
来自 SuperResolutionApp（Secure Mode 路径）——加载一个显示面板，为其绑定动态纹理并展示：
```text
displaySceneGraph = session.newSceneFromGLTFSuspend("Display512.glb")

session.newPipeline().run {
    updateSceneGraphProperty(
        displaySceneGraph, "/", PBRMaterials[0].BaseColorTexture, dynamicTexture,
    )
    switchSceneVisibility(displaySceneGraph, displaySceneGraph)
    submit(mapOf(), null, null)
}
```

## 空间模式说明

* 场景图张量是**全局**的（会话作用域），因此多条管线可以跨帧寻址同一个场景。
* 形如 `"/"`（根节点）的实体路径用于寻址已加载 glTF 内部的节点；材质/纹理/变换更新都以这些路径为目标。
* 加载是 I/O 密集型操作——建议在协程中优先使用 `newSceneFromGLTFSuspend`（参见[异步管线模式](zh-workflows-async-pipeline-patterns)）。

## 相关算子

* [updateSceneGraphProperty](zh-reference-operators-update-scene-graph-property) —— 更改材质/变换/纹理。
* [switchSceneVisibility](zh-reference-operators-switch-scene-visibility) —— 显示或隐藏它。
* [驱动场景图输出](zh-workflows-drive-scene-graph-output)

