根据张量值显示或隐藏场景实体。可用于仅在结果就绪时才显示，或根据逐帧条件切换实体的可见性。
## 签名
```text
Pipeline.switchSceneVisibility(
    sceneEntity: Tensor,
    visible: Tensor,
)
```

## 参数 / 结果
| 名称 | 类型 | 说明 |
| --- | --- | --- |
| `sceneEntity` | 输入 | 来自 [newSceneFromGLTF](zh-reference-operators-new-scene-from-gltf) 的场景图张量。 |
| `visible` | 输入 | 驱动可见性的张量（非零 → 可见）。 |
## 示例
来自 SuperResolutionApp 初始化管线——在纹理绑定完成后，让显示面板变为可见：
```text
switchSceneVisibility(displaySceneGraph, displaySceneGraph)
```

## 空间模式说明

* `visible` 张量让可见性可以由数据驱动——传入一个比较/归约结果（例如来自 [bytewiseAny](zh-reference-operators-bytewise-any)），即可仅在条件成立时才显示实体。
* 可与 [submit](zh-reference-operators-submit) 的 `condition` 结合使用，实现完全条件化的更新。

## 相关算子

* [updateSceneGraphProperty](zh-reference-operators-update-scene-graph-property) —— 修改实体属性。
* [newSceneFromGLTF](zh-reference-operators-new-scene-from-gltf) —— 加载场景。
* [驱动场景图输出](zh-workflows-drive-scene-graph-output)

