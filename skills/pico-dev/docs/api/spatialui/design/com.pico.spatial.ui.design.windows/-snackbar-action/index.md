# SnackbarAction | PICO Spatial SDK

ui:design / com.pico.spatial.ui.design.windows / SnackbarAction 
# SnackbarAction
```kotlin
interface SnackbarAction
```
Represents an action that can be performed in a snack. 
Members 
## Functions
dismiss 
```kotlin
abstract fun dismiss()
```
Dismisses the snack. This function is called when the snack needs to be dismissed. 
perform Action 
```kotlin
abstract fun performAction()
```
This function should be called when the user clicks on the action button in the snack.