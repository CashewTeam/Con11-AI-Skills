# StageUpperLimbRenderModelManager | PICO Spatial SDK

ui:platform / com.pico.spatial.ui.platform / StageUpperLimbRenderModelManager 
# StageUpperLimbRenderModelManager
```kotlin
interface StageUpperLimbRenderModelManager
```
Manager for upper limb render model of stage. 
Members 
## Functions
add Upper Limb Render Mode Change Listener 
```kotlin
abstract fun addUpperLimbRenderModeChangeListener(listener: UpperLimbRenderModeChangeListener)
```
Add a listener to listen upper limb render mode change. 
remove Upper Limb Render Mode Change Listener 
```kotlin
abstract fun removeUpperLimbRenderModeChangeListener(listener: UpperLimbRenderModeChangeListener)
```
Remove a listener to stop listen upper limb render mode change. 
set Upper Limb Render Mode 
```kotlin
abstract fun setUpperLimbRenderMode(upperLimbRenderMode: UpperLimbRenderMode): StageParamsUpdater.UpdateResult
```
Set upper limb render mode of stage.