# getBlendShapeWeights | PICO Spatial SDK

core / com.pico.spatial.core.ecs / BlendShapeControllerComponent / getBlendShapeWeights 
# getBlendShapeWeights
```kotlin
fun getBlendShapeWeights(): List<Float>
```
Get the weights of all BlendShapes. 
#### Return
A list of weights for all BlendShapes, or an empty list if no BlendShapes are available. 
```kotlin
fun getBlendShapeWeights(subsetName: String): List<Float>
```
Gets the weights of a BlendShape subset by its name. 
Returns an empty list if the subset does not exist. 
#### Return
A list of BlendShape weights in the subset; empty if none. 
#### Parameters
subset Name 
The subset name.