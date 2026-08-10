# TEXTURE_USAGE_NONE | PICO Spatial SDK

core / com.pico.spatial.core.ecs.video / TextureUsageFlag / TEXTURE_USAGE_NONE 
# TEXTURE_USAGE_NONE
```kotlin
const val TEXTURE_USAGE_NONE: Long = 0
```
No special texture usage flag. 
This is the default flag indicating that the texture buffer has no special usage requirements and can be used in any context without hardware protection constraints. Textures created with this flag can be freely accessed by standard rendering pipelines. 
#### See also
Surface Render Texture 
Default usage when no flag is specified.