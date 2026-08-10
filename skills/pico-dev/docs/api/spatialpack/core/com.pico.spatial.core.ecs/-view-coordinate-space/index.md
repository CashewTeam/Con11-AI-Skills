# ViewCoordinateSpace | PICO Spatial SDK

core / com.pico.spatial.core.ecs / ViewCoordinateSpace 
# ViewCoordinateSpace
```kotlin
sealed interface ViewCoordinateSpace
```
Coordinate space for views, including the SpatialUI View, Standard Android View. 
#### Inheritors
Local Global Members 
## Types
Global 
```kotlin
object Global : ViewCoordinateSpace
```
A singleton object of  ViewCoordinateSpace . Provides a global coordinate space with its origin positioned at the top-left-back corner of the WindowContainer containing the view. 
Local 
```kotlin
object Local : ViewCoordinateSpace
```
A singleton object of  ViewCoordinateSpace . Provides a local coordinate space with its origin positioned at the top-left-back corner of the view.