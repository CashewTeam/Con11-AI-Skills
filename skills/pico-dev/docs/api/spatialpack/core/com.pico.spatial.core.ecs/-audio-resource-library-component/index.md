# AudioResourceLibraryComponent | PICO Spatial SDK

core / com.pico.spatial.core.ecs / AudioResourceLibraryComponent 
# AudioResourceLibraryComponent
```kotlin
@MainThread
```class  AudioResourceLibraryComponent  :  Component 
A  Component  that manages audio resources as a key-value dictionary for organized audio playback. 
This component provides centralized storage and access to  AudioResource  instances using named keys.  AudioResource s can be added, removed, and retrieved using named keys, enabling: 
- 
Structured audio resource management. 
- 
Dynamic runtime audio switching. 
- 
Timeline integration for sequenced playback. 
Members 
## Constructors
Audio Resource Library Component 
```kotlin
constructor()
```
Constructs an empty  AudioResourceLibraryComponent . 
## Functions
add 
```kotlin
fun add(name: String, resource: AudioAsset): Boolean
```
Adds an  AudioAsset  to the  AudioResourceLibraryComponent  using a specified name. 
clear 
```kotlin
fun clear()
```
Removes all  AudioResource s and  AudioGroupResource s from the  AudioResourceLibraryComponent . 
clone 
```kotlin
open override fun clone(): Component
```
Creates and returns a copy of this  Component  instance. 
contains 
```kotlin
fun contains(name: String): Boolean
```
Checks if the  AudioResourceLibraryComponent  contains an  AudioResource  with the given name. 
equals 
```kotlin
open operator override fun equals(other: Any?): Boolean
```get 
```kotlin
fun get(name: String): AudioResource?
```
Gets an  AudioResource  from the  AudioResourceLibraryComponent  using a specified name. 
```kotlin
inline fun <T : AudioAsset> get(name: String): T?
```
Gets an  AudioAsset  of a specific type from the  AudioResourceLibraryComponent  using a specified name. 
get All Audio Group Resources 
```kotlin
fun getAllAudioGroupResources(): List<AudioGroupResource>
```
Gets all  AudioGroupResource s within the  AudioResourceLibraryComponent . 
get All Audio Resources 
```kotlin
fun getAllAudioResources(): List<AudioResource>
```
Gets all  AudioResource s within the  AudioResourceLibraryComponent . 
get All Names 
```kotlin
fun getAllNames(): List<String>
```
Gets the names of all  AudioResource s and  AudioGroupResource s within the  AudioResourceLibraryComponent . 
hash Code 
```kotlin
open override fun hashCode(): Int
```remove 
```kotlin
fun remove(name: String)
```
Removes an  AudioAsset  from the  AudioResourceLibraryComponent  using a specified name. 
to String 
```kotlin
open override fun toString(): String
```