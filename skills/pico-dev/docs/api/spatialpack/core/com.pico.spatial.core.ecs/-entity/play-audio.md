# playAudio | PICO Spatial SDK

core / com.pico.spatial.core.ecs / Entity / playAudio 
# playAudio
```kotlin
@MainThread
```fun  playAudio ( audioResource :  AudioAsset ) :  AudioPlayerController 
Plays the specified audio attached to the entity and returns a controller to manage audio playback. 
Ensure that the entity has one of the following components before calling this method:  ObjectAudioComponent ,  AmbientAudioComponent , or  ChannelAudioComponent . 
Note: 
- 
For same audio resource, the same controller will be returned until the controller is closed. 
- 
Users should check the controller's  valid  property before use to ensure successful preparation. 
- 
Highly recommended to hold the return controller for same audio resource to play multiple times. 
- 
For Single SpatialAPP, the max number of controllers that can be created is 40(ObjectAudio+AmbientAudio)+40(ChannelAudio) at some time. 
- 
For System, the max number of controllers that can be created is 256(ObjectAudio+AmbientAudio)+256(ChannelAudio) at some time. 
#### Return
An  AudioPlayerController  instance for managing audio playback if the operation succeeds; otherwise, returns an invalid controller. Users should check the controller's  valid  property before use. 
#### Parameters
audio Resource 
The  AudioAsset  instance representing the audio to play, can be  AudioResource  or  AudioGroupResource .