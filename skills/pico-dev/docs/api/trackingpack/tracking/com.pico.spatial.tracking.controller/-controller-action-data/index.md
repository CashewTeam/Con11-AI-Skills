# ControllerActionData | PICO Spatial SDK

tracking / com.pico.spatial.tracking.controller / ControllerActionData 
# ControllerActionData
```kotlin
@RequiredFullSpace
```class  ControllerActionData 
Input actions for both left and right controllers. 
- 
left : states for the left controller (X/Y, Trigger, Grip, Thumbstick) 
- 
right : states for the right controller (A/B, Trigger, Grip, Thumbstick) 
Provides a single snapshot that bundles both controllers to simplify simultaneous handling. 
Members 
## Constructors
Controller Action Data 
```kotlin
constructor(left: ControllerAction, right: ControllerAction)
```
## Properties
left 
```kotlin
val left: ControllerAction
```
Actions of the left controller. 
right 
```kotlin
val right: ControllerAction
```
Actions of the right controller. 
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