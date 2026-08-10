# VideoPlayerComponent | PICO Spatial SDK

core / com.pico.spatial.core.ecs / VideoPlayerComponent 
# VideoPlayerComponent
```kotlin
@MainThread
```class  VideoPlayerComponent  :  Component 
A  Component  that can be constructed with  CypressMediaPlayer ,  VideoMaterial , and  MeshResource , allowing you to render a 3D video. 
This component allows you to play a 3D video on the surface of a specified entity. It utilizes  CypressMediaPlayer  as the video player and is a high-level component, Using this component for 3D video rendering is highly recommended due to its simplicity and ease of use. 
## Usage Example:

```
//Create an entityval entity = Entity()//Create playerval player = CypressMediaPlayer()//Implement callbackval callback =    object : CypressMediaPlayerCallback {        override fun onPrepared() {           player?.apply {                play()                Log.i(TAG, "onPrepared Event")            }        }        override fun onStarted() {            Log.i(TAG, "onStarted Event")        }        override fun onStopped() {            Log.i(TAG, "onStopped Event")        }        override fun onCompleted() {            Log.i(TAG, "onCompleted Event")        }        override fun onSeekToCompleted() {            Log.i(TAG, "onSeekToCompleted Event")        }        override fun onError(error: CypressMediaPlayerErrorCode) {            Log.e(TAG, "onError Event, error: $error")        }        override fun onPaused() {            Log.i(TAG, "onPaused Event")        }        override fun onVideoSizeChanged(width: Int, height: Int) {            Log.i(TAG, "onVideoSizeChanged Event, width: $width, height: $height")        }    }//Register callbackplayer.registerPlayerCallBack(callback)//setDataSourceplayer.setDataSource("your_video_path.mp4")//create meshval mesh = MeshResource.generatePanel(2.0f, 1.0f, 0.3f)//create materialval videoMat =    VideoMaterial(        BlendingMode.TRANSPARENT,        VideoDimensionMode.SIDE_BY_SIDE,        MaterialCullingMode.BACK    )//create VideoPlayerComponentif (mesh.valid && videoMat.valid) {    val videoPlayerComponent = VideoPlayerComponent(player,mesh, videoMat)    //add component to entity    entity.components.set(videoPlayerComponent)    //prepareAsync, after VideoPlayerComponent is added to entity, the video can start to play.    //you can also call the prepareAsync method to prepare the video and because the prepare is asynchronously,    //so please play it when the prepare callback happened.    player.prepareAsync()    //do something you want to do, you can control the video by the player.   }//release resources, you can call the close method to release the resources manually one by one.entity.destroy()//release player when you don't need it anymore, don't forget to call the close method to release the player.player.unregisterCypressMediaPlayerCallback()player.close()
```
#### See also
Cypress Media Player 
for how to create a CypressMediaPlayer. 
Video Material 
for how to create a VideoMaterial. 
Mesh Resource 
for how to create a MeshResource. 
Members 
## Constructors
Video Player Component 
```kotlin
constructor(player: CypressMediaPlayer, meshResource: MeshResource, videoMaterial: VideoMaterial)
```
Creates a  VideoPlayerComponent  instance with the given  CypressMediaPlayer ,  MeshResource , and  VideoMaterial , allowing the user to create a customized mesh themselves or use an existing model's mesh to render the video on the model entity's surface. 
## Functions
clone 
```kotlin
open override fun clone(): Component
```
Creates and returns a copy of this  Component  instance. 
equals 
```kotlin
open operator override fun equals(other: Any?): Boolean
```get Display Mode 
```kotlin
fun getDisplayMode(): DisplayMode
```
Gets the display mode of the  VideoPlayerComponent . 
get Mesh 
```kotlin
fun getMesh(): MeshResource
```
Gets the  MeshResource  of the  VideoPlayerComponent  instance. 
get Stereo Disparity 
```kotlin
fun getStereoDisparity(): Float
```
Gets the stereo disparity for 3D video, which adjusts the left/right eye rendering offset on the eye buffer. 
get Texture Sample Mode 
```kotlin
fun getTextureSampleMode(): VideoTextureSampleMode
```
Gets the  VideoTextureSampleMode  of the  VideoPlayerComponent  set before. Default:NONE. 
get Texture Sample Name 
```kotlin
fun getTextureSampleName(): String
```
Gets the texture sample name of the  VideoPlayerComponent  set before. 
get Video Material 
```kotlin
fun getVideoMaterial(): VideoMaterial
```
Gets the material of the  VideoPlayerComponent . 
get Video Player 
```kotlin
fun getVideoPlayer(): CypressMediaPlayer
```
Gets the specified  CypressMediaPlayer  instance you set. 
hash Code 
```kotlin
open override fun hashCode(): Int
```set Display Mode 
```kotlin
fun setDisplayMode(displayMode: DisplayMode)
```
Sets the display mode of the  VideoPlayerComponent . 
set Material 
```kotlin
fun setMaterial(material: VideoMaterial)
```
Sets the  VideoMaterial  of the  VideoPlayerComponent  instance. 
set Mesh 
```kotlin
fun setMesh(meshResource: MeshResource)
```
Sets the  MeshResource  of the  VideoPlayerComponent  instance. 
set Stereo Disparity 
```kotlin
fun setStereoDisparity(stereoDisparity: Float)
```
Sets the stereo disparity for 3D video. Only effective for 3D (non-mono) videos when DisplayMode is Stereo. The valid range is -40.0f, 40.0f. 
set Texture Sample Mode 
```kotlin
fun setTextureSampleMode(textureSampleMode: VideoTextureSampleMode)
```
Sets the  VideoTextureSampleMode  for the  VideoPlayerComponent  instance. Default is NONE. Typically used together with  setTextureSampleName . 
set Texture Sample Name 
```kotlin
fun setTextureSampleName(textureSampleName: String)
```
Sets the texture sample name for the  VideoPlayerComponent  instance. 
to String 
```kotlin
open override fun toString(): String
```