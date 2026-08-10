# createPlane | PICO Spatial SDK

core / com.pico.spatial.core.ecs.resource / MeshResource / Companion / createPlane 
# createPlane
```kotlin
@JvmStatic
```fun  createPlane ( width :  Float ,  height :  Float ,  cornerRadius :  Float  =  0.0f ) :  MeshResource 
Synchronously creates a plane mesh resource. 
Bounding Box Specification: The bounding box of the generated plane has a fixed center at the origin {0.0f, 0.0f, 0.0f} (local space). Its half-extents are defined as follows (plane is perpendicular to Z-axis and lies on the X-Y plane): 
- 
X-axis half-extent: width / 2.0f (full extent: -width/2 to width/2). 
- 
Y-axis half-extent: height / 2.0f (full extent: -height/2 to height/2). 
- 
Z-axis half-extent: 0.0f (plane has no thickness along Z-axis). 
#### Return
A  MeshResource  object representing the generated plane. This mesh can be used in 2D or 3D scenes and simulations where planes of specific sizes and corner styles are required. 
#### Parameters
width 
The width of the plane, measured in meters (m). Must be greater than  0 . Represents the horizontal dimension of the plane in 2D space. 
height 
The height of the plane, measured in meters (m). Must be greater than  0 . Represents the vertical dimension of the plane in 2D space. 
corner Radius 
(Optional) The radius of the plane's corners, measured in meters (m). The default value is  0 . If the value is greater than 0, transforms the rectangular plane into a plane with rounded corners. If the value is less than  0 , it is considered as  0 . The actual radius used is the minimum of the specified radius and half the length of the plane's smallest side. This ensures that rounded corners are properly formed without distorting the plane geometry. However, if the provided radius does not meet this condition, the runtime calculation will adjust it to ensure the plane's geometric integrity. 
#### Throws
Resource Loading Exception 
If any error occurs during the loading process. That all  float  parameters are within reasonable ranges:     - All  float  parameters must be positive and represent valid 3D dimensions.     - Extremely small values (approaching 0) may lose their practical significance in 3D       contexts and will be treated as 0 where applicable.     - Excessively large values may lose their geometric or physical significance in 3D       space and may be clamped or adjusted at runtime to maintain the integrity of the       geometry, or may result in an exception being thrown.