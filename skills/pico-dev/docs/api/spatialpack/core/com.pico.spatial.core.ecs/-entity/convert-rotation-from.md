# convertRotationFrom | PICO Spatial SDK

core / com.pico.spatial.core.ecs / Entity / convertRotationFrom 
# convertRotationFrom
```kotlin
@MainThread
```fun  convertRotationFrom ( rotation :  Quat ,  baseEntity :  Entity ? ) :  Quat 
Converts a rotation relative to a  baseEntity  to the current entity. 
Attention: "relative to" an Entity is different from "in the local coordinate system/space of" the Entity. In common, you may use the converted result to place an entity, when your target is get a position "in the local coordinate system/space of" the entity. Here the proper targetEntity should be the parent of the entity. For example: Here we have two entities, entityA and entityB, which are in different coordinate spaces. And we have rotationA which is relative to entityA. Our target is to place entityB with rotationA. In this case, the proper targetEntity should be entityA's parent. 

```
entityB.components.get<TransformComponent>()?.quaternion = entityB.getParent()     ?.convertRotationTo(rotationA, entityA)
```
#### Return
The converted rotation relative to current entity. 
#### Parameters
rotation 
The rotation relative to  baseEntity . 
base Entity 
The base entity from which the rotation will be converted. If null, the rotation will be converted relative to the  com.pico.spatial.core.container.SpatialContainer  where the current entity is placed in.