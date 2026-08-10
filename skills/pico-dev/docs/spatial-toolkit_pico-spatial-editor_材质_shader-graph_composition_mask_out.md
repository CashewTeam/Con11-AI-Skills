输出前景中不与背景重叠的区域。

**Out** 节点使用前景和背景输入的 Alpha 通道来决定输出结果。从视觉上看，这意味着只有前景中不与背景 Alpha 重叠的部分会被保留下来。

* 输出的 RGB 分量为：F⋅(1 − b)
* 输出的 Alpha 分量为：f⋅(1 − b)

## **参数说明**

* **Foreground**：Color 4 类型的前景输入，其中 `F` 表示该参数的 RGB 分量，`f` 表示该参数的 Alpha 分量。
* **Background**：Color 4 类型的背景输入，其中 `B` 表示该参数的 RGB 分量，`b` 表示该参数的 Alpha 分量。
* **Mix**：混合操作的权重。**Mix** 值越高，混合效果越明显。默认值为 `1`。取值超出 `0` 到 `1` 范围时，会产生超出该节点预期功能之外的未定义效果。

## **节点使用说明**
下面的示例节点图展示了如何使用 **Out** 节点将两种纹理进行混合。

下方展示了两张原始图像、背景 Alpha 图像以及将最终混合纹理应用到立方体表面的结果（**Mix** = 0.5）。

<strong>Foreground</strong>

<strong>Background</strong>

<strong>Background Alpha</strong>

混合后的材质如下：

