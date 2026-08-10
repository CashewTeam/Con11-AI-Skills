# ModelComponent | PICO Spatial SDK

core / com.pico.spatial.core.ecs / ModelComponent / ModelComponent 
# ModelComponent
```kotlin
constructor(mesh: MeshResource, material: Material)
```
Creates a  ModelComponent  with the specified mesh and material. 
#### Parameters
mesh 
The  MeshResource  defining the model's shape. 
material 
The  Material  defining the model's surface appearance. 
```kotlin
constructor(mesh: MeshResource, materials: Array<Material>)
```
Creates a  ModelComponent  with the specified mesh and an array of materials. 
#### Parameters
mesh 
The  MeshResource  defining the model's shape. 
materials 
An array of  Material  objects defining the model's surface appearance.