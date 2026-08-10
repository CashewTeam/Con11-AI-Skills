# or | PICO Spatial SDK

core / com.pico.spatial.core.ecs / EntityQueryCondition / or 
# or
```kotlin
fun or(other: EntityQueryCondition): EntityQueryCondition
```
Combines the current condition with another condition using logical  OR . 
#### Return
A new  EntityQueryCondition  that represents the logical  OR  of the current and the other condition. 
#### Parameters
other 
The other condition to combine with.