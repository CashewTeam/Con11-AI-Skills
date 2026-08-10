# contains | PICO Spatial SDK

core / com.pico.spatial.core.ecs / AudioResourceLibraryComponent / contains 
# contains
```kotlin
fun contains(name: String): Boolean
```
Checks if the  AudioResourceLibraryComponent  contains an  AudioResource  with the given name. 
#### Return
true  if the  AudioResource  is found;  false  otherwise. 
#### Parameters
name 
The name of the  AudioResource . The name must be unique, can have a maximum length of 256 bytes, and should only include characters from a-z, A-Z, 0-9, _.