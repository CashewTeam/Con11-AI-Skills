# file | PICO Spatial SDK

ui:foundation / com.pico.spatial.ui.foundation.content / Source / Companion / file 
# file
```kotlin
fun file(localFile: File): Source<String>
```
Create a data source from a local file. 
Creates a file data source using the given File object, supporting loading model files from the local file system. 
#### Return
File data source instance 
#### Parameters
local File 
The local file object to be loaded 
```kotlin
fun file(absolutePath: String): Source<String>
```
Create a data source from an absolute file path. 
Creates a file data source using the given absolute path string, supporting loading model files from the local file system. 
#### Return
File data source instance 
#### Parameters
absolute Path 
The absolute path of the file to be loaded