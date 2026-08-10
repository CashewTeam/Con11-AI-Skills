# convertScaleTo | PICO Spatial SDK

core / com.pico.spatial.core.ecs / Entity / convertScaleTo 
# convertScaleTo
```kotlin
@MainThread
```fun  convertScaleTo ( scale :  Vector3 ,  targetEntity :  Entity ? ) :  Vector3 
Converts a scale relative to the current entity to a  targetEntity . 
Attention: "relative to" an Entity is different from "in the local coordinate system/space of" the Entity. In common, you may use the converted result to place an entity, when your target is get a scale "in the local coordinate system/space of" the entity. Here the proper targetEntity should be the parent of the entity. For example: Here we have two entities, entityA and entityB, which are in different coordinate spaces. And we have scaleA which is relative to entityA. Our target is to place entityB with scaleA. In this case, the proper targetEntity should be entityA's parent. 

```
entityB.components.get<TransformComponent>()?.scale = entityA.convertScaleTo(scaleA,entityB.getParent())
```
#### Return
The converted scale relative to target entity. 
#### Parameters
scale 
The scale relative to the current entity. 
target Entity 
The target entity to which the scale will be converted. If null, the scale will be converted relative to the  com.pico.spatial.core.container.SpatialContainer  where the current entity is placed in.