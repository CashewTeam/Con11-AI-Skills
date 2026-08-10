# imageWidth | PICO Spatial SDK

spatialml:securemr / com.pico.spatial.ml.securemr / SpatialMLSession / InitInfo / imageWidth 
# imageWidth
```kotlin
val imageWidth: Int
```
#### Parameters
image Width 
the expected image width when accessing the camera in this session. We recommend the image width to match the desired output tensor's width in  Pipeline.rectifiedVSTAccess  to avoid unnecessary image resizing. Must be greater than zero. Unit is pixel.