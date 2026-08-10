# rotation | PICO Spatial SDK

foundation / com.pico.spatial.core.math / Matrix4 / Companion / rotation 
# rotation
```kotlin
@JvmStatic
```fun  rotation ( eulerAngles :  EulerAngles ) :  Matrix4 
Creates and returns a 4x4 rotation matrix from the provided Euler angles (yaw, pitch, roll) specified in  degrees . 
All input Euler angle components ( yaw ,  pitch ,  roll ) must be finite numbers. 
#### Return
A new  Matrix4  instance representing the specified rotation. 
#### Parameters
euler Angles 
A  EulerAngles  object containing yaw, pitch, and roll angles in  degrees . All angles must be finite.