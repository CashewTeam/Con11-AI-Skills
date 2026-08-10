# SpatialActivityDelegate | PICO Spatial SDK

ui:platform / com.pico.spatial.ui.platform.stub.delegate / SpatialActivityDelegate 
# SpatialActivityDelegate
```kotlin
interface SpatialActivityDelegate
```
The  SpatialActivityDelegate  is responsible for providing the spatial content to the activity. 
Members 
## Types
Companion 
```kotlin
object Companion
```
companion object 
## Functions
set Spatial Content 
```kotlin
abstract fun setSpatialContent()
```
Set the spatial content to a custom activity. Like  Activity.setContentView , this method should be called at  Activity.onCreate . Be noticed that, when using a  SpatialActivityDelegate , you should not call  Activity.setContentView  or ComponentActivity.setContent anymore.