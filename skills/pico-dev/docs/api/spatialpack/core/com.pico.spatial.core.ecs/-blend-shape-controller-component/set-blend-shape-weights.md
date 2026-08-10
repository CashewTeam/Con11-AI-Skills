# setBlendShapeWeights | PICO Spatial SDK

core / com.pico.spatial.core.ecs / BlendShapeControllerComponent / setBlendShapeWeights 
# setBlendShapeWeights
```kotlin
fun setBlendShapeWeights(weights: List<Float>): Boolean
```
Set the weights of all BlendShapes. 
#### Return
true  if the weights were successfully set,  false  if the number of weights does not match the number of BlendShapes. 
#### Parameters
weights 
A list of weights to set for all BlendShapes. 
```kotlin
fun setBlendShapeWeights(subsetName: String, weights: List<Float>): Boolean
```
Set the weights of a BlendShape subset by its name. 
#### Return
true  if the weights were successfully set,  false  if the number of weights does not match the number of BlendShapes in the subset. 
#### Parameters
subset Name 
The name of the BlendShape subset. 
weights 
A list of weights to set for the BlendShapes in the subset.