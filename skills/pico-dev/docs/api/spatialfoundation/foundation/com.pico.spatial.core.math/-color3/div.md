# div | PICO Spatial SDK

foundation / com.pico.spatial.core.math / Color3 / div 
# div
```kotlin
operator fun div(scalar: Float): Color3
```
Divides the  Color3  instance by a scalar value. 
#### Return
A new  Color3  instance, which is the result of dividing the  Color3  instance by the scalar value. 
#### Parameters
scalar 
The scalar value to divide the  Color3  instance by. 
#### Throws
Illegal Argument Exception 
If the scalar value is zero. 
```kotlin
operator fun div(another: Color3): Color3
```
Divides the  Color3  instance by another  Color3  instance. 
#### Return
A new  Color3  instance, which is the result of dividing the  Color3  instance by the another  Color3  instance. 
#### Parameters
another 
Another  Color3  instance. 
#### Throws
Illegal Argument Exception 
If the other Color4 has zero value.