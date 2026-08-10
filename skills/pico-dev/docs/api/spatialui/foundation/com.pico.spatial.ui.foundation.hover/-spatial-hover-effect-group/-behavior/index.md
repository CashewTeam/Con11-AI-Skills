# Behavior | PICO Spatial SDK

ui:foundation / com.pico.spatial.ui.foundation.hover / SpatialHoverEffectGroup / Behavior 
# Behavior
```kotlin
@JvmInline
```value  class  Behavior ( mask :  Int ) 
Represents a view how to behave in a group. 
Each bit means: 
- 
0 Whether the group state changes will be triggered. 
- 
1 Whether the group state changes will be responded. Example: 
- 
0x00: Does not respond and does not trigger. (Only triggers itself) 
- 
0x01: Triggers but does not respond. 
- 
0x10: Responds but does not trigger. 
- 
0x11: Responds and triggers. 
Members 
## Constructors
Behavior 
```kotlin
constructor(mask: Int)
```
## Types
Companion 
```kotlin
object Companion
```
Holds behavior constants 
## Functions
or 
```kotlin
infix fun or(other: SpatialHoverEffectGroup.Behavior): SpatialHoverEffectGroup.Behavior
```
Bitwise operator to combine two  Behavior  instances. 
to String 
```kotlin
open override fun toString(): String
```