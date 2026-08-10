# ShaderGraphMaterial | PICO Spatial SDK

core / com.pico.spatial.core.ecs.resource / ShaderGraphMaterial 
# ShaderGraphMaterial
```kotlin
class ShaderGraphMaterial : Material
```
Provides methods to query and modify material parameters for dynamic customization at runtime. 
Each parameter is accessible by name and supports various data types. 
Members 
## Types
Companion 
```kotlin
object Companion
```
The companion object of  ShaderGraphMaterial . 
## Functions
get Blending Mode 
```kotlin
fun getBlendingMode(): BlendingMode
```
Gets the blending mode of the  ShaderGraphMaterial . 
get Culling Mode 
```kotlin
fun getCullingMode(): MaterialCullingMode
```
Gets the  MaterialCullingMode  of the  ShaderGraphMaterial . 
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
get Name 
```kotlin
fun getName(): String
```
Gets the name of the  ShaderGraphMaterial . 
get Parameter 
```kotlin
inline fun <T> getParameter(parameterName: String): T
```
```kotlin
fun <T> getParameter(parameterName: String, clazz: Class<T>): T
```
Gets the value of a parameter by its name and type. 
get Parameter Names 
```kotlin
fun getParameterNames(): Array<String>
```
Gets all parameter names of the  ShaderGraphMaterial . 
get Polygon Fill Mode 
```kotlin
fun getPolygonFillMode(): PolygonFillMode
```
Gets the fill mode for rendering polygons in the material. 
set Blending Mode 
```kotlin
fun setBlendingMode(blendingMode: BlendingMode)
```
Sets the blending mode of the  ShaderGraphMaterial . 
set Culling Mode 
```kotlin
fun setCullingMode(cullingMode: MaterialCullingMode)
```
Sets the  MaterialCullingMode  of the  ShaderGraphMaterial . 
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
set Parameter 
```kotlin
fun setParameter(parameterName: String, value: TextureResource)
```
Sets the value of a texture resource parameter by its name. 
```kotlin
fun setParameter(parameterName: String, value: Color3)
```
Sets the value of a color3 parameter by its name. 
```kotlin
fun setParameter(parameterName: String, value: Color4)
```
Sets the value of a color4 parameter by its name. 
```kotlin
fun setParameter(parameterName: String, value: Matrix3)
```
Sets the value of a matrix3 parameter by its name. 
```kotlin
fun setParameter(parameterName: String, value: Matrix4)
```
Sets the value of a matrix4 parameter by its name. 
```kotlin
fun setParameter(parameterName: String, value: Vector2)
```
Sets the value of a vector2 parameter by its name. 
```kotlin
fun setParameter(parameterName: String, value: Vector3)
```
Sets the value of a vector3 parameter by its name. 
```kotlin
fun setParameter(parameterName: String, value: Vector4)
```
Sets the value of a vector4 parameter by its name. 
```kotlin
fun setParameter(parameterName: String, value: Boolean)
```
Sets the value of a boolean parameter by its name. 
```kotlin
fun setParameter(parameterName: String, value: Float)
```
Sets the value of a float parameter by its name. 
```kotlin
fun setParameter(parameterName: String, value: Int)
```
Sets the value of an integer parameter by its name. 
set Polygon Fill Mode 
```kotlin
fun setPolygonFillMode(polygonFillMode: PolygonFillMode)
```
Sets the fill mode for rendering polygons in the material.