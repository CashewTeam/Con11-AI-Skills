# Companion | PICO Spatial SDK

core / com.pico.spatial.core.ecs / Entity / Companion 
# Companion
```kotlin
object Companion
```
The companion object of  Entity . 
Members 
## Functions
load 
```kotlin
@JvmStatic
```fun  load ( file :  File ) :  Entity 
Synchronously loads a 3D model from a file and returns its root entity. 
```kotlin
@JvmStatic
```fun  load ( uriString :  String ) :  Entity 
Synchronously loads a 3D model from the specified URI string and returns its root entity. 
```kotlin
@JvmStatic
```fun  load ( contentResolver :  ContentResolver ,  uri :  Uri ) :  Entity 
Synchronously loads a 3D model from a content provider URI and returns its root entity. 
```kotlin
@JvmStatic
```fun  load ( inputStream :  InputStream ,  format :  ModelFormat ) :  Entity 
Synchronously loads a 3D model from an InputStream and returns its root entity. 
```kotlin
@JvmStatic
```fun  load ( modelName :  String ,  bundle :  AssetBundle ) :  Entity 
Synchronously loads a 3D model from the specified  AssetBundle  and returns its root entity. 
load Suspend 
```kotlin
@JvmStatic
```suspend  fun  loadSuspend ( file :  File ) :  Entity 
Asynchronously loads a 3D model from a file and returns its root entity. 
```kotlin
@JvmStatic
```suspend  fun  loadSuspend ( uriString :  String ) :  Entity 
Asynchronously loads a 3D model from the specified URI string and returns its root entity. 
```kotlin
@JvmStatic
```suspend  fun  loadSuspend ( contentResolver :  ContentResolver ,  uri :  Uri ) :  Entity 
Asynchronously loads a 3D model from a content provider URI and returns its root entity. 
```kotlin
@JvmStatic
```suspend  fun  loadSuspend ( inputStream :  InputStream ,  format :  ModelFormat ) :  Entity 
Asynchronously loads a 3D model from an InputStream and returns its root entity. 
```kotlin
@JvmStatic
```suspend  fun  loadSuspend ( modelName :  String ,  bundle :  AssetBundle ) :  Entity 
Asynchronously loads an entity from the specified model name in the  AssetBundle , and the root node will be returned as an entity.