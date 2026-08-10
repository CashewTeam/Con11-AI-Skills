# AudioMixerGroupsComponent | PICO Spatial SDK

core / com.pico.spatial.core.ecs / AudioMixerGroupsComponent 
# AudioMixerGroupsComponent
```kotlin
@MainThread
```class  AudioMixerGroupsComponent  :  Component 
A  Component  that manages audio mix groups for spatial audio processing. 
This component serves as a container for  AudioMixerGroupResource  instances associated with an  Entity , providing methods to: 
- 
Add new audio mix groups. 
- 
Remove existing groups. 
- 
Query currently attached groups. 
Members 
## Constructors
Audio Mixer Groups Component 
```kotlin
constructor()
```
Creates an  AudioMixerGroupsComponent  instance. 
```kotlin
constructor(mixerGroupResource: AudioMixerGroupResource)
```
Creates an  AudioMixerGroupsComponent  instance with a valid  AudioMixerGroupResource . 
## Functions
add Mixer Group 
```kotlin
fun addMixerGroup(mixerGroupResource: AudioMixerGroupResource)
```
Adds an  AudioMixerGroupResource  to this component. 
clear 
```kotlin
fun clear()
```
Clears all  AudioMixerGroupResource  in this component. 
clone 
```kotlin
open override fun clone(): Component
```
Creates and returns a copy of this  Component  instance. 
equals 
```kotlin
open operator override fun equals(other: Any?): Boolean
```get All Mixer Groups 
```kotlin
fun getAllMixerGroups(): List<AudioMixerGroupResource>
```
Gets all  AudioMixerGroupResource  in this component. 
get Mixer Group 
```kotlin
fun getMixerGroup(name: String): AudioMixerGroupResource?
```
Gets an  AudioMixerGroupResource  by its name. 
hash Code 
```kotlin
open override fun hashCode(): Int
```remove Mixer Group 
```kotlin
fun removeMixerGroup(name: String)
```
Removes an  AudioMixerGroupResource  by its name. If not found, no action is taken. 
to String 
```kotlin
open override fun toString(): String
```