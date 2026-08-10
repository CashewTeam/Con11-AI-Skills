# CameraAnchor | PICO Spatial SDK

spatialml:securemr / com.pico.spatial.ml.securemr / SceneGraphProperty / CameraAnchor 
# CameraAnchor
```kotlin
sealed class CameraAnchor : SceneGraphProperty
```
Update the camera anchor component of an entity.  CameraAnchor  component is an hidden component for SpatialML container only. It allows you to use a transform matrix with respect to the camera coordinate space, to override the local transform updated by  SceneGraphProperty.Transform . 
Updating the  CameraAnchor  component can be helpful if you deploy some tracking algorithms through the SpatialML module. The poses returned by tracking algorithm are usually relative to the camera coordinate space. If so, you can use the returned poses to update the  CameraAnchor  component, so that your entity's pose will follow the tracking target. 
#### Inheritors
Follow Locked Members 
## Types
Follow 
```kotlin
object Follow : SceneGraphProperty.CameraAnchor
```
The  CameraAnchor.Follow  sets the camera anchor to be at the following mode, which means, once the camera anchor is set, the world pose of the entity will always be updated so that its transform with respect to the camera coordinate space will always remain the same as the provided matrix. 
Locked 
```kotlin
object Locked : SceneGraphProperty.CameraAnchor
```
The  CameraAnchor.Locked  sets the camera anchor to be at the locked mode, which means, the world pose of the entity will be overridden to the pose specified by the provided matrix with respect to the camera coordinate space at that moment. The world pose of the entity will then be locked, regardless of head/camera movement and the SpatialML container movement.