# createBlendShapeSubsetByNames | PICO Spatial SDK

core / com.pico.spatial.core.ecs / BlendShapeControllerComponent / createBlendShapeSubsetByNames 
# createBlendShapeSubsetByNames
```kotlin
fun createBlendShapeSubsetByNames(subsetName: String, blendShapeNames: List<String>): Boolean
```
Create a BlendShape subset by names. 
#### Return
true  if the subset was successfully created,  false  if the names are invalid. 
#### Parameters
subset Name 
The name of the BlendShape subset to create. 
blend Shape Names 
A list of names of BlendShapes to include in the subset.