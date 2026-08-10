# acquireSurface | PICO Spatial SDK

core / com.pico.spatial.core.ecs.resource / SurfaceRenderTexture / acquireSurface 
# acquireSurface
```kotlin
fun acquireSurface(): Surface?
```
Acquires a  Surface  for rendering, suitable for use with Android media player. 
#### Return
The  Surface  to render on if the  SurfaceRenderTexture  is valid; otherwise  null . 
#### Throws
Illegal State Exception 
If this resource is closed or invalid. 
Note: 
- 
The returned  Surface  is only valid while the  SurfaceRenderTexture  is valid. 
- 
The  Surface  is released automatically when the  SurfaceRenderTexture  is closed. 
- 
The same  Surface  instance is returned on every call unless the previously acquired  Surface  has been released.