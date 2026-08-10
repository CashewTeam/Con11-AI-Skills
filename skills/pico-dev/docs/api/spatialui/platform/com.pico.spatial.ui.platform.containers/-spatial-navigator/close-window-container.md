# closeWindowContainer | PICO Spatial SDK

ui:platform / com.pico.spatial.ui.platform.containers / SpatialNavigator / closeWindowContainer 
# closeWindowContainer
```kotlin
abstract fun closeWindowContainer(id: String, tag: String? = null)
```
Close a WindowContainer by  id  and optional  tag 
#### Parameters
id 
Id of window container that you want to close 
tag 
When tag is null, all the opened window container with the same  id  will be close. When is set, only the window with the same id and tag will be close. 
```kotlin
abstract fun closeWindowContainer()
```
Close the current WindowContainer