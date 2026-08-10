# Companion | PICO Spatial SDK

core / com.pico.spatial.core.ecs.animation / OrbitAnimation / Companion 
# Companion
```kotlin
object Companion
```
The companion of  OrbitAnimation . 
Members 
## Functions
create Orbit Animation 
```kotlin
@JvmStatic
```fun  createOrbitAnimation ( name :  String  =  "" ,  duration :  Float  =  0.0f ,  axis :  Vector3  =  Vector3(0f, 1f, 0f) ,  startTransform :  Transform  =  Transform() ,  spinClockwise :  Boolean  =  true ,  orientToPath :  Boolean  =  false ,  rotationCount :  Float  =  0.0f ,  delay :  Float  =  0.0f ,  repeatMode :  RepeatMode  =  RepeatMode.RESTART ,  repeatCount :  Int  =  0 ,  offset :  Float  =  0.0f ,  speed :  Float  =  1.0f ,  trimStart :  Float ?  =  null ,  trimEnd :  Float ?  =  null ,  trimDuration :  Float ?  =  null ) :  OrbitAnimation 
Create an  OrbitAnimation  object with the specified parameters.