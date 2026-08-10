一种合并操作，将预乘 Alpha 的前景分层叠加到背景之上。

**Matte** 节点使用前景和背景输入的 Alpha 通道来决定输出结果。

* 输出的 RGB 分量为：`Ff + B(1 − f)`
* 输出的 Alpha 分量为：`f + b(1 − f)`

也就是说，前景会按照其 Alpha 值叠加到背景之上，而背景仅在前景未覆盖的部分保留下来。
## **参数说明**

* **Foreground**：Color 4 类型的前景输入，其中 `F` 表示该参数的 RGB 分量，`f` 表示该参数的 Alpha 分量。
* **Background**：Color 4 类型的背景输入，其中 `B` 表示该参数的 RGB 分量，`b` 表示该参数的 Alpha 分量。
* **Mix**：混合操作的权重。**Mix** 值越高，混合效果越明显。默认值为 `1`。取值超出 `0` 到 `1` 范围时，会产生超出该节点预期功能之外的未定义效果。

### **节点使用说明**
下面的示例节点图展示了如何使用 **Matte** 节点将两种纹理进行混合。

下方展示了两张原始图像、前景 Alpha 图像以及将最终混合纹理应用到立方体表面的结果（**Mix** = 1）。

<strong>Foreground</strong>

<strong>Foreground Alpha</strong>

<strong>Background</strong>

混合后的材质如下：

