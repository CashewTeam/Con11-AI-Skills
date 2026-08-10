# remove | PICO Spatial SDK

core / com.pico.spatial.core.ecs / AudioResourceLibraryComponent / remove 
# remove
```kotlin
fun remove(name: String)
```
Removes an  AudioAsset  from the  AudioResourceLibraryComponent  using a specified name. 
#### Parameters
name 
The name of the  AudioAsset  to be removed. The name must be unique, can have a maximum length of 256 bytes, and should only contain characters from a-z, A-Z, 0-9, _.