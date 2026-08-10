# InitInfo | PICO Spatial SDK

spatialml:securemr / com.pico.spatial.ml.securemr / SpatialMLSession / InitInfo 
# InitInfo
```kotlin
class InitInfo(val imageWidth: Int, val imageHeight: Int, val containerWidth: Int, val containerHeight: Int, val containerDepth: Int)
```
Configuration structure for framework session handle. 
#### Parameters
image Width 
the expected image width when accessing the camera in this session. We recommend the image width to match the desired output tensor's width in  Pipeline.rectifiedVSTAccess  to avoid unnecessary image resizing. Must be greater than zero. Unit is pixel. 
image Height 
the expected image height when accessing the camera in this session. We recommend the image height to match the desired output tensor's height in  Pipeline.rectifiedVSTAccess  to avoid unnecessary image resizing. Must be greater than zero. Unit is pixel. 
container Width 
the width of the SpatialML container at initialization. Must be greater than zero if you want to use the SpatialML container; zero or negative to disable the SpatialML container. 
container Height 
the height of the SpatialML container at initialization. Must be greater than zero if you want to use the SpatialML container; zero or negative to disable the SpatialML container. 
container Depth 
the depth of SpatialML container at initialization. If zero, the SpatialML container will be in portal mode; if positive, the SpatialML container will be in volumetric mode; if negative, SpatialML container will be disabled. 
#### See also
Pipeline. rectified VSTAccess Members 
## Constructors
Init Info 
```kotlin
constructor(imageWidth: Int, imageHeight: Int, containerWidth: Int, containerHeight: Int, containerDepth: Int)
```
## Properties
container Depth 
```kotlin
val containerDepth: Int
```container Height 
```kotlin
val containerHeight: Int
```container Width 
```kotlin
val containerWidth: Int
```image Height 
```kotlin
val imageHeight: Int
```image Width 
```kotlin
val imageWidth: Int
```