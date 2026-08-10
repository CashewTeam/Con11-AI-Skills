# unbindSurfaceRenderTexture | PICO Spatial SDK

core / com.pico.spatial.core.ecs.resource / VideoMaterial / unbindSurfaceRenderTexture 
# unbindSurfaceRenderTexture
```kotlin
fun unbindSurfaceRenderTexture()
```
Unbind surface render texture with current video material. 
When the  SurfaceRenderTexture  is no longer needed for this  VideoMaterial , it is recommended to call this method to unbind the  SurfaceRenderTexture  from this  VideoMaterial . After unbinding, the  SurfaceRenderTexture  will be released unless  .toGlobal()  was called on it before this unbind operation happened. In the following example, the  SurfaceRenderTexture  will be kept alive and can be used for other purposes, such as binding it to other  VideoMaterial  instances. 
#### Throws
Illegal State Exception 
If this material has been closed or is invalid. 
Note: After unbinding, the  SurfaceRenderTexture  is no longer bound to this  VideoMaterial , the render path of the  VideoMaterial  will be interrupted, the display of the current video will be interrupted as well. 
###Example: 

```
//create a video player and play a video.val player = MediaPlayer()player.setDataSource(videoUri)player.prepare()//create a surface render texture.val surfaceRenderTexture = SurfaceRenderTexture(width, height, maxBufferCount, usageFlag)surfaceRenderTexture.toGlobal()//bind the surface render texture to the video material.val videoMaterial = VideoMaterial(blendingMode)videoMaterial.bindSurfaceRenderTexture(surfaceRenderTexture)//create VideoComponentval entity = Entity()val videoComponent = VideoComponent(mesh,videoMaterial)entity.components.set(videoComponent)//set surface to player and start playing the video. surfaceRenderTexture.acquireSurface()?.let { surface ->  if(surface.isValid) {    player.setSurface(surface)    player.start()  } }//When need to bind the surface render texture to other video material.videoMaterial.unbindSurfaceRenderTexture()//repeat step 3 to bind the surface render texture to other video material.val videoMaterialB = VideoMaterial(blendingMode)videoMaterialB.bindSurfaceRenderTexture(surfaceRenderTexture)
```