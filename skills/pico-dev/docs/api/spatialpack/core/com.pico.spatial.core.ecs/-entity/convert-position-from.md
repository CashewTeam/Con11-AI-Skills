# convertPositionFrom | PICO Spatial SDK

core / com.pico.spatial.core.ecs / Entity / convertPositionFrom 
# convertPositionFrom
```kotlin
@MainThread
```fun  convertPositionFrom ( position :  Vector3 ,  baseEntity :  Entity ? ) :  Vector3 
Converts a position relative to a  baseEntity  to the current entity. 
Attention: "relative to" an Entity is different from "in the local coordinate system/space of" the Entity. In common, you may use the converted result to place an entity, when your target is get a position "in the local coordinate system/space of" the entity. Here the proper targetEntity should be the parent of the entity. For example: Here we have two entities, entityA and entityB, which are in different coordinate spaces. And we have positionA which is relative to entityA. Our target is to place entityB at positionA. In this case, the proper targetEntity should be entityA's parent. 

```
entityB.components.get<TransformComponent>()?.position = entityB.getParent()     ?.convertPositionFrom(positionA, entityA)
```
#### Return
The converted position relative to current entity. 
#### Parameters
position 
The position relative to  baseEntity . 
base Entity 
The base entity from which the position will be converted. If null, the position will be converted relative to the  com.pico.spatial.core.container.SpatialContainer  where the current entity is placed in.