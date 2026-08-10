# PolygonFillMode | PICO Spatial SDK

core / com.pico.spatial.core.ecs.resource / PolygonFillMode 
# PolygonFillMode
```kotlin
enum PolygonFillMode : Enum<PolygonFillMode>
```
Fill modes for rendering polygons. 
Members Entries 
## Entries
FILL 
```kotlin
FILL
```
Polygons are rendered as filled. Each polygon's interior is shaded based on the material and lighting conditions. 
LINE 
```kotlin
LINE
```
Polygons are rendered as wireframes. Only the edges of each polygon are drawn, which is useful for visualizing the mesh structure. 
UNKNOWN 
```kotlin
UNKNOWN
```
Reserved value for forward compatibility. 
## Properties
entries 
```kotlin
val entries: EnumEntries<PolygonFillMode>
```
Returns a representation of an immutable list of all enum entries, in the order they're declared. 
value 
```kotlin
val value: Int
```
## Functions
value Of 
```kotlin
fun valueOf(value: String): PolygonFillMode
```
Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.) 
values 
```kotlin
fun values(): Array<PolygonFillMode>
```
Returns an array containing the constants of this enum type, in the order they're declared.