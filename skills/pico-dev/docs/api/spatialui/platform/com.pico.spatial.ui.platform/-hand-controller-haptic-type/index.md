# HandControllerHapticType | PICO Spatial SDK

ui:platform / com.pico.spatial.ui.platform / HandControllerHapticType 
# HandControllerHapticType
```kotlin
@Stable
```class  HandControllerHapticType ( level :  Int ,  frequency :  Int ,  duration :  Int ) 
hand controller haptic type, provide default haptic type 
- 
Press 
- 
Hover 
- 
Step 
- 
None 
Members 
## Constructors
Hand Controller Haptic Type 
```kotlin
constructor(level: Int, frequency: Int, duration: Int)
```
## Types
Companion 
```kotlin
object Companion
```
the companion object of HandControllerHapticType 
## Functions
coerce To Valid Range 
```kotlin
fun coerceToValidRange(): HandControllerHapticType
```
coerce haptic type to valid range 
copy 
```kotlin
fun copy(level: Int = this.level, frequency: Int = this.frequency, duration: Int = this.duration): HandControllerHapticType
```
copy haptic type 
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