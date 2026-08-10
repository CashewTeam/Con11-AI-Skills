# PhysicallyBasedMaterial | PICO Spatial SDK

core / com.pico.spatial.core.ecs.resource / PhysicallyBasedMaterial 
# PhysicallyBasedMaterial
```kotlin
class PhysicallyBasedMaterial : Material
```
A material that simulates the appearance of real-world objects. 
PhysicallyBasedMaterial  is used in scenarios where realistic rendering is required. This material simulates how light interacts with surfaces based on physical properties, resulting in highly realistic visuals. 
Use cases: 
- 
AAA games that require realistic environments and character models. 
- 
Architectural visualization to create lifelike representations of buildings and interiors. 
- 
Film and animation production where high-quality rendering is essential. 
- 
Virtual reality (VR) and augmented reality (AR) applications that demand immersive and realistic visuals. 
Material Property Blending: 
PhysicallyBasedMaterial allows for the blending of different material properties to achieve the desired visual effect. The  PropertyValue  and  TextureResource  are combined using a multiplicative blending mode. This means that the final appearance of the material is the result of multiplying the property value with the texture color. This blending mode helps in creating more dynamic and visually interesting effects by combining uniform values and detailed texture information. Allowing for flexible customization and control over the material's appearance. These properties may be represented by different data types, such as linear color, floats, to accommodate various material characteristics. 
Members 
## Types
Companion 
```kotlin
object Companion
```
The companion object of  PhysicallyBasedMaterial . 
## Functions
get Ambient Occlusion 
```kotlin
fun getAmbientOcclusion(): Float
```
Gets the ambient occlusion value of the  PhysicallyBasedMaterial . 
get Ambient Occlusion Texture 
```kotlin
fun getAmbientOcclusionTexture(): TextureResource
```
Gets the ambient occlusion texture of the  PhysicallyBasedMaterial . 
get Base Color 
```kotlin
fun getBaseColor(): Color4
```
Gets the base color of the  PhysicallyBasedMaterial . 
get Base Color Texture 
```kotlin
fun getBaseColorTexture(): TextureResource
```
Gets the base color texture of the  PhysicallyBasedMaterial . 
get Blending Mode 
```kotlin
fun getBlendingMode(): BlendingMode
```
Gets the blending mode of the  PhysicallyBasedMaterial . 
get Culling Mode 
```kotlin
fun getCullingMode(): MaterialCullingMode
```
Gets the  MaterialCullingMode  of the PhysicallyBasedMaterial. 
get Depth Test 
```kotlin
fun getDepthTest(): Boolean
```
Gets the state of depth testing for the material. 
get Depth Write 
```kotlin
fun getDepthWrite(): Boolean
```
Gets the state of depth writing for the material. 
get Emissive Color 
```kotlin
fun getEmissiveColor(): Color4
```
Gets the emissive color of the  PhysicallyBasedMaterial . 
get Emissive Texture 
```kotlin
fun getEmissiveTexture(): TextureResource
```
Gets the emissive texture of the  PhysicallyBasedMaterial . 
get Metallic 
```kotlin
fun getMetallic(): Float
```
Gets the metallic value of the  PhysicallyBasedMaterial . 
get Metallic Texture 
```kotlin
fun getMetallicTexture(): TextureResource
```
Gets the metallic texture of the  PhysicallyBasedMaterial . 
get Name 
```kotlin
fun getName(): String
```
Gets the name of the  PhysicallyBasedMaterial . 
get Normal Scale 
```kotlin
fun getNormalScale(): Float
```
Gets the normal scale of the  PhysicallyBasedMaterial . 
get Normal Texture 
```kotlin
fun getNormalTexture(): TextureResource
```
Gets the normal texture of the  PhysicallyBasedMaterial . 
get Opacity 
```kotlin
fun getOpacity(): Float
```
Gets the opacity of the  PhysicallyBasedMaterial . 
get Polygon Fill Mode 
```kotlin
fun getPolygonFillMode(): PolygonFillMode
```
Gets the fill mode for rendering polygons in the material. 
get Roughness 
```kotlin
fun getRoughness(): Float
```
Gets the roughness of the  PhysicallyBasedMaterial . 
get Roughness Texture 
```kotlin
fun getRoughnessTexture(): TextureResource
```
Gets the roughness texture of the  PhysicallyBasedMaterial . 
set Ambient Occlusion 
```kotlin
fun setAmbientOcclusion(ao: Float)
```
Sets the ambient occlusion value of the  PhysicallyBasedMaterial . 
set Ambient Occlusion Texture 
```kotlin
fun setAmbientOcclusionTexture(texture: TextureResource)
```
Sets the ambient occlusion texture of the  PhysicallyBasedMaterial . 
set Base Color 
```kotlin
fun setBaseColor(color: Color4)
```
Sets the base color of the  PhysicallyBasedMaterial  using a color value. 
set Base Color Texture 
```kotlin
fun setBaseColorTexture(texture: TextureResource)
```
Sets the base color of the  PhysicallyBasedMaterial  using a texture. 
set Blending Mode 
```kotlin
fun setBlendingMode(blendingMode: BlendingMode)
```
Sets the blending mode of the  PhysicallyBasedMaterial . 
set Culling Mode 
```kotlin
fun setCullingMode(cullingMode: MaterialCullingMode)
```
Sets the  MaterialCullingMode  of the  PhysicallyBasedMaterial . 
set Depth Test 
```kotlin
fun setDepthTest(depthTest: Boolean)
```
Enables or disables depth testing for the material. 
set Depth Write 
```kotlin
fun setDepthWrite(depthWrite: Boolean)
```
Enables or disables depth writing for the material. 
set Emissive Color 
```kotlin
fun setEmissiveColor(color: Color4)
```
Sets the emissive color of the  PhysicallyBasedMaterial . 
set Emissive Texture 
```kotlin
fun setEmissiveTexture(texture: TextureResource)
```
Sets the emissive texture of the  PhysicallyBasedMaterial . 
set Metallic 
```kotlin
fun setMetallic(metallic: Float)
```
Sets the metallic value of the  PhysicallyBasedMaterial . 
set Metallic Texture 
```kotlin
fun setMetallicTexture(texture: TextureResource)
```
Sets the metallic property of the  PhysicallyBasedMaterial  using a texture. 
set Normal Scale 
```kotlin
fun setNormalScale(scale: Float)
```
Sets the normal scale of the  PhysicallyBasedMaterial . 
set Normal Texture 
```kotlin
fun setNormalTexture(texture: TextureResource)
```
Sets the normal texture of the  PhysicallyBasedMaterial . 
set Opacity 
```kotlin
fun setOpacity(opacity: Float)
```
Sets the opacity of the  PhysicallyBasedMaterial . 
set Polygon Fill Mode 
```kotlin
fun setPolygonFillMode(polygonFillMode: PolygonFillMode)
```
Sets the fill mode for rendering polygons in the material. 
set Roughness 
```kotlin
fun setRoughness(roughness: Float)
```
Sets the roughness value of the  PhysicallyBasedMaterial . 
set Roughness Texture 
```kotlin
fun setRoughnessTexture(texture: TextureResource)
```
Sets the roughness of the  PhysicallyBasedMaterial  using a texture.