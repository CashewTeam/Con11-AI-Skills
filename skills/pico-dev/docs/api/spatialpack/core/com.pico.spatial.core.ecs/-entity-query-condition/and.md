# and | PICO Spatial SDK

core / com.pico.spatial.core.ecs / EntityQueryCondition / and 
# and
```kotlin
fun and(other: EntityQueryCondition): EntityQueryCondition
```
Combines the current condition with another condition using logical  AND . 
#### Return
A new  EntityQueryCondition  that represents the logical  AND  of the current and the other condition. 
#### Parameters
other 
The other condition to combine with.