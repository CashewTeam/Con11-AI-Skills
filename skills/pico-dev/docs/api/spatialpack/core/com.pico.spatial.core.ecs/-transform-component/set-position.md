# setPosition | PICO Spatial SDK

core / com.pico.spatial.core.ecs / TransformComponent / setPosition 
# setPosition
```kotlin
fun setPosition(position: Vector3): TransformComponent
```
Sets the location of the  TransformComponent . 
This operation is valid only when the  TransformComponent  is mounted on an entity; otherwise, it will just record data through Component. 
#### Return
The  TransformComponent  object for method chaining. 
#### Parameters
position 
The given position.