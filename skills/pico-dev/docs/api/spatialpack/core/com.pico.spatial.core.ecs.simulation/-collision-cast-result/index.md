# CollisionCastResult | PICO Spatial SDK

core / com.pico.spatial.core.ecs.simulation / CollisionCastResult 
# CollisionCastResult
```kotlin
class CollisionCastResult
```
A result of collision cast. 
Members 
## Properties
distance 
```kotlin
val distance: Float
```
The distance from the ray origin to the collision point, or the convex shape travel distance, or the cone projection distance. 
entity 
```kotlin
val entity: Entity
```
The entity that was hit. 
material Index 
```kotlin
val materialIndex: Int
```
The index of the sub-mesh that owns the hit triangle. This can be used to identify which material was hit from  ModelComponent.materials . When the hit collider is created from  ShapeResource.createStaticMesh , this value is a non-negative index. Otherwise, this value is  -1 . 
normal 
```kotlin
val normal: Vector3
```
The normal of the collision point in given space. 
position 
```kotlin
val position: Vector3
```
The position of the collision point in given space. 
shape Index 
```kotlin
val shapeIndex: Int
```
The index of the collision's shapeResource in the  CollisionComponent 's shapes array. 
uv0 
```kotlin
val uv0: Vector2
```
The UV coordinate of the hit point on the first UV channel (UV0). When the hit collider is created from  ShapeResource.createStaticMesh  and the underlying mesh contains a UV0 set, this value is the interpolated UV at the hit position. Otherwise, this value is  Vector2.ZERO . 
uv1 
```kotlin
val uv1: Vector2
```
The UV coordinate of the hit point on the second UV channel (UV1). When the hit collider is created from  ShapeResource.createStaticMesh  and the underlying mesh contains a secondary UV set (UV1), this value is the interpolated UV at the hit position. Otherwise, this value is  Vector2.ZERO . 
## Functions
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