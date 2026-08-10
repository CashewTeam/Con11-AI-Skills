# openWindowContainer | PICO Spatial SDK

ui:platform / com.pico.spatial.ui.platform.containers / SpatialNavigator / openWindowContainer 
# openWindowContainer
```kotlin
abstract fun openWindowContainer(id: String, tag: String? = null, bundle: Bundle? = null)
```
Open a WindowContainer by  id  and optional  tag 
#### Parameters
id 
WindowContainer id 
tag 
When is null, a new window instance will always be created. when is not null, if an opened window container has the same id and tag, then this window container instance will be reused. when you deliver a new tag, a new window instance will always be created. 
bundle 
You can deliver customized data to window container content through a bundle