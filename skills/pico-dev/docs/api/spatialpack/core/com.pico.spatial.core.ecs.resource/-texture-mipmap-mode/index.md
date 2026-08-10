# TextureMipmapMode | PICO Spatial SDK

core / com.pico.spatial.core.ecs.resource / TextureMipmapMode 
# TextureMipmapMode
```kotlin
enum TextureMipmapMode : Enum<TextureMipmapMode>
```
The mipmap mode of the texture. 
Members Entries 
## Entries
NONE 
```kotlin
NONE
```
No mipmap will be generated. 
GENERATE_ALL 
```kotlin
GENERATE_ALL
```
Generate all levels of mipmap. 
## Properties
entries 
```kotlin
val entries: EnumEntries<TextureMipmapMode>
```
Returns a representation of an immutable list of all enum entries, in the order they're declared. 
## Functions
value Of 
```kotlin
fun valueOf(value: String): TextureMipmapMode
```
Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.) 
values 
```kotlin
fun values(): Array<TextureMipmapMode>
```
Returns an array containing the constants of this enum type, in the order they're declared.