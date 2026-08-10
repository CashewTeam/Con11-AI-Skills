输出背景中与前景 Alpha 重叠的区域。
**Mask** 节点使用前景和背景输入的 Alpha 通道来决定输出结果。

* 输出的 RGB 分量为：`B⋅f`
* 输出的 Alpha 分量为：`b⋅f`

也就是说，背景会按照前景的 Alpha 进行遮罩，只有与前景 Alpha 重叠的部分会被输出。

## **参数说明**

* **Foreground**：Color 4 类型的前景输入，其中 `F` 表示该参数的 RGB 分量，`f` 表示该参数的 Alpha 分量。
* **Background**：Color 4 类型的背景输入，其中 `B` 表示该参数的 RGB 分量，`b` 表示该参数的 Alpha 分量。
* **Mix**：混合操作的权重。**Mix** 值越高，混合效果越明显。默认值为 `1`。取值超出 `0` 到 `1` 范围时，会产生超出该节点预期功能之外的未定义效果。

### **节点使用说明**
下面的示例节点图展示了如何使用 **Mask** 节点将两种纹理进行混合。

下方展示了两张原始图像、前景 Alpha 图像以及将最终混合纹理应用到立方体表面的结果（**Mix** = 0.5）。

<strong>Foreground</strong>

<strong>Foreground Alpha</strong>

<strong>Background</strong>

混合后的材质如下：

