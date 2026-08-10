# SpatialAppScope | PICO Spatial SDK

ui:foundation / com.pico.spatial.ui.foundation.dsl / SpatialAppScope 
# SpatialAppScope
```kotlin
interface SpatialAppScope
```
A interface which be used to attach PICO OS concept. ONLY could be touched by developers at app entry point 
Members Members & Extensions 
## Properties
context 
```kotlin
abstract val context: Context
```
The context of the app 
density 
```kotlin
abstract val density: Density
```
A density of the screen 
## Functions
Default Stage 
```kotlin
fun SpatialAppScope.DefaultStage(content: @Composable StageScope.() -> Unit)
```
The first  Stage  of app, started by PICO OS. Currently must be configured at app's AndroidManifest.xml 
Default Window Container 
```kotlin
fun SpatialAppScope.DefaultWindowContainer(content: @Composable WindowContainerScope.() -> Unit)
```
The first  WindowContainer  of app, started by PICO OS. Currently must be configured at app's AndroidManifest.xml 
Stage 
```kotlin
fun SpatialAppScope.Stage(id: String, immersion: Immersion? = null, brightness: Brightness? = null, upperLimbRenderMode: UpperLimbRenderMode? = null, targetActivity: Class<out ComponentActivity>? = null, content: @Composable StageScope.() -> Unit)
```
Declare a Stage with unique  id . the  id  is used to executes open/close operation 
Window Container 
```kotlin
fun SpatialAppScope.WindowContainer(id: String, form: Form? = null, properties: ContainerProperties.() -> Unit = {}, content: @Composable WindowContainerScope.() -> Unit)
```
```kotlin
fun SpatialAppScope.WindowContainer(id: String, form: Form? = null, defaultSize: WindowContainerSize? = null, resizeType: ContainerResizeType? = null, defaultResizeRestriction: ContainerResizeRestriction? = null, enableMaterialBackground: Boolean? = null, volumeAlignment: VolumeAlignment? = null, defaultVolumeBasePanelType: VolumeBasePanelType? = null, defaultCaptionBarType: CaptionBarType? = null, placement: PlacementContext.() -> Placement? = null, targetActivity: Class<out ComponentActivity>? = null, worldScale: WorldScale? = null, content: @Composable WindowContainerScope.() -> Unit)
```
Declare a WindowContainer with unique  id . the  id  is used to open/close the WindowContainer.