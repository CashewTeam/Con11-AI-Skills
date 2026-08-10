# createCapsule | PICO Spatial SDK

core / com.pico.spatial.core.ecs.resource / MeshResource / Companion / createCapsule 
# createCapsule
```kotlin
@JvmStatic
```fun  createCapsule ( height :  Float ,  radius :  Float ) :  MeshResource 
Synchronously creates a capsule mesh resource. 
Bounding Box Specification: The bounding box of the generated capsule has a fixed center at the origin {0.0f, 0.0f, 0.0f} (local space). Its half-extents are defined as follows: 
- 
X-axis half-extent: equal to radius (full extent: -radius to radius). 
- 
Y-axis half-extent: height / 2.0f + radius (full extent: -height/2 - radius to height/2 + radius). 
- 
Z-axis half-extent: equal to radius (full extent: -radius to radius). 
#### Return
A  MeshResource  object representing the generated capsule. 
#### Parameters
height 
The height of the capsule, measured in meters (m). Must be greater than or equal to  0 . 
radius 
The radius of the capsule, measured in meters (m). Must be greater than or equal to  0 . 
#### Throws
Resource Loading Exception 
If any error occurs during the loading process. That all  float  parameters are within reasonable ranges:     - All  float  parameters must be positive and represent valid 3D dimensions.     - Extremely small values (approaching 0) may lose their practical significance in 3D       contexts and will be treated as 0 where applicable.     - Excessively large values may lose their geometric or physical significance in 3D       space and may be clamped or adjusted at runtime to maintain the integrity of the       geometry, or may result in an exception being thrown.