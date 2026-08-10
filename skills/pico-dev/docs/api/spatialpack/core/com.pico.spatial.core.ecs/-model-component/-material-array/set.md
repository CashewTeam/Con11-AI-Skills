# set | PICO Spatial SDK

core / com.pico.spatial.core.ecs / ModelComponent / MaterialArray / set 
# set
```kotlin
operator fun set(index: Int, material: Material)
```
Sets the material at the specified index for this component. 
The index corresponds to a specific material applied to a part of the mesh. For example, a car model might have different materials for the body, windows, and tires. 
#### Parameters
index 
The position in the material array. 
material 
The  Material  to assign at the specified index. 
#### Throws
Index Out Of Bounds Exception 
If  index  is outside the bounds of the array.