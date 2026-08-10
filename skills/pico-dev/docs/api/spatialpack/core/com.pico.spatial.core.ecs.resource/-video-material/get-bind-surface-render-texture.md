# getBindSurfaceRenderTexture | PICO Spatial SDK

core / com.pico.spatial.core.ecs.resource / VideoMaterial / getBindSurfaceRenderTexture 
# getBindSurfaceRenderTexture
```kotlin
fun getBindSurfaceRenderTexture(): SurfaceRenderTexture?
```
Gets the bound  SurfaceRenderTexture  of the VideoMaterial. 
#### Return
The  SurfaceRenderTexture  that VideoMaterial is using, or null if none is bound. 
#### Throws
Illegal State Exception 
If this material has been closed or is invalid.