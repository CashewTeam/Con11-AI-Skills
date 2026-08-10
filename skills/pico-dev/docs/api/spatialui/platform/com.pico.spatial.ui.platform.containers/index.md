# com.pico.spatial.ui.platform.containers | PICO Spatial SDK

ui:platform / com.pico.spatial.ui.platform.containers 
# Package-level declarations
Types Functions Properties 
## Types
Open Stage Result 
```kotlin
sealed class OpenStageResult
```
The result of  openStage 
Spatial Container Scope 
```kotlin
interface SpatialContainerScope
```
Interface defining the scope of a spatial container, such as a  WindowContainer  or  Stage . 
Spatial Container State Manager 
```kotlin
interface SpatialContainerStateManager
```
Provides the  SpatialContainer 's states by  State . 
Spatial Navigator 
```kotlin
interface SpatialNavigator
```
Navigator for spatial container 
Stage Scope 
```kotlin
interface StageScope : SpatialContainerScope
```
Interface representing the scope of a  Stage , which extends the  SpatialContainerScope 
Stage Style 
```kotlin
enum StageStyle : Enum<StageStyle>
```
Stage 's styles 
Upper Limb Render Mode Change Listener 
```kotlin
interface UpperLimbRenderModeChangeListener
```
Listener for upper limb render mode change events. 
Window Container Params Updater 
```kotlin
interface WindowContainerParamsUpdater
```
Provides functionality to update and retrieve the mutable parameters of a WindowContainer 
Window Container Scope 
```kotlin
interface WindowContainerScope : SpatialContainerScope, WindowContainerConstraintsScope
```
Interface representing the scope of a  WindowContainer , which extends the  SpatialContainerScope  and  WindowContainerConstraintsScope . 
## Properties
Local Spatial Navigator 
```kotlin
val LocalSpatialNavigator: ProvidableCompositionLocal<SpatialNavigator>
```
LocalSpatialNavigator 
Local Window Container Params Updater 
```kotlin
val LocalWindowContainerParamsUpdater: ProvidableCompositionLocal<WindowContainerParamsUpdater>
```
LocalWindowContainerParamsUpdater 
## Functions
close Stage 
```kotlin
suspend fun closeStage()
```
Close current Stage opened by app 
close Window Container 
```kotlin
fun Context.closeWindowContainer(id: String, tag: String? = null)
```
Close a WindowContainer by  id  and optional  tag . 
minimize Window Container 
```kotlin
fun Context.minimizeWindowContainer(id: String, tag: String? = null): Boolean
```
Minimize a WindowContainer by  id  and optional  tag , can only be used when there is a stage open. 
open Stage 
```kotlin
suspend fun Context.openStage(id: String, style: StageStyle? = null, bundle: Bundle? = null, upperLimbRenderMode: UpperLimbRenderMode? = null): OpenStageResult
```
Open a Stage by id. 
open Window Container 
```kotlin
fun Context.openWindowContainer(id: String, tag: String? = null, bundle: Bundle? = null)
```
Open a WindowContainer by  id  and optional  tag 
restore Window Container 
```kotlin
fun Context.restoreWindowContainer(id: String, tag: String? = null): Boolean
```
Restore a WindowContainer by  id  and optional  tag , can only be used when there is a stage open.