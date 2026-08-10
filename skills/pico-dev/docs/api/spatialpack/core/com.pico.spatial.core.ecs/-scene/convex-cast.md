# convexCast | PICO Spatial SDK

core / com.pico.spatial.core.ecs / Scene / convexCast 
# convexCast
```kotlin
@MainThread
```fun  convexCast ( shape :  ShapeResource ,  origin :  Vector3 ,  orientation :  Quat ,  direction :  Vector3 ,  length :  Float ,  hitMode :  CollisionCastHitMode ,  group :  CollisionGroup ,  referenceEntity :  Entity ?  =  null ) :  CollisionCastHitResults 
Projects a convex shape for collision detection against all geometry in the scene. 
#### Return
The results of the collision cast query. 
#### Parameters
shape 
The shape resource to cast. 
origin 
The origin point of the shape relative to  referenceEntity . 
orientation 
The orientation quaternion of the shape relative to  referenceEntity . 
direction 
The direction vector of the shape relative to  referenceEntity . 
length 
The length of the shape relative to  referenceEntity . 
hit Mode 
The hit mode of collision cast. 
group 
The collision group to filter against. 
reference Entity 
The entity which defines the reference coordinate system. If null, uses the container's coordinate system.