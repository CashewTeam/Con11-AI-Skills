# setDataSource | PICO Spatial SDK

core / com.pico.spatial.core.ecs.video / CypressMediaPlayer / setDataSource 
# setDataSource
```kotlin
fun setDataSource(path: String): Boolean
```
Sets a video file as the data source for the player. 
Ensure the player is valid before calling this method, otherwise it will throw an  IllegalStateException . 
#### Return
true  if the data source is set successfully;  false  otherwise. 
#### Parameters
path 
The path to the video file. It can be a storage path (not Android assets) or a URL. or url path. 
```kotlin
fun setDataSource(fd: Int, offset: Long, length: Long): Boolean
```
Sets a video file as the data source using a file descriptor, offset, and length. It is safe to close the file descriptor after setting the data source. 
Ensure the player is valid before calling this method, otherwise it will throw an  IllegalStateException . 
#### Return
true  if the data source is set successfully;  false  otherwise. 
#### Parameters
fd 
The file descriptor of the video file. 
offset 
The offset of the video file. 
length 
the length of the video file. 
```kotlin
fun setDataSource(afd: AssetFileDescriptor): Boolean
```
Sets a video file as the data source using an  AssetFileDescriptor . It is safe to close the  AssetFileDescriptor  after setting the data source. 
Ensure the player is valid before calling this method, otherwise it will throw an  IllegalStateException . 
#### Return
true  if the data source is set successfully;  false  otherwise. 
#### Parameters
afd 
The  AssetFileDescriptor  of the video file. 
#### See also
Asset File Descriptor