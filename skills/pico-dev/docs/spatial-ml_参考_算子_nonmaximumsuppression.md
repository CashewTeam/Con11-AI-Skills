抑制相互重叠的检测框，只保留分数最高且互不重叠的候选框。这是目标检测模型产生大量原始重叠框之后的标准后处理步骤。
## 签名
```text
Pipeline.nonMaximumSuppression(
    iou: Float,
    scores: Tensor,
    boxes: Tensor,
    scoresResult: Tensor? = null,
    boxesResult: Tensor? = null,
    indicesResult: Tensor? = null,
)
```

## 参数 / 结果
| 名称 | 类型 | 说明 |
| --- | --- | --- |
| `iou` | float | 交并比（IoU）阈值；与某个保留框重叠程度超过该阈值的框会被抑制。 |
| `scores` | 输入 | 每个框对应的置信度分数。 |
| `boxes` | 输入 | 候选框，形状为 `Nx4`，采用 `XXYY`（x 最小值、x 最大值、y 最小值、y 最大值）布局。 |
| `scoresResult` | 结果 | 可选，保留下来的分数。 |
| `boxesResult` | 结果 | 可选，保留下来的框。 |
| `indicesResult` | 结果 | 可选，保留框的索引。 |
## 空间模式说明

* 在 [runModelInference](zh-reference-operators-run-model-inference) 之后、将检测结果提升到 3D 之前运行此算子。可以只提供这三个结果张量中的任意子集。
* 框的形状为 `Nx4`，采用 `XXYY` 布局。
* 可与 [argmax](zh-reference-operators-argmax) 结合使用以为每个框选取类别，再用 [uvTo3DInCameraSpace](zh-reference-operators-uv-to-3d-in-camera-space) 将保留下来的检测结果放置到场景中。

## 相关算子

* [runModelInference](zh-reference-operators-run-model-inference) —— 生成原始检测框。
* [argmax](zh-reference-operators-argmax) —— 类别选择。
* [get](zh-reference-operators-get) —— 切片取出保留的检测结果。

