# load | PICO Spatial SDK

core / com.pico.spatial.core.ecs.resource / AudioResource / Companion / load 
# load
```kotlin
@JvmStatic
```fun  load ( name :  String ,  path :  String ,  loadType :  LoadType  =  LoadType.FROM_ASSETS ) :  AudioResource 
Loads an audio resource using the specified loading method. 
#### Return
A valid  AudioResource  instance if the loading succeeds; otherwise, an invalid instance will be returned. 
#### Parameters
name 
The name of the audio resource. 
path 
The path to the audio resource. 
load Type 
The loading method to use, which defaults to  FROM_ASSETS . 
#### Throws
Resource Loading Exception 
If any error occurs during loading. 
```kotlin
@JvmStatic
```fun  load ( name :  String ,  path :  String ,  loadType :  LoadType  =  LoadType.FROM_ASSETS ,  config :  AudioResourceConfig ) :  AudioResource 
Loads an audio resource using the specified loading method, with additional configuration. 
#### Return
A valid  AudioResource  instance if the loading succeeds; otherwise, an invalid instance will be returned. 
#### Parameters
name 
The name of the audio resource. 
path 
The path to the audio resource. 
load Type 
The loading method to use, which defaults to  FROM_ASSETS . 
config 
The configuration for the audio resource, which is specified with  AudioResourceConfig . 
#### Throws
Resource Loading Exception 
If any error occurs during loading. 
```kotlin
@JvmStatic
```fun  load ( name :  String ,  uri :  Uri ,  context :  Context ) :  AudioResource 
Loads an audio resource from the specified URL. 
#### Return
A valid  AudioResource  instance if the loading succeeds; otherwise, an invalid instance will be returned. 
#### Parameters
name 
The name of the audio resource. 
uri 
The  Uri  of the audio resource. The supported  Uri  schemes are  file:// ,  content:// , and  android.resource:// . URI schemes such as  http://  and  https://  are not supported. 
context 
The current  Context , representing the active component or application environment from which this method is called. 
#### Throws
Resource Loading Exception 
If any error occurs during loading. 
```kotlin
@JvmStatic
```fun  load ( name :  String ,  uri :  Uri ,  context :  Context ,  config :  AudioResourceConfig ) :  AudioResource 
Loads an audio resource from the specified URI with the provided configuration. 
#### Return
A valid instance if the loading succeeds; otherwise, an invalid instance will be returned. 
#### Parameters
name 
The name of the audio resource. 
uri 
The  Uri  of the audio resource. The supported  Uri  schemes are  file:// ,  content:// , and  android.resource:// . Schemes like  http://  and  https://  are not supported. 
context 
The current  Context , representing the active component or application environment from which this method is called. 
config 
The configuration for the audio resource, which is specified with  AudioResourceConfig . 
#### Throws
Resource Loading Exception 
If any error occurs during loading. 
```kotlin
@JvmStatic
```fun  load ( bundle :  AssetBundle ,  path :  String ) :  AudioResource 
Loads an audio resource from the specified  AssetBundle . 
#### Return
A valid instance if the loading succeeds; otherwise, an invalid instance will be returned. 
#### Parameters
bundle 
The  AssetBundle  containing the audio resource. 
path 
The relative path to the audio resource in the  AssetBundle . 
#### Throws
Resource Loading Exception 
If any error occurs during loading.