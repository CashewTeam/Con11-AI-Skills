# TEXTURE_USAGE_PROTECTED_CONTENT | PICO Spatial SDK

core / com.pico.spatial.core.ecs.video / TextureUsageFlag / TEXTURE_USAGE_PROTECTED_CONTENT 
# TEXTURE_USAGE_PROTECTED_CONTENT
```kotlin
const val TEXTURE_USAGE_PROTECTED_CONTENT: Long
```
The texture buffer must not be used outside of a protected hardware path. 
This flag enforces that the texture buffer can only be processed within secure hardware environments. It is typically used for content that requires digital rights management (DRM) protection. Textures created with this flag have restricted access and cannot be processed by unsecured software components. 
## Security Implications
- 
The texture content cannot be screenshotted or captured by unsecured applications. 
- 
Direct memory access to the texture buffer is restricted. 
- 
Only hardware-protected rendering paths can utilize this texture. 
- 
This flag is particularly useful for DRM-protected media that requires hardware-level security. 
- 
On emulator, this flag is not supported due to limitations in the emulator environment.