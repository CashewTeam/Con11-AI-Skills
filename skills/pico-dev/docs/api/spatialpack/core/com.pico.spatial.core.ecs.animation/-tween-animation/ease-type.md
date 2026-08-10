# easeType | PICO Spatial SDK

core / com.pico.spatial.core.ecs.animation / TweenAnimation / easeType 
# easeType
```kotlin
fun easeType(easeType: EaseType): TweenAnimation
```
Sets the ease type of the animation. 
#### Return
This  TweenAnimation  object, for method chaining. 
#### Parameters
ease Type 
The ease type. The default value is  EaseType.LINEAR . 
```kotlin
var easeType: EaseType
```
The  EaseType  of the animation. This defines the rate of change of the animation over time, allowing for effects such as acceleration, deceleration, or linear motion. It affects the smoothness, style, and realism of the animation.