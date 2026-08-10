# SnackbarResult | PICO Spatial SDK

ui:design / com.pico.spatial.ui.design.windows / SnackbarResult 
# SnackbarResult
```kotlin
sealed class SnackbarResult
```
Possible results of the  SnackbarHostState.show  call 
This sealed class represents all possible outcomes when showing a snack: 
- 
Successful display with specific user interaction result 
- 
Failure case with details 
#### Inheritors
Dismissed ActionPerformed Failure Members 
## Constructors
Snackbar Result 
```kotlin
protected constructor()
```
## Types
Action Performed 
```kotlin
data object ActionPerformed : SnackbarResult
```
Represents a snack where the user explicitly clicked the action button 
Dismissed 
```kotlin
data object Dismissed : SnackbarResult
```
Represents a snack that was automatically dismissed after timeout or manually dismissed by the user 
Failure 
```kotlin
class Failure : SnackbarResult
```
Represents a failed attempt to show a snack