按照 [SortType](zh-reference-tensor-types-and-enums#%E9%A2%9C%E8%89%B2-%E5%BD%92%E4%B8%80%E5%8C%96-%E8%8C%83%E6%95%B0%E4%B8%8E%E6%8E%92%E5%BA%8F%E7%9B%B8%E5%85%B3%E6%9E%9A%E4%B8%BE)（`BY_ROW` 或 `BY_COLUMN`）对矩阵张量进行排序。可用于对候选项的行进行排序（例如按得分对检测结果行排序）。
## 签名
```text
Pipeline.sortMatrix(
    sortType: SortType,
    source: Tensor,
    sortedResult: Tensor? = null,
    indexResult: Tensor? = null,
)
```

## 参数 / 结果
| 名称 | 类型 | 说明 |
| --- | --- | --- |
| `sortType` | 枚举 | `BY_ROW` 或 `BY_COLUMN`。 |
| `source` | 输入 | 要排序的矩阵张量。 |
| `sortedResult` | 结果 | 可选，用于接收排序后数值的张量。 |
| `indexResult` | 结果 | 可选，用于接收排列索引的张量。 |
## 空间模式说明

* 通过 `SortType`（`BY_ROW` / `BY_COLUMN`）选择排序轴。可以只提供 `sortedResult`、只提供 `indexResult`，或两者都提供。
* 如果只需排序单个向量，请使用 [sortVec](zh-reference-operators-sort-vec)。

## 相关算子

* [sortVec](zh-reference-operators-sort-vec) —— 对向量进行排序。
* [nonMaximumSuppression](zh-reference-operators-non-maximum-suppression) —— 检测结果后处理。

