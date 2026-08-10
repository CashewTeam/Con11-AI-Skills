# TextureColorSpace | PICO Spatial SDK

core / com.pico.spatial.core.ecs.resource / TextureColorSpace 
# TextureColorSpace
```kotlin
enum TextureColorSpace : Enum<TextureColorSpace>
```
The color space of the texture. 
Members Entries 
## Entries
SRGB 
```kotlin
SRGB
```
Specifies that the texture is in sRGB color space. 
DISPLAY_P3 
```kotlin
DISPLAY_P3
```
Specifies that the texture is in Display P3 color space. 
REC2020 
```kotlin
REC2020
```
Specifies that the texture is in Rec. 2020 color space. 
ACES_CG 
```kotlin
ACES_CG
```
Specifies that the texture is in ACEScg color space. 
RAW 
```kotlin
RAW
```
Specifies that the texture is not in any color space and will be used unmodified. 
## Properties
entries 
```kotlin
val entries: EnumEntries<TextureColorSpace>
```
Returns a representation of an immutable list of all enum entries, in the order they're declared. 
## Functions
value Of 
```kotlin
fun valueOf(value: String): TextureColorSpace
```
Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.) 
values 
```kotlin
fun values(): Array<TextureColorSpace>
```
Returns an array containing the constants of this enum type, in the order they're declared.