# createTorus | PICO Spatial SDK

core / com.pico.spatial.core.ecs.resource / MeshResource / Companion / createTorus 
# createTorus
```kotlin
@JvmStatic
```fun  createTorus ( outerRingRadius :  Float ,  innerRingRadius :  Float ) :  MeshResource 
Synchronously creates a torus mesh resource. 
Bounding Box Specification: The bounding box of the generated torus has a fixed center at the origin {0.0f, 0.0f, 0.0f} (local space). Its half-extents are defined as follows: 
- 
X-axis half-extent: equal to outerRingRadius (full extent: -outerRingRadius to outerRingRadius) 
- 
Y-axis half-extent: (outerRingRadius - innerRingRadius) / 2.0f (full extent: -(outerRingRadius - innerRingRadius)/2 to (outerRingRadius - innerRingRadius)/2) 
- 
Z-axis half-extent: equal to outerRingRadius (full extent: -outerRingRadius to outerRingRadius) 
This method creates a torus mesh resource based on the specified outer and inner ring radii. The outer ring radius ( outerRingRadius ) must always be greater than the inner ring radius ( innerRingRadius ), and both radii must be greater than 0. The mesh is generated through a native call that takes these radii as inputs. 
#### Return
A  MeshResource  object representing the generated torus. 
#### Parameters
outer Ring Radius 
The radius of the torus's outer ring, measured in meters (m). Must be greater than  0  and  innerRingRadius . 
inner Ring Radius 
The radius of the torus's inner ring, measured in meters (m). Must be greater than  0  and less than  outerRingRadius . 
#### Throws
Resource Loading Exception 
If any error occurs during the loading process. That all  float  parameters are within reasonable ranges:     - All  float  parameters must be positive and represent valid 3D dimensions.     - Extremely small values (approaching 0) may lose their practical significance in 3D       contexts and will be treated as 0 where applicable.     - Excessively large values may lose their geometric or physical significance in 3D       space and may be clamped or adjusted at runtime to maintain the integrity of the       geometry, or may result in an exception being thrown.