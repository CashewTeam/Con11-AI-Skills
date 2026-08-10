# load | PICO Spatial SDK

core / com.pico.spatial.core.ecs.resource / TextureResource / Companion / load 
# load
```kotlin
@JvmStatic
```fun  load ( path :  String ,  loadType :  LoadType  =  LoadType.FROM_ASSETS ,  option :  TextureCreateOption  =  TextureCreateOption() ) :  TextureResource 
Loads a  TextureResource  from a file path. 
Note: For complex or high-resolution resources that require significant processing time, it is strongly recommended to leverage coroutines for loading. This approach prevents blocking the main thread, ensuring a responsive and fluid user experience. 
#### Return
The loaded  TextureResource . 
#### Parameters
path 
The file path of the texture. 
load Type 
The loading method; defaults to  FROM_ASSETS . 
option 
Options for creating the texture resource. 
#### Throws
Resource Loading Exception 
If an error occurs during the loading process. 
```kotlin
@JvmStatic
```fun  load ( path :  String ,  loadType :  LoadType  =  LoadType.FROM_ASSETS ) :  TextureResource 
Loads a  TextureResource  from a file path. 
#### Return
The loaded  TextureResource . 
#### Parameters
path 
The file path of the texture. 
load Type 
The loading method; defaults to  FROM_ASSETS . 
#### Throws
Resource Loading Exception 
If an error occurs during the loading process. 
Note: For complex or high-resolution resources that require significant processing time, it is strongly recommended to leverage coroutines for loading. This approach prevents blocking the main thread, ensuring a responsive and fluid user experience.