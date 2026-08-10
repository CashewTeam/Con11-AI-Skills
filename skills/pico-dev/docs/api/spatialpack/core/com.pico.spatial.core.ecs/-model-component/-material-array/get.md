# get | PICO Spatial SDK

core / com.pico.spatial.core.ecs / ModelComponent / MaterialArray / get 
# get
```kotlin
operator fun get(index: Int): Material
```
Gets the material at the specified index from this component. 
The index corresponds to a specific material applied to a part of the mesh. For example, a car model might have different materials for the body, windows, and tires. 
#### Return
The  Material  at the specified index. 
#### Parameters
index 
The position in the material array. A single mesh can have multiple materials applied to different parts. 
#### Throws
Index Out Of Bounds Exception 
If  index  is outside the bounds of the array. 
Resource Loading Exception 
If the material resource obtained from the component is invalid.