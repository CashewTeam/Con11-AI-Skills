# createBox | PICO Spatial SDK

core / com.pico.spatial.core.ecs.resource / MeshResource / Companion / createBox 
# createBox
```kotlin
@JvmStatic
```fun  createBox ( size :  Vector3 ,  cornerRadius :  Float  =  0.0f ) :  MeshResource 
Synchronously creates a box mesh resource. 
Bounding Box Specification: The bounding box of the generated box has a fixed center at the origin {0.0f, 0.0f, 0.0f} (local space). Its half-extents are defined as follows: 
- 
X-axis half-extent: size.x / 2.0f (full extent: -size.x/2 to size.x/2). 
- 
Y-axis half-extent: size.y / 2.0f (full extent: -size.y/2 to size.y/2). 
- 
Z-axis half-extent: size.z / 2.0f (full extent: -size.z/2 to size.z/2). 
#### Return
A  MeshResource  object representing the generated box. This mesh can be used in 3D scenes and simulations where boxes of specific sizes and corner styles are required. 
#### Parameters
size 
The size of the box as a  Vector3 , measured in meters (m). Each dimension (x, y, z) respectively represents the length, width, and height of the box. Each dimension must be greater than 0. 
corner Radius 
(Optional) The radius of the box's corners, measured in meters (m). The default value is  0 . If the radius is greater than  0 , adds rounded corners to the box, thereby transforming the box into a rounded box. If the radius is specified as less than  0 , it will be automatically considered as 0, indicating sharp corners. The actual radius used for the rounded corners is calculated at runtime as the minimum of the provided radius and half the length of the smallest side of the box. This ensures that the rounded corners are correctly formed without any geometric distortion, maintaining the geometric integrity of the shape. If the provided radius does not meet this condition, the runtime calculation will adjust it to ensure the box's geometric integrity. 
#### Throws
Resource Loading Exception 
If any error occurs during the loading process. That all  float  parameters are within reasonable ranges:     - All  float  parameters must be positive and represent valid 3D dimensions.     - Extremely small values (approaching 0) may lose their practical significance in 3D       contexts and will be treated as 0 where applicable.     - Excessively large values may lose their geometric or physical significance in 3D       space and may be clamped or adjusted at runtime to maintain the integrity of the       geometry, or may result in an exception being thrown.