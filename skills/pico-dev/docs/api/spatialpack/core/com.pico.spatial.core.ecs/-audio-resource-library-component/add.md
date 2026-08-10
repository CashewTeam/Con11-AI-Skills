# add | PICO Spatial SDK

core / com.pico.spatial.core.ecs / AudioResourceLibraryComponent / add 
# add
```kotlin
fun add(name: String, resource: AudioAsset): Boolean
```
Adds an  AudioAsset  to the  AudioResourceLibraryComponent  using a specified name. 
#### Return
true  if the  AudioAsset  is added successfully;  false  otherwise. 
#### Parameters
name 
The name for the  AudioAsset , which must be unique and can have a maximum length of 256 bytes. The name should only include characters from a-z, A-Z, 0-9, _. 
resource 
The  AudioAsset  to be added. Can be either  AudioResource  or  AudioGroupResource .