# ControllerHapticConfiguration | PICO Spatial SDK

ui:platform / com.pico.spatial.ui.platform / ControllerHapticConfiguration 
# ControllerHapticConfiguration
```kotlin
@Stable
```class  ControllerHapticConfiguration ( val  hover :  HandControllerHapticType  =  HandControllerHapticType.Hover ,  val  press :  HandControllerHapticType  =  HandControllerHapticType.Press ,  val  step :  HandControllerHapticType  =  HandControllerHapticType.Step ,  val  none :  HandControllerHapticType  =  HandControllerHapticType.None ) 
hand controller haptic configuration, provide 
- 
Hover 
- 
Press 
- 
Step 
- 
None 
Members 
## Constructors
Controller Haptic Configuration 
```kotlin
constructor(hover: HandControllerHapticType = HandControllerHapticType.Hover, press: HandControllerHapticType = HandControllerHapticType.Press, step: HandControllerHapticType = HandControllerHapticType.Step, none: HandControllerHapticType = HandControllerHapticType.None)
```
## Types
Companion 
```kotlin
object Companion
```
the companion object of ControllerHapticConfiguration 
## Properties
hover 
```kotlin
val hover: HandControllerHapticType
```
hover haptic type in configuration 
none 
```kotlin
val none: HandControllerHapticType
```
none haptic type in configuration 
press 
```kotlin
val press: HandControllerHapticType
```
press haptic type in configuration 
step 
```kotlin
val step: HandControllerHapticType
```
step haptic type in configuration 
## Functions
copy 
```kotlin
fun copy(hover: HandControllerHapticType = this.hover, press: HandControllerHapticType = this.press, step: HandControllerHapticType = this.step, none: HandControllerHapticType = this.none): ControllerHapticConfiguration
```
copy hand controller haptic configuration with new values 
equals 
```kotlin
open operator override fun equals(other: Any?): Boolean
```
override equals function 
hash Code 
```kotlin
open override fun hashCode(): Int
```
override hashCode function