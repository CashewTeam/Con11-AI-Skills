# ObjectAudioComponent | PICO Spatial SDK

core / com.pico.spatial.core.ecs / ObjectAudioComponent 
# ObjectAudioComponent
```kotlin
@MainThread
```class  ObjectAudioComponent  :  Component 
A  Component  used to create spatial audio effects in the scene, such as spatial sound effects, spatial music, and so on. 
This component takes the audio source's position and orientation into account, and therefore create a more immersive and realistic audio experience. 
This component supports only mono (single-channel) audio. It automatically downmixes any multichannel sources to mono. For best quality and to avoid unintended artifacts, use mono audio whenever possible. 
Notes: 
- 
Do not add  ObjectAudioComponent ,  AmbientAudioComponent , and  ChannelAudioComponent  to the same entity simultaneously. 
- 
Always add  ObjectAudioComponent ,  AmbientAudioComponent , or  ChannelAudioComponent  to the entity before calling  Entity.prepareAudio  or  Entity.playAudio . 
Members 
## Constructors
Object Audio Component 
```kotlin
constructor()
```
The default constructor for  ObjectAudioComponent  with no parameters. 
```kotlin
constructor(@FloatRange(from = 0.0, to = 1.0) volume: Float = 1.0f, directivity: Directivity = Directivity(0.0f, 0.0f), distanceAttenuationMode: DistanceAttenuationMode = DistanceAttenuationMode.INVERSE_SQUARED, reverbVolume: Float = 1.0f, soundRadiusLevel: Float = 0.1f)
```
Creates a new ObjectAudioComponent with the specified parameters. 
## Properties
directivity 
```kotlin
var directivity: Directivity
```
The directivity of the  ObjectAudioComponent . The valid value range is  ([0.0, 1.0],[0.0, ∞]) . The default value is  (0.0,0.0) . For more information about directivity, refer to  Directivity . 
distance Attenuation Mode 
```kotlin
var distanceAttenuationMode: DistanceAttenuationMode
```
The distance attenuation mode for audio. 
reverb Volume 
```kotlin
var reverbVolume: Float
```
The reverb volume level of the  ObjectAudioComponent . The valid value range is  [0.0, 1.0] . The default value is  1.0f . 
sound Radius Level 
```kotlin
var soundRadiusLevel: Float
```
The sound radius level of the  ObjectAudioComponent . The valid value should above 0.0f. The default value is  0.1f . 
volume 
```kotlin
var volume: Float
```
The volume of audio. The valid value range is  [0.0, 1.0] . The default value is  1.0f . 
## Functions
clone 
```kotlin
open override fun clone(): Component
```
Creates and returns a copy of this  Component  instance. 
equals 
```kotlin
open operator override fun equals(other: Any?): Boolean
```hash Code 
```kotlin
open override fun hashCode(): Int
```to String 
```kotlin
open override fun toString(): String
```