# convertRotation | PICO Spatial SDK

core / com.pico.spatial.core.coordinate / SpatialCoordinateSpaceConverter / convertRotation 
# convertRotation
```kotlin
abstract fun convertRotation(rotation: Quat, from: ViewCoordinateSpace, to: SpatialCoordinateSpace): Quat
```
Convert a rotation from  ViewCoordinateSpace  to  SpatialCoordinateSpace . 
#### Return
A  Quat  to describe a rotation in  SpatialCoordinateSpace . 
#### Parameters
rotation 
A  Quat  to describe a rotation in  ViewCoordinateSpace . 
from 
A  ViewCoordinateSpace , the origin of  ViewCoordinateSpace.Global  is positioned at the top-left-back corner of the WindowContainer containing the View; the origin of  ViewCoordinateSpace.Local  is positioned at the top-left-back corner of the current View. 
to 
A  SpatialCoordinateSpace , with origin positioned at the center of the View. 
```kotlin
abstract fun convertRotation(rotation: Quat, from: SpatialCoordinateSpace, to: ViewCoordinateSpace): Quat
```
Convert a rotation from  SpatialCoordinateSpace  to  ViewCoordinateSpace . 
#### Return
A  Quat  to describe a rotation in  ViewCoordinateSpace . 
#### Parameters
rotation 
A  Quat  to describe a rotation in  SpatialCoordinateSpace . 
from 
A  SpatialCoordinateSpace , with origin positioned at the center of the View. 
to 
A  ViewCoordinateSpace , the origin of  ViewCoordinateSpace.Global  is positioned at the top-left-back corner of the WindowContainer containing the View; the origin of  ViewCoordinateSpace.Local  is positioned at the top-left-back corner of the current View.