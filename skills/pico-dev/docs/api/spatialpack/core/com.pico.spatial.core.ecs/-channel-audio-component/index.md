# ChannelAudioComponent | PICO Spatial SDK

core / com.pico.spatial.core.ecs / ChannelAudioComponent 
# ChannelAudioComponent
```kotlin
@MainThread
```class  ChannelAudioComponent  :  Component 
A  Component  that can be added to an entity to enable channel audio effects. 
This component do not take audio source's position and orientation into account, left channel is heard from the left, and the right channel is heard from the right. 
Notes: 
- 
Do not add  ObjectAudioComponent ,  AmbientAudioComponent , and  ChannelAudioComponent  to the same entity simultaneously. 
- 
Always add  ObjectAudioComponent ,  AmbientAudioComponent , or  ChannelAudioComponent  to the entity before calling  Entity.prepareAudio  or  Entity.playAudio . 
Members 
## Constructors
Channel Audio Component 
```kotlin
constructor()
```
Creates a  ChannelAudioComponent  instance with empty settings. 
```kotlin
constructor(@FloatRange(from = 0.0, to = 1.0) volume: Float = 1.0f)
```
Creates a  ChannelAudioComponent  with an initial volume. 
## Properties
volume 
```kotlin
var volume: Float
```
The volume of the audio. The valid value range is  [0.0, 1.0] . The default value is  1.0f . 
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