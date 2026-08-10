材质（Material）定义了物体表面如何与光线交互，从而决定物体的视觉属性，如金属质感、透明度、光泽度等。材质通过着色器实现光照计算，并与纹理结合产生丰富的视觉效果。
材质系统的核心组成部分包括：

* **着色器程序**：定义光照模型和渲染算法；
* **属性：**基础颜色、法线、金属度、粗糙度、透明度、反光率、自发光强度等。

## 材质类型
PICO Spatial SDK 支持以下几种较为基础且常见的材质，包括 UnlitMaterial 和 PhysicallyBasedMaterial。
| **材质名称** | **定义** | **主要特点** | **使用场景** |
| --- | --- | --- | --- |
| UnlitMaterial | UnlitMaterial（无光照材质）是一种不受光的材质，始终以平面着色方式渲染，外观完全由纹理和材质属性决定。 | * 无光照计算，性能最高 ;  * 不投射或接收阴影 ;  * 视觉效果稳定一致，但缺乏真实感 | UI 元素、特效贴图（如粒子、2D 图标）、卡通渲染、始终需要保持一致外观的对象。 |
| PhysicallyBasedMaterial | PhysicallyBasedMaterial (PBR)（基于物理渲染的材质）是一种模拟真实世界物体外观的材质。 | * 高度真实感 ;  * 能适配各种光照条件 ;  * 计算量大，对性能要求高 | 高品质游戏、影视级渲染、VR/AR 应用、对材质真实感要求高的场景。 |
PICO Spatial SDK 支持的较为高阶的材质包括 ShaderGraphMaterial 和 VideoMaterial，详情参考《[ShaderGraphMaterial](./spatial-sdk_渲染_shadergraphmaterial.md)》和《[使用 VideoMaterial](./spatial-sdk_视频_使用-videomaterial.md)》。
PhysicsMaterialResource 是专门用于物理模拟的材质资源，定义了物体在物理交互中的表面特性，包括静摩擦力、动摩擦力和碰撞回弹系数。与渲染材质（如 PBR、Unlit）不同，物理材质完全不涉及视觉外观和渲染效果，仅影响物体的碰撞、摩擦和运动行为。由于其功能与本文介绍的渲染材质系统完全独立，故不在此处详述。

## 加载材质
可以通过以下几种方式加载材质：

* 使用 `Entity.load` 加载 3D 模型、得到返回的 entity 实例 `modelEntity` 之后，可以通过 `modelEntity` 获取其 `ModelComponent` 实例，进而获取到材质资源列表和对应的材质资源，详情参考《[模型](./spatial-sdk_资源管理_模型.md)》。
* 调用 `assetBundle.loadMaterial` 从 Spatial Editor 的项目中加载 UnlitMaterial、PhysicallyBasedMaterial 和 ShaderGraphMaterial，详情参考《[AssetBundle](./spatial-sdk_资源管理_assetbundle.md)》。
* 调用 `ShaderGraphMaterial.loadFromAssetBundle` 加载 Spatial Editor 项目中的 `ShaderGraphMaterial`，详情参考《[ShaderGraphMaterial](./spatial-sdk_渲染_shadergraphmaterial.md)》。

## 创建材质
SDK 提供了相应的静态函数用于创建材质实例。在创建时，需要传入 `BlendingMode` 参数，以指定材质的混合模式。
```Kotlin
fun createMaterialResourceExample() {
    val unlitMaterial = UnlitMaterial.create(BlendingMode.OPAQUE)
    val pbrMaterial = PhysicallyBasedMaterial.create(BlendingMode.TRANSPARENT)
}
```

## 调整材质的属性
创建材质后，你可以按需修改材质实例的属性。UnlitMaterial 和 PhysicallyBasedMaterial 支持的属性如下：
| **属性** | **描述** | **UnlitMaterial** | **PhysicallyBasedMaterial** |
| --- | --- | --- | --- |
| CullingMode | 面剔除模式，控制哪些面被渲染。 ;; * `FRONT`：只渲染背面 ;  * `BACK`：只渲染正面 ;  * `NONE`：正反面都渲染 ;  * `FRONT_AND_BACK`：正反面都不渲染 | ✅ | ✅ |
| PolygonFillMode | 多边形填充模式。 ;; * `FILL`：实心填充 ;  * `LINE`：线框模式 | ✅ | ✅ |
| DepthTest | 深度测试开关，控制是否进行深度比较以确定像素前后关系。 | ✅ | ✅ |
| DepthWrite | 深度写入开关，控制是否将像素深度写入深度缓冲区。 | ✅ | ✅ |
| BlendingMode | 混合模式，控制当前像素与背景像素的混合方式。 ;; * `OPAQUE`：完全不透明 ;  * `TRANSPARENT`：标准 Alpha 透明，但保持高光效果 ;  * `ADD`：颜色相加混合 ;  * `FADE`：Alpha 淡化，高光和反射同时淡化 ;  * `MASKED`：遮罩模式，基于阈值的完全透明或不透明 | ✅ | ✅ |
| Opacity | 透明度，控制材质的整体透明程度，范围为 [0.0f, 1.0f]。 | ✅ | ✅ |
| BaseColor | 基础颜色，即材质的主要颜色。在 PBR 中是漫反射颜色，在其他材质中是主色调，数据类型为 Color4。 | ✅ | ✅ |
| BaseColorTexture | 基础颜色贴图，提供基础颜色的纹理贴图，与 BaseColor 相乘得到最终颜色。 | ✅ | ✅ |
| ToneMapping ;   | 色调映射开关。控制是否对该材质应用色调映射效果。默认为 true。 ;  色调映射能将高动态范围（HDR）图像中过亮或过暗的区域调整至屏幕可正常显示的亮度范围内，同时尽可能保留画面的细节和观感。 | ✅ | - |
| Roughness | 粗糙度，控制表面的微观粗糙程度，影响反射的锐利度，范围为[0.0f, 1.0f]。`0` 表示镜面，`1` 表示完全粗糙。 | - | ✅ |
| RoughnessTexture | 粗糙度贴图，提供表面粗糙度的纹理变化信息。 | - | ✅ |
| Metallic | 金属度，控制材质的金属特性，范围为 [0.0f, 1.0f]。`0` 表示非金属（电介质），`1` 表示纯金属。 | - | ✅ |
| MetallicTexture | 金属度贴图，提供表面金属度的纹理变化，也可与粗糙度纹理打包在一起使用。 | - | ✅ |
| NormalScale | 法线强度，控制法线贴图效果的强度，用于调节表面细节的凹凸程度，范围为 [0.0f, 1.0f]。 | - | ✅ |
| NormalTexture | 法线贴图，存储表面细节的法线信息，用于增加表面凹凸细节而不增加几何复杂度。 | - | ✅ |
| AmbientOcclusion | 环境光遮蔽强度，控制环境光遮蔽贴图的强度，用于调节表面缝隙和凹陷处的阴影程度，增加深度感。 | - | ✅ |
| AmbientOcclusionTexture | 环境光遮蔽贴图，提供表面缝隙和凹陷处的阴影信息，通常烘焙了静态阴影信息。 | - | ✅ |
| EmissiveColor | 自发光颜色，材质自身发出的光线颜色，不受光照影响，数据类型为 Color4。 | - | ✅ |
| EmissiveTexture | 自发光贴图，定义材质哪些区域发光以及光的颜色和强度。 | - | ✅ |
其中，两种材质都支持的通用属性包括：

* **渲染控制**：CullingMode、PolygonFillMode、DepthTest、DepthWrite
* **混合与透明**：BlendingMode、Opacity
* **基础外观**：BaseColor、BaseColorTexture

PBR 材质专有的属性包括：

* **物理特性**：Roughness、Metallic 及其对应纹理
* **细节增强**：NormalScale、NormalTexture
* **光照增强**：AmbientOcclusion、EmissiveColor 及其纹理

Unlit 材质专有的属性包括：

* **后期处理**：ToneMapping

材质复杂度按照以下顺序递减：

* **PhysicallyBasedMaterial**：功能最全面，支持所有属性
* **UnlitMaterial**：仅支持基本的颜色和渲染控制

## 使用建议
建议按照以下流程使用材质：

1. 根据物体类型选择合适的材质类型。
2. 选择必要的纹理（至少包含基础颜色纹理）。
3. 调整材质的属性以优化视觉效果。
4. 测试材质在不同光照条件下的表现。

## API 参考
`UnlitMaterial` 和 `PhysicallyBasedMaterial` 类中提供了材质相关的属性和函数，详情参阅 API 参考。根据你所处的地理位置选择合适的文档链接：

* 中国大陆：[https://developer-cn.picoxr.com/spatial-api/index.html](https://developer-cn.picoxr.com/spatial-api/index.html)
* 非中国大陆：[https://developer.picoxr.com/spatial-api/index.html](https://developer.picoxr.com/spatial-api/index.html)
