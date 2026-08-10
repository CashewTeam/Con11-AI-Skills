# getBlendShapeWeight | PICO Spatial SDK

core / com.pico.spatial.core.ecs / BlendShapeControllerComponent / getBlendShapeWeight 
# getBlendShapeWeight
```kotlin
fun getBlendShapeWeight(index: Int): Float?
```
Get the weight of a BlendShape by its index. 
#### Return
The weight of the BlendShape at the specified index, or  null  if the index is invalid. 
#### Parameters
index 
The index of the BlendShape. 
```kotlin
fun getBlendShapeWeight(blendShapeName: String): Float?
```
Get the weight of a BlendShape by its name. 
#### Return
The weight of the BlendShape with the specified name, or  null  if the name is invalid. 
#### Parameters
blend Shape Name 
The name of the BlendShape.