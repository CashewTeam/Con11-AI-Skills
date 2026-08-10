# translate | PICO Spatial SDK

foundation / com.pico.spatial.core.math / Matrix4 / Companion / translate 
# translate
```kotlin
@JvmStatic
```fun  translate ( translation :  Vector3 ) :  Matrix4 
Creates and returns a 4x4 matrix representing a 3D translation. 
The translation distances along the X, Y, and Z axes are provided by the components of the input  translation  vector. 
The resulting matrix is structured for post-multiplication with column vectors (e.g.,  TransformedPoint = TranslationMatrix * OriginalPoint ). It will have the translation components in the last column: 

```
| 1.0  0.0  0.0  translation.x || 0.0  1.0  0.0  translation.y || 0.0  0.0  1.0  translation.z || 0.0  0.0  0.0  1.0           |
```
#### Return
A new  Matrix4  instance representing the specified 3D translation. 
#### Parameters
translation 
A  Vector3  whose  x ,  y , and  z  components define the translation distances along the respective axes.