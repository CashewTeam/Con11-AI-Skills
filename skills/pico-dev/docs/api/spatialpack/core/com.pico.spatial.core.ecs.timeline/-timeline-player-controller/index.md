# TimelinePlayerController | PICO Spatial SDK

core / com.pico.spatial.core.ecs.timeline / TimelinePlayerController 
# TimelinePlayerController
```kotlin
@MainThread
```class  TimelinePlayerController  :  Closeable 
A controller that manages timeline playback. 
Members 
## Properties
entity 
```kotlin
val entity: Entity?
```
The entity that the timeline player is playing on. 
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
Closes the current controller. 
get Duration 
```kotlin
fun getDuration(): Float
```
Gets the duration of the timeline. 
is Complete 
```kotlin
fun isComplete(): Boolean
```
Returns whether the timeline has completed. 
is Paused 
```kotlin
fun isPaused(): Boolean
```
Returns whether the timeline is paused. 
is Playing 
```kotlin
fun isPlaying(): Boolean
```
Returns whether the timeline is playing. 
is Stopped 
```kotlin
fun isStopped(): Boolean
```
Returns whether the timeline is stopped. 
pause 
```kotlin
fun pause()
```
Pauses the timeline. 
play 
```kotlin
fun play()
```
Plays the timeline. 
resume 
```kotlin
fun resume()
```
Resumes the timeline. 
stop 
```kotlin
fun stop()
```
Stops the timeline.