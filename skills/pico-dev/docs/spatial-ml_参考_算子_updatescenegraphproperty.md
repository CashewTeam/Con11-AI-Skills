更新已加载场景图中某个实体的属性——例如其变换、材质颜色、基础颜色纹理等。这是空间模式管线将结果推送到用户可见画面的主要方式。
## 签名
```text
Pipeline.updateSceneGraphProperty(
    sceneEntity: Tensor,
    entityPath: String,
    targetProperty: SceneGraphProperty,
    data: Tensor,
)
```

## 参数 / 结果
| 名称 | 类型 | 说明 |
| --- | --- | --- |
| `sceneEntity` | 输入 | 来自 [newSceneFromGLTF](zh-reference-operators-new-scene-from-gltf) 的场景图张量。 |
| `entityPath` | 输入 | 目标节点的路径，例如根节点为 `"/"`。 |
| `targetProperty` | 输入 | 要设置的属性——参见 [SceneGraphProperty](zh-reference-tensor-types-and-enums#scenegraphproperty)。 |
| `data` | 输入 | 保存新值的张量（矩阵、颜色、纹理等）。 |
## 示例
来自 SuperResolutionApp——将管线的动态纹理绑定为面板的基础颜色纹理：
```text
updateSceneGraphProperty(
    displaySceneGraph,
    "/",
    PBRMaterials[0].BaseColorTexture,   // SceneGraphProperty
    dynamicTexture,                     // UINT8 dynamic-texture global tensor
)
```

若要移动实体，则改为针对变换属性传入一个 `[4,4]` 矩阵：
```text
updateSceneGraphProperty(scene, "/node", SceneGraphProperty.Transform.LocalMatrix, poseMatrix)
```

## 空间模式说明

* `SceneGraphProperty` 是一个密封（sealed）层级结构：`Transform`（例如 `Transform.LocalMatrix`）、`PBRMaterials[i].BaseColor` / `.BaseColorTexture`、`Text`、`CameraAnchor`。参见 [张量类型与枚举](zh-reference-tensor-types-and-enums#scenegraphproperty)。
* `data` 张量的类型/形状必须与目标属性相匹配（变换需要矩阵，纹理需要纹理张量）。
* 只需绑定一次**动态纹理**张量，后续帧只需通过 [copy](zh-reference-operators-copy) 写入该纹理即可更新可见画面——无需每帧都更新属性（示例中所采用的正是这一模式）。

## 相关算子

* [newSceneFromGLTF](zh-reference-operators-new-scene-from-gltf) —— 先加载场景。
* [switchSceneVisibility](zh-reference-operators-switch-scene-visibility) —— 显示/隐藏实体。
* [makeTransform](zh-reference-operators-make-transform) —— 为变换更新构建矩阵。
* [驱动场景图输出](zh-workflows-drive-scene-graph-output)

