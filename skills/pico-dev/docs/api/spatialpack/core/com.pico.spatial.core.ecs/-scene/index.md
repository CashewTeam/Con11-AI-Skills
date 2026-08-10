# Scene | PICO Spatial SDK

core / com.pico.spatial.core.ecs / Scene 
# Scene
```kotlin
class Scene : EventSource
```
Represents a scene. 
A scene manages a collection of  Entity  objects. Typically, a  com.pico.spatial.core.container.SpatialContainer  hosts a scene, and all 3D entities created within the container belong to that scene. 
Members 
## Functions
convex Cast 
```kotlin
@MainThread
```fun  convexCast ( shape :  ShapeResource ,  origin :  Vector3 ,  orientation :  Quat ,  direction :  Vector3 ,  length :  Float ,  hitMode :  CollisionCastHitMode ,  group :  CollisionGroup ,  referenceEntity :  Entity ?  =  null ) :  CollisionCastHitResults 
Projects a convex shape for collision detection against all geometry in the scene. 
equals 
```kotlin
open operator override fun equals(other: Any?): Boolean
```hash Code 
```kotlin
open override fun hashCode(): Int
```query Entity 
```kotlin
@MainThread
```fun  queryEntity ( vararg  conditions :  EntityQueryCondition ) :  List < Entity > 
Queries a list of entities based on one or more conditions. 
ray Cast 
```kotlin
@MainThread
```fun  rayCast ( origin :  Vector3 ,  direction :  Vector3 ,  length :  Float ,  hitMode :  CollisionCastHitMode ,  group :  CollisionGroup ,  referenceEntity :  Entity ?  =  null ) :  CollisionCastHitResults 
Projects a ray for collision detection against all geometry in the scene. 
subscribe 
```kotlin
@MainThread
```fun  < T  :  Event >  subscribe ( eventType :  Class < T > ,  on :  EventSource ?  =  null ,  componentType :  Class < out  Component > ?  =  null ,  subscriber :  EventSubscriber < T > ) :  Cancellable 
Subscribes to an event of the specified type. 
to String 
```kotlin
open override fun toString(): String
```