# createBlendShapeSubsetByIndices | PICO Spatial SDK

core / com.pico.spatial.core.ecs / BlendShapeControllerComponent / createBlendShapeSubsetByIndices 
# createBlendShapeSubsetByIndices
```kotlin
fun createBlendShapeSubsetByIndices(subsetName: String, indices: List<Int>): Boolean
```
Create a BlendShape subset by indices. 
#### Return
true  if the subset was successfully created,  false  if the indices are invalid. 
#### Parameters
subset Name 
The name of the BlendShape subset to create. 
indices 
A list of indices of BlendShapes to include in the subset.