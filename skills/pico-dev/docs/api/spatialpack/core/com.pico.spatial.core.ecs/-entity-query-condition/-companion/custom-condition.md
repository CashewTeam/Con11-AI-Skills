# customCondition | PICO Spatial SDK

core / com.pico.spatial.core.ecs / EntityQueryCondition / Companion / customCondition 
# customCondition
```kotlin
@JvmStatic
```fun  customCondition ( condition :  ( Entity )  ->  Boolean ) :  EntityQueryCondition 
Creates a custom condition defined by a lambda function. 
#### Return
An  EntityQueryCondition  that encapsulates the custom condition logic. 
#### Parameters
condition 
A lambda that evaluates the entity and returns  true  when it matches.