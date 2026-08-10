# CypressMediaPlayer | PICO Spatial SDK

core / com.pico.spatial.core.ecs.video / CypressMediaPlayer 
# CypressMediaPlayer
```kotlin
class CypressMediaPlayer : Closeable
```
Controls video playback in combination with  VideoPlayerComponent . 
Currently, as part of the Spatial Video Module,  CypressMediaPlayer  cannot render videos independently. It only provides APIs for controlling video playback, including  play ,  pause ,  stop , and more. Video Rendering must be done with  VideoPlayerComponent . 
It's recommended to check the player's validity before using its APIs. 
### Code sample:

```
// Create the media playerval player = CypressMediaPlayer()// Implement the callbackval callback =    object : CypressMediaPlayerCallback {        override fun onPrepared() {           player?.apply {                play()                Log.i(TAG, "onPrepared Event")            }        }        // Override other methods    }// Register the callbackplayer.registerPlayerCallBack(callBack)// Set the video sourceplayer.setDataSource("your_video_path.mp4")// Create a mesh and materialval mesh = MeshResource.generatePanel(2.0f, 1.0f, 0.3f)val material =    VideoMaterial(        BlendingMode.TRANSPARENT,        VideoDimensionMode.SIDE_BY_SIDE,        MaterialCullingMode.BACK    )// Create an entity, a VideoPlayerComponent, and add the component to the entityval entity = Entity()if (mesh.valid && material.valid) {    val videoPlayerComponent = VideoPlayerComponent(player,mesh, material)    entity.components.set(videoPlayerComponent)    // We recommend to call prepareAsync() first. Since preparation is asynchronous, you should    // wait for the [CypressMediaPlayerCallback.onPrepared] callback before other methods.    player.prepareAsync()    // Other operations to control the playback   }// Release the resourceplayer.unregisterCypressMediaPlayerCallback()player.close()
```Members 
## Constructors
Cypress Media Player 
```kotlin
constructor()
```
Constructs a new  CypressMediaPlayer  instance. 
## Properties
valid 
```kotlin
@get:JvmName(name = "isValid")
```val  valid :  Boolean 
The current state of the player. 
## Functions
close 
```kotlin
open override fun close()
```
Releases the player manually to free the resources and memory it occupies. 
get Current Position 
```kotlin
fun getCurrentPosition(): Long
```
Gets the current playback position of the video in milliseconds. 
get Duration 
```kotlin
fun getDuration(): Long
```
Gets the total duration of the video, in milliseconds. 
get Playback Speed 
```kotlin
fun getPlaybackSpeed(): Float
```
Gets the playback speed of the player. 
get Video Height 
```kotlin
fun getVideoHeight(): Int
```
Gets the height of the currently configured video data source. 
get Video Width 
```kotlin
fun getVideoWidth(): Int
```
Gets the width of the currently configured video data source. 
get Volume 
```kotlin
fun getVolume(): Float
```
Gets the volume of video playback. 
is Complete 
```kotlin
fun isComplete(): Boolean
```
Checks whether the video playback is complete. 
is Playing 
```kotlin
fun isPlaying(): Boolean
```
Checks whether the video is currently playing. 
pause 
```kotlin
fun pause(): Boolean
```
Pauses video playback. 
play 
```kotlin
fun play(): Boolean
```
Starts video playback. 
prepare 
```kotlin
fun prepare(): Boolean
```
Prepares the video player for playback. 
prepare Async 
```kotlin
fun prepareAsync(): Boolean
```
Asynchronously prepares the video for playback. 
register Cypress Media Player Callback 
```kotlin
fun registerCypressMediaPlayerCallback(callBack: CypressMediaPlayerCallback)
```
Registers callback(s) for the player. 
reset 
```kotlin
fun reset(): Boolean
```
Resets the media player to its uninitialized state. 
resume 
```kotlin
fun resume(): Boolean
```
Resumes video playback. 
seek To 
```kotlin
fun seekTo(time: Long): Boolean
```
Seeks to the specified position in the video. 
set Data Source 
```kotlin
fun setDataSource(afd: AssetFileDescriptor): Boolean
```
Sets a video file as the data source using an  AssetFileDescriptor . It is safe to close the  AssetFileDescriptor  after setting the data source. 
```kotlin
fun setDataSource(path: String): Boolean
```
Sets a video file as the data source for the player. 
```kotlin
fun setDataSource(fd: Int, offset: Long, length: Long): Boolean
```
Sets a video file as the data source using a file descriptor, offset, and length. It is safe to close the file descriptor after setting the data source. 
set Loop 
```kotlin
fun setLoop(loop: Boolean): Boolean
```
Sets the loop mode for video playback. 
set Playback Speed 
```kotlin
fun setPlaybackSpeed(speed: Float): Boolean
```
Sets the speed for video playback. 
set Volume 
```kotlin
fun setVolume(volume: Float): Boolean
```
Sets the volume for video playback. 
stop 
```kotlin
fun stop(): Boolean
```
Stops video playback. 
unregister Cypress Media Player Callback 
```kotlin
fun unregisterCypressMediaPlayerCallback()
```
Unregisters all callback(s) for the player.