# div | PICO Spatial SDK

foundation / com.pico.spatial.core.math / Color4 / div 
# div
```kotlin
operator fun div(other: Color4): Color4
```
Divides by another  Color4  instance. 
#### Return
The new  Color4  instance. 
#### Parameters
other 
Another  Color4  instance to be divided. 
#### Throws
Illegal Argument Exception 
If the other  Color4  has zero value. 
```kotlin
operator fun div(scalar: Float): Color4
```
Divides by a scalar value. 
#### Return
The new  Color4  instance. 
#### Parameters
scalar 
The value will be divided. 
#### Throws
Illegal Argument Exception 
If the scalar value is zero.