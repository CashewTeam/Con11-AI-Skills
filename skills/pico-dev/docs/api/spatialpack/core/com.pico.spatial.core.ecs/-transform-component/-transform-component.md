# TransformComponent | PICO Spatial SDK

core / com.pico.spatial.core.ecs / TransformComponent / TransformComponent 
# TransformComponent
```kotlin
constructor()
```
The default constructor. 
```kotlin
constructor(transform: Transform)
```
Creates a  TransformComponent  initialized with the values from the given  Transform . 
#### Parameters
transform 
The  Transform  providing position, rotation, and scale values. 
```kotlin
constructor(position: Vector3, rotation: EulerAngles, scale: Vector3)
```
Creates a  TransformComponent  with the specified position, rotation, and scale. 
#### Parameters
position 
The  Vector3  position. 
rotation 
The  EulerAngles  rotation. 
scale 
The  Vector3  scale. 
```kotlin
constructor(position: Vector3, rotation: Quat, scale: Vector3)
```
Creates a  TransformComponent  with the specified position, rotation, and scale. 
#### Parameters
position 
The  Vector3  position. 
rotation 
The  Quat  rotation. 
scale 
The  Vector3  scale.