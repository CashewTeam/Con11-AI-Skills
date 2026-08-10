# SpatialContainerType | PICO Spatial SDK

core / com.pico.spatial.core.container / SpatialContainerType 
# SpatialContainerType
```kotlin
enum SpatialContainerType : Enum<SpatialContainerType>
```
The types of  SpatialContainer . 
Members Entries 
## Entries
WINDOW_CONTAINER 
```kotlin
WINDOW_CONTAINER
```
Represents a  SpatialContainer  of type  WindowContainer . 
STAGE 
```kotlin
STAGE
```
Represents a  SpatialContainer  of type  Stage . 
## Properties
entries 
```kotlin
val entries: EnumEntries<SpatialContainerType>
```
Returns a representation of an immutable list of all enum entries, in the order they're declared. 
## Functions
value Of 
```kotlin
fun valueOf(value: String): SpatialContainerType
```
Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.) 
values 
```kotlin
fun values(): Array<SpatialContainerType>
```
Returns an array containing the constants of this enum type, in the order they're declared.