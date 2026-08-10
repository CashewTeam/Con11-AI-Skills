# DrawOrderGroup | PICO Spatial SDK

core / com.pico.spatial.core.ecs / DrawOrderGroup 
# DrawOrderGroup
```kotlin
@MainThread
```class  DrawOrderGroup 
The identifier that defines a specific draw order group for rendering management. 
This object represents a rendering boundary; components assigned to the same group are clustered together, allowing for fine-grained control over their sorting priority and visual layering relative to other groups. 
It is typically used within a  DrawOrderGroupComponent  to resolve depth-conflict issues between complex model and particle systems. 
Members 
## Types
Companion 
```kotlin
object Companion
```
The companion object of  DrawOrderGroup . 
## Functions
equals 
```kotlin
open operator override fun equals(other: Any?): Boolean
```hash Code 
```kotlin
open override fun hashCode(): Int
```is Valid 
```kotlin
fun isValid(): Boolean
```
Checks if the draw order group is valid. 
to String 
```kotlin
open override fun toString(): String
```