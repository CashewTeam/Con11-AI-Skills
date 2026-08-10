查找张量中最大值所在的索引。这是在计算图内部将模型的类别分数向量转换为预测类别索引的标准方式。
## 签名
```text
Pipeline.argmax(
    source: Tensor,
    result: Tensor,
)
```

## 参数 / 结果
| 名称 | 类别 | 说明 |
| --- | --- | --- |
| `source` | 输入 | 分数/logit 张量。 |
| `result` | 结果 | 接收最大元素的索引。其最后一个维度必须足够大，以容纳每个源维度对应的一个索引。 |
## 空间模式说明

* 在 [runModelInference](zh-reference-operators-run-model-inference) 之后运行，以选出预测类别。
* 可与 [get](zh-reference-operators-get) 结合使用，切片取出与命中索引关联的数据。

## 相关算子

* [runModelInference](zh-reference-operators-run-model-inference) —— 生成分数。
* [sortVec](zh-reference-operators-sort-vec) —— 完整排序（top-k）。
* [nonMaximumSuppression](zh-reference-operators-non-maximum-suppression) —— 检测结果后处理。

