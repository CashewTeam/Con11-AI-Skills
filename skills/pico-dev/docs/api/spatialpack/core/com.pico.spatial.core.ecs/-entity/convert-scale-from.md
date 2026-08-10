# convertScaleFrom | PICO Spatial SDK

core / com.pico.spatial.core.ecs / Entity / convertScaleFrom 
# convertScaleFrom
```kotlin
@MainThread
```fun  convertScaleFrom ( scale :  Vector3 ,  baseEntity :  Entity ? ) :  Vector3 
Converts a scale relative to a  baseEntity  to the current entity. 
Attention: "relative to" an Entity is different from "in the local coordinate system/space of" the Entity. In common, you may use the converted result to place an entity, when your target is get a scale "in the local coordinate system/space of" the entity. Here the proper baseEntity should be the parent of the entity. For example: Here we have two entities, entityA and entityB, which are in different coordinate spaces. And we have scaleA which is relative to entityA. Our target is to place entityB with scaleA. In this case, the proper baseEntity should be entityA's parent. 

```
entityB.components.get<TransformComponent>()?.scale = entityA.convertScaleFrom(scaleA,entityA)
```
#### Return
The converted position relative to current entity. 
#### Parameters
scale 
The scale relative to  baseEntity . 
base Entity 
The base entity from which the position will be converted. If null, the scale will be converted relative to the  com.pico.spatial.core.container.SpatialContainer  where the current entity is placed in.