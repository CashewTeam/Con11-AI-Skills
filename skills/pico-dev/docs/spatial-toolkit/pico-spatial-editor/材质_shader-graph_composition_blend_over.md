一种合并操作，使用前景的 Alpha 通道将前景叠加到背景之上。输出的 RGB 分量为：`F + B(1 − f)`，输出的 Alpha 分量为：`f + b(1 − f)`。

## **参数说明**

* **Foreground**：Color 4 类型的前景输入。其中，`F` 表示该参数的 RGB 分量，`f` 表示该参数的 Alpha 分量。
* **Background**：Color 4 类型的背景输入。其中，`B` 表示该参数的 RGB 分量，`b` 表示该参数的 Alpha 分量。
* **Mix**：混合操作的权重。`Mix` 值越高，混合效果越明显。默认值为 `1`。取值超出 `0` 到 `1` 范围时，会产生超出该节点预期功能之外的未定义效果。

## **节点使用说明**
**Over** 节点根据前景和背景输入的 Alpha 通道来确定输出结果。前景的 Alpha 值越低，背景就越多地混合到前景中。
下面的示例节点图展示了如何使用 **Over** 节点将两种纹理进行混合。

下方展示了两张原始图像、前景 Alpha 图像以及将最终混合纹理应用到立方体表面的结果（**Mix** = 0.5）。

<strong>Foreground</strong>

<strong>Foreground Alpha</strong>

<strong>Background</strong>

混合后的材质如下：

