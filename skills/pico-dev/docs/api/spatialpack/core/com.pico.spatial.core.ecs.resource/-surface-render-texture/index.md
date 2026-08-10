# SurfaceRenderTexture | PICO Spatial SDK

core / com.pico.spatial.core.ecs.resource / SurfaceRenderTexture 
# SurfaceRenderTexture
```kotlin
class SurfaceRenderTexture : Resource
```
Managed SurfaceRenderTexture resource for Android media rendering; this resource obeys the lifecycle management of  Resource . Calling  toGlobal()  can make it reusable. 
This class provides Android  Surface  object that can be used as rendering targets for Android media player or other Surface-based renderers. 
Usage with VideoMaterial: 
- 
Get instance via  SurfaceRenderTexture(width,height,maxBufferCount,usageFlag) . 
- 
Call  acquireSurface  to get the Android Surface. 
- 
Configure media player with the Surface. 
- 
Call  Surface.release  when rendering completes to release the Surface. 
- 
Final cleanup via  close . 
### Example:

```
// Create media player and set data sourceval mediaPlayer = MediaPlayer()mediaPlayer.setDataSource(videoUrl)mediaPlayer.prepare()//create surfaceRenderTexture with default size 1920x1080 and maxBufferCount 3 and hold it.val surfaceRenderTexture = SurfaceRenderTexture()surfaceRenderTexture.toGlobal()// Create video renderer work flow with VideoComponentval videoMaterial = VideoMaterial(    blendingMode = BlendingMode.OPAQUE,    videoDimensionMode = VideoDimensionMode.SIDE_BY_SIDE,    cullingMode = MaterialCullingMode.BACK,    defaultColor = Color4.BLACK)videoMaterial.bindSurfaceRenderTexture(surfaceRenderTexture)if (surfaceRenderTexture.valid) {    val surface = surfaceRenderTexture.acquireSurface()    // Configure media player with the surface    surface?.let {        mediaPlayer.setSurface(it)    }}val mesh = MeshResource.createPlane(0.96f, 0.54f)val videoComponent = VideoComponent(mesh, videoMaterial)val videoEntity = Entity()videoEntity.components.set(videoComponent)// Playback control:- Start: Call `mediaPlayer.start()`- Pause: Call `mediaPlayer.pause()`- Resume: Call `mediaPlayer.resume()`- Stop: Call `mediaPlayer.stop()`- Release: Call `mediaPlayer.release()`// Release Resource when no longer needed:- videoEntity.destroy()// or call close to release the resource manually when you want to reuse surfaceRenderTexture.- surfaceRenderTexture.close()
```
Notes: 
- 
Surface objects become invalid after  SurfaceRenderTexture  is closed. 
- 
Always stop the video player before closing the surfaceRenderTexture. 
#### See also
Video Material. bind Surface Render Texture 
The method to bind surfaceRenderTexture to VideoMaterial. 
Members 
## Constructors
Surface Render Texture 
```kotlin
constructor(width: Int = 1920, height: Int = 1080, maxBufferCount: Int = 3, usageFlag: Long = TextureUsageFlag.TEXTURE_USAGE_NONE)
```
Create a SurfaceRenderTexture resource with the specified width, height, maxBufferCount, and usageFlag. 
## Functions
acquire Surface 
```kotlin
fun acquireSurface(): Surface?
```
Acquires a  Surface  for rendering, suitable for use with Android media player. 
close 
```kotlin
open override fun close()
```
You need to manually release the resource to free the memory it occupies.