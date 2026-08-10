# ModelComponent | PICO Spatial SDK

core / com.pico.spatial.core.ecs / ModelComponent 
# ModelComponent
```kotlin
@MainThread
```class  ModelComponent  :  Component 
A  Component  that renders 3D models. 
ModelComponent  is part of the Entity-Component-System (ECS) architecture and defines an entity's visual appearance using a mesh and materials. 
Notes: 
- 
A Mesh is a collection of vertices, edges, and faces that define the shape of a 3D object. 
- 
Materials define the appearance of the surface of a mesh. They include properties like color and textures. 
Members 
## Constructors
Model Component 
```kotlin
constructor(mesh: MeshResource, material: Material)
```
Creates a  ModelComponent  with the specified mesh and material. 
```kotlin
constructor(mesh: MeshResource, materials: Array<Material>)
```
Creates a  ModelComponent  with the specified mesh and an array of materials. 
## Types
Material Array 
```kotlin
class MaterialArray : Iterable<Material>
```
A dynamic array of  Material  instances for a  ModelComponent . 
## Properties
is Visible 
```kotlin
var isVisible: Boolean
```
Controls whether this model component is rendered. 
materials 
```kotlin
val materials: ModelComponent.MaterialArray
```
The materials used by the model. 
mesh 
```kotlin
var mesh: MeshResource
```
The  MeshResource  instance of the model. 
mesh Instances 
```kotlin
var meshInstances: MeshInstancesResource?
```
The  MeshInstancesResource  instance of the model. The default value is  null . 
## Functions
clone 
```kotlin
open override fun clone(): Component
```
Creates and returns a copy of this  Component  instance. 
equals 
```kotlin
open operator override fun equals(other: Any?): Boolean
```hash Code 
```kotlin
open override fun hashCode(): Int
```to String 
```kotlin
open override fun toString(): String
```