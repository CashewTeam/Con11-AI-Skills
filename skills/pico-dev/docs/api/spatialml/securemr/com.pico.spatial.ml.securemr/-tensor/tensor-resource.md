# tensorResource | PICO Spatial SDK

spatialml:securemr / com.pico.spatial.ml.securemr / Tensor / tensorResource 
# tensorResource
```kotlin
open var tensorResource: SharedMemory?
```
The content to the tensor. The provided SharedMemory shall be closed by the caller after the setter completes. 
#### Throws
Spatial MLException 
If the usage is not allowed by the SpatialML run-time Framework, or if the framework encounter internal error and cannot perform the requested behavior.