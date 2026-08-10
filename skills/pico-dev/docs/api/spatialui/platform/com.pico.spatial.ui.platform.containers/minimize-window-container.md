# minimizeWindowContainer | PICO Spatial SDK

ui:platform / com.pico.spatial.ui.platform.containers / minimizeWindowContainer 
# minimizeWindowContainer
```kotlin
fun Context.minimizeWindowContainer(id: String, tag: String? = null): Boolean
```
Minimize a WindowContainer by  id  and optional  tag , can only be used when there is a stage open. 
This method is open for android platform. And  SpatialNavigator.minimizeWindowContainer  is recommended to use in SpatialUI DSL. 
#### Return
return true if succeed,else false. 
#### Parameters
id 
Id of window container that you want to minimize 
tag 
When tag is null, all the opened window container with the same  id  will be minimize. When is set, only the window with the same id and tag will be minimize.