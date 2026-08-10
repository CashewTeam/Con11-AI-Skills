计算矩阵张量的奇异值分解（SVD），生成 U、Σ、Vᵀ 三个因子。可用于图中的最小二乘拟合、位姿/朝向估计或降维。
## 签名
```text
Pipeline.singularValueDecomposition(
    source: Tensor,
    wResult: Tensor? = null,
    uResult: Tensor? = null,
    vtResult: Tensor? = null,
)
```

## 参数 / 结果
| 名称 | 类型 | 说明 |
| --- | --- | --- |
| `source` | 输入 | 待分解的 `MxN` 矩阵。 |
| `wResult` | 结果 | 可选，奇异值，形状为 `min(M,N) x 1`。 |
| `uResult` | 结果 | 可选，左奇异向量，形状为 `M x min(M,N)`。 |
| `vtResult` | 结果 | 可选，右奇异向量（已转置），形状为 `min(M,N) x N`。 |
## 空间模式说明

* 这是一个进阶的线性代数构建块；大多数视觉放置需求通过 [solvePnP](zh-reference-operators-solve-pnp) 或 [getAffine](zh-reference-operators-get-affine) 即可满足。
* 可以只提供 `wResult`、`uResult`、`vtResult` 中的任意子集；每个都需预先按上表所示形状分配。

## 相关算子

* [inversion](zh-reference-operators-inversion) —— 矩阵求逆。
* [solvePnP](zh-reference-operators-solve-pnp) —— 位姿估计。

