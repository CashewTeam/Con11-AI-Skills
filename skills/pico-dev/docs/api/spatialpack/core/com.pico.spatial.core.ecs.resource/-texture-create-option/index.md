# TextureCreateOption | PICO Spatial SDK

core / com.pico.spatial.core.ecs.resource / TextureCreateOption 
# TextureCreateOption
```kotlin
class TextureCreateOption
```
Options for creating a  TextureResource . 
Members 
## Constructors
Texture Create Option 
```kotlin
constructor()
```
## Properties
color Space 
```kotlin
var colorSpace: TextureColorSpace
```
The color space of the texture. Defaults to  TextureColorSpace.SRGB . 
mipmap Mode 
```kotlin
var mipmapMode: TextureMipmapMode
```
The mipmap mode of the texture. Defaults to  TextureMipmapMode.GENERATE_ALL . 
name 
```kotlin
var name: String?
```
Name of the texture. Optional; defaults to  null . 
texture Encoding 
```kotlin
var textureEncoding: TextureEncoding
```
The encoding of the texture. Defaults to  TextureEncoding.SRGB . 
## Functions
equals 
```kotlin
open operator override fun equals(other: Any?): Boolean
```hash Code 
```kotlin
open override fun hashCode(): Int
```to String 
```kotlin
open override fun toString(): String
```