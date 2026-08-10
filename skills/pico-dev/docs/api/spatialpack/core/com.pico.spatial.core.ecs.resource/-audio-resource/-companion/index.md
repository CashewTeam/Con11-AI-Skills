# Companion | PICO Spatial SDK

core / com.pico.spatial.core.ecs.resource / AudioResource / Companion 
# Companion
```kotlin
object Companion
```
The companion object of  AudioResource . 
Members 
## Functions
load 
```kotlin
@JvmStatic
```fun  load ( bundle :  AssetBundle ,  path :  String ) :  AudioResource 
Loads an audio resource from the specified  AssetBundle . 
```kotlin
@JvmStatic
```fun  load ( name :  String ,  uri :  Uri ,  context :  Context ) :  AudioResource 
Loads an audio resource from the specified URL. 
```kotlin
@JvmStatic
```fun  load ( name :  String ,  path :  String ,  loadType :  LoadType  =  LoadType.FROM_ASSETS ) :  AudioResource 
Loads an audio resource using the specified loading method. 
```kotlin
@JvmStatic
```fun  load ( name :  String ,  uri :  Uri ,  context :  Context ,  config :  AudioResourceConfig ) :  AudioResource 
Loads an audio resource from the specified URI with the provided configuration. 
```kotlin
@JvmStatic
```fun  load ( name :  String ,  path :  String ,  loadType :  LoadType  =  LoadType.FROM_ASSETS ,  config :  AudioResourceConfig ) :  AudioResource 
Loads an audio resource using the specified loading method, with additional configuration.