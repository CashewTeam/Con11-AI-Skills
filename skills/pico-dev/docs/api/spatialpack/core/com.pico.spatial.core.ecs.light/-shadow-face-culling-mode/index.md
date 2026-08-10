# ShadowFaceCullingMode | PICO Spatial SDK

core / com.pico.spatial.core.ecs.light / ShadowFaceCullingMode 
# ShadowFaceCullingMode
```kotlin
enum ShadowFaceCullingMode : Enum<ShadowFaceCullingMode>
```
Defines the face culling strategy applied during shadow map rendering. 
Face culling determines which triangle faces are discarded during the shadow rendering pass, optimizing performance by avoiding unnecessary fragment processing. The culling decision is based on the triangle's winding order relative to the light's viewpoint. 
Members Entries 
## Entries
BACK 
```kotlin
BACK
```
Culls back-facing triangles during shadow rendering. 
FRONT 
```kotlin
FRONT
```
Culls front-facing triangles during shadow rendering. 
NONE 
```kotlin
NONE
```
Disables face culling during shadow rendering. 
AUTO 
```kotlin
AUTO
```
Automatically inherits the culling mode from the associated material. 
UNKNOWN 
```kotlin
UNKNOWN
```
Reserved value for forward compatibility. 
## Properties
entries 
```kotlin
val entries: EnumEntries<ShadowFaceCullingMode>
```
Returns a representation of an immutable list of all enum entries, in the order they're declared. 
value 
```kotlin
val value: Int
```
The value of the ShadowFaceCullingMode. 
## Functions
value Of 
```kotlin
fun valueOf(value: String): ShadowFaceCullingMode
```
Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.) 
values 
```kotlin
fun values(): Array<ShadowFaceCullingMode>
```
Returns an array containing the constants of this enum type, in the order they're declared.