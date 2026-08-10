# SpatialHoverEffectGroup | PICO Spatial SDK

ui:foundation / com.pico.spatial.ui.foundation.hover / SpatialHoverEffectGroup 
# SpatialHoverEffectGroup
```kotlin
class SpatialHoverEffectGroup
```
Represents a group for managing spatial hover effects. Each instance has a unique group ID for identifying the group. 
Use  obtain  to create new instances with incrementing IDs. 
Members 
## Types
Behavior 
```kotlin
@JvmInline
```value  class  Behavior ( mask :  Int ) 
Represents a view how to behave in a group. 
Companion 
```kotlin
object Companion
```
Companion object that provides factory methods for  SpatialHoverEffectGroup . 
## Functions
behavior 
```kotlin
fun behavior(behavior: SpatialHoverEffectGroup.Behavior): SpatialHoverEffectGroup
```
Sets the behavior of the spatial hover effect group. 
equals 
```kotlin
open operator override fun equals(other: Any?): Boolean
```hash Code 
```kotlin
open override fun hashCode(): Int
```to String 
```kotlin
open override fun toString(): String
```