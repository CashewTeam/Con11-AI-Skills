根据图像文件生成 2D 纹理。

## 参数说明

* **File**：用于指定该纹理所使用的图像文件。
* **U Wrap Mode**：指定当纹理坐标 U 超出 0 到 1 范围时的处理方式。默认值为 **clamp_to_edge**。
* **V Wrap Mode**：指定当纹理坐标 V 超出 0 到 1 范围时的处理方式。默认值为 **clamp_to_edge**。
* **Border Color**：指定用于填充未被图像内容覆盖区域的边界颜色。默认值为 **transparent_black**。
* **Mag Filter**：指定图像放大显示时使用的过滤模式。默认值为 **linear**。
* **Min Filter**：指定图像缩小显示时使用的过滤模式。默认值为 **linear**。
* **Mip Filter**：指定使用 mipmapping 时的过滤模式。若为 **None**，则不使用 mipmapping。默认值为 **linear**。
* **Max Anisotropy**：指定各向异性过滤级别，仅在启用 mipmapping 时生效。默认值为 **1**。
* **Max LOD Clamp**：指定允许使用的最大 LOD 值。默认值为 **65504**。
* **Min LOD Clamp**：指定允许使用的最小 LOD 值。默认值为 **0**。
* **Texture Coordinates**：指定用于读取纹理数据的二维纹理坐标。默认使用当前 UV 坐标。
* **No Flip V**：指定是否不对 V 方向进行翻转。
* **Bias**：指定 LOD 偏移量，用于影响两个 LOD 层级之间的采样倾向。默认值为 **0**。
* **Dynamic Min LOD Clamp**：指定可在运行时动态修改的最小 LOD 值。

## 节点使用说明
### Wrap Mode 参数的可选值

* **clamp_to_border**：边界钳制。节点会将超出正常范围的纹理坐标设置为 **Border Color** 参数指定的颜色。
* **clamp_to_edge**：边缘钳制。节点会将超出正常范围的纹理坐标钳制到正常范围内。也就是说，大于 1 的值会被设为 1，小于 0 的值会被设为 0。这意味着图像边缘处的颜色会向外延展，填充纹理剩余区域。
* **mirrored_clamp_to_edge**：镜像边缘钳制。节点会对超出正常范围的纹理坐标执行镜像边缘钳制。超出范围的部分不会被循环重复，而是按照边界方向进行镜像延展，并最终限制在边缘区域内，因此图像边缘会以更连续的镜像方式向外扩展。
* **mirrored_repeat**：节点会对超出正常范围的纹理坐标进行镜像重复。
* **repeat**：节点会让超出正常范围的纹理坐标“循环回绕”。这种行为等价于对坐标执行模 1 运算。

### Mag Filter 和 Min Filter 的可选值

* **linear**：过滤器使用邻近值的线性插值来确定最终渲染内容。
* **nearest**：过滤器使用最近邻值来确定最终渲染内容。

### Mip Filter 的可选值
**Mip Filter** 参数具有与 **Mag Filter** 和 **Min Filter** 相同的可选值，另外还增加了 **None** 选项，表示不使用 mipmapping。
### 节点使用示例
下面的节点图展示了如何把从图像文件创建 2D 材质。

下图显示了 2D 材质渲染到立方体的效果。

<strong>勾选 Flip V </strong>

<strong>不勾选 Flip V </strong>

