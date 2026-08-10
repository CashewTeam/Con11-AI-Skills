# com.pico.spatial.ui.foundation.dsl | PICO Spatial SDK

ui:foundation / com.pico.spatial.ui.foundation.dsl 
# Package-level declarations
Types Functions 
## Types
Brightness 
```kotlin
@Stable
```sealed  class  Brightness 
Presents  Stage 's brightness 
Container Properties 
```kotlin
interface ContainerProperties
```
Interface that defines the properties of a  WindowContainer . 
Container Proxy 
```kotlin
class ContainerProxy
```
ContainerProxy  is used to describe a window container instance. 
Form 
```kotlin
enum Form : Enum<Form>
```
Form of  WindowContainer . 
Immersion 
```kotlin
class Immersion
```
The range of  Stage 's immersion 
Placement 
```kotlin
class Placement
```
Placement  is used to describe the original position of a window container relative to  anchorContainer  when a new window container is created. 
Placement Context 
```kotlin
interface PlacementContext
```
PlacementContext  holds necessary information for window container placement. 
Spatial App Scope 
```kotlin
interface SpatialAppScope
```
A interface which be used to attach PICO OS concept. ONLY could be touched by developers at app entry point 
Volume Alignment 
```kotlin
enum VolumeAlignment : Enum<VolumeAlignment>
```
Represents how a  WindowContainer  of form  Form.Volumetric  will align. 
Window Container Size 
```kotlin
class WindowContainerSize
```
The size of the  WindowContainer . support both  Dp  and  LengthUnit . 
World Scale 
```kotlin
enum WorldScale : Enum<WorldScale>
```
The way how a  WindowContainer  will be scaled in the world. Available options include: 
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
Immersion 
```kotlin
fun Immersion(@IntRange(from = 0, to = 100) default: Int, @IntRange(from = 0, to = 100) min: Int = 0, @IntRange(from = 0, to = 100) max: Int = 100): Immersion
```
The range of  Stage 's immersion 
launch 
```kotlin
fun Application.launch(block: SpatialAppScope.() -> Unit)
```
Extension function for android platform, use  Application  as receiver to start a spatial app context so we can create dsl like this 
register Component 
```kotlin
inline fun <T : Component> registerComponent()
```
Register custom  Component  type. 
register System 
```kotlin
inline fun <T : System> registerSystem()
```
Extensions for  System  to easily register new system type 
Stage 
```kotlin
fun SpatialAppScope.Stage(id: String, immersion: Immersion? = null, brightness: Brightness? = null, upperLimbRenderMode: UpperLimbRenderMode? = null, targetActivity: Class<out ComponentActivity>? = null, content: @Composable StageScope.() -> Unit)
```
Declare a Stage with unique  id . the  id  is used to executes open/close operation 
unregister Component 
```kotlin
inline fun <T : Component> unregisterComponent()
```
Unregister previously registered custom  Component  type. 
unregister System 
```kotlin
inline fun <T : System> unregisterSystem()
```
Unregister  System  by type 
Window Container 
```kotlin
fun SpatialAppScope.WindowContainer(id: String, form: Form? = null, properties: ContainerProperties.() -> Unit = {}, content: @Composable WindowContainerScope.() -> Unit)
```
```kotlin
fun SpatialAppScope.WindowContainer(id: String, form: Form? = null, defaultSize: WindowContainerSize? = null, resizeType: ContainerResizeType? = null, defaultResizeRestriction: ContainerResizeRestriction? = null, enableMaterialBackground: Boolean? = null, volumeAlignment: VolumeAlignment? = null, defaultVolumeBasePanelType: VolumeBasePanelType? = null, defaultCaptionBarType: CaptionBarType? = null, placement: PlacementContext.() -> Placement? = null, targetActivity: Class<out ComponentActivity>? = null, worldScale: WorldScale? = null, content: @Composable WindowContainerScope.() -> Unit)
```
Declare a WindowContainer with unique  id . the  id  is used to open/close the WindowContainer.