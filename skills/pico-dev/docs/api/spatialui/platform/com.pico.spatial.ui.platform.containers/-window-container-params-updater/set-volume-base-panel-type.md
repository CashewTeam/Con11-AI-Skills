# setVolumeBasePanelType | PICO Spatial SDK

ui:platform / com.pico.spatial.ui.platform.containers / WindowContainerParamsUpdater / setVolumeBasePanelType 
# setVolumeBasePanelType
```kotlin
abstract suspend fun setVolumeBasePanelType(volumeBasePanelType: VolumeBasePanelType): WindowContainerParamsUpdater.UpdateResult
```
Updates the visibility state of the volume base panel in the WindowContainer 
Note: This setting only takes effect when the WindowContainer's form is IN_VOLUME. 
#### Parameters
volume Base Panel Type 
New base panel show state to apply