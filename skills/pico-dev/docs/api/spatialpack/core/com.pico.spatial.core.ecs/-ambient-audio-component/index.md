# AmbientAudioComponent | PICO Spatial SDK

core / com.pico.spatial.core.ecs / AmbientAudioComponent 
# AmbientAudioComponent
```kotlin
@MainThread
```class  AmbientAudioComponent  :  Component 
A  Component  used to create ambient audio effects in the scene, such as ambient sound effects, ambient music, and more. 
This component takes the audio source's relative orientation into account, creating a more immersive and realistic audio experience. 
Notes: 
- 
Do not add  ObjectAudioComponent ,  AmbientAudioComponent , and  ChannelAudioComponent  to the same entity simultaneously. 
- 
Always add  ObjectAudioComponent ,  AmbientAudioComponent , or  ChannelAudioComponent  to the entity before calling  Entity.prepareAudio  or  Entity.playAudio . 
Members 
## Constructors
Ambient Audio Component 
```kotlin
constructor()
```
Creates a new  AmbientAudioComponent  with default settings. 
```kotlin
constructor(@FloatRange(from = 0.0, to = 1.0) volume: Float = 1.0f, ambientOrientationMode: AmbientOrientationMode = AmbientOrientationMode.ORIENTATION_ONLY)
```
Creates an  AmbientAudioComponent  instance with the specified volume and ambient orientation mode. 
## Properties
ambient Orientation Mode 
```kotlin
var ambientOrientationMode: AmbientOrientationMode
```
The ambient orientation mode for audio. 
volume 
```kotlin
var volume: Float
```
The volume value of audio, range  [0.0, 1.0] , Default value is 1.0f. 
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