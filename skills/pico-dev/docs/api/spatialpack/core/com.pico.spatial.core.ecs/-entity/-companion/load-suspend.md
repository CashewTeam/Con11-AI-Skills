# loadSuspend | PICO Spatial SDK

core / com.pico.spatial.core.ecs / Entity / Companion / loadSuspend 
# loadSuspend
```kotlin
@JvmStatic
```suspend  fun  loadSuspend ( uriString :  String ) :  Entity 
Asynchronously loads a 3D model from the specified URI string and returns its root entity. 
For  content://  scheme, use  Entity.loadSuspend(contentResolver: ContentResolver, uri: Uri)  instead. 
#### Return
The loaded root entity, which is attached to the scene. If any error occurs during the loading process, an  ResourceLoadingException  will be thrown. 
#### Parameters
uri String 
The URI representing the location of the 3D model to load. Currently supported schemes include  asset://  and  file:// . 
```kotlin
@JvmStatic
```suspend  fun  loadSuspend ( file :  File ) :  Entity 
Asynchronously loads a 3D model from a file and returns its root entity. 
#### Return
The loaded root entity, which is attached to the scene. If any error occurs during the loading process, an  ResourceLoadingException  will be thrown. 
#### Parameters
file 
The file containing the 3D model data to load. Supported file formats are .usdz and .glb. 
```kotlin
@JvmStatic
```suspend  fun  loadSuspend ( contentResolver :  ContentResolver ,  uri :  Uri ) :  Entity 
Asynchronously loads a 3D model from a content provider URI and returns its root entity. 
For  asset://  or  file://  scheme, use  Entity.load(uriString: String)  instead. 
### Memory and concurrency notes
- 
This API loads through the in-memory path. The full content URI data is read before the asynchronous load starts and may be temporarily retained in memory until the loading job completes. 
- 
Loading multiple large content URI models in parallel can significantly increase peak memory usage and may cause an  OutOfMemoryError . 
- 
For remote models, large models, or list/grid experiences that load multiple models, prefer copying the data to an app cache file first, then call  loadSuspend  with a  file://  URI or  loadSuspend  with a  File . For pages that may start many large loads at once, consider limiting concurrent model loading to fit the device memory budget. 
#### Return
The loaded root entity, which is attached to the scene. If any error occurs during the loading process, an  ResourceLoadingException  will be thrown. 
#### Parameters
content Resolver 
The  ContentResolver  for accessing the content provider. 
uri 
The content  Uri  pointing to the 3D model data. Only  content://  scheme is supported. 
```kotlin
@JvmStatic
```suspend  fun  loadSuspend ( inputStream :  InputStream ,  format :  ModelFormat ) :  Entity 
Asynchronously loads a 3D model from an InputStream and returns its root entity. 
### Memory and concurrency notes
- 
This API loads through the in-memory path. The full stream is read before the asynchronous load starts and may be temporarily retained in memory until the loading job completes. 
- 
Loading multiple large streams in parallel can significantly increase peak memory usage and may cause an  OutOfMemoryError . 
- 
For remote models, large models, or list/grid experiences that load multiple models, prefer downloading or copying the data to an app cache file first, then call  loadSuspend  with a  file://  URI or  loadSuspend  with a  File . For pages that may start many large loads at once, consider limiting concurrent model loading to fit the device memory budget. 
#### Return
The loaded root entity, which is attached to the scene. If any error occurs during the loading process, an  ResourceLoadingException  will be thrown. 
#### Parameters
input Stream 
The InputStream containing the raw model data. 
format 
The  ModelFormat  of the source of the InputStream that should be specified explicitly. 
```kotlin
@JvmStatic
```suspend  fun  loadSuspend ( modelName :  String ,  bundle :  AssetBundle ) :  Entity 
Asynchronously loads an entity from the specified model name in the  AssetBundle , and the root node will be returned as an entity. 
#### Return
The loaded root entity, which is attached to the scene. If any error occurs during the loading process, an  ResourceLoadingException  will be thrown. 
#### Parameters
model Name 
The name of the model in the asset bundle. 
bundle 
The asset bundle containing the model.