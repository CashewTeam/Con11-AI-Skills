# BlendingMode | PICO Spatial SDK

core / com.pico.spatial.core.ecs.resource / BlendingMode 
# BlendingMode
```kotlin
enum BlendingMode : Enum<BlendingMode>
```
Represents the blending mode of the material. 
Blending mode determines how the material blends with the background or other materials. 
Members Entries 
## Entries
OPAQUE 
```kotlin
OPAQUE
```
Opaque mode means the material is fully opaque. No transparency is applied, and the material completely covers any background or underlying objects. 
TRANSPARENT 
```kotlin
TRANSPARENT
```
Transparent mode means the alpha value controls the transparency of the material, allowing the background or underlying objects to be visible through it. Specular highlights and reflections remain unaffected. 
ADD 
```kotlin
ADD
```
Additive blending mode, the colors of the material are added to the colors of the background. 
FADE 
```kotlin
FADE
```
Fade blending mode, the alpha value not only affects the transparency of the material, but also gradually fades the specular highlights and reflections. 
MASKED 
```kotlin
MASKED
```
Masked blending mode, pixels are either fully opaque or fully transparent, based on a threshold. 
UNKNOWN 
```kotlin
UNKNOWN
```
Reserved value for forward compatibility. 
## Properties
entries 
```kotlin
val entries: EnumEntries<BlendingMode>
```
Returns a representation of an immutable list of all enum entries, in the order they're declared. 
value 
```kotlin
val value: Int
```
The integer value of the blending mode. 
## Functions
value Of 
```kotlin
fun valueOf(value: String): BlendingMode
```
Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.) 
values 
```kotlin
fun values(): Array<BlendingMode>
```
Returns an array containing the constants of this enum type, in the order they're declared.