# com.pico.spatial.sense.plane | PICO Spatial SDK

sense / com.pico.spatial.sense.plane 
# Package-level declarations
Types 
## Types
Plane Anchor 
```kotlin
@RequiredFullSpace
```class  PlaneAnchor  :  Anchor 
Represents a plane anchor in 3D space with a unique identifier, transform properties, and additional mesh-related data. 
Plane Orientation 
```kotlin
enum PlaneOrientation : Enum<PlaneOrientation>
```
Enum class representing the orientation of a plane in 3D space. Used to describe the spatial alignment of a plane. 
Plane Tracking Manager 
```kotlin
object PlaneTrackingManager
```
Provides plane tracking functionalities, including managing and updating plane anchors.