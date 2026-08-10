# setResizeRestriction | PICO Spatial SDK

ui:platform / com.pico.spatial.ui.platform.containers / WindowContainerParamsUpdater / setResizeRestriction 
# setResizeRestriction
```kotlin
abstract suspend fun setResizeRestriction(resizeRestriction: ContainerResizeRestriction): WindowContainerParamsUpdater.UpdateResult
```
Updates the resize restriction of the associated WindowContainer 
Note: This setting only takes effect when the WindowContainer's form is ON_PLAIN. 
#### Parameters
resize Restriction 
New resize restriction to apply