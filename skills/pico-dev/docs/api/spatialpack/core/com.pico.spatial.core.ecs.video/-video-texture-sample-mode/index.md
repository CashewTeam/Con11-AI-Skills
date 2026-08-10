# VideoTextureSampleMode | PICO Spatial SDK

core / com.pico.spatial.core.ecs.video / VideoTextureSampleMode 
# VideoTextureSampleMode
```kotlin
enum VideoTextureSampleMode : Enum<VideoTextureSampleMode>
```
Represents the video texture sample mode of the material. VideoTextureSampleMode determines how the material samples the video texture. Default:NONE. 
Members Entries 
## Entries
NONE 
```kotlin
NONE
```
No texture will be broadcast by video component. 
RAW 
```kotlin
RAW
```
Raw texture mode. 
RAW_AND_BLURRED 
```kotlin
RAW_AND_BLURRED
```
Raw and blurred texture mode. 
UNKNOWN 
```kotlin
UNKNOWN
```
Reserved value for forward compatibility. 
## Properties
entries 
```kotlin
val entries: EnumEntries<VideoTextureSampleMode>
```
Returns a representation of an immutable list of all enum entries, in the order they're declared. 
value 
```kotlin
val value: Int
```
The integer value of the  VideoTextureSampleMode . 
## Functions
value Of 
```kotlin
fun valueOf(value: String): VideoTextureSampleMode
```
Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.) 
values 
```kotlin
fun values(): Array<VideoTextureSampleMode>
```
Returns an array containing the constants of this enum type, in the order they're declared.