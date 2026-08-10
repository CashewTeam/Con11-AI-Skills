# ModelFormat | PICO Spatial SDK

core / com.pico.spatial.core.ecs / ModelFormat 
# ModelFormat
```kotlin
enum ModelFormat : Enum<ModelFormat>
```
Represents supported 3D model formats. 
Members Entries 
## Entries
USD 
```kotlin
USD
```
USD variants, commonly for model files that has an extension of ".usdz", ".usda", and ".usdc". 
GLTF 
```kotlin
GLTF
```
GLTF variants, commonly for model files that has an extension of ".glb" and ".gltf". 
OBJ 
```kotlin
OBJ
```
OBJ format, commonly for model files that has an extension of ".obj". 
STL 
```kotlin
STL
```
STL format, commonly for model files that has an extension of ".stl". 
## Properties
entries 
```kotlin
val entries: EnumEntries<ModelFormat>
```
Returns a representation of an immutable list of all enum entries, in the order they're declared. 
format String 
```kotlin
val formatString: String
```
The string identifier, which is typically used in file extensions or content types. 
## Functions
value Of 
```kotlin
fun valueOf(value: String): ModelFormat
```
Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.) 
values 
```kotlin
fun values(): Array<ModelFormat>
```
Returns an array containing the constants of this enum type, in the order they're declared.