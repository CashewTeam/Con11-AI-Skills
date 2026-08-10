# convertRotationTo | PICO Spatial SDK

core / com.pico.spatial.core.ecs / Entity / convertRotationTo 
# convertRotationTo
```kotlin
@MainThread
```fun  convertRotationTo ( rotation :  Quat ,  targetEntity :  Entity ? ) :  Quat 
Converts a rotation relative to the current entity to a  targetEntity . 
Attention: "relative to" an Entity is different from "in the local coordinate system/space of" the Entity. In common, you may use the converted result to place an entity, when your target is get a position "in the local coordinate system/space of" the entity. Here the proper targetEntity should be the parent of the entity. For example: Here we have two entities, entityA and entityB, which are in different coordinate spaces. And we have rotationA which is relative to entityA. Our target is to place entityB with rotationA. In this case, the proper targetEntity should be entityA's parent. 

```
entityB.components.get<TransformComponent>()?.quaternion = entityA.convertRotationTo(rotationA,entityB.getParent())
```
#### Return
The converted rotation relative to target entity. 
#### Parameters
rotation 
The rotation relative to the current entity. 
target Entity 
The target entity to which the rotation will be converted. If null, the rotation will be converted relative to the  com.pico.spatial.core.container.SpatialContainer  where the current entity is placed in.