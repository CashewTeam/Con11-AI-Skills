# VolumeViewPointManager | PICO Spatial SDK

ui:platform / com.pico.spatial.ui.platform / VolumeViewPointManager 
# VolumeViewPointManager
```kotlin
interface VolumeViewPointManager
```
The interface of volume View Point. when you register a  VolumeViewPointListener  to the  VolumeViewPointManager , the  VolumeViewPointListener  will be called when the viewpoint of the container changes. 
#### See also
Local Volume View Point Manager Members 
## Properties
viewpoint 
```kotlin
abstract val viewpoint: State<ViewPoint>
```
The  State  of the current ViewPoint, default is  ViewPoint.Front . 
## Functions
add View Point Listener 
```kotlin
abstract fun addViewPointListener(listener: VolumeViewPointListener)
```
Add a  VolumeViewPointListener  to the  VolumeViewPointManager . 
remove View Point Listener 
```kotlin
abstract fun removeViewPointListener(listener: VolumeViewPointListener)
```
Remove a  VolumeViewPointListener  from the  VolumeViewPointManager .