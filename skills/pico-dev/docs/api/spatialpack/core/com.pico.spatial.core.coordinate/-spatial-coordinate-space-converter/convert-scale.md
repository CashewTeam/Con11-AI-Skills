# convertScale | PICO Spatial SDK

core / com.pico.spatial.core.coordinate / SpatialCoordinateSpaceConverter / convertScale 
# convertScale
```kotlin
abstract fun convertScale(scale: Vector3, from: ViewCoordinateSpace, to: SpatialCoordinateSpace): Vector3
```
Convert a scale from  ViewCoordinateSpace  to  SpatialCoordinateSpace . 
#### Return
A  Vector3  to describe a rotation in  SpatialCoordinateSpace . 
#### Parameters
scale 
A  Vector3  to describe a rotation in  ViewCoordinateSpace . 
from 
A  ViewCoordinateSpace , the origin of  ViewCoordinateSpace.Global  is positioned at the top-left-back corner of the WindowContainer containing the View; the origin of  ViewCoordinateSpace.Local  is positioned at the top-left-back corner of the current View. 
to 
A  SpatialCoordinateSpace , with origin positioned at the center of the View. 
```kotlin
abstract fun convertScale(scale: Vector3, from: SpatialCoordinateSpace, to: ViewCoordinateSpace): Vector3
```
Convert a scale from  SpatialCoordinateSpace  to  ViewCoordinateSpace . 
#### Return
A  Vector3  to describe a rotation in  SpatialCoordinateSpace . 
#### Parameters
scale 
A  Vector3  to describe a rotation in  SpatialCoordinateSpace . 
from 
A  SpatialCoordinateSpace , with origin positioned at the center of the View. 
to 
A  ViewCoordinateSpace , the origin of  ViewCoordinateSpace.Global  is positioned at the top-left-back corner of the WindowContainer containing the View; the origin of  ViewCoordinateSpace.Local  is positioned at the top-left-back corner of the current View.