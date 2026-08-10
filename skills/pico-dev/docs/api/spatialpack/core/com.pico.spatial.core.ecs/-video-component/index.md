# VideoComponent | PICO Spatial SDK

core / com.pico.spatial.core.ecs / VideoComponent 
# VideoComponent
```kotlin
@MainThread
```class  VideoComponent  :  Component 
A  Component  that can be constructed using a provided  VideoMaterial  and  MeshResource . With the given parameters, this component can be used to render a 3D video. 
By utilizing this component, you can project a 3D video onto the surface of a chosen entity. This component integrates with third-party video players, allowing video playback through the  android.view.Surface  method. 
## Usage Example:

```
//Create a video playerval mediaPlayer = MediaPlayer()mediaPlayer.setDataSource("your_video_path.mp4")mediaPlayer.prepare().........//Create a SpatialView to display the video.val videoEntity = Entity()SpatialView(    modifier = Modifier.size(782.dp, 412.dp),    initial =  { content, _ ->    //Create a mesh for the video    val mesh = MeshResource.createPlane(0.9f, 0.45f, 0.0f)    //Create a VideoMaterial for the video.    val videoMaterial = VideoMaterial(BlendingMode.OPAQUE,        VideoDimensionMode.MONO,        MaterialCullingMode.BACK)    //Create a SurfaceRenderTexture and acquire a surface, set it to player.    val surfaceRenderTexture = SurfaceRenderTexture()    surfaceRenderTexture.toGlobal()    videoMaterial.bindSurfaceRenderTexture(surfaceRenderTexture)    if(surfaceRenderTexture.valid)    {        val surface = surfaceRenderTexture.acquireSurface()        surface?.apply{            mediaPlayer.setSurface(surface)        }    }    //Create a VideoComponent for the video.    val videoComponent = VideoComponent(mesh, videoMaterial)    //Add video component to video entity.    videoEntity.apply {        components.set(videoComponent)    }    content.addEntity(videoEntity)    //Start playing the video.    mediaPlayer.start()    })......//Stop and release player and resource when no longer needed.mediaPlayer.stop()mediaPlayer.release()videoEntity.destroy()
```
#### See also
Surface Render Texture 
for how to acquire  android.view.Surface . 
Members 
## Constructors
Video Component 
```kotlin
constructor(meshResource: MeshResource, videoMaterial: VideoMaterial)
```
Creates a  VideoComponent  instance with the given  MeshResource  and  VideoMaterial . 
## Functions
clone 
```kotlin
open override fun clone(): Component
```
Creates and returns a copy of this  Component  instance. 
equals 
```kotlin
open operator override fun equals(other: Any?): Boolean
```get Audio Bind Id 
```kotlin
fun getAudioBindId(): Long?
```
Gets the audio binding ID when using  VideoComponent  to play video with spatial audio effects. 
get Display Mode 
```kotlin
fun getDisplayMode(): DisplayMode
```
Gets the display mode of the  VideoComponent . 
get Mesh 
```kotlin
fun getMesh(): MeshResource
```
Gets the mesh of the  VideoComponent . 
get Stereo Disparity 
```kotlin
fun getStereoDisparity(): Float
```
Gets the stereo disparity for 3D video, which adjusts the left/right eye rendering offset on the eye buffer. 
get Texture Sample Mode 
```kotlin
fun getTextureSampleMode(): VideoTextureSampleMode
```
Gets the  VideoTextureSampleMode  of the  VideoComponent  set before. Default:NONE. 
get Texture Sample Name 
```kotlin
fun getTextureSampleName(): String
```
Gets the texture sample name of the  VideoComponent  set before. 
get Video Material 
```kotlin
fun getVideoMaterial(): VideoMaterial
```
Gets the material of the  VideoComponent . 
hash Code 
```kotlin
open override fun hashCode(): Int
```set Display Mode 
```kotlin
fun setDisplayMode(displayMode: DisplayMode)
```
Sets the display mode of the  VideoComponent . 
set Material 
```kotlin
fun setMaterial(videoMaterial: VideoMaterial)
```
Sets the material of the  VideoComponent . 
set Mesh 
```kotlin
fun setMesh(meshResource: MeshResource)
```
Sets the mesh for the  VideoComponent . 
set Stereo Disparity 
```kotlin
fun setStereoDisparity(stereoDisparity: Float)
```
Sets the stereo disparity for 3D video. Only effective for 3D (non-mono) videos when DisplayMode is Stereo. The valid range is -40.0f, 40.0f. 
set Texture Sample Mode 
```kotlin
fun setTextureSampleMode(textureSampleMode: VideoTextureSampleMode)
```
Sets the  VideoTextureSampleMode  for the  VideoComponent  instance. Default is NONE. Typically used together with  setTextureSampleName . 
set Texture Sample Name 
```kotlin
fun setTextureSampleName(textureSampleName: String)
```
Sets the texture sample name for the  VideoComponent  instance. 
to String 
```kotlin
open override fun toString(): String
```trim Margin Rect 
```kotlin
fun trimMarginRect(marginRect: Rect)
```
Sets the margin rectangle of the  VideoComponent .