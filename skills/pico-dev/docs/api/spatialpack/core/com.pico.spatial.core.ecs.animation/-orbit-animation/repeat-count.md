# repeatCount | PICO Spatial SDK

core / com.pico.spatial.core.ecs.animation / OrbitAnimation / repeatCount 
# repeatCount
```kotlin
fun repeatCount(repeatCount: Int): OrbitAnimation
```
Set the repeat count of the animation. 
#### Return
This  OrbitAnimation  object to allow for method chaining. 
#### Parameters
repeat Count 
The repeat count. Use  INFINITE  to repeat indefinitely. A positive value specifies how many times to repeat after the initial run. For example, a value of  1  means the animation plays twice in total. The default value is  0 , meaning the animation runs only once with no repetition.