# convertPosition | PICO Spatial SDK

core / com.pico.spatial.core.coordinate / SpatialCoordinateSpaceConverter / convertPosition 
# convertPosition
```kotlin
abstract fun convertPosition(position: Vector3, from: SpatialCoordinateSpace, to: ViewCoordinateSpace): Vector3
```
Converts a position from  SpatialCoordinateSpace  to  ViewCoordinateSpace . 
Attention: The  Vector3  is Float value, while  Vector3  is Int value, there may be some loss of precision about 0.0001. Besides, if position  Vector3 's property is  Float.MAX_VALUE , the return value property of  Vector3  will be  Int.MAX_VALUE . 
#### Return
Offset in a  ViewCoordinateSpace  in pixels. 
#### Parameters
position 
The position in a  SpatialCoordinateSpace  in meters. 
from 
A  SpatialCoordinateSpace , with root Entity of Space. 
to 
A  ViewCoordinateSpace , the origin of  ViewCoordinateSpace.Global  is positioned at the top-left-back corner of the WindowContainer containing the View; the origin of  ViewCoordinateSpace.Local  is positioned at the top-left-back corner of the current View. 
#### Throws
Illegal State Exception 
If you use this after the associated View is destroyed. 
```kotlin
abstract fun convertPosition(position: Vector3, from: ViewCoordinateSpace, to: SpatialCoordinateSpace): Vector3
```
Converts a position from  ViewCoordinateSpace  to  SpatialCoordinateSpace . 
#### Return
Position in the  SpatialCoordinateSpace  in meters. The origin is the  com.pico.spatial.core.ecs.TransformComponent._position  of the  com.pico.spatial.core.ecs.Entity . 
#### Parameters
position 
Position in a  ViewCoordinateSpace  in pixels. 
from 
A  ViewCoordinateSpace , the origin of  ViewCoordinateSpace.Global  is positioned at the top-left-back corner of the WindowContainer containing the View; the origin of  ViewCoordinateSpace.Local  is positioned at the top-left-back corner of the current View. 
to 
A  SpatialCoordinateSpace , with origin positioned at the center of the View. 
#### Throws
Illegal State Exception 
If you use this after the associated View is destroyed.