本教程将介绍如何使用 Shader Graph 创建一个发光球体材质，整个过程仅需一个球体和少量节点。最终，该材质将呈现出基础色与更明亮的边缘光相结合的效果。
另外，本教程还将额外介绍如何通过 Shader Graph 为发光球实现脉冲动画。
## 准备工作
在 PICO Spatial Editor 中创建一个球体用于关联 Shader Graph 材质。

1. 创建一个 Spatial Editor 项目。
2. 在 **Hierarchy** 窗口，选择 **+ > Primitive Shapes -> Sphere**，创建一个球体。

你可以在 Spatial Editor 中查看创建的球体。

## 步骤一：创建基础 Shader Graph
我们先创建一个最小可工作的 Shader Graph，让球体先显示一个基础颜色。

1. 打开你的 Spatial Editor 项目。
2. 选中你创建的球体，然后选择 Spatial Editor 下方的 **Shader Graph** 标签页，点击 **Create Material** 在球体下创建一个 Shader Graph 材质。Shader Graph 默认包含一个 **Preview Surface** 节点和一个 **output** 节点。

3. 重命名你创建的 Shader Graph 材质，例如 `GlowMaterial`。

4. 在 Shader Graph 标签页，点击左侧 **Input Node** 面板的 **+** 按钮添加一个类型为 **Color 3** 的输入节点，将其重命名为 **BaseColor**，并在右侧的 **Shader Graph Inspector** 窗口中设置这个输入节点的值。蓝色、青色或紫色都很适合发光球。因此你可以把 **Color 3** 节点的 RGB(0-1) 值设置为：
   * R: 0.2
   * G: 0.6
   * B: 1.0

5. 将 **BaseColor** 输入节点连接到 **Preview Surface** 节点的 **Diffuse Color** 输入，然后保存 Shader Graph。

6. 在 **Hierarchy** 窗口选中球体，然后在右侧的 **Inspector** 窗口找到 **Material Bindings** 组件，把 **Binding** 设置为你创建的 Shader Graph 材质，从而将材质应用到场景中的球体。

此时，你应该看到一个**纯色球体**。

## 步骤二：添加边缘光
我们使用一个边缘效果节点来生成“靠近轮廓更亮”的区域。

1. 在 Shader Graph 标签页，点击左侧 **Input Node** 面板的 **+** 按钮添加以下输入节点，重命名这些输入节点，并在右侧的 **Shader Graph Inspector** 窗口中设置这些输入节点的值。
   | **节点** | **名称** | **值** | **作用** |
   | --- | --- | --- | --- |
   | Color3 | GlowColor | 建议偏亮的青蓝色或白蓝色。本教程中将其 RGB(0-1) 值设置为： ;; * R: 0.63 ;     * G: 0.77 ;     * B: 0.92 | 控制边缘发光颜色。 |
   | Float | GlowIntensity | 2.0 | 控制发光强度。 |
   | Float | EdgePower | 3.0 | 控制边缘光的宽度和锐度。 |

1. 添加一个 **Fresnel Effect** 节点。把 **EdgePower** 输入节点连接到 **Fresnel Effect** 节点的 **Power** 输入。
   **Fresnel Effect** 节点本质上是一个角度计算节点。它会根据表面法线（**Normal**）、观察方向（**View Dir**）及强度（**Power**）输出一个 0 到 1 左右变化的值，这个值通常正面较低，边缘较高。
   **Power** 的值会影响边缘光的分布：

   * 数值越低，边缘范围越宽。
   * 数值越高，边缘越细、越集中。

2. 添加一个 **Multiply** 节点。这样可以把边缘效果染成你想要的颜色。
   * 输入 **In 1**：**GlowColor** 输入节点的输出
   * 输入 **In 2**：**Fresnel Effect** 节点输出

3. 再添加一个 **Multiply** 节点。这样可以单独控制发光亮度，而不影响基础颜色。
   * 输入 **In 1**：上一个 **Multiply** 节点的结果
   * 输入 **In 2**：**GlowIntensity** 输入节点的输出

## 步骤三：合并基础颜色和边缘光
因为在步骤一中，你已经把 **BaseColor** 输入节点的输出连接到了 **Preview Surface** 节点的 **Diffuse Color** 输入，你只需要把步骤二的最终输出连接到  **Preview Surface** 节点的 **Emissive Color** 输入即可合并基础颜色和边缘光。
**Diffuse Color** 决定物体在受光时显示什么颜色，而 **Emissive Color** 决定物体自己发出什么颜色的光。因此，基础颜色会连接到 **Diffuse Color**；边缘光会连接到 **Emissive Color**。

此时你应该看到：

* 球体有一个基础颜色
* 球体边缘更亮
* 看起来像一个简单的能量球或发光球

接下来，你还可以在 **GlowMaterial** 的 **Inspector** 窗口中微调以下输出参数，体验不同的效果。

* **BaseColor** 输入节点：控制球体主体颜色。
* **GlowColor** 输入节点：控制边缘光颜色。
* **GlowIntensity** 输入节点：控制整体发光强度。
* **EdgePower** 输入节点：控制边缘范围。

## 步骤四：增加脉冲动画
如果你想让发光球更有动感，可以加一个简单的脉冲动画。

1. 先添加两个输入节点，用来控制脉冲效果。已有的 **GlowIntensity** 输入节点将作为基础亮度值使用。
   | **节点** | **名称** | **值** | **作用** |
   | --- | --- | --- | --- |
   | Float | PulseSpeed | 2 | 控制脉冲速度 |
   | Float | PulseAmplitude | 0.8 | 控制亮度变化幅度 |

2. 添加一个 **Time** 节点。这个节点会持续输出随时间增长的值。先不要把它直接接到发光强度上，否则发光强度只会越来越大，而不会往回摆动。
3. 添加一个 **Multiply** 节点，用来控制脉冲速度。
   * 输入 **In 1**：**Time** 节点的输出
   * 输入 **In 2**：**PulseSpeed** 输入节点的输出

4. 添加一个 **Sin** 节点。把上一步 **Multiply** 节点的输出连接到 Sin 节点的输入。现在你得到一个会在 `-1` 到 `1` 之间反复变化的值：sin(**Time** × **PulseSpeed**)。这就是脉冲的波形。

5. 再添加一个 **Multiply** 节点，用来控制波动幅度。这一步会把波形缩放到你想要的范围：sin(**Time** × **PulseSpeed**) × **PulseAmplitude**。
   * 输入 **In 1**：**Sin** 节点的输出
   * 输入 **In 2**：**PulseAmplitude** 输入节点的输出

6. 添加一个 **Add** 节点。把上下波动的值调整到一个正常的亮度基线附近。最终结果：sin(**Time** × **PulseSpeed**) × **PulseAmplitude** + **GlowIntensity**。
   * 输入 **In 1**：上一步 **Multiply** 节点的输出
   * 输入 **In 2**：**GlowIntensity** 输入节点的输出。

7. 把 **Add** 节点的输出代替原先的 **GlowIntensity** 节点的输出，连接到 **Multiply** 节点的 **In 2** 输入。

此时，你可以看到发光球效果：

* 球体边缘持续发光
* 发光强度缓慢增强再减弱

接下来，你还可以在 **GlowMaterial** 的 **Inspector** 窗口中微调以下输出参数，体验不同的效果。

* **GlowIntensity**：基础亮度
* **PulseAmplitude**：波动幅度
* **PulseSpeed**：变化速度

## 接下来你可以
现在你已经创建了一个简单的 Shader Graph。接下来，你可以了解 Shader Graph 中每个节点的用法。详情参阅 [Shader Graph 节点概览](./spatial-toolkit_pico-spatial-editor_材质_shader-graph_shader-graph-节点概览.md)。

