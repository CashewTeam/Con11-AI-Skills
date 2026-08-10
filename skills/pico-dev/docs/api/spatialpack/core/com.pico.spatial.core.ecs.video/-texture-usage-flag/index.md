# TextureUsageFlag | PICO Spatial SDK

core / com.pico.spatial.core.ecs.video / TextureUsageFlag 
# TextureUsageFlag
```kotlin
object TextureUsageFlag
```
Defines texture usage flags for controlling how texture buffers are utilized in video processing. 
This class provides bitmask flags that specify special requirements and constraints for texture buffers used in video rendering pipelines. These flags help enforce security and hardware-specific constraints when creating surface render textures for video content. 
## Usage
Texture usage flags are typically passed as parameters when creating surface render textures through the video material system: 

```
// Create a surface render texture with protected content flagval surfaceRenderTexture = SurfaceRenderTexture(    width = 1920,    height = 1080,    usageFlag = TextureUsageFlag.TEXTURE_USAGE_PROTECTED_CONTENT)// Create a surface render texture with no special flags (default)val defaultTexture = SurfaceRenderTexture(    width = 1920,    height = 1080)
```
Note: 
- 
Protected Content Security : When using  TEXTURE_USAGE_PROTECTED_CONTENT , ensure that your     application has the necessary permissions to handle protected video content. This flag is     typically used for DRM-protected media that requires hardware-level security. 
- 
Hardware Compatibility : Not all devices may support protected content textures. Always     check device capabilities before using protected content flags in production applications. 
- 
Flag Combinations : Currently, only individual flags are supported. Future versions may     support combining multiple flags using bitwise operations. 
#### See also
Surface Render Texture 
The factory method that utilizes these flags 
Members 
## Properties
TEXTURE_ USAGE_ NONE 
```kotlin
const val TEXTURE_USAGE_NONE: Long = 0
```
No special texture usage flag. 
TEXTURE_ USAGE_ PROTECTED_ CONTENT 
```kotlin
const val TEXTURE_USAGE_PROTECTED_CONTENT: Long
```
The texture buffer must not be used outside of a protected hardware path.