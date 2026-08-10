# AudioMixerGroupResource | PICO Spatial SDK

core / com.pico.spatial.core.ecs.resource / AudioMixerGroupResource 
# AudioMixerGroupResource
```kotlin
class AudioMixerGroupResource : Resource
```
Manages a group of audio resources. 
Provides group-level volume and playback speed control for audio resources configured with  com.pico.spatial.core.ecs.audio.AudioResourceConfig  using the same  mixerGroupID . 
The name of the  AudioMixerGroupResource  acts as the link between  AudioResource  and  AudioMixerGroupResource . To control volume and playback speed by group, audio resources must be loaded with a  com.pico.spatial.core.ecs.audio.AudioResourceConfig  whose  mixerGroupID  matches the name of this  AudioMixerGroupResource . 
Members 
## Constructors
Audio Mixer Group Resource 
```kotlin
constructor(name: String, volume: Float = 1.0f, playbackSpeed: Float = 1.0f)
```
Creates an  AudioMixerGroupResource  with a specified name, volume, and playback speed. 
## Functions
close 
```kotlin
open override fun close()
```
You need to manually release the resource to free the memory it occupies. 
get Name 
```kotlin
fun getName(): String
```
Gets the name of this  AudioMixerGroupResource . 
get Playback Speed 
```kotlin
fun getPlaybackSpeed(): Float
```
Gets the playback speed of this  AudioMixerGroupResource . 
get Volume 
```kotlin
fun getVolume(): Float
```
Gets the volume of this  AudioMixerGroupResource . 
set Playback Speed 
```kotlin
fun setPlaybackSpeed(playbackSpeed: Float)
```
Sets the playback speed of this  AudioMixerGroupResource . 
set Volume 
```kotlin
fun setVolume(volume: Float)
```
Sets the volume of this  AudioMixerGroupResource .