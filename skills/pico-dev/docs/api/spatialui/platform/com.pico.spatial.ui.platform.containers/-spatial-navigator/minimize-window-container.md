# minimizeWindowContainer | PICO Spatial SDK

ui:platform / com.pico.spatial.ui.platform.containers / SpatialNavigator / minimizeWindowContainer 
# minimizeWindowContainer
```kotlin
abstract fun minimizeWindowContainer(id: String, tag: String? = null): Boolean
```
Minimize a WindowContainer by  id  and optional  tag , can only be used when there is a stage open. 
#### Return
return true if succeed,else false. 
#### Parameters
id 
Id of window container that you want to close 
tag 
When tag is null, all the opened window container with the same  id  will be minimized. When is set, only the window with the same id and tag will be minimized. 
```kotlin
abstract fun minimizeWindowContainer(): Boolean
```
Minimize the current WindowContainer, can only be used when there is a stage open 
#### Return
return true if succeed,else false.