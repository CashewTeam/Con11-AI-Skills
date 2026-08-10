# SnackbarHostState | PICO Spatial SDK

ui:design / com.pico.spatial.ui.design.windows / SnackbarHostState 
# SnackbarHostState
```kotlin
@Stable
```interface  SnackbarHostState 
State of the  SnackbarHost , can be retrieved by  LocalSnackbarHostState  inside composable function 
#### Samples
com.pico.spatial.ui.design.samples.SnackSample Members 
## Functions
dismiss 
```kotlin
abstract fun dismiss()
```
Dismisses the currently displayed snack, if any. 
show 
```kotlin
abstract suspend fun show(message: @Composable () -> Unit, description: @Composable () -> Unit? = null, leadingIcon: @Composable () -> Unit? = null, trailingActions: @Composable SnackbarAction.() -> Unit? = null, duration: SnackbarDuration = SnackbarDuration.Default, enableBackgroundMaterial: Boolean = true, backgroundColor: Color? = null): SnackbarResult
```
Displays a snack with the provided message, description, leading icon, trailing actions, and duration. 
```kotlin
abstract suspend fun show(message: String, description: String = "", leadingIcon: @Composable () -> Unit? = null, action: String = "", duration: SnackbarDuration = SnackbarDuration.Default, enableBackgroundMaterial: Boolean = true, backgroundColor: Color? = null): SnackbarResult
```
Shows or queues a snack, will be shown at bottom of the  SnackbarHost 's window