# SurfaceRenderTexture | PICO Spatial SDK

core / com.pico.spatial.core.ecs.resource / SurfaceRenderTexture / SurfaceRenderTexture 
# SurfaceRenderTexture
```kotlin
constructor(width: Int = 1920, height: Int = 1080, maxBufferCount: Int = 3, usageFlag: Long = TextureUsageFlag.TEXTURE_USAGE_NONE)
```
Create a SurfaceRenderTexture resource with the specified width, height, maxBufferCount, and usageFlag. 
Note: The  SurfaceRenderTexture  can automatically adapt to the video resolution changes without requiring recreation. You only need to initialize it once with a specific resolution. 
Important: To prevent the  SurfaceRenderTexture  from being garbage collected, we highly recommend maintaining a strong reference to the returned  SurfaceRenderTexture  instance until it is no longer needed. If the  SurfaceRenderTexture  is only stored in a local variable and no other references exist, it may be garbage collected prematurely, leading to unexpected behavior. If you want to reuse the  SurfaceRenderTexture  instance, please call 'toGlobal()' to make it a global resource when it is created. 
#### Parameters
width 
The width of the  SurfaceRenderTexture  to initialize. 
height 
The height of the  SurfaceRenderTexture  to initialize. 
max Buffer Count 
The max buffer count of the  SurfaceRenderTexture  to initialize. 
usage Flag 
The texture usage flag to use. Default is  TextureUsageFlag.TEXTURE_USAGE_NONE . Note:  TextureUsageFlag.TEXTURE_USAGE_PROTECTED_CONTENT  is only supported on physical devices.