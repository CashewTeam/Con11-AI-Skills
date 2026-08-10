# MaterialCullingMode | PICO Spatial SDK

core / com.pico.spatial.core.ecs.resource / MaterialCullingMode 
# MaterialCullingMode
```kotlin
enum MaterialCullingMode : Enum<MaterialCullingMode>
```
Specifies the face culling mode used when rendering a material. 
Face culling determines which triangle faces are discarded during the rendering pass, optimizing performance by avoiding unnecessary fragment processing. The culling decision is based on the triangle's winding order relative to the camera's viewpoint. 
Default:  BACK . 
Members Entries 
## Entries
NONE 
```kotlin
NONE
```
Disables face culling. 
FRONT 
```kotlin
FRONT
```
Culls front-facing triangles. 
BACK 
```kotlin
BACK
```
Culls back-facing triangles. 
FRONT_AND_BACK 
```kotlin
FRONT_AND_BACK
```
Culls both front- and back-facing triangles. 
UNKNOWN 
```kotlin
UNKNOWN
```
Reserved value for forward compatibility. 
## Properties
entries 
```kotlin
val entries: EnumEntries<MaterialCullingMode>
```
Returns a representation of an immutable list of all enum entries, in the order they're declared. 
value 
```kotlin
val value: Int
```
The integer value of the culling mode. 
## Functions
value Of 
```kotlin
fun valueOf(value: String): MaterialCullingMode
```
Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.) 
values 
```kotlin
fun values(): Array<MaterialCullingMode>
```
Returns an array containing the constants of this enum type, in the order they're declared.