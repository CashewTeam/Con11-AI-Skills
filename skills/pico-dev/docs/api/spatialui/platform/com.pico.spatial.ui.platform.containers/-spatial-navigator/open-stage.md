# openStage | PICO Spatial SDK

ui:platform / com.pico.spatial.ui.platform.containers / SpatialNavigator / openStage 
# openStage
```kotlin
abstract suspend fun openStage(id: String, style: StageStyle? = null, bundle: Bundle? = null, upperLimbRenderMode: UpperLimbRenderMode = UpperLimbRenderMode.Default): OpenStageResult
```
Open a Stage by id 
#### Return
The  OpenStageResult  that represents the openStage result. 
#### Parameters
id 
unique id of Stage 
style 
which  StageStyle  will be applied with this time for Stage, cannot be changed during stage alive 
bundle 
You can deliver customized data to Stage content through a bundle 
upper Limb Render Mode 
the upperLimbRenderMode of Stage