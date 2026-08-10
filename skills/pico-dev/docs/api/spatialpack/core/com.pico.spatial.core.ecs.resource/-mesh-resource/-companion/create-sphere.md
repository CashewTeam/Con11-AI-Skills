# createSphere | PICO Spatial SDK

core / com.pico.spatial.core.ecs.resource / MeshResource / Companion / createSphere 
# createSphere
```kotlin
@JvmStatic
```fun  createSphere ( radius :  Float ) :  MeshResource 
Synchronously creates a sphere mesh resource. 
Bounding Box Specification: The bounding box of the generated sphere has a fixed center at the origin {0.0f, 0.0f, 0.0f} (local space). Its half-extents are equal to the radius of the sphere in all three axes: 
- 
X-axis half-extent: radius (full extent: -radius to radius). 
- 
Y-axis half-extent: radius (full extent: -radius to radius). 
- 
Z-axis half-extent: radius (full extent: -radius to radius). 
#### Return
A  MeshResource  object representing the generated sphere. 
#### Parameters
radius 
The radius of the sphere, measured in meters (m). Must be greater than or equal to  0 . 
#### Throws
Resource Loading Exception 
If any error occurs during the loading process. That all  float  parameters are within reasonable ranges:     - All  float  parameters must be positive and represent valid 3D dimensions.     - Extremely small values (approaching 0) may lose their practical significance in 3D       contexts and will be treated as 0 where applicable.     - Excessively large values may lose their geometric or physical significance in 3D       space and may be clamped or adjusted at runtime to maintain the integrity of the       geometry, or may result in an exception being thrown.