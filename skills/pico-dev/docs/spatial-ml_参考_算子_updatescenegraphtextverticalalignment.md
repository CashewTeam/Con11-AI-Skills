使用 [TextVerticalAlignment](zh-reference-tensor-types-and-enums#%E6%96%87%E6%9C%AC%E5%AF%B9%E9%BD%90%E6%9E%9A%E4%B8%BE) 值，设置已加载场景图中某个文本实体的垂直对齐方式。
## 签名
```text
Pipeline.updateSceneGraphTextVerticalAlignment(
    sceneEntity: Tensor,
    entityPath: String,
    alignment: TextVerticalAlignment,
)
```

## 参数 / 结果
| 名称 | 类型 | 说明 |
| --- | --- | --- |
| `sceneEntity` | 输入 | 来自 [newSceneFromGLTF](zh-reference-operators-new-scene-from-gltf) 的场景图张量。 |
| `entityPath` | 输入 | 文本节点的路径。 |
| `verticalAlignment` | 枚举 | 垂直对齐方式的取值。 |
## 空间模式说明

* 目标节点必须是文本实体。
* 除非对齐方式需要随内容变化，否则只需在初始化时设置一次。

## 相关算子

* [updateSceneGraphTextContent](zh-reference-operators-update-scene-graph-text-content) —— 设置字符串内容。
* [updateSceneGraphTextHorizontalAlignment](zh-reference-operators-update-scene-graph-text-horizontal-alignment)
* [驱动场景图输出](zh-workflows-drive-scene-graph-output)

