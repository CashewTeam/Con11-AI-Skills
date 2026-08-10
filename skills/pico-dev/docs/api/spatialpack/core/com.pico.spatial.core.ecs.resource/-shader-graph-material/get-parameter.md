# getParameter | PICO Spatial SDK

core / com.pico.spatial.core.ecs.resource / ShaderGraphMaterial / getParameter 
# getParameter
```kotlin
fun <T> getParameter(parameterName: String, clazz: Class<T>): T
```
Gets the value of a parameter by its name and type. 
#### Return
The value of the parameter of the specified name and type. 
#### Parameters
T 
The type of the parameter to retrieve. Supported types include: Integer, Boolean, Float, Color3, Color4, Vector2, Vector3, Vector4, Matrix3, Matrix4, TextureResource. 
parameter Name 
The name of the parameter to retrieve. 
clazz 
The class of the parameter type. 
#### Throws
Illegal State Exception 
If this material is closed or invalid. 
Illegal Argument Exception 
If the specified parameter type is not supported. 
```kotlin
inline fun <T> getParameter(parameterName: String): T
```
Gets the value of a parameter by its name and type. 
#### Return
The value of the parameter of the specified name and type. 
#### Parameters
T 
The type of the parameter to retrieve. Supported types include: Integer, Boolean, Float, Color3, Color4, Vector2, Vector3, Vector4, Matrix3, Matrix4, TextureResource. 
parameter Name 
The name of the parameter to retrieve. 
#### Throws
Illegal State Exception 
If this material is closed or invalid. 
Illegal Argument Exception 
If the specified parameter type is not supported.