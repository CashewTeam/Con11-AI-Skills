# load | PICO Spatial SDK

core / com.pico.spatial.core.ecs / Entity / Companion / load 
# load
```kotlin
@JvmStatic
```fun  load ( uriString :  String ) :  Entity 
Synchronously loads a 3D model from the specified URI string and returns its root entity. 
WARNING: 
- 
This method performs blocking I/O. While it can be called on the main thread, on slow devices or with unstable storage/content-provider latency it may cause jank or even ANR. 
- 
Prefer the async API  loadSuspend(...) . If you must use a sync call, execute it off the main thread or in a coroutine context such as  withContext(Dispatchers.IO) . 
For complex or high-resolution resources that require significant processing time, it is strongly recommended to leverage coroutines for loading. This approach prevents blocking the main thread, ensuring a responsive and fluid user experience. 
### Usage
Recommended to call within a coroutine context (preferably not  Dispatchers.Main ): 

```
val entity = withContext(Dispatchers.IO) {    Entity.load("asset://models/box.usdz")  // Asset example    // or    Entity.load("file:///sdcard/models/box.glb")  // File example}
```
### Performance notes
- 
This is a blocking I/O operation. Heavy operations block the calling thread. 
- 
Large models may cause frame drops or even ANR if called on main thread. 
- 
Textures are recommended to be pre-compressed (ASTC/ETC2). 
- 
Single texture memory limit: 256MB (includes mipmaps). 
- 
File access time affects loading duration. 
### Security considerations
- 
Ensure the file is accessible and has the necessary permissions. 
- 
Avoid loading models from files that may contain sensitive data. 
- 
Avoid loading models from files that are not intended for public consumption. 
#### Return
The root entity of the loaded scene. 
#### Parameters
uri String 
The URI representing the location of the 3D model to load. Supported URI schemes: 
- 
asset://  - Loads from application assets. 
- 
file://  - Loads from local storage. For  content://  URIs, use  load(contentResolver: ContentResolver, uri: Uri)  instead. 
#### See also
loadSuspend(String) for non-blocking alternative. 
#### Throws
Resource Loading Exception 
If loading fails due to invalid URI, missing file, unsupported format, and more. 
```kotlin
@JvmStatic
```fun  load ( file :  File ) :  Entity 
Synchronously loads a 3D model from a file and returns its root entity. 
WARNING: 
- 
This method performs blocking I/O. While it can be called on the main thread, on slow devices or with unstable storage access it may cause jank or even ANR. 
- 
Prefer the async API  loadSuspend(...) . If you must use a sync call, execute it off the main thread or in a coroutine context such as  withContext(Dispatchers.IO) . 
For complex or high-resolution resources that require significant processing time, it is strongly recommended to leverage coroutines for loading. This approach prevents blocking the main thread, ensuring a responsive and fluid user experience. 
### Usage
Recommended to call within a coroutine context (preferably not  Dispatchers.Main ): 

```
val entity = withContext(Dispatchers.IO) {    Entity.load(File("/sdcard/models/box.glb"))}
```
### Performance notes
- 
This is a blocking I/O operation. Heavy operations block the calling thread. 
- 
Large models may cause frame drops or even ANR if called on main thread. 
- 
Textures are recommended to be pre-compressed (ASTC/ETC2). 
- 
Single texture memory limit: 256MB (includes mipmaps). 
- 
File access time affects loading duration. 
### Security considerations
- 
Ensure the file is accessible and has the necessary permissions. 
- 
Avoid loading models from files that may contain sensitive data. 
- 
Avoid loading models from files that are not intended for public consumption. 
#### Return
The root entity of the loaded scene. 
#### Parameters
file 
The file containing the 3D model to load. The path must be accessible. Supported file formats: 
- 
USD variants:  .usdz ,  .usda ,  .usdc . 
- 
GLTF variants:  .glb ,  .gltf . 
#### See also
loadSuspend(File) for non-blocking alternative. 
#### Throws
Resource Loading Exception 
If loading fails due to invalid format, missing assets, exceeding memory limits, and more. 
```kotlin
@JvmStatic
```fun  load ( contentResolver :  ContentResolver ,  uri :  Uri ) :  Entity 
Synchronously loads a 3D model from a content provider URI and returns its root entity. 
WARNING: 
- 
This method performs blocking I/O. While it can be called on the main thread, with unstable content-provider response or high system load it may cause jank or even ANR. 
- 
Prefer the async API  loadSuspend(...) . If you must use a sync call, execute it off the main thread or in a coroutine context such as  withContext(Dispatchers.IO) . 
For complex or high-resolution resources that require significant processing time, it is strongly recommended to leverage coroutines for loading. This approach prevents blocking the main thread, ensuring a responsive and fluid user experience. 
To load a  .gltf  model, make sure that all data is stored in a single  .gltf  file. While for  Entity.load(uriString: String)  and  Entity.load(file: File) , you can also load a  .gltf  model stored in a folder (in this case, the actual data is stored in the  .bin  file, instead of the  .gltf  file). 
### Usage
Recommended to call within a coroutine context (preferably not  Dispatchers.Main ): 

```
val entity = withContext(Dispatchers.IO) {    Entity.load(        contentResolver,        Uri.parse("content://com.example.provider/models/box.glb")    )}
```
### Performance notes
- 
This is a blocking I/O operation. Heavy operations block the calling thread. 
- 
Large models may cause frame drops or even ANR if called on main thread. 
- 
The content URI is loaded through the in-memory path. The full model data is read before loading and may be temporarily retained in memory by the loading job. Loading multiple large models from content URIs in parallel can significantly increase peak memory usage and may cause an  OutOfMemoryError . 
- 
For remote models, large models, or list/grid experiences that load multiple models, prefer copying the data to an app cache file first, then call  load  with a  file://  URI or  load  with a  File . For pages that may start many large loads at once, consider limiting concurrent model loading to fit the device memory budget. 
- 
Textures are recommended to be pre-compressed (ASTC/ETC2). 
- 
Single texture memory limit: 256MB (includes mipmaps). 
- 
Content provider response time affects loading duration. 
### Security considerations
- 
Ensure the content provider has the necessary permissions to access the specified URI. 
- 
Avoid loading models from URIs that may contain sensitive data. 
#### Return
The root entity of the loaded scene. 
#### Parameters
content Resolver 
The  ContentResolver  for accessing the content provider. 
uri 
The content  Uri  pointing to the 3D model data. Only supports  content://  URIs. For other schemes such as  asset://  and  file://  URIs, use  load(uriString: String)  instead. 
#### See also
loadSuspend(ContentResolver, Uri) for non-blocking alternative. 
#### Throws
Resource Loading Exception 
If loading fails due to invalid data, unsupported format, exceeding memory limits, and more. 
Security Exception 
If the caller does not have permission to access the content provider. 
```kotlin
@JvmStatic
```fun  load ( inputStream :  InputStream ,  format :  ModelFormat ) :  Entity 
Synchronously loads a 3D model from an InputStream and returns its root entity. 
WARNING: 
- 
This method performs blocking I/O. While it can be called on the main thread, if the stream source or storage is unstable it may cause jank or even ANR. 
- 
Prefer the async API  loadSuspend(...) . If you must use a sync call, execute it off the main thread or in a coroutine context such as  withContext(Dispatchers.IO) . 
For complex or high-resolution resources that require significant processing time, it is strongly recommended to leverage coroutines for loading. This approach prevents blocking the main thread, ensuring a responsive and fluid user experience. 
### Supported Formats
- 
All  ModelFormat  variants supported by the engine. 
- 
Format must match the actual stream content. 
- 
To load a  .gltf  model, make sure that all data is stored in a single  .gltf  file. While for  Entity.load(uriString: String)  and  Entity.load(file: File) , you can also load a  .gltf  model stored in a folder (in this case, the actual data is stored in the  .bin  file, instead of the  .gltf  file). 
### Usage
Recommended to call within a coroutine context (preferably not  Dispatchers.Main ): 

```
val entity = withContext(Dispatchers.IO) {    context.assets.open("models/box.usdz").use { inputStream ->        Entity.load(inputStream, ModelFormat.USD)    }}
```
### Performance Notes
- 
This is a blocking I/O operation. Heavy operations block the calling thread. 
- 
Large models may cause frame drops or even ANR if called on main thread. 
- 
This API loads through the in-memory path. The full stream is read before loading and may be temporarily retained in memory by the loading job. Loading multiple large streams in parallel can significantly increase peak memory usage and may cause an  OutOfMemoryError . 
- 
For remote models, large models, or list/grid experiences that load multiple models, prefer downloading or copying the data to an app cache file first, then call  load  with a  file://  URI or  load  with a  File . For pages that may start many large loads at once, consider limiting concurrent model loading to fit the device memory budget. 
- 
Textures are recommended to be pre-compressed (ASTC/ETC2). 
- 
Single texture memory limit: 256MB (includes mipmaps). 
### Resource Management
- 
The caller is responsible for opening/closing the InputStream. 
- 
For automatic resource cleanup, use  .use { }  block as shown in example. 
#### Return
The root entity of the loaded scene. 
#### Parameters
input Stream 
The InputStream containing the raw model data. 
format 
The  ModelFormat  of the provided data (must match actual content). 
#### Throws
Resource Loading Exception 
If loading fails due to invalid data, unsupported format, exceeding memory limits exceeded, and more. 
```kotlin
@JvmStatic
```fun  load ( modelName :  String ,  bundle :  AssetBundle ) :  Entity 
Synchronously loads a 3D model from the specified  AssetBundle  and returns its root entity. 
WARNING: 
- 
This method performs blocking I/O. While it can be called on the main thread, with large bundles or unstable device/storage performance it may cause jank or even ANR. 
- 
Prefer the async API  loadSuspend(...) . If you must use a sync call, execute it off the main thread or in a coroutine context such as  withContext(Dispatchers.IO) . 
For complex or high-resolution resources that require significant processing time, it is strongly recommended to leverage coroutines for loading. This approach prevents blocking the main thread, ensuring a responsive and fluid user experience. 
### Supported file
- 
AssetBundle s ( .bundle ) will be automatically packaged into  asset://  when: 
- 
Spatial Tools dependency is properly configured; 
- 
Spatial Editor project is properly configured; 
- 
Both bundle name and model name are exactly matched; 
- 
Gradle build pipeline completes successfully. 
### Usage
Recommended to call within a coroutine context (preferably not  Dispatchers.Main ): 

```
val entity = withContext(Dispatchers.IO) {    AssetBundle.load("asset://main.bundle").use { bundle ->        Entity.load("character_model", bundle)    }}
```
### Performance Notes
- 
This is a blocking I/O operation. Heavy operations block the calling thread. 
- 
Large models may cause frame drops if called on main thread; 
- 
Textures are recommended to be pre-compressed (ASTC/ETC2); 
- 
Single texture memory limit: 256MB (includes mipmaps); 
- 
The AssetBundle should be closed after use (prefer  .use {}  block); 
### Error Handling & Requirements
- 
Model Name must exactly match USD "Scene" names (case-sensitive) in the corresponding Spatial Editor project. 
- 
Bundle name must match SpatialPackConfig settings in app's build.gradle. 
#### Return
The root entity of the loaded scene. 
#### Parameters
model Name 
The name of the model asset in the bundle (case-sensitive). 
bundle 
The loaded  AssetBundle  containing the model resources. 
#### See also
Asset Bundle. Companion. load 
for bundle loading procedure. 
#### Throws
Resource Loading Exception 
If loading fails due to missing model, invalid format, exceeding memory limits, and more.