# createVideoPanel | PICO Spatial SDK

core / com.pico.spatial.core.ecs.resource / MeshResource / Companion / createVideoPanel 
# createVideoPanel
```kotlin
@JvmStatic
```fun  createVideoPanel ( width :  Float ,  height :  Float ,  cornerRadius :  Float ) :  MeshResource 
Creates a mesh resource for a video panel. 
This function generates a rectangular video panel mesh with the specified width and height, divided into a grid based on the given row and column counts. 
#### Return
A mesh resource representing the created video panel. 
#### Parameters
width 
The width of the panel, measured in meters (m). Must be greater than  0 . Represents the horizontal dimension of the panel in 2D space. 
height 
The height of the panel, measured in meters (m). Must be greater than  0 . Represents the vertical dimension of the panel in 2D space. 
corner Radius 
The radius of the panel's corners, measured in meters (m). The default value is  0 . If the radius is greater than  0 , adds rounded corners to the box, thereby transforming the box into a rounded box. If the radius is specified as less than  0 , it will be automatically considered as 0, indicating sharp corners. The actual radius used for the rounded corners is calculated at runtime as the minimum of the provided radius and half the length of the smallest side of the box. This ensures that the rounded corners are correctly formed without any geometric distortion, maintaining the geometric integrity of the shape. If the provided radius does not meet this condition, the runtime calculation will adjust it to ensure the box's geometric integrity. 
#### Throws
Resource Loading Exception 
If an error occurs during the loading process. Ensure that all  float  parameters are within reasonable ranges:     - All  float  parameters must be positive and represent valid 3D dimensions.     - Extremely small values (approaching 0) may lose their practical significance in 3D       contexts and will be treated as 0 where applicable.     - Excessively large values may lose their geometric or physical significance in 3D       space and may be clamped or adjusted at runtime to maintain the integrity of the       geometry, or may result in an exception being thrown.