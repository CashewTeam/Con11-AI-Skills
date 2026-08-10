# isRotationLocked | PICO Spatial SDK

core / com.pico.spatial.core.ecs / RigidBodyComponent / isRotationLocked 
# isRotationLocked
```kotlin
var isRotationLocked: Bool3
```
A tuple of boolean values that indicates whether the rotation of the rigid body is locked around each of the three axes. 
The axes correspond to the euler angles in the following order: (x-axis: pitch, y-axis: yaw, z-axis: roll). 
- 
The first value locks rotation around the x-axis (pitch). 
- 
The second value locks rotation around the y-axis (yaw). 
- 
The third value locks rotation around the z-axis (roll). 
The default value is  Bool3(false, false, false) , meaning that rotation is not locked around any axis.