# playTimeline | PICO Spatial SDK

core / com.pico.spatial.core.ecs / Entity / playTimeline 
# playTimeline
```kotlin
@MainThread
```fun  playTimeline ( ) :  TimelinePlayerController 
Plays a preloaded Timeline using the current entity. 
Notes: A Timeline is a developer-configured sequence created and edited in the Editor. Its data is imported along with the model when the model is loaded (e.g., via  AssetBundle.load ). 
#### Return
The  TimelinePlayerController  responsible for managing playback of the Timeline.