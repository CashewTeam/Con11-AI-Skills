计算方阵张量的逆矩阵。最常见的用途是对仿射矩阵或变换矩阵求逆，以便将结果映射回原始坐标系。
## 签名
```text
Pipeline.inversion(
    source: Tensor,
    result: Tensor,
)
```

## 参数 / 结果
| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `source` | 输入 | 待求逆的方阵张量。 |
| `result` | 结果 | 逆矩阵。 |
## 空间模式说明

* 输入必须是合法的、可逆的方阵。
* 典型用法：先对裁剪/仿射矩阵求逆，再使用 [applyAffinePoint](zh-reference-operators-apply-affine-point) 将模型空间中的点变换回相机空间。

## 相关算子

* [applyAffinePoint](zh-reference-operators-apply-affine-point) — 将求逆后的变换应用于点。
* [makeTransform](zh-reference-operators-make-transform) — 构造变换矩阵。
* [singularValueDecomposition](zh-reference-operators-singular-value-decomposition) — 相关的线性代数算子。

