# scaleBy | PICO Spatial SDK

core / com.pico.spatial.core.ecs / TransformComponent / scaleBy 
# scaleBy
```kotlin
fun scaleBy(factor: Float): TransformComponent
```
Scales the current  TransformComponent  by the given factor. 
This method multiplies the current scale vector by the specified factor. For example, with an initial scale of  Vector3(1f, 1f, 1f)  and a factor of  0.5f , the result will be  Vector3(0.5f, 0.5f, 0.5f) . Calling it again with the same factor produces  Vector3(0.25f, 0.25f, 0.25f) . 
To set the scale vector directly, use  setScaleVector . 
#### Return
The  TransformComponent  object for method chaining. 
#### Parameters
factor 
The scalar multiplier for the current scale.