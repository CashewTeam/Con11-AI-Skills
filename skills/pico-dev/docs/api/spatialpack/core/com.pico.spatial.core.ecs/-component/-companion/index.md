# Companion | PICO Spatial SDK

core / com.pico.spatial.core.ecs / Component / Companion 
# Companion
```kotlin
object Companion
```
The companion object of  Component . 
Members 
## Functions
is Cloneable 
```kotlin
@JvmStatic
```fun  isCloneable ( componentClass :  Class < out  Component > ) :  Boolean 
Checks if the component class is cloneable. 
register 
```kotlin
@JvmStatic
```fun  register ( clazz :  Class < out  Component > ) 
Registers a custom component class. 
unregister 
```kotlin
@JvmStatic
```fun  unregister ( clazz :  Class < out  Component > ) 
Unregisters a previously registered custom component class.