# Companion | PICO Spatial SDK

core / com.pico.spatial.core.ecs.resource / TextureResource / Companion 
# Companion
```kotlin
object Companion
```
The companion of  TextureResource . 
Members 
## Functions
create 
```kotlin
@JvmStatic
```fun  create ( bitmap :  Bitmap ) :  TextureResource 
Creates a  TextureResource  from a  Bitmap . 
load 
```kotlin
@JvmStatic
```fun  load ( path :  String ,  loadType :  LoadType  =  LoadType.FROM_ASSETS ) :  TextureResource 
```kotlin
@JvmStatic
```fun  load ( path :  String ,  loadType :  LoadType  =  LoadType.FROM_ASSETS ,  option :  TextureCreateOption  =  TextureCreateOption() ) :  TextureResource 
Loads a  TextureResource  from a file path.