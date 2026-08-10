# reset | PICO Spatial SDK

core / com.pico.spatial.core.ecs.video / CypressMediaPlayer / reset 
# reset
```kotlin
fun reset(): Boolean
```
Resets the media player to its uninitialized state. 
This method performs the following actions sequentially: 
- 
Clears the current data source 
- 
Releases resources associated with the current playback 
- 
Brings the player back to the idle state 
After resetting, you must: 
- 
Call  setDataSource  to set a new data source 
- 
Call  prepare  or  prepareAsync  before starting playback again 
Typical use cases: 
- 
Switching between different video sources 
- 
Recovering from playback errors 
- 
Releasing resources before reusing the player instance 
Example usage: 

```
player.reset() // Reset existing configurationplayer.setDataSource("new_video.mp4") // Set new sourceplayer.prepare() // Prepare for playbackplayer.play() // Start playback
```
Note: 
- 
Do NOT call this method within any  CypressMediaPlayerCallback  methods (e.g. onPrepared, onCompleted). This may cause deadlocks or unexpected state conflicts. 
#### Return
true  if the reset operation succeeded,  false  otherwise. A return value of  false  typically indicates:     - The player is in an invalid state (already closed).     - Internal resource release failed. 
#### See also
Cypress Media Player. set Data Source 
For setting new data sources after reset 
Cypress Media Player. prepare 
For asynchronous preparation 
#### Throws
Illegal State Exception 
if called on an invalid player instance. Always check valid before invocation.