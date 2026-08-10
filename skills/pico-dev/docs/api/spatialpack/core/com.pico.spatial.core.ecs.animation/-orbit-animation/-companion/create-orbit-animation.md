# createOrbitAnimation | PICO Spatial SDK

core / com.pico.spatial.core.ecs.animation / OrbitAnimation / Companion / createOrbitAnimation 
# createOrbitAnimation
```kotlin
@JvmStatic
```fun  createOrbitAnimation ( name :  String  =  "" ,  duration :  Float  =  0.0f ,  axis :  Vector3  =  Vector3(0f, 1f, 0f) ,  startTransform :  Transform  =  Transform() ,  spinClockwise :  Boolean  =  true ,  orientToPath :  Boolean  =  false ,  rotationCount :  Float  =  0.0f ,  delay :  Float  =  0.0f ,  repeatMode :  RepeatMode  =  RepeatMode.RESTART ,  repeatCount :  Int  =  0 ,  offset :  Float  =  0.0f ,  speed :  Float  =  1.0f ,  trimStart :  Float ?  =  null ,  trimEnd :  Float ?  =  null ,  trimDuration :  Float ?  =  null ) :  OrbitAnimation 
Create an  OrbitAnimation  object with the specified parameters. 
#### Return
An  OrbitAnimation  object with the specified parameters. 
#### Parameters
name 
The name of the animation. 
duration 
The duration of the animation in seconds. 
axis 
The direction vector of the revolution axis (normalized internally). 
start Transform 
The object's initial transform (position / rotation / scale) at animation start. 
spin Clockwise 
Whether the orbit proceeds in a clockwise direction. 
orient To Path 
If true, the object's orientation continuously aligns to the tangent of its orbital path (i.e., faces direction of motion). 
rotation Count 
Number of full revolutions during the entire animation duration. 
delay 
The delay of the animation in seconds. 
repeat Mode 
The repeat mode of the animation. 
repeat Count 
How many times an animation is repeated. Use  INFINITE  to repeat indefinitely, or a non-negative integer. For example, a value of  1  means that the animation is repeated once after the initial playback ends, so the animation plays a total of two times. The default value is  0 , which means no repetition. 
offset 
The offset of the animation in seconds. 
speed 
The speed of the animation. 
trim Start 
The start time of the trimmed animation in seconds. 
trim End 
The end time of the trimmed animation in seconds. 
trim Duration 
The duration of the trimmed animation in seconds.