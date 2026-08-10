# Companion | PICO Spatial SDK

core / com.pico.spatial.core.ecs / EntityQueryCondition / Companion 
# Companion
```kotlin
object Companion
```
The companion object of  EntityQueryCondition . 
Members 
## Functions
custom Condition 
```kotlin
@JvmStatic
```fun  customCondition ( condition :  ( Entity )  ->  Boolean ) :  EntityQueryCondition 
Creates a custom condition defined by a lambda function. 
has Component 
```kotlin
@JvmStatic
```fun  < T  :  Component >  hasComponent ( componentClass :  Class < T > ) :  EntityQueryCondition 
Creates a condition to check whether an entity has a component of the specified type.