# openWindowContainer | PICO Spatial SDK

ui:platform / com.pico.spatial.ui.platform.containers / openWindowContainer 
# openWindowContainer
```kotlin
fun Context.openWindowContainer(id: String, tag: String? = null, bundle: Bundle? = null)
```
Open a WindowContainer by  id  and optional  tag 
This method is open for android platform. And  SpatialNavigator.openWindowContainer  is recommended to use in SpatialUI DSL. 
#### Parameters
id 
WindowContainer id 
tag 
When is null, a new window instance will always be created. when is not null, if an opened window container has the same id and tag, then this window container instance will be reused. when you deliver a new tag, a new window instance will always be created. 
bundle 
You can deliver customized data to window container content through a bundle