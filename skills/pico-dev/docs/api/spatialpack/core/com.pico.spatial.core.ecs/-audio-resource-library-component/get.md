# get | PICO Spatial SDK

core / com.pico.spatial.core.ecs / AudioResourceLibraryComponent / get 
# get
```kotlin
fun get(name: String): AudioResource?
```
Gets an  AudioResource  from the  AudioResourceLibraryComponent  using a specified name. 
#### Return
The corresponding  AudioResource  if found; null otherwise. 
#### Parameters
name 
The name of the  AudioResource . The name must be unique, can have a maximum length of 256 bytes, and should only include characters from a-z, A-Z, 0-9, _. 
```kotlin
inline fun <T : AudioAsset> get(name: String): T?
```
Gets an  AudioAsset  of a specific type from the  AudioResourceLibraryComponent  using a specified name. 
#### Return
The corresponding  AudioAsset  if found and of the correct type; null otherwise. 
#### Parameters
T 
The type of  AudioAsset  to retrieve. Must be either  AudioResource  or  AudioGroupResource , or any future subclass of  AudioAsset . 
name 
The name of the  AudioAsset . The name must be unique, can have a maximum length of 256 bytes, and should only include characters from a-z, A-Z, 0-9, _. 
#### Throws
Illegal Argument Exception 
if the stored  AudioAsset  type does not match the requested type  T .