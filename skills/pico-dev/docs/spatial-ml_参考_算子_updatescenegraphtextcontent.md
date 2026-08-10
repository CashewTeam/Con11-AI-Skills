设置已加载场景图中某个文本实体的字符串内容。可用于显示由计算图结果驱动的动态标签——识别出的文本、计数、状态等。
## 签名
```text
Pipeline.updateSceneGraphTextContent(
    sceneEntity: Tensor,
    entityPath: String,
    text: String,
)
```

## 参数 / 结果
| 名称 | 类型 | 说明 |
| --- | --- | --- |
| `sceneEntity` | 输入 | 来自 [newSceneFromGLTF](zh-reference-operators-new-scene-from-gltf) 的场景图张量。 |
| `entityPath` | 输入 | 文本节点的路径。 |
| `text` | 输入 | 要显示的字符串。 |
## 空间模式说明

* 目标节点必须是 glTF 场景中的文本实体。
* 该文本是一个 Kotlin `String`——本算子是对 [updateSceneGraphProperty](zh-reference-operators-update-scene-graph-property) 配合 `Text.Content` 属性的便捷封装。
* 可与对齐相关算子搭配使用以控制版式。

## 相关算子

* [updateSceneGraphTextHorizontalAlignment](zh-reference-operators-update-scene-graph-text-horizontal-alignment)
* [updateSceneGraphTextVerticalAlignment](zh-reference-operators-update-scene-graph-text-vertical-alignment)
* [updateSceneGraphProperty](zh-reference-operators-update-scene-graph-property) —— 其他实体属性。
* [驱动场景图输出](zh-workflows-drive-scene-graph-output)

