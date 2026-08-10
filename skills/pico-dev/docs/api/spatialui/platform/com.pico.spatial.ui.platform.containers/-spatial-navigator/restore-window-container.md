# restoreWindowContainer | PICO Spatial SDK

ui:platform / com.pico.spatial.ui.platform.containers / SpatialNavigator / restoreWindowContainer 
# restoreWindowContainer
```kotlin
abstract fun restoreWindowContainer(id: String, tag: String? = null): Boolean
```
Restore a WindowContainer by  id  and optional  tag , can only be used when there is a stage open. 
#### Return
return true if succeed,else false. 
#### Parameters
id 
Id of window container that you want to close 
tag 
When tag is null, all the opened window container with the same  id  will be restored. When is set, only the window with the same id and tag will be restored. 
```kotlin
abstract fun restoreWindowContainer(): Boolean
```
Restore the current WindowContainer, can only be used when there is a stage open 
#### Return
return true if succeed,else false.