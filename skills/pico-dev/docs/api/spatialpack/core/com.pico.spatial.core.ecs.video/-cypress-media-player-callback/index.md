# CypressMediaPlayerCallback | PICO Spatial SDK

core / com.pico.spatial.core.ecs.video / CypressMediaPlayerCallback 
# CypressMediaPlayerCallback
```kotlin
interface CypressMediaPlayerCallback
```
Defines callbacks for  CypressMediaPlayer  events such as playback state changes, errors, and completion. 
Implement this interface to receive notifications from a  CypressMediaPlayer  instance. Register your implementation using  CypressMediaPlayer.registerCypressMediaPlayerCallback  to react to events like: 
- 
Playback state changes (for example, prepared, started, completed). 
- 
Errors during media playback. 
- 
Completion of seek operation. 
### Code sample:

```
val callback = object : CypressMediaPlayerCallback {    override fun onPrepared() {        // Operations after the playback is prepared        // Recommended to call play() here to ensure the playback is fully prepared        player?.apply {            play()        }    }    override fun onStarted() {        // Operations after the playback starts    }    override fun onCompleted() {       // Operations after the playback completes    }    override fun onSeekToCompleted() {       // Operations after the seek operation is completed    }    override fun onError(error: CypressMediaPlayerErrorCode) {        // Handle errors    }    override fun onPaused() {        // Operations after the playback is paused    }    override fun onStopped() {        // Operations after the playback is stopped    }    override fun onVideoSizeChanged(width: Int, height: Int) {        // Operations when the video size changes    }}cypressMediaPlayer.registerCypressMediaPlayerCallback(callBack)
```Members 
## Functions
on Completed 
```kotlin
abstract fun onCompleted()
```
Callback triggered when video playback reaches the end. 
on Error 
```kotlin
abstract fun onError(error: CypressMediaPlayerErrorCode)
```
Callback triggered when an error occurs. 
on Paused 
```kotlin
abstract fun onPaused()
```
Callback triggered when the video playback is paused. 
on Prepared 
```kotlin
abstract fun onPrepared()
```
Callback triggered after the user calls the  CypressMediaPlayer.prepareAsync()  method. 
on Seek To Completed 
```kotlin
abstract fun onSeekToCompleted()
```
Callback triggered after the user calls the  CypressMediaPlayer.seekTo()  method, and the video completes the seek operation. 
on Started 
```kotlin
abstract fun onStarted()
```
Callback triggered after the user calls the  CypressMediaPlayer.play()  method. 
on Stopped 
```kotlin
abstract fun onStopped()
```
Callback triggered when the video playback is stopped. 
on Video Size Changed 
```kotlin
abstract fun onVideoSizeChanged(width: Int, height: Int)
```
Callback triggered when the video size changes.