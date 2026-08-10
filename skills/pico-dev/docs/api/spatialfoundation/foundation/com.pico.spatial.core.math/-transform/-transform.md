# Transform | PICO Spatial SDK

foundation / com.pico.spatial.core.math / Transform / Transform 
# Transform
```kotlin
constructor()
```
Creates a  Transform  instance with position, rotation (as  EulerAngles ), and scale. This is the default  Transform  constructor. 
The position is  Vector3.ZERO , the rotation is  Quat.identity() , and the scale is  Vector3.ONE . 
```kotlin
constructor(position: Vector3, rotation: EulerAngles, scale: Vector3)
```
Creates a  Transform  instance with specified position, rotation (as  EulerAngles ), and scale. 
#### Parameters
position 
The position vector. 
rotation 
The rotation represented as an  EulerAngles . 
scale 
The scale vector. 
```kotlin
constructor(position: Vector3, rotation: Quat, scale: Vector3)
```
Creates a  Transform  instance with specified position, rotation (as Quat), and scale. 
#### Parameters
position 
The position vector. 
rotation 
The rotation represented as a quaternion. 
scale 
The scale vector.