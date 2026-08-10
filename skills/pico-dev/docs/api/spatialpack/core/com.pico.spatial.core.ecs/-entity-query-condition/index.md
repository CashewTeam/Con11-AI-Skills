# EntityQueryCondition | PICO Spatial SDK

core / com.pico.spatial.core.ecs / EntityQueryCondition 
# EntityQueryCondition
```kotlin
class EntityQueryCondition
```
Encapsulates conditions for querying entities. It allows checking whether an entity meets a specific condition through a condition function. 
Members 
## Types
Companion 
```kotlin
object Companion
```
The companion object of  EntityQueryCondition . 
## Functions
and 
```kotlin
fun and(other: EntityQueryCondition): EntityQueryCondition
```
Combines the current condition with another condition using logical  AND . 
not 
```kotlin
operator fun not(): EntityQueryCondition
```
Returns a new condition that represents the logical negation of the current condition. 
or 
```kotlin
fun or(other: EntityQueryCondition): EntityQueryCondition
```
Combines the current condition with another condition using logical  OR .