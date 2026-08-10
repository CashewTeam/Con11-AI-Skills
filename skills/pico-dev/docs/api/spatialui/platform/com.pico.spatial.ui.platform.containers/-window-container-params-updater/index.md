# WindowContainerParamsUpdater | PICO Spatial SDK

ui:platform / com.pico.spatial.ui.platform.containers / WindowContainerParamsUpdater 
# WindowContainerParamsUpdater
```kotlin
interface WindowContainerParamsUpdater
```
Provides functionality to update and retrieve the mutable parameters of a WindowContainer 
Important restriction : The methods in this interface should only be called by WindowContainer type containers. If called on non-WindowContainer containers (e.g. Stage), these methods will throw an  IllegalStateException  with detailed error information. 
Members 
## Types
Update Result 
```kotlin
sealed class UpdateResult
```
Represents the result of an update operation on WindowContainer parameters. 
## Functions
set Caption Bar Type 
```kotlin
abstract suspend fun setCaptionBarType(captionBarType: CaptionBarType): WindowContainerParamsUpdater.UpdateResult
```
Updates the auto-hide behavior of the caption bar in the WindowContainer 
set Resize Restriction 
```kotlin
abstract suspend fun setResizeRestriction(resizeRestriction: ContainerResizeRestriction): WindowContainerParamsUpdater.UpdateResult
```
Updates the resize restriction of the associated WindowContainer 
set Volume Base Panel Type 
```kotlin
abstract suspend fun setVolumeBasePanelType(volumeBasePanelType: VolumeBasePanelType): WindowContainerParamsUpdater.UpdateResult
```
Updates the visibility state of the volume base panel in the WindowContainer