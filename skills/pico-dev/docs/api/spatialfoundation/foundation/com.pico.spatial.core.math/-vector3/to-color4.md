# toColor4 | PICO Spatial SDK

foundation / com.pico.spatial.core.math / Vector3 / toColor4 
# toColor4
```kotlin
fun toColor4(alpha: Float): Color4
```
Converts this vector (interpreted as RGB color components) and a given alpha value into a Color4 object. 
It is assumed that the x, y, z components of this vector and the provided alpha will be clamped within the range 0.0, 1.0 by the Color4 constructor. 
#### Return
A  Color4  object representing the RGBA color. 
#### Parameters
alpha 
The alpha component for the color, typically in the range 0.0, 1.0.