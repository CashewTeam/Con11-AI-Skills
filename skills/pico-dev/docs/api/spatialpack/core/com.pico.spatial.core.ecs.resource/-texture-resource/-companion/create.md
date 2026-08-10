# create | PICO Spatial SDK

core / com.pico.spatial.core.ecs.resource / TextureResource / Companion / create 
# create
```kotlin
@JvmStatic
```fun  create ( bitmap :  Bitmap ) :  TextureResource 
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
Note: For complex or high-resolution resources that require significant processing time, it is strongly recommended to leverage coroutines for loading. This approach prevents blocking the main thread, ensuring a responsive and fluid user experience.