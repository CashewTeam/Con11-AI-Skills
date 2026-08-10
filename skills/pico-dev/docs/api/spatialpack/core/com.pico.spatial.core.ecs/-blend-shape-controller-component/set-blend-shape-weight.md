# setBlendShapeWeight | PICO Spatial SDK

core / com.pico.spatial.core.ecs / BlendShapeControllerComponent / setBlendShapeWeight 
# setBlendShapeWeight
```kotlin
fun setBlendShapeWeight(index: Int, weight: Float): Boolean
```
Set the weight of a BlendShape by its index. 
#### Return
true  if the weight was successfully set,  false  if the index is invalid. 
#### Parameters
index 
The index of the BlendShape. 
weight 
The weight to set for the BlendShape at the specified index. 
```kotlin
fun setBlendShapeWeight(blendShapeName: String, weight: Float): Boolean
```
Set the weight of a BlendShape by its name. 
#### Return
true  if the weight was successfully set,  false  if the name is invalid. 
#### Parameters
blend Shape Name 
The name of the BlendShape. 
weight 
The weight to set for the BlendShape with the specified name.