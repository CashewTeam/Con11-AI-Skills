# Companion | PICO Spatial SDK

core / com.pico.spatial.core.ecs / System / Companion 
# Companion
```kotlin
object Companion
```
The companion object of  System . 
Members 
## Functions
register 
```kotlin
@JvmStatic
```fun  register ( clazz :  Class < out  System > ) 
Registers a custom  System  with the ECS. 
unregister 
```kotlin
@JvmStatic
```fun  unregister ( clazz :  Class < out  System > ) 
Unregisters a custom  System  from the ECS.