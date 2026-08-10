# SpatialNavigator | PICO Spatial SDK

ui:platform / com.pico.spatial.ui.platform.containers / SpatialNavigator 
# SpatialNavigator
```kotlin
interface SpatialNavigator
```
Navigator for spatial container 
Members 
## Functions
close Stage 
```kotlin
abstract suspend fun closeStage()
```
Close the current Stage opened by app 
close Window Container 
```kotlin
abstract fun closeWindowContainer()
```
Close the current WindowContainer 
```kotlin
abstract fun closeWindowContainer(id: String, tag: String? = null)
```
Close a WindowContainer by  id  and optional  tag 
minimize Window Container 
```kotlin
abstract fun minimizeWindowContainer(): Boolean
```
Minimize the current WindowContainer, can only be used when there is a stage open 
```kotlin
abstract fun minimizeWindowContainer(id: String, tag: String? = null): Boolean
```
Minimize a WindowContainer by  id  and optional  tag , can only be used when there is a stage open. 
open Stage 
```kotlin
abstract suspend fun openStage(id: String, style: StageStyle? = null, bundle: Bundle? = null, upperLimbRenderMode: UpperLimbRenderMode = UpperLimbRenderMode.Default): OpenStageResult
```
Open a Stage by id 
open Window Container 
```kotlin
abstract fun openWindowContainer(id: String, tag: String? = null, bundle: Bundle? = null)
```
Open a WindowContainer by  id  and optional  tag 
restore Window Container 
```kotlin
abstract fun restoreWindowContainer(): Boolean
```
Restore the current WindowContainer, can only be used when there is a stage open 
```kotlin
abstract fun restoreWindowContainer(id: String, tag: String? = null): Boolean
```
Restore a WindowContainer by  id  and optional  tag , can only be used when there is a stage open.