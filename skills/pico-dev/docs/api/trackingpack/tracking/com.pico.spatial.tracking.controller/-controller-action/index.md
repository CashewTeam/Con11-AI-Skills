# ControllerAction | PICO Spatial SDK

tracking / com.pico.spatial.tracking.controller / ControllerAction 
# ControllerAction
```kotlin
class ControllerAction
```
Snapshot of input actions for a single controller. 
Includes button pressed/touched states, analog values for trigger/grip, and the 2D thumbstick vector. All fields represent the current frame and may be identical to the previous frame; consumers should diff frames themselves if change detection is required. Value ranges:  triggerValue / gripValue  in 0.0, 1.0; thumbstick vector in -1.0, 1.0. 
Members 
## Constructors
Controller Action 
```kotlin
constructor(xButtonPressed: Boolean, xButtonTouched: Boolean, yButtonPressed: Boolean, yButtonTouched: Boolean, aButtonPressed: Boolean, aButtonTouched: Boolean, bButtonPressed: Boolean, bButtonTouched: Boolean, triggerPressed: Boolean, triggerTouched: Boolean, triggerValue: Float, gripPressed: Boolean, gripValue: Float, thumbstickPressed: Boolean, thumbstickTouched: Boolean, thumbstickValue: ThumbstickValue)
```
## Properties
a Button Pressed 
```kotlin
val aButtonPressed: Boolean
```
Whether the A button (on right controller) is pressed. 
a Button Touched 
```kotlin
val aButtonTouched: Boolean
```
Whether the A button (on right controller) is touched. 
b Button Pressed 
```kotlin
val bButtonPressed: Boolean
```
Whether the B button (on right controller) is pressed. 
b Button Touched 
```kotlin
val bButtonTouched: Boolean
```
Whether the B button (on right controller) is touched. 
grip Pressed 
```kotlin
val gripPressed: Boolean
```
Whether the grip is pressed. 
grip Value 
```kotlin
val gripValue: Float
```
Analog value of the grip in the range 0.0, 1.0. 
thumbstick Pressed 
```kotlin
val thumbstickPressed: Boolean
```
Whether the thumbstick is pressed. 
thumbstick Touched 
```kotlin
val thumbstickTouched: Boolean
```
Whether the thumbstick is touched. 
thumbstick Value 
```kotlin
val thumbstickValue: ThumbstickValue
```
2D thumbstick value; see  ThumbstickValue . Components are in -1.0, 1.0. 
trigger Pressed 
```kotlin
val triggerPressed: Boolean
```
Whether the trigger button is pressed. 
trigger Touched 
```kotlin
val triggerTouched: Boolean
```
Whether the trigger button is touched. 
trigger Value 
```kotlin
val triggerValue: Float
```
Analog value of the trigger in the range 0.0, 1.0. 
x Button Pressed 
```kotlin
val xButtonPressed: Boolean
```
Whether the X button (on left controller) is pressed. 
x Button Touched 
```kotlin
val xButtonTouched: Boolean
```
Whether the X button (on left controller) is touched. 
y Button Pressed 
```kotlin
val yButtonPressed: Boolean
```
Whether the Y button (on left controller) is pressed. 
y Button Touched 
```kotlin
val yButtonTouched: Boolean
```
Whether the Y button (on left controller) is touched. 
## Functions
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