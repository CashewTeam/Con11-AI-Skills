# repeatCount | PICO Spatial SDK

core / com.pico.spatial.core.ecs.animation / TweenAnimation / repeatCount 
# repeatCount
```kotlin
fun repeatCount(repeatCount: Int): TweenAnimation
```
Sets how many times the animation should repeat. 
#### Return
This  TweenAnimation  object, for method chaining. 
#### Parameters
repeat Count 
The repeat count. Use  INFINITE  to repeat indefinitely. A positive value specifies how many times to repeat after the initial run. For example, a value of  1  means the animation plays twice in total. The default value is  0 , meaning the animation runs only once with no repetition.