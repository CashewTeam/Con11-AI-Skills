# ModelEntity | PICO Spatial SDK

core / com.pico.spatial.core.ecs / ModelEntity / ModelEntity 
# ModelEntity
```kotlin
constructor(mesh: MeshResource, material: Material)
```
Creates a  ModelEntity  with a specified mesh and material. 
#### Parameters
mesh 
The  MeshResource  defining the model's shape. 
material 
The  Material  defining the model's surface appearance. 
```kotlin
constructor(mesh: MeshResource, materials: Array<Material>)
```
Creates a ModelEntity with a specified mesh and an array of materials. 
#### Parameters
mesh 
The  MeshResource  defining the model's shape. 
materials 
An array of  Material s defining the model's surface appearance.