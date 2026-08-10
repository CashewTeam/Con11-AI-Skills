# ModelEntity | PICO Spatial SDK

core / com.pico.spatial.core.ecs / ModelEntity 
# ModelEntity
```kotlin
class ModelEntity : Entity
```
A class for rendering a model with specified mesh and materials. 
Members 
## Constructors
Model Entity 
```kotlin
constructor(mesh: MeshResource, material: Material)
```
Creates a  ModelEntity  with a specified mesh and material. 
```kotlin
constructor(mesh: MeshResource, materials: Array<Material>)
```
Creates a ModelEntity with a specified mesh and an array of materials.