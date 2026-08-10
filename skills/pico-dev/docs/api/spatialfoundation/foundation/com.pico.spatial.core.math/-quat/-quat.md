# Quat | PICO Spatial SDK

foundation / com.pico.spatial.core.math / Quat / Quat 
# Quat
```kotlin
constructor(x: Float, y: Float, z: Float, w: Float)
```
Constructs a new  Quat  instance with the specified x, y, z, and w components. 
#### Parameters
x 
The x position of the  Quat . 
y 
The y position of the  Quat . 
z 
The z position of the  Quat . 
w 
The w position of the  Quat . 
```kotlin
constructor()
```
The default  Quat  constructor. 
It uses (0f, 0f, 0f, 1f) to initialize the  Quat  instance. 
```kotlin
constructor(another: Quat)
```
Initializes a new  Quat  instance from another existing  Quat  instance. 
#### Parameters
another 
Another existing  Quat  instance and its values will be used to initialize a new  Quat  instance. 
```kotlin
constructor(rotAxis: Vector3, rotAngle: Float)
```
Initializes a  Quat  instance using an angle and axis of rotation. 
#### Parameters
rot Axis 
A  Vector3  instance representing the rotation axis (x, y, z). This vector will be normalized if it is not ready. 
rot Angle 
The rotation angle in radians.