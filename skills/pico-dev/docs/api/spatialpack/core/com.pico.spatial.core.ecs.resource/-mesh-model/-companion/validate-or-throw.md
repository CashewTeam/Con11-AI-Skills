# validateOrThrow | PICO Spatial SDK

core / com.pico.spatial.core.ecs.resource / MeshModel / Companion / validateOrThrow 
# validateOrThrow
```kotlin
@JvmStatic
```fun  validateOrThrow ( meshModel :  MeshModel ) 
Validates that a  MeshModel  instance is structurally consistent before it is consumed. 
This method checks that: 
- 
MeshModel.positions  is not empty. 
- 
MeshModel.triangleIndices  is not empty and its size is a multiple of 3. 
- 
Every value in  MeshModel.triangleIndices  references a valid vertex in  MeshModel.positions . 
- 
Optional per-vertex attributes ( MeshModel.normals ,  MeshModel.tangents ,  MeshModel.uv0 ,  MeshModel.uv1 , and  MeshModel.colors ) match the vertex count when present. 
- 
Every channel in  MeshModel.colors  is finite and within the normalized range  [0, 1] . 
Performance note: this method iterates over  MeshModel.triangleIndices  (and optional attribute lists such as  MeshModel.colors ) to validate every element. For large meshes, this can be CPU-expensive. Prefer using it for Debug/development-time validation and diagnostics, and avoid calling it in Release builds. 
#### Parameters
mesh Model 
the mesh data to validate. 
#### Throws
Illegal Argument Exception 
if any of the above constraints is violated.