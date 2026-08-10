# closeWindowContainer | PICO Spatial SDK

ui:platform / com.pico.spatial.ui.platform.containers / closeWindowContainer 
# closeWindowContainer
```kotlin
fun Context.closeWindowContainer(id: String, tag: String? = null)
```
Close a WindowContainer by  id  and optional  tag . 
This method is open for android platform. And  SpatialNavigator.closeWindowContainer  is recommended to use in SpatialUI DSL. 
#### Parameters
id 
Id of window container that you want to close 
tag 
When tag is null, all the opened window container with the same  id  will be close. When is set, only the window with the same id and tag will be close.