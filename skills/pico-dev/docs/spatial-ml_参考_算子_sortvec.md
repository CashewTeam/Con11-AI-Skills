将向量（标量数组）张量的元素按升序排序，可选择性地输出排序后的数值和/或排列索引。
## 签名
```text
Pipeline.sortVec(
    source: Tensor,
    sortedResult: Tensor? = null,
    indexResult: Tensor? = null,
)
```

## 参数 / 结果
| 名称 | 类型 | 说明 |
| --- | --- | --- |
| `source` | 输入 | 要排序的向量张量。 |
| `sortedResult` | 结果 | 可选，用于接收排序后数值的张量（初始化信息与 `source` 相同）。 |
| `indexResult` | 结果 | 可选，用于接收排列索引的张量。 |
## 空间模式说明

* `sortVec` 对一维向量排序，**不**接受排序类型参数。可以只提供 `sortedResult`、只提供 `indexResult`，或两者都提供——但至少要提供一个。
* 当单纯使用 [argmax](zh-reference-operators-argmax) 无法满足需求时，可用它对得分向量做 top-k 选取。
* 处理二维数据时请使用 [sortMatrix](zh-reference-operators-sort-matrix)。

## 相关算子

* [sortMatrix](zh-reference-operators-sort-matrix) —— 按行或按列对矩阵排序。
* [argmax](zh-reference-operators-argmax) —— 取单个最优索引。

