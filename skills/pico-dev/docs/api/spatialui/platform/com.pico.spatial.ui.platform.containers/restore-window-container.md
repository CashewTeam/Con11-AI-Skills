# restoreWindowContainer | PICO Spatial SDK

ui:platform / com.pico.spatial.ui.platform.containers / restoreWindowContainer 
# restoreWindowContainer
```kotlin
fun Context.restoreWindowContainer(id: String, tag: String? = null): Boolean
```
Restore a WindowContainer by  id  and optional  tag , can only be used when there is a stage open. 
This method is open for android platform. And  SpatialNavigator.restoreWindowContainer  is recommended to use in SpatialUI DSL. 
#### Return
return true if succeed,else false. 
#### Parameters
id 
Id of window container that you want to restore 
tag 
When tag is null, all the opened window container with the same  id  will be restore. When is set, only the window with the same id and tag will be restore.