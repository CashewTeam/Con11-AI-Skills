对一个或多个操作数张量应用算术表达式，并将结果写入目标张量。推荐的写法是传入一个 Kotlin 闭包，其最后一行即为要求值的表达式——操作数的形状和数据类型会在构建时被校验。
## 签名
```text
Pipeline.arithmetic(
    result: Tensor,
    arithmeticOperations: PipelineArithmeticScope.() -> PipelineArithmeticScope.TensorArithmetic,
)
```

闭包中的最后一个表达式会被赋值给 `result`。在闭包内部，你可以像普通 Kotlin 数学运算一样操作张量（和标量），该作用域会校验操作数之间的兼容性。
## 参数 / 结果
| 名称 | 类别 | 说明 |
| --- | --- | --- |
| `result` | 结果 | 目标张量。其维度必须与闭包最终表达式的形状一致。可与某个操作数别名相同，以执行原地运算。 |
| `arithmeticOperations` | 闭包 | 一个 `PipelineArithmeticScope` 代码块；其最后一行的值即为结果。 |
## 支持的运算
在闭包内部，你可以使用以下方式组合张量和标量：
| 运算 | 含义 |
| --- | --- |
| `a + b`, `a - b` | 逐元素加 / 减。 |
| `a * b` | 矩阵乘法。 |
| `a / b` | 逐元素除法（支持标量，例如 `t / 255.0`）。 |
| `a ^ b` | 逐元素幂运算。 |
| `a.T()` / `transpose(a)` | 矩阵转置。 |
| `inv(a)` | 矩阵求逆。 |
| `sin`, `cos`, `tan`, `asin`, `acos`, `atan`, `sinh`, `cosh`, `tanh` | 逐元素三角函数。 |
| `a.power(n)` | 按标量进行逐元素幂运算。 |
## 示例
以下摘自 SuperResolution 示例——在推理前将来自 `UINT8` 的浮点值归一化到模型所需的 `[0,1]` 范围，推理后再缩放回 `[0,255]` 以便显示：
```text
// scale into the model's 0..1 range
arithmetic(affinedFloat) { affinedFloat / 255.0 }

// ... runModelInference ...

// scale the model output back to 0..255 for display
arithmetic(zoomedResult) { zoomedResult * 255.0 }
```

单个表达式中包含多个操作数的例子，摘自 Stylization 示例：
```yaml
arithmetic(stylizedImage) { stylizeInput - stylizeClip + stylizeOutput }
```

## 空间模式说明

* **所有操作数必须是二维矩阵**——即维度恰好为二的多维张量（[MultiDimensionalInitInfo](zh-reference-tensor-types-and-enums#multidimensionalinitinfo)）。
* **操作数必须是浮点类型**（例如 `FLOAT32`）；不允许使用多通道像素图像数据类型。请先用 [copy](zh-reference-operators-copy) 将 `UINT8` 图像数据转换为浮点张量。
* 单个闭包中**最多可涉及 10 个张量**——更长的计算请拆分到多个 `arithmetic` 调用中。
* 将结果写回某个操作数即可实现原地运算。
* 已弃用的字符串表达式重载（`arithmetic(expression, operands, result)`，使用 `{0}`、`{1}` 等占位符）仍然存在，但更推荐使用上述闭包写法，因为它会校验操作数的形状和数据类型。

## 相关算子

* [normalize](zh-reference-operators-normalize) —— 预设的归一化方案。
* [elementwiseMultiply](zh-reference-operators-elementwise-multiply) —— 逐元素乘积。
* [copy](zh-reference-operators-copy) —— 数据类型转换。
* [为模型准备图像数据](zh-workflows-prepare-image-data)

