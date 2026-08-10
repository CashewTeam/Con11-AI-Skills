# rayCast | PICO Spatial SDK

core / com.pico.spatial.core.ecs / Scene / rayCast 
# rayCast
```kotlin
@MainThread
```fun  rayCast ( origin :  Vector3 ,  direction :  Vector3 ,  length :  Float ,  hitMode :  CollisionCastHitMode ,  group :  CollisionGroup ,  referenceEntity :  Entity ?  =  null ) :  CollisionCastHitResults 
Projects a ray for collision detection against all geometry in the scene. 
#### Return
The results of the collision cast query. 
#### Parameters
origin 
The origin point of the ray relative to  referenceEntity . 
direction 
The direction vector of the ray relative to  referenceEntity . 
length 
The length of the ray relative to  referenceEntity . 
hit Mode 
The hit mode of collision cast. 
group 
The collision group to filter against. 
reference Entity 
The entity which defines the reference coordinate system. If null, uses the container's coordinate system.