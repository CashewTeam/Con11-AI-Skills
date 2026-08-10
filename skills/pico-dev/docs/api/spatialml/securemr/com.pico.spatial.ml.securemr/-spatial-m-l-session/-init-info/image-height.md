# imageHeight | PICO Spatial SDK

spatialml:securemr / com.pico.spatial.ml.securemr / SpatialMLSession / InitInfo / imageHeight 
# imageHeight
```kotlin
val imageHeight: Int
```
#### Parameters
image Height 
the expected image height when accessing the camera in this session. We recommend the image height to match the desired output tensor's height in  Pipeline.rectifiedVSTAccess  to avoid unnecessary image resizing. Must be greater than zero. Unit is pixel.