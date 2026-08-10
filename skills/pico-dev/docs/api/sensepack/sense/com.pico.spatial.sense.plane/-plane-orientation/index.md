# PlaneOrientation | PICO Spatial SDK

sense / com.pico.spatial.sense.plane / PlaneOrientation 
# PlaneOrientation
```kotlin
enum PlaneOrientation : Enum<PlaneOrientation>
```
Enum class representing the orientation of a plane in 3D space. Used to describe the spatial alignment of a plane. 
Members Entries 
## Entries
UNKNOWN_ORIENTATION 
```kotlin
UNKNOWN_ORIENTATION
```
Unknown orientation. 
HORIZONTAL_UPWARD 
```kotlin
HORIZONTAL_UPWARD
```
The plane is horizontal and facing upward. Example: A flat surface like a floor or a tabletop. 
HORIZONTAL_DOWNWARD 
```kotlin
HORIZONTAL_DOWNWARD
```
The plane is horizontal and facing downward. Example: The underside of a surface like a table or a ceiling. 
VERTICAL 
```kotlin
VERTICAL
```
The plane is vertical. Example: Upright surfaces such as walls or doors. 
ARBITRARY 
```kotlin
ARBITRARY
```
The plane has an arbitrary orientation that doesn't fall into strictly horizontal or vertical categories. Example: Slanted surfaces such as ramps or inclined objects. 
## Properties
entries 
```kotlin
val entries: EnumEntries<PlaneOrientation>
```
Returns a representation of an immutable list of all enum entries, in the order they're declared. 
value 
```kotlin
val value: Int
```
The integer value corresponding to the plane orientation. 
## Functions
value Of 
```kotlin
fun valueOf(value: String): PlaneOrientation
```
Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.) 
values 
```kotlin
fun values(): Array<PlaneOrientation>
```
Returns an array containing the constants of this enum type, in the order they're declared.