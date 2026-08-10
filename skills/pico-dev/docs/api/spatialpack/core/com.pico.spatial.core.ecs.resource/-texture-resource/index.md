# TextureResource | PICO Spatial SDK

core / com.pico.spatial.core.ecs.resource / TextureResource 
# TextureResource
```kotlin
class TextureResource : Resource
```
A representation of a texture. 
Members 
## Constructors
Texture Resource 
```kotlin
constructor(path: String, loadType: LoadType = LoadType.FROM_ASSETS, option: TextureCreateOption = TextureCreateOption())
```
Constructs a  TextureResource  from a file path. 
```kotlin
constructor(path: String, loadType: LoadType = LoadType.FROM_ASSETS)
```
Constructs a  TextureResource  from a file path. 
```kotlin
constructor(bitmap: Bitmap)
```
Creates a  TextureResource  from a  Bitmap . 
## Types
Companion 
```kotlin
object Companion
```
The companion of  TextureResource . 
## Functions
close 
```kotlin
open override fun close()
```
You need to release the resource manually to ensure that the resource no longer takes up memory.