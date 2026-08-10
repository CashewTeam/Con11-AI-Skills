# MaterialTarget | PICO Spatial SDK

core / com.pico.spatial.core.ecs.animation / MaterialTarget 
# MaterialTarget
```kotlin
enum MaterialTarget : Enum<MaterialTarget>
```
Describes a reference to an animated material property. 
Members Entries 
## Entries
NONE 
```kotlin
NONE
```
Invalid material target. 
BASE_COLOR 
```kotlin
BASE_COLOR
```
The base color factor. 
METALLIC 
```kotlin
METALLIC
```
The metallic factor. 
ROUGHNESS 
```kotlin
ROUGHNESS
```
The roughness factor. 
EMISSIVE 
```kotlin
EMISSIVE
```
The emissive color factor. 
NORMAL 
```kotlin
NORMAL
```
The normal intensity. 
OPACITY 
```kotlin
OPACITY
```
The opacity factor. 
## Properties
entries 
```kotlin
val entries: EnumEntries<MaterialTarget>
```
Returns a representation of an immutable list of all enum entries, in the order they're declared. 
## Functions
value Of 
```kotlin
fun valueOf(value: String): MaterialTarget
```
Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.) 
values 
```kotlin
fun values(): Array<MaterialTarget>
```
Returns an array containing the constants of this enum type, in the order they're declared.