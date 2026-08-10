# Companion | PICO Spatial SDK

ui:foundation / com.pico.spatial.ui.foundation.hover / SpatialHoverEffectGroup / Behavior / Companion 
# Companion
```kotlin
object Companion
```
Holds behavior constants 
Members 
## Properties
Responder 
```kotlin
@JvmStatic
```val  Responder :  SpatialHoverEffectGroup.Behavior 
The view will response to group state change. 
Standalone 
```kotlin
@JvmStatic
```val  Standalone :  SpatialHoverEffectGroup.Behavior 
This behavior just like outside of group, only activate when self is hovered. 
Trigger 
```kotlin
@JvmStatic
```val  Trigger :  SpatialHoverEffectGroup.Behavior 
Change the view state will also trigger group state change. 
Trigger And Responder 
```kotlin
@JvmStatic
```val  TriggerAndResponder :  SpatialHoverEffectGroup.Behavior 
Change the view state will also trigger group state change, and the view will response to group state change.