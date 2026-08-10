# bindSurfaceRenderTexture | PICO Spatial SDK

core / com.pico.spatial.core.ecs.resource / VideoMaterial / bindSurfaceRenderTexture 
# bindSurfaceRenderTexture
```kotlin
fun bindSurfaceRenderTexture(surfaceRenderTexture: SurfaceRenderTexture)
```
Bind a  SurfaceRenderTexture  instance with current video material. 
#### Parameters
surface Render Texture 
The  SurfaceRenderTexture  instance to bind. 
#### Throws
Illegal State Exception 
If this material or the given surface render texture is invalid. 
Note: When bind a new  SurfaceRenderTexture  to the same  VideoMaterial , if another  SurfaceRenderTexture  was previously bound, it will be automatically released unless  .toGlobal()  was called on it before this bind operation happened. In the following example, the  SurfaceRenderTexture  will be kept valid and can be reused safely. 
###Example: 

```
//create a video player and play a video.val player = MediaPlayer()player.setDataSource(videoUri)player.prepare()//create a surface render texture.val surfaceRenderTexture = SurfaceRenderTexture(width, height, maxBufferCount, usageFlag)surfaceRenderTexture.toGlobal()//bind the surface render texture to the video material.val videoMaterial = VideoMaterial(blendingMode)videoMaterial.bindSurfaceRenderTexture(surfaceRenderTexture)//create meshval mesh = MeshResource.createPlane(0.9f, 0.45f, 0.0f)//create VideoComponentval entity = Entity()val videoComponent = VideoComponent(mesh,videoMaterial)entity.components.set(videoComponent)//set surface to player and start playing the video. surfaceRenderTexture.acquireSurface()?.let { surface ->  if(surface.isValid) {    player.setSurface(surface)     player.start()  } }
```