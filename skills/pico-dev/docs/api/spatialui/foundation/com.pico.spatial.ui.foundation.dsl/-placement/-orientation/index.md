# Orientation | PICO Spatial SDK

ui:foundation / com.pico.spatial.ui.foundation.dsl / Placement / Orientation 
# Orientation
```kotlin
enum Orientation : Enum<Placement.Orientation>
```
The orientation of the new window container relative to  anchorContainer . 
Members Entries 
## Entries
None 
```kotlin
None
```
None, means no placement. 
Top 
```kotlin
Top
```
Above the anchor window. 
Bottom 
```kotlin
Bottom
```
Below the anchor window. 
Left 
```kotlin
Left
```
To left of the anchor window. 
Right 
```kotlin
Right
```
To right of the anchor window. 
## Properties
entries 
```kotlin
val entries: EnumEntries<Placement.Orientation>
```
Returns a representation of an immutable list of all enum entries, in the order they're declared. 
## Functions
value Of 
```kotlin
fun valueOf(value: String): Placement.Orientation
```
Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.) 
values 
```kotlin
fun values(): Array<Placement.Orientation>
```
Returns an array containing the constants of this enum type, in the order they're declared.