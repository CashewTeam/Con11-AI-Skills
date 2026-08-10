本文介绍 Shader Graph 中的节点。
## 什么是 Shader Graph 节点
在 Shader Graph 的节点图中，每个节点都定义了一项具体的功能，可以是输入、处理或输出。节点通过输入或输出端口与其他节点交换信息。你可以通过边连接不同节点的端口。只有数据类型相同的端口才能通过边连接。
Shader Graph 中的节点可分为以下几类：
| **名称** | **作用** | **示例** |
| --- | --- | --- |
| **输入节点** | 用于提供不同类型的输入数据，例如 Float、Boolean、Color、Vector、Matrix 和 Filename 等。 |; |
| **处理节点** | 用于处理输入数据，例如执行数学运算、逻辑判断、通道处理、颜色调整、混合与转换、定义材质属性等。 |; ;   |
| **输出节点** | 用于接收节点网络的最终结果，并根据结果类型输出到 Surface 或 Geometry Modifier 通道。 ;; * Surface 用于材质表面属性修改。 ;  * Geometry Modifier 用于几何形态修改。 |; |
## 节点列表
### Adjustment
对输入的数据（通常是颜色或数值）进行后期处理风格的艺术化调整或校正。
| **节点** | **描述** |
| --- | --- |
| [Contrast](./spatial-toolkit_pico-spatial-editor_材质_shader-graph_adjustment_contrast.md) | 通过线性斜率乘数来调整输入值（浮点或颜色）的对比度。 |
| [HSV Adjust](./spatial-toolkit_pico-spatial-editor_材质_shader-graph_adjustment_hsv-adjust.md) | 通过一个向量来调整输入 RGB 颜色的 HSV。 |
| [HSV To RGB](./spatial-toolkit_pico-spatial-editor_材质_shader-graph_adjustment_hsv-to-rgb.md) | 将颜色从 HSV 颜色空间转换回 RGB 颜色空间。 |
| [RGB To HSV](./spatial-toolkit_pico-spatial-editor_材质_shader-graph_adjustment_rgb-to-hsv.md) | 将颜色从 RGB 颜色空间转换到 HSV 颜色空间。 |
| [Luminance](./spatial-toolkit_pico-spatial-editor_材质_shader-graph_adjustment_luminance.md) | 接收一个 RGB 颜色作为输入，并输出一个在所有颜色通道中均包含该颜色亮度信息的灰度值。 |
| [Range](./spatial-toolkit_pico-spatial-editor_材质_shader-graph_adjustment_range.md) | 将一个范围内的输入值重新映射到另一个范围。还提供了 Gamma 校正和限制输出的选项。 |
| [Remap](./spatial-toolkit_pico-spatial-editor_材质_shader-graph_adjustment_remap.md) | 通过线性方式将输入值从一个范围映射到另一个范围。 |
| [Saturate](./spatial-toolkit_pico-spatial-editor_材质_shader-graph_adjustment_saturate.md) | 调节颜色的饱和度。 |
| [Smooth Step](./spatial-toolkit_pico-spatial-editor_材质_shader-graph_adjustment_smooth-step.md) | 使用 Hermite 插值法，将一个在从低到高范围内的输入值平滑地重新映射到 0 到 1 的输出范围。 |
### Channel
用于访问、重排、组合和分离向量的各个分量（通道）。
| **节点** | **描述** |
| --- | --- |
| [Convert](/spatial-editor-shader-graph-Convert) | 将输入的数据流从一种数据类型转换为另一种数据类型。 |
| [Combine 2](./spatial-toolkit_pico-spatial-editor_材质_shader-graph_channel_combine-2.md) | 将两个数据流的通道组合成一个兼容类型的双通道输出流。 |
| [Extract](./spatial-toolkit_pico-spatial-editor_材质_shader-graph_channel_extract.md) | 从 Color N 或 Vector N 流中提取指定通道号。 |
| [Combine 3](./spatial-toolkit_pico-spatial-editor_材质_shader-graph_channel_combine-3.md) | 将三个流中的通道组合成单个兼容输出流的三个通道。 |
| [Combine 4](./spatial-toolkit_pico-spatial-editor_材质_shader-graph_channel_combine-4.md) | 将四个流中的通道组合成单个兼容输出流的四个通道。 |
| [Swizzle](./spatial-toolkit_pico-spatial-editor_材质_shader-graph_channel_swizzle.md) | 对输入流的通道执行任意排列，并返回一个指定类型的新数据流。 |
| [Separate 2](./spatial-toolkit_pico-spatial-editor_材质_shader-graph_channel_separate-2.md) | 将 Vector 2 的每个通道分别输出为一个单独的 Float 输出。 |
| [Separate 3](./spatial-toolkit_pico-spatial-editor_材质_shader-graph_channel_separate-3.md) | 将 Color 3、Vector 3 或 Matrix 3 的每个通道分别输出为一个单独的 Float 或 Float 3 输出。 |
| [Separate 4](./spatial-toolkit_pico-spatial-editor_材质_shader-graph_channel_separate-4.md) | 将 Color 4、Vector 4 或 Matrix 4 的每个通道分别输出为一个单独的 Float 或 Float 4 输出。 |
### Composition
将多个数据值组合为单一输出。你可以使用 **Composition** 节点来组合纹理，从而实现特定的外观效果。例如，可以只在前景纹理透明的区域显示背景纹理。
#### Blend
按不同混合模式对前景和背景输入进行颜色混合或合成。
| **节点** | **描述** |
| --- | --- |
| [Burn](./spatial-toolkit_pico-spatial-editor_材质_shader-graph_composition_blend_burn.md) | 一种混合操作，使用背景来使前景层变暗。 |
| [Difference](./spatial-toolkit_pico-spatial-editor_材质_shader-graph_composition_blend_difference.md) | 输出前景和背景值之间的距离。 |
| [Dodge](./spatial-toolkit_pico-spatial-editor_材质_shader-graph_composition_blend_dodge.md) | 一种混合操作，可根据前景使背景层变亮。 |
| [Mix](./spatial-toolkit_pico-spatial-editor_材质_shader-graph_composition_blend_mix.md) | 混合前景和背景输入，根据混合值加权。 |
| [Over](./spatial-toolkit_pico-spatial-editor_材质_shader-graph_composition_blend_over.md) | 一种合并操作，使用前景的 Alpha 通道将前景叠加到背景之上。 |
| [Overlay](./spatial-toolkit_pico-spatial-editor_材质_shader-graph_composition_blend_overlay.md) | 一种混合操作，对暗部执行乘法混合，对亮部执行滤色混合。 |
| [Additive Mix](./spatial-toolkit_pico-spatial-editor_材质_shader-graph_composition_blend_additive-mix.md) | 一种将前景值与背景值相加的混合操作。 |
| [Screen](./spatial-toolkit_pico-spatial-editor_材质_shader-graph_composition_blend_screen.md) | 一种混合操作，会提亮比白色更暗的区域。 |
#### Mask
根据遮罩或 Alpha 重叠关系提取、保留或排除输入的特定区域。
| **节点** | **描述** |
| --- | --- |
| [Mask](./spatial-toolkit_pico-spatial-editor_材质_shader-graph_composition_mask_mask.md) | 输出背景中与前景 Alpha 重叠的区域。 |
| [Matte](./spatial-toolkit_pico-spatial-editor_材质_shader-graph_composition_mask_matte.md) | 一种合并操作，可将预乘前景层叠在背景之上。 |
| [In](./spatial-toolkit_pico-spatial-editor_材质_shader-graph_composition_mask_in.md) | 输出前景中与背景 Alpha 重叠的区域。 |
| [Out](./spatial-toolkit_pico-spatial-editor_材质_shader-graph_composition_mask_out.md) | 输出前景中不与背景重叠的区域。 |
| [Inside](./spatial-toolkit_pico-spatial-editor_材质_shader-graph_composition_mask_inside.md) | 将一个遮罩乘到输入的所有通道上。 |
| [Outside](./spatial-toolkit_pico-spatial-editor_材质_shader-graph_composition_mask_outside.md) | 将遮罩的补值（1 - 遮罩）乘到输入的所有通道上。 |
#### Mode
按特定合成模式对前景和背景输入执行组合运算。
| **节点** | **描述** |
| --- | --- |
| [Disjoint Over](./spatial-toolkit_pico-spatial-editor_材质_shader-graph_composition_mode_disjoint-over.md) | 一种合并操作，可将前景层叠加在背景颜色之上，但假定两者同时覆盖的半透明区域没有重叠。 |
| [Subtractive Mix](./spatial-toolkit_pico-spatial-editor_材质_shader-graph_composition_mode_subtractive-mix.md) | 将前景值从背景值中相减。 |
#### Premult
Premult 节点用于对输入颜色执行预乘或反预乘处理，即将 RGB 通道与 Alpha 通道相乘或相除。
| **节点** | **描述** |
| --- | --- |
| [Premult](./spatial-toolkit_pico-spatial-editor_材质_shader-graph_composition_premult_premult.md) | 将输入的 RGB 通道与输入的 Alpha 通道相乘。 |
| [Unpremult](./spatial-toolkit_pico-spatial-editor_材质_shader-graph_composition_premult_unpremult.md) | 使用输入的 RGB 通道除以输入的 Alpha 通道。 |
### Input
用于提供不同类型的输入数据。
#### Constant
提供一个常量值作为输入，该常量可以是数值、向量或颜色等。
| **节点** | **描述** |
| --- | --- |
| [Float](./spatial-toolkit_pico-spatial-editor_材质_shader-graph_input_constant_float.md) | 常量浮点数值。 |
| [Integer](./spatial-toolkit_pico-spatial-editor_材质_shader-graph_input_constant_integer.md) | 常量整数值。 |
| [Boolean](./spatial-toolkit_pico-spatial-editor_材质_shader-graph_input_constant_boolean.md) | 常量布尔值。 |
| [Vector2](./spatial-toolkit_pico-spatial-editor_材质_shader-graph_input_constant_vector2.md) | 包含两个浮点分量 (x, y) 的常量 Vector 2。 |
| [Vector3](./spatial-toolkit_pico-spatial-editor_材质_shader-graph_input_constant_vector3.md) | 包含三个浮点分量 (x, y, z) 的常量 Vector 3。 |
| [Vector4](./spatial-toolkit_pico-spatial-editor_材质_shader-graph_input_constant_vector4.md) | 包含四个浮点分量 (x, y, z, w) 的常量 Vector 4。 |
| [Color3](./spatial-toolkit_pico-spatial-editor_材质_shader-graph_input_constant_color3.md) | 包含三个浮点分量 (r, g, b) 的常量 Color3 向量。 |
| [Color4](./spatial-toolkit_pico-spatial-editor_材质_shader-graph_input_constant_color4.md) | 包含四个浮点分量（r, g, b, a）的常量 Color4 向量。 |
| [Matrix3x3](./spatial-toolkit_pico-spatial-editor_材质_shader-graph_input_constant_matrix3x3.md) | 一个常量 Matrix3x3 (浮点) 值（行主序）。 |
| [Matrix4x4](./spatial-toolkit_pico-spatial-editor_材质_shader-graph_input_constant_matrix4x4.md) | 一个常量 Matrix4x4 (浮点) 值（行主序）。 |
#### Texture
提供纹理数据作为输入。
| **节点** | **描述** |
| --- | --- |
| [Image File](./spatial-toolkit_pico-spatial-editor_材质_shader-graph_input_texture_image-file.md) | 指向一个本地图像文件的常量路径。 |
| [UV Texture](./spatial-toolkit_pico-spatial-editor_材质_shader-graph_input_texture_uv-texture.md) | MaterialX 版本的 USD UV 纹理读取器。 |
| [Tiled Image](./spatial-toolkit_pico-spatial-editor_材质_shader-graph_input_texture_tiled-image.md) | 用于从图像中采样数据，并提供在 UV 空间中进行偏移与平铺的功能。 |
| [Image](./spatial-toolkit_pico-spatial-editor_材质_shader-graph_input_texture_image.md) | 从单个图像或多层图像中的某一层采样数据。 |
| [Mipmap Bias Image](./spatial-toolkit_pico-spatial-editor_材质_shader-graph_input_texture_mipmap-bias-image.md) | 包含多级渐远纹理偏差参数的图像节点。 |
| [Bound Video Texture](./spatial-toolkit_pico-spatial-editor_材质_shader-graph_input_texture_bound-video-texture.md) | 读取当前模型已绑定的视频纹理，并根据输入的纹理坐标对其进行采样。 |
| [Video Texture LOD](./spatial-toolkit_pico-spatial-editor_材质_shader-graph_input_texture_video-texture-lod.md) | 用于从视频文件中采样像素。 |
| [Texture Size](./spatial-toolkit_pico-spatial-editor_材质_shader-graph_input_texture_texture-size.md) | 获取纹理大小和纹素大小。 |
| [Cube Image](./spatial-toolkit_pico-spatial-editor_材质_shader-graph_input_texture_cube-image.md) | 生成立方体纹理。 |
| [Cube Image LOD](./spatial-toolkit_pico-spatial-editor_材质_shader-graph_input_texture_cube-image-lod.md) | 生成并配置立方体纹理。相比 **Cube Image** 节点增加了 LOD 参数。 |
| [Cube Image Gradient](/spatial-editor-shader-graph-CubeImageGradiant) | 生成并配置立方体纹理。相比 **Cube Image** 节点增加了 Gradient 相关设置。 |
| [Image 2D](/spatial-editor-shader-graph-noth0ily) | 根据图像文件生成 2D 纹理。 |
| [Image 2D LOD](/spatial-editor-shader-graph-s2kla19w) | 从图像文件创建 2D 纹理，并支持显式指定采样所使用的 LOD 层级。 |
#### Data
提供与当前着色点或绑定几何体相关的数据输入，例如位置、法线、切线、颜色、纹理坐标以及其他几何属性。
| **节点** | **描述** |
| --- | --- |
| [Surface Screen Position](./spatial-toolkit_pico-spatial-editor_材质_shader-graph_input_data_surface-screen-position.md) | 当前所处理的数据的屏幕空间坐标。 |
| [Bitangent](./spatial-toolkit_pico-spatial-editor_材质_shader-graph_input_data_bitangent.md) | 当前所处理的数据在指定坐标空间中的几何副切线向量。 |
| [Geom Color](./spatial-toolkit_pico-spatial-editor_材质_shader-graph_input_data_geom-color.md) | 当前处理的几何位置处与几何体关联的颜色，通常由顶点颜色定义。 |
| [Geom Propvalue](/spatial-editor-shader-graph-t9eu5jwh) | 当前绑定几何体的指定可变几何属性（使用 MaterialX 定义）的值。 |
| [Primvar Reader](./spatial-toolkit_pico-spatial-editor_材质_shader-graph_input_data_primvar-reader.md) | 使着色网络能够使用几何体上定义的数据。 |
| [Normal](./spatial-toolkit_pico-spatial-editor_材质_shader-graph_input_data_normal.md) | 与当前处理数据相关联的几何法线，定义于特定坐标空间中。 |
| [Position](./spatial-toolkit_pico-spatial-editor_材质_shader-graph_input_data_position.md) | 与当前处理数据相关联的坐标，定义于特定坐标空间中。 |
| [Tangent](./spatial-toolkit_pico-spatial-editor_材质_shader-graph_input_data_tangent.md) | 当前所处理的数据在指定坐标空间中的几何切线向量。 |
| [Texture Coordinates](./spatial-toolkit_pico-spatial-editor_材质_shader-graph_input_data_texture-coordinates.md) | 当前所处理的数据的二维或三维纹理坐标。 |
| [Two Sided Sign](./spatial-toolkit_pico-spatial-editor_材质_shader-graph_input_data_two-sided-sign.md) | 根据当前片元位于表面几何体的正面还是背面返回符号值（+1 或 -1）。 |
#### Global
用于访问由系统提供的全局着色输入，例如相机、视图、变换矩阵等渲染上下文信息。
| **节点** | **描述** |
| --- | --- |
| [Camera Index Switch](./spatial-toolkit_pico-spatial-editor_材质_shader-graph_input_global_camera-index-switch.md) | 在立体渲染中为每只眼睛渲染不同的结果。 |
| [Camera Position](./spatial-toolkit_pico-spatial-editor_材质_shader-graph_input_global_camera-position.md) | 场景中相机的位置。 |
| [Surface Model To View](./spatial-toolkit_pico-spatial-editor_材质_shader-graph_input_global_surface-model-to-view.md) | 将模型空间转换到视图空间的 Matrix4x4（Float）矩阵，用于表面着色。 |
| [Surface Model To World](./spatial-toolkit_pico-spatial-editor_材质_shader-graph_input_global_surface-model-to-world.md) | 将模型空间转换到世界空间的 Matrix4x4（Float）矩阵，用于表面着色。 |
| [Surface Projection To View](./spatial-toolkit_pico-spatial-editor_材质_shader-graph_input_global_surface-projection-to-view.md) | 将投影空间转换到视图空间的 Matrix4x4（Float）矩阵，用于表面着色。 |
| [Surface View Direction](./spatial-toolkit_pico-spatial-editor_材质_shader-graph_input_global_surface-view-direction.md) | 返回从当前表面着色点指向视图参考点的方向向量。 |
| [View Direction](./spatial-toolkit_pico-spatial-editor_材质_shader-graph_input_global_view-direction.md) | 返回从指定位置指向视图参考点的方向向量，并以所选坐标空间输出。 |
| [Surface View To Projection](./spatial-toolkit_pico-spatial-editor_材质_shader-graph_input_global_surface-view-to-projection.md) | 将视图空间转换到投影空间的 Matrix4x4（Float）矩阵，用于表面着色。 |
| [Surface World To View](./spatial-toolkit_pico-spatial-editor_材质_shader-graph_input_global_surface-world-to-view.md) | 将世界空间到视图空间的 Matrix4x4（Float）矩阵，用于表面着色。 |
| [Vertex Model To View](./spatial-toolkit_pico-spatial-editor_材质_shader-graph_input_global_vertex-model-to-view.md) | 将模型空间转换到视图空间的 Matrix4x4（Float）矩阵，用于顶点着色。 |
| [Vertex Model To World](./spatial-toolkit_pico-spatial-editor_材质_shader-graph_input_global_vertex-model-to-world.md) | 将模型空间转换到世界空间的 Matrix4x4（Float）矩阵，用于顶点着色。 |
| [Vertex World To Model](./spatial-toolkit_pico-spatial-editor_材质_shader-graph_input_global_vertex-world-to-model.md) | 将世界空间转换到模型空间的 Matrix4x4（Float）矩阵，用于顶点着色。 |
| [Vertex Projection To View](./spatial-toolkit_pico-spatial-editor_材质_shader-graph_input_global_vertex-projection-to-view.md) | 将投影空间转换到视图空间的 Matrix4x4（Float）矩阵，用于顶点着色。 |
| [Vertex View To Projection](./spatial-toolkit_pico-spatial-editor_材质_shader-graph_input_global_vertex-view-to-projection.md) | 将视图空间转换到投影空间的 Matrix4x4（Float）矩阵，用于顶点着色。 |
| [Vertex Normal To World](/spatial-editor-shader-graph-uxc15rla) | 将顶点法线从模型空间变换到世界空间的 Matrix3x3（Float）矩阵。 ;   |
| [Time](./spatial-toolkit_pico-spatial-editor_材质_shader-graph_input_global_time.md) | 输出本地环境的当前时间（秒）。 |
| [Up Direction](./spatial-toolkit_pico-spatial-editor_材质_shader-graph_input_global_up-direction.md) | 向上向量的方向。 |
| [Scene Texel Size](./spatial-toolkit_pico-spatial-editor_材质_shader-graph_input_global_scene-texel-size.md) | 提供当前场景纹理的尺寸信息，以及单个纹素对应的归一化大小。 |
| [Camera Direction](./spatial-toolkit_pico-spatial-editor_材质_shader-graph_input_global_camera-direction.md) | 返回相机当前朝向的 float 3 方向向量。 |
| [Camera Up Direction](./spatial-toolkit_pico-spatial-editor_材质_shader-graph_input_global_camera-up-direction.md) | 返回相机当前上方向的 float 3 方向向量。 |
| [Object Radius](/spatial-editor-shader-graph-ObjectRadius) | 返回对象在指定空间中的包围半径。 |
| [Object Bounds](/spatial-editor-shader-graph-fxncdhsm) | 返回对象在指定空间中的包围盒信息，包括尺寸、最小坐标和最大坐标。 |
| [Object Position](/spatial-editor-shader-graph-z0xkfxod) | 返回对象原点在指定空间中的 float3 位置向量。 |
| [Object Up Direction](/spatial-editor-shader-graph-8muhu5bc) | 返回对象上方向在指定空间中的 float3 方向向量。 |
| [Object Forward Direction](./spatial-toolkit_pico-spatial-editor_材质_shader-graph_input_global_object-forward-direction.md) | 返回对象前方向在指定空间中的 float3 方向向量。 |
### Logic
进行条件判断和布尔运算，控制着色器的执行流程。
| **节点** | **描述** |
| --- | --- |
| [If Equal](./spatial-toolkit_pico-spatial-editor_材质_shader-graph_logic_if-equal.md) | 根据 **Value1** 是否等于 **Value2** 输出不同结果：若两者相等，则输出 **True Result**；否则输出 **False Result**。 |
| [If Greater](/spatial-editor-shader-graph-If_Greater) | 根据 **Value1** 是否大于 **Value2** 输出不同结果：若 **Value1** > **Value2**，则输出 **True Result**；否则输出 **False Result**。 |
| [If Greater Or Equal](./spatial-toolkit_pico-spatial-editor_材质_shader-graph_logic_if-greater-or-equal.md) | 根据 **Value1** 是否大于或等于 **Value2** 输出不同结果：若 **Value1** >= **Value2**，则输出 **True Result**；否则输出 **False Result**。 |
| [Switch](./spatial-toolkit_pico-spatial-editor_材质_shader-graph_logic_switch.md) | 根据选择器输入开关的值，从 10 个输入流中选择并输出一个值。 |
| [And](./spatial-toolkit_pico-spatial-editor_材质_shader-graph_logic_and.md) | **In 1** 和 **In 2** 两个布尔值的逻辑与（And）运算。 |
| [Or](./spatial-toolkit_pico-spatial-editor_材质_shader-graph_logic_or.md) | **In 1** 和 **In 2** 两个布尔值的逻辑或（OR）运算。 |
| [Xor](./spatial-toolkit_pico-spatial-editor_材质_shader-graph_logic_xor.md) | **In 1** 和 **In 2** 两个布尔值的逻辑异或（XOR）运算。 |
| [Not](./spatial-toolkit_pico-spatial-editor_材质_shader-graph_logic_not.md) | 返回输入的逻辑非（!）运算结果。 |
### Math
对数值执行数学运算和变换操作。
#### Basic
提供了基础的数学运算功能，如加、减、乘、除等。
| **节点** | **描述** |
| --- | --- |
| [Add](./spatial-toolkit_pico-spatial-editor_材质_shader-graph_math_basic_add.md) | 将两个值相加。 |
| [Divide](./spatial-toolkit_pico-spatial-editor_材质_shader-graph_math_basic_divide.md) | 将两个值相除。两个矩阵相除是 in1 与 in2 的逆矩阵的乘积。 |
| [Multiply](./spatial-toolkit_pico-spatial-editor_材质_shader-graph_math_basic_multiply.md) | 将两个值相乘。 |
| [Power](./spatial-toolkit_pico-spatial-editor_材质_shader-graph_math_basic_power.md) | 计算一个值的指定次幂。 |
| [Safe Power](./spatial-toolkit_pico-spatial-editor_材质_shader-graph_math_basic_safe-power.md) | 计算一个值的指定次幂，并将底数的符号赋给输出。 |
| [Sqrt](./spatial-toolkit_pico-spatial-editor_材质_shader-graph_math_basic_sqrt.md) | 计算一个值的平方根。 |
| [Subtract](./spatial-toolkit_pico-spatial-editor_材质_shader-graph_math_basic_subtract.md) | 将两个值相减。 |
#### Advanced
提供了更复杂的数学运算和变换功能，例如指数函数、对数函数、偏导数等。
| **节点** | **描述** |
| --- | --- |
| [Absval](./spatial-toolkit_pico-spatial-editor_材质_shader-graph_math_advanced_absval.md) | 输出每个输入通道的绝对值。 |
| [Exponential 2](./spatial-toolkit_pico-spatial-editor_材质_shader-graph_math_advanced_exponential-2.md) | 2 的 X 次幂。 |
| [Exponential 10](/spatial-editor-shader-graph-Exponential_10) | 10 的 X 次幂。 |
| [Exp](./spatial-toolkit_pico-spatial-editor_材质_shader-graph_math_advanced_exp.md) | 输出以输入值为指数的 e 的幂。 |
| [Modulo](./spatial-toolkit_pico-spatial-editor_材质_shader-graph_math_advanced_modulo.md) | 将 **In 1** 除以 **In 2** 再减去整数部分后，输出剩余的小数部分。 |
| [Log](./spatial-toolkit_pico-spatial-editor_材质_shader-graph_math_advanced_log.md) | 自然对数。 |
| [Log 2](./spatial-toolkit_pico-spatial-editor_材质_shader-graph_math_advanced_log-2.md) | 以 2 为底的对数。 |
| [Log 10](./spatial-toolkit_pico-spatial-editor_材质_shader-graph_math_advanced_log-10.md) | 以 10 为底的对数。 |
| [Normal Map Decode](./spatial-toolkit_pico-spatial-editor_材质_shader-graph_math_advanced_normal-map-decode.md) | 应用公式 `2x - 1`，可将法线值的范围从 `[0, 1]` 重映射到 `[-1, 1]`。 |
| [Distance](./spatial-toolkit_pico-spatial-editor_材质_shader-graph_math_advanced_distance.md) | 返回 X 和 Y 之间的距离。 |
| [Distance Square](./spatial-toolkit_pico-spatial-editor_材质_shader-graph_math_advanced_distance-square.md) | 返回 X 和 Y 之间距离的平方。 |
| [DDX](./spatial-toolkit_pico-spatial-editor_材质_shader-graph_math_advanced_ddx.md) | 返回输入值在屏幕空间 X 方向上的偏导数。 |
| [DDY](./spatial-toolkit_pico-spatial-editor_材质_shader-graph_math_advanced_ddy.md) | 返回输入值在屏幕空间 Y 方向上的偏导数。 |
#### Range
设置数值的范围。
| **节点** | **描述** |
| --- | --- |
| [Fractional](./spatial-toolkit_pico-spatial-editor_材质_shader-graph_math_range_fractional.md) | 返回浮点数的小数部分。 |
| [Clamp](./spatial-toolkit_pico-spatial-editor_材质_shader-graph_math_range_clamp.md) | 按通道将输入限制在 **Low** 和 **High** 范围内。 |
| [Max](/8yadp090/rc2gkbqd) | 输出 **In 1** 和 **In 2** 中的最大值。 |
| [Min](./spatial-toolkit_pico-spatial-editor_材质_shader-graph_math_range_min.md) | 输出 **In 1** 和 **In 2** 中的最小值。 |
| [One Minus](./spatial-toolkit_pico-spatial-editor_材质_shader-graph_math_range_one-minus.md) | 从 1 减去输入值。 |
#### Round
对数值进行四舍五入、向上取整或向下取整等操作。
| **节点** | **描述** |
| --- | --- |
| [Floor](./spatial-toolkit_pico-spatial-editor_材质_shader-graph_math_round_floor.md) | 按通道输出小于或等于传入值的最近整数值。 |
| [Ceil](./spatial-toolkit_pico-spatial-editor_材质_shader-graph_math_round_ceil.md) | 按通道输出大于或等于传入值的最近整数值。 |
| [Step](./spatial-toolkit_pico-spatial-editor_材质_shader-graph_math_round_step.md) | 如果 **In** < **Edge**，返回 0.0，否则返回 1.0。 |
| [Round](./spatial-toolkit_pico-spatial-editor_材质_shader-graph_math_round_round.md) | 按通道四舍五入到最近的整数值。 |
| [Sign](./spatial-toolkit_pico-spatial-editor_材质_shader-graph_math_round_sign.md) | 输入值每个通道的符号：负数为 -1，正数为 +1，零为 0。 |
#### Geometry
处理几何和空间相关的数据运算，例如向量运算、法线处理、方向变换以及纹理坐标变换。
| **节点** | **描述** |
| --- | --- |
| [Cross Product](./spatial-toolkit_pico-spatial-editor_材质_shader-graph_math_geometry_cross-product.md) | 计算两个输入向量的叉积。 |
| [Dot Product](./spatial-toolkit_pico-spatial-editor_材质_shader-graph_math_geometry_dot-product.md) | 输出两个向量的点积。 |
| [Magnitude](./spatial-toolkit_pico-spatial-editor_材质_shader-graph_math_geometry_magnitude.md) | 输出向量的浮点数幅值。 |
| [Reflect](./spatial-toolkit_pico-spatial-editor_材质_shader-graph_math_geometry_reflect.md) | 计算一个向量关于另一个向量的反射结果。 |
| [Refract](./spatial-toolkit_pico-spatial-editor_材质_shader-graph_math_geometry_refract.md) | 根据给定的表面法线和折射率（eta），计算输入向量的折射结果。 |
| [Normalize](./spatial-toolkit_pico-spatial-editor_材质_shader-graph_math_geometry_normalize.md) | 输出归一化后的向量。 |
| [Normal Map](./spatial-toolkit_pico-spatial-editor_材质_shader-graph_math_geometry_normal-map.md) | 将法线向量从对象空间或切线空间转换为世界空间。 |
| [Rotate 2D](./spatial-toolkit_pico-spatial-editor_材质_shader-graph_math_geometry_rotate-2d.md) | 将一个 2D 向量在二维空间中绕原点旋转。 |
| [Rotate 3D](./spatial-toolkit_pico-spatial-editor_材质_shader-graph_math_geometry_rotate-3d.md) | 围绕指定的单位轴向量旋转 3D 向量。 |
| [Place 2D](./spatial-toolkit_pico-spatial-editor_材质_shader-graph_math_geometry_place-2d.md) | 对用于 2D 纹理放置的 UV 纹理坐标进行变换。 |
#### Matrix
进行矩阵运算，如矩阵的乘法、转置、求逆等操作。
| **节点** | **描述** |
| --- | --- |
| [Inverse Matrix](./spatial-toolkit_pico-spatial-editor_材质_shader-graph_math_matrix_inverse-matrix.md) | 输出矩阵的逆矩阵。 |
| [Determinant](./spatial-toolkit_pico-spatial-editor_材质_shader-graph_math_matrix_determinant.md) | 输出矩阵的浮点行列式。 |
| [Transpose](./spatial-toolkit_pico-spatial-editor_材质_shader-graph_math_matrix_transpose.md) | 输出矩阵的转置矩阵。 |
#### Procedural
##### 2D Procedural
为材质生成 2D 噪声。
| **节点** | **描述** |
| --- | --- |
| [Cell Noise 2D](./spatial-toolkit_pico-spatial-editor_材质_shader-graph_math_procedural_2d-procedural_cell-noise-2d.md) | 2D 蜂窝噪声生成器。 |
| [Noise 2D](./spatial-toolkit_pico-spatial-editor_材质_shader-graph_math_procedural_2d-procedural_noise-2d.md) | 2D Perlin 噪声生成器。 |
| [Ramp 4 Corners](./spatial-toolkit_pico-spatial-editor_材质_shader-graph_math_procedural_2d-procedural_ramp-4-corners.md) | 四点线性值渐变（梯度）生成器。 |
| [Ramp Horizontal](./spatial-toolkit_pico-spatial-editor_材质_shader-graph_math_procedural_2d-procedural_ramp-horizontal.md) | 从左到右的线性值渐变（梯度）生成器。 |
| [Ramp Vertical](./spatial-toolkit_pico-spatial-editor_材质_shader-graph_math_procedural_2d-procedural_ramp-vertical.md) | 从上到下的线性值渐变（梯度）生成器。 |
| [Split Horizontal](./spatial-toolkit_pico-spatial-editor_材质_shader-graph_math_procedural_2d-procedural_split-horizontal.md) | 在指定 U 值处从左到右分割遮罩。 |
| [Split Vertical](./spatial-toolkit_pico-spatial-editor_材质_shader-graph_math_procedural_2d-procedural_split-vertical.md) | 在指定 V 值处从上到下分割遮罩。 |
| [Worley Noise 2D](./spatial-toolkit_pico-spatial-editor_材质_shader-graph_math_procedural_2d-procedural_worley-noise-2d.md) | 2D Worley 噪声生成器。 |
##### 3D Procedural
为材质生成 3D 噪声。
| **节点** | **描述** |
| --- | --- |
| [Cellular Noise 3D](./spatial-toolkit_pico-spatial-editor_材质_shader-graph_math_procedural_3d-procedural_cellular-noise-3d.md) | 3D 蜂窝噪声生成器。 |
| [Fractal Noise 3D](./spatial-toolkit_pico-spatial-editor_材质_shader-graph_math_procedural_3d-procedural_fractal-noise-3d.md) | 通过叠加多个不同频率和振幅的 3D Perlin 噪声层（octave），生成一种以 0 为中心波动的 3D 分形噪声。 |
| [Noise 3D](./spatial-toolkit_pico-spatial-editor_材质_shader-graph_math_procedural_3d-procedural_noise-3d.md) | 3D Perlin 噪声生成器。 |
| [Worley Noise 3D](./spatial-toolkit_pico-spatial-editor_材质_shader-graph_math_procedural_3d-procedural_worley-noise-3d.md) | 3D Worley 噪声生成器。 |
#### Transforms
对材质的纹理、颜色等属性进行变换操作。
| **节点** | **描述** |
| --- | --- |
| [Transform 2D](./spatial-toolkit_pico-spatial-editor_材质_shader-graph_math_transforms_transform-2d.md) | 对 2D 输入应用仿射变换的节点。 |
| [Transform Matrix](./spatial-toolkit_pico-spatial-editor_材质_shader-graph_math_transforms_transform-matrix.md) | 通过矩阵变换向量。 |
| [Transform Normal](./spatial-toolkit_pico-spatial-editor_材质_shader-graph_math_transforms_transform-normal.md) | 将法线从一个空间转换到另一个空间。 |
| [Transform Point](./spatial-toolkit_pico-spatial-editor_材质_shader-graph_math_transforms_transform-point.md) | 将坐标从一个空间变换到另一个空间。 |
| [Transform Vector](./spatial-toolkit_pico-spatial-editor_材质_shader-graph_math_transforms_transform-vector.md) | 将 3D 向量从一个空间变换到另一个空间。 |
#### Trigometry
在材质中进行三角函数运算。
| **节点** | **描述** |
| --- | --- |
| [Cos](./spatial-toolkit_pico-spatial-editor_材质_shader-graph_math_trigonometry_cos.md) | 传入值的余弦值（弧度）。 |
| [Sin](./spatial-toolkit_pico-spatial-editor_材质_shader-graph_math_trigonometry_sin.md) | 传入值的正弦值（弧度）。 |
| [Tan](./spatial-toolkit_pico-spatial-editor_材质_shader-graph_math_trigonometry_tan.md) | 传入值的正切值（弧度）。 |
| [Acos](./spatial-toolkit_pico-spatial-editor_材质_shader-graph_math_trigonometry_acos.md) | 传入值的反余弦值（弧度）。 |
| [Asin](./spatial-toolkit_pico-spatial-editor_材质_shader-graph_math_trigonometry_asin.md) | 传入值的反正弦值（弧度）。 |
| [Atan2](./spatial-toolkit_pico-spatial-editor_材质_shader-graph_math_trigonometry_atan2.md) | **In Y**/ **In X** 的反正切值（弧度）。 |
| [PI](./spatial-toolkit_pico-spatial-editor_材质_shader-graph_math_trigonometry_pi.md) | 返回圆周率 PI (π)。 |
### Surface
定义材质表面的最终物理属性，并输出到引擎的渲染管线。
| **节点** | **描述** |
| --- | --- |
| [Preview Surface](./spatial-toolkit_pico-spatial-editor_材质_shader-graph_surface_preview-surface.md) | MaterialX 版本的 USD 预览表面。 |
| [PBR Surface](./spatial-toolkit_pico-spatial-editor_材质_shader-graph_surface_pbr-surface.md) | 用于基于物理渲染 (PBR) 材质的表面着色器。 |
| [Unlit Surface](./spatial-toolkit_pico-spatial-editor_材质_shader-graph_surface_unlit-surface.md) | 用于无光照材质的表面着色器。 |
| [Occlusion Surface](./spatial-toolkit_pico-spatial-editor_材质_shader-graph_surface_occlusion-surface.md) | 为不接收动态光照的遮挡材质定义属性的表面着色器。 |
### Vertex
调整模型顶点的位置。
| **节点** | **描述** |
| --- | --- |
| [Geometry Modifier](./spatial-toolkit_pico-spatial-editor_材质_shader-graph_vertex_geometry-modifier.md) | 根据输入参数修改几何体的顶点属性，并对每个顶点执行一次。 |
| [Vertex Index](./spatial-toolkit_pico-spatial-editor_材质_shader-graph_vertex_vertex-index.md) | 返回当前顶点在网格中的索引值。 |
### Other
| **节点** | **描述** |
| --- | --- |
| [Node Graph](./spatial-toolkit_pico-spatial-editor_材质_shader-graph_other_node-graph.md) | 可包含着色节点及其他节点图的节点。 |
| [Dot](./spatial-toolkit_pico-spatial-editor_材质_shader-graph_other_dot.md) | 用于在节点图中对连线进行可视化导向的传递节点。 |
| [Named Dot](./spatial-toolkit_pico-spatial-editor_材质_shader-graph_other_named-dot.md) | 值传递节点。作用类似于全局变量，用于在 Node Graph 中传递数据。 |
| [Debug Value](./spatial-toolkit_pico-spatial-editor_材质_shader-graph_other_debug-value.md) | 将输入值渲染到表面以进行显示。 |
| [Sticky Note](./spatial-toolkit_pico-spatial-editor_材质_shader-graph_other_sticky-note.md) | 便签，用于对节点图添加注释。 |
| [Environment Radiance](./spatial-toolkit_pico-spatial-editor_材质_shader-graph_other_environment-radiance.md) | 根据真实世界环境信息以及一张 IBL 贴图（可由开发者提供，也可使用默认贴图），返回环境的漫反射辐射值和镜面反射辐射值。 |
| [Instance Custom Data](./spatial-toolkit_pico-spatial-editor_材质_shader-graph_other_instance-custom-data.md) | 返回存储在实例自定义数据中的浮点值 |
| [Fresnel Effect](./spatial-toolkit_pico-spatial-editor_材质_shader-graph_other_fresnel-effect.md) | 根据表面法线方向与视线方向计算菲涅耳效果。 |
