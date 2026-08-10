# TextureEncoding | PICO Spatial SDK

core / com.pico.spatial.core.ecs.resource / TextureEncoding 
# TextureEncoding
```kotlin
enum TextureEncoding : Enum<TextureEncoding>
```
The encoding of texture. 
Members Entries 
## Entries
SRGB 
```kotlin
SRGB
```
The sRGB encoding. Follows human visual perception of brightness and includes gamma correction. 
LINEAR 
```kotlin
LINEAR
```
The linear encoding. No gamma correction applied, preserves linear intensity values. 
## Properties
entries 
```kotlin
val entries: EnumEntries<TextureEncoding>
```
Returns a representation of an immutable list of all enum entries, in the order they're declared. 
## Functions
value Of 
```kotlin
fun valueOf(value: String): TextureEncoding
```
Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.) 
values 
```kotlin
fun values(): Array<TextureEncoding>
```
Returns an array containing the constants of this enum type, in the order they're declared.