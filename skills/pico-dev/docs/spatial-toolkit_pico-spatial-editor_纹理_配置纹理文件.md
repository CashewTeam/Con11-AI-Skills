本文介绍如何在 Spatial Editor 中配置纹理文件。
你把纹理文件作为资源添加到 Spatial Editor 后，可以配置纹理文件的材质类型、色彩空间、材质形状、材质格式、最大尺寸、MipMap 以及压缩质量。
## 操作步骤
参见以下步骤配置你的纹理文件。

1. 在 Spatial Editor 的 **Project Browser** 标签页，找到并选中你需要配置的纹理文件。
2. 在右侧的配置窗口，修改纹理文件的配置。详情参阅 [配置参考](/editor/configure-texture-file)。

## 配置参考
| 参数 | 描述 |
| --- | --- |
| Texture Type | 材质类型。 ;; * **Default**：默认纹理。 ;  * **Normal**：法线贴图，用于表现物体表面的凹凸细节。 |
| Color Space | 色彩空间。在 **Textures Type** 为 **Normal** 时，该参数强制为 **Raw** 且不可修改。 |
| Texture Shape | 纹理形状。 ;; * **2D**：表示纹理形状为二维平面。; * **Cube**：表示纹理形状为立方体。 如果你把贴图添加到 IBL 相关的[灯光组件](./spatial-toolkit_pico-spatial-editor_组件_组件类型_灯光组件.md)，**Texture Shape** 会被自动设置为 **Cube**。 |
| Texture Format | 纹理格式。 |
| Compression Quality | 设置 ASTC 纹理压缩的采样质量。采样质量越高，则纹理的质量越高，但压缩时间也会相应增加。该参数仅 **Texture** **Format** 属于 ASTC 纹理压缩格式时出现。 ;; * **Fast**：采样质量为 0。; * **Normal**：采样质量为 60。 ;  * **High**：采样质量为 98。 ;  * **Best**：采样质量为 100。 |
| Max Size | 设置纹理导入后的最大尺寸（如 2048, 4096）。如果原始图片尺寸超过此值，会被自动缩放至此大小以节省显存。 |
| Generate MipMaps | 是否生成 MipMap。你可以通过对 MipMap 进行锐化操作提升纹理的清晰度。 |
| MipMap Mode | 设置生成 MipMap 的算法。 ;; * **DEFAULT**：（默认）适用于 **Texture Shape** 为 **2D** 时的场景。 ;  * **ENV_LIGHTING**：适用于 **Texture Shape** 为 **Cube** 时的场景。 如果你把贴图添加到 IBL 相关的[灯光组件](./spatial-toolkit_pico-spatial-editor_组件_组件类型_灯光组件.md)，**Texture Shape** 会被自动设置为 **Cube，MipMap Mode** 会被自动设置为 **ENV_LIGHTING。** |
| Sharpness Level | MipMap 的锐化等级。 ;; * **None**：不对 MipMap 进行锐化操作。 ;  * **Low**：低等级锐化。 ;  * **Medium**：中等级锐化。 ;  * **High**：高等级锐化 |
| Y Flip | 是否翻转法线贴图的 Y 轴（绿色通道）。用于修正法线贴图视觉上“凹凸相反”的问题。通常用于适配不同建模软件导出的法线标准。 ;  该参数仅 **Texture** 为 **Normal** 时出现。 |

