# convertSize | PICO Spatial SDK

core / com.pico.spatial.core.coordinate / SpatialCoordinateSpaceConverter / convertSize 
# convertSize
```kotlin
abstract fun convertSize(size: Vector3, from: ViewCoordinateSpace, to: SpatialCoordinateSpace): Vector3
```
Convert a size from  ViewCoordinateSpace  to  SpatialCoordinateSpace . 
#### Return
Size in the  SpatialCoordinateSpace  in meters. 
#### Parameters
size 
Size in a  ViewCoordinateSpace  in pixels. 
from 
A  ViewCoordinateSpace , the origin of  ViewCoordinateSpace.Global  is positioned at the top-left-back corner of the WindowContainer containing the View; the origin of  ViewCoordinateSpace.Local  is positioned at the top-left-back corner of the current View. 
to 
A  SpatialCoordinateSpace , with origin positioned at the center of the View. 
#### Throws
Illegal State Exception 
If you use this after the associated View is destroyed. 
```kotlin
abstract fun convertSize(size: Vector3, from: SpatialCoordinateSpace, to: ViewCoordinateSpace): Vector3
```
Convert a size from  SpatialCoordinateSpace  to  ViewCoordinateSpace . 
#### Return
Size in the  SpatialCoordinateSpace  in meters. 
#### Parameters
size 
Size in a  SpatialCoordinateSpace  in pixels. 
from 
A  SpatialCoordinateSpace . 
to 
A  ViewCoordinateSpace , with origin positioned at the center of the View. 
#### Throws
Illegal State Exception 
If you use this after the associated View is destroyed.