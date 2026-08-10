# registerCypressMediaPlayerCallback | PICO Spatial SDK

core / com.pico.spatial.core.ecs.video / CypressMediaPlayer / registerCypressMediaPlayerCallback 
# registerCypressMediaPlayerCallback
```kotlin
fun registerCypressMediaPlayerCallback(callBack: CypressMediaPlayerCallback)
```
Registers callback(s) for the player. 
Only the first registration takes effect; subsequent registrations will be ignored. 
Ensure the player is valid before calling this method, otherwise it will throw an  IllegalStateException . 
#### Parameters
call Back 
The  CypressMediaPlayerCallback  to register with the player.