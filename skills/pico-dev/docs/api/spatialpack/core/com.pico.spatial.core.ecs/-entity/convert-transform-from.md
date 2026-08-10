# convertTransformFrom | PICO Spatial SDK

core / com.pico.spatial.core.ecs / Entity / convertTransformFrom 
# convertTransformFrom
```kotlin
@MainThread
```fun  convertTransformFrom ( transform :  Transform ,  baseEntity :  Entity ? ) :  Transform 
Converts a  Transform  relative to a  baseEntity  to the current entity. 
Attention: "relative to" an Entity is different from "in the local coordinate system/space of" the Entity. In common, you may use the converted result to place an entity, when your target is get a position "in the local coordinate system/space of" the entity. Here the proper baseEntity should be the parent of the entity. For example: Here we have two entities, entityA and entityB, which are in different coordinate spaces. And we have transformA which is relative to entityA. Our target is to place entityB with transformA. In this case, the proper baseEntity should be entityA's parent. 

```
entityB.components.set(TransformComponent(entityB.getParent()     !!.convertTransformFrom(transformA.position, entityA)))
```
#### Return
The converted  Transform  relative to current entity. 
#### Parameters
transform 
The  Transform  relative to  baseEntity . 
base Entity 
The base entity from which the  Transform  will be converted. If null, the  Transform  will be converted relative to the  com.pico.spatial.core.container.SpatialContainer  where the current entity is placed in.