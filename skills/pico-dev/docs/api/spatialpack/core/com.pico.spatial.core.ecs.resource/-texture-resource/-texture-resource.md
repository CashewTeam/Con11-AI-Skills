# TextureResource | PICO Spatial SDK

core / com.pico.spatial.core.ecs.resource / TextureResource / TextureResource 
# TextureResource
```kotlin
constructor(path: String, loadType: LoadType = LoadType.FROM_ASSETS, option: TextureCreateOption = TextureCreateOption())
```
Constructs a  TextureResource  from a file path. 
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
constructor(path: String, loadType: LoadType = LoadType.FROM_ASSETS)
```
Constructs a  TextureResource  from a file path. 
#### Parameters
path 
The file path of the texture. 
load Type 
The loading method; defaults to  FROM_ASSETS . 
#### Throws
Resource Loading Exception 
If an error occurs during the loading process. 
```kotlin
constructor(bitmap: Bitmap)
```
Creates a  TextureResource  from a  Bitmap . 
Only a part of format is supported now: 
- 
Bitmap.Config.ARGB_8888 
- 
Bitmap.Config.RGBA_F16 
If a Bitmap with unsupported format is given, an  IllegalArgumentException  will be thrown. 
Note: Do not modify the bitmap while creating the texture resource. 
#### Return
The created  TextureResource . 
#### Parameters
bitmap 
The source bitmap. 
#### Throws
Resource Loading Exception 
If an error occurs during the loading process. 
Illegal Argument Exception 
If the bitmap has an unsupported format.