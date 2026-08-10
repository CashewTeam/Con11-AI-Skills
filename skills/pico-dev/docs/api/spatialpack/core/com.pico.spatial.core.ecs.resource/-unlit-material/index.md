# UnlitMaterial | PICO Spatial SDK

core / com.pico.spatial.core.ecs.resource / UnlitMaterial 
# UnlitMaterial
```kotlin
class UnlitMaterial : Material
```
A material type that renders without being affected by scene lighting. 
Material Property Blending: 
UnlitMaterial  allows for the blending of different material properties to achieve the desired visual effect.  PropertyValue  and  TextureResource  are combined using a multiplicative blending mode. This means that the final appearance of the material is the result of multiplying the property value with the texture color. This blending mode helps in creating more dynamic and visually interesting effects by combining uniform values and detailed texture information. Allowing for flexible customization and control over the material's appearance. These properties may be represented by different data types, such as linear color and float, to accommodate various material characteristics. 
Members 
## Types
Companion 
```kotlin
object Companion
```
The companion object of  UnlitMaterial . 
## Functions
get Base Color 
```kotlin
fun getBaseColor(): Color4
```
Gets the base color of the  UnlitMaterial . 
get Base Color Texture 
```kotlin
fun getBaseColorTexture(): TextureResource
```
Gets the base color texture of the  UnlitMaterial . 
get Blending Mode 
```kotlin
fun getBlendingMode(): BlendingMode
```
Gets the blending mode of the  UnlitMaterial . 
get Culling Mode 
```kotlin
fun getCullingMode(): MaterialCullingMode
```
Gets the  MaterialCullingMode  of the  UnlitMaterial . 
get Depth Test 
```kotlin
fun getDepthTest(): Boolean
```
Gets the state of depth testing for the  UnlitMaterial . 
get Depth Write 
```kotlin
fun getDepthWrite(): Boolean
```
Gets the state of depth writing for the  UnlitMaterial . 
get Name 
```kotlin
fun getName(): String
```
Gets the name of the  UnlitMaterial . 
get Opacity 
```kotlin
fun getOpacity(): Float
```
Gets the opacity of the  UnlitMaterial . 
get Polygon Fill Mode 
```kotlin
fun getPolygonFillMode(): PolygonFillMode
```
Gets the fill mode for rendering polygons in the  UnlitMaterial . 
is Apply Tone Mapping 
```kotlin
fun isApplyToneMapping(): Boolean
```
Gets whether tone mapping is applied to the  UnlitMaterial . 
set Apply Tone Mapping 
```kotlin
fun setApplyToneMapping(isApplyToneMapping: Boolean)
```
Sets whether to apply tone mapping to the  UnlitMaterial . 
set Base Color 
```kotlin
fun setBaseColor(color: Color4)
```
Sets the base color of the  UnlitMaterial . 
set Base Color Texture 
```kotlin
fun setBaseColorTexture(texture: TextureResource)
```
Sets the texture to be used as the base color for the  UnlitMaterial . 
set Blending Mode 
```kotlin
fun setBlendingMode(blendingMode: BlendingMode)
```
Sets the blending mode of the  UnlitMaterial . 
set Culling Mode 
```kotlin
fun setCullingMode(cullingMode: MaterialCullingMode)
```
Sets the  MaterialCullingMode  of the  UnlitMaterial . 
set Depth Test 
```kotlin
fun setDepthTest(depthTest: Boolean)
```
Enables or disables depth testing for the  UnlitMaterial . 
set Depth Write 
```kotlin
fun setDepthWrite(depthWrite: Boolean)
```
Enables or disables depth writing for the  UnlitMaterial . 
set Opacity 
```kotlin
fun setOpacity(opacity: Float)
```
Sets the opacity of the  UnlitMaterial . 
set Polygon Fill Mode 
```kotlin
fun setPolygonFillMode(polygonFillMode: PolygonFillMode)
```
Sets the fill mode for rendering polygons in the  UnlitMaterial .