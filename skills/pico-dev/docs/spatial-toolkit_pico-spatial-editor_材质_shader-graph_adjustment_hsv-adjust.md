通过一个向量来调整输入 RGB 颜色的 HSV。
此节点不会改变 **Color 4** 类型的 Alpha 通道值。

## 参数说明

* **In**：输入颜色。
* **Amount**：HSV 调整量。默认为 `(0,1,1)`，表示不调整 HSV。**Amount** 向量的的三个 **Float** 值分别代表：
   * **色相 (Hue)**: 将 `Amount` 向量的第一个值与颜色的色相相加。正值会使色相沿着“红→绿→蓝”的方向旋转。值为 `1` 代表旋转一整圈，颜色不变。
   * **饱和度 (Saturation)**: 将颜色的饱和度乘以 `Amount` 向量的第二个值。
   * **明度 (Value)**: 将颜色的明度乘以 `Amount` 向量的第三个值。

## 节点使用说明
以下是一个 Shader Graph 示例，使用 **HSV Adjust** 节点（**Type** 为 **Color 3**）来把纹理的 HSV 调整为 (0.5, 1, 1)。

应用 Shader Graph 前后的对比效果如下：

应用 Shader Graph 前

应用 Shader Graph 后

