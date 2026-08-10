# AnimationPlaybackController | PICO Spatial SDK

core / com.pico.spatial.core.ecs.animation / AnimationPlaybackController 
# AnimationPlaybackController
```kotlin
@MainThread
```class  AnimationPlaybackController  :  Closeable 
A controller that manages animation playback. 
Members 
## Properties
entity 
```kotlin
val entity: Entity?
```
The entity that the animation is playing on. 
valid 
```kotlin
@get:JvmName(name = "isValid")
```val  valid :  Boolean 
The controller is valid. 
## Functions
close 
```kotlin
open override fun close()
```
Closes the controller and releases resources. 
get Duration 
```kotlin
fun getDuration(): Float
```
Gets the duration of the animation. 
get Speed 
```kotlin
fun getSpeed(): Float
```
Gets the current playback speed of the animation. 
get Time 
```kotlin
fun getTime(): Float
```
Gets the time the animation is currently at. 
is Complete 
```kotlin
fun isComplete(): Boolean
```
Returns whether the animation has completed. 
is Paused 
```kotlin
fun isPaused(): Boolean
```
Returns whether the animation is paused. 
is Playing 
```kotlin
fun isPlaying(): Boolean
```
Returns whether the animation is playing. 
is Stopped 
```kotlin
fun isStopped(): Boolean
```
Returns whether the animation is currently stopped. 
pause 
```kotlin
fun pause()
```
Pauses the animation. 
resume 
```kotlin
fun resume()
```
Resumes a paused animation. 
set Speed 
```kotlin
fun setSpeed(speed: Float)
```
Sets the playback speed. 
set Time 
```kotlin
fun setTime(time: Float)
```
Sets the current playback time. 
stop 
```kotlin
fun stop()
```
Stops an animation.