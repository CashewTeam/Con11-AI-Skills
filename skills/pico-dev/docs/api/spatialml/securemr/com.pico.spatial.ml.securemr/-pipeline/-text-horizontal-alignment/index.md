# TextHorizontalAlignment | PICO Spatial SDK

spatialml:securemr / com.pico.spatial.ml.securemr / Pipeline / TextHorizontalAlignment 
# TextHorizontalAlignment
```kotlin
enum TextHorizontalAlignment : Enum<Pipeline.TextHorizontalAlignment>
```
Horizontal alignment that can be used to update  SceneGraphProperty.Text.HorizontalAlignment . 
#### See also
Pipeline. update Scene Graph Text Horizontal Alignment Members Entries 
## Entries
LEFT 
```kotlin
LEFT
```
The text will be left-aligned. 
CENTER 
```kotlin
CENTER
```
The text will be center-aligned. 
RIGHT 
```kotlin
RIGHT
```
The text will be right-aligned. 
JUSTIFIED 
```kotlin
JUSTIFIED
```
The text will be justified-aligned, in which case spaces between words are adjusted to align both left and right edges with the container. 
FLUSH 
```kotlin
FLUSH
```
The text will be flush-aligned, in which case spaces between  all characters  are adjusted to align both left and right edges with the container. 
## Properties
entries 
```kotlin
val entries: EnumEntries<Pipeline.TextHorizontalAlignment>
```
Returns a representation of an immutable list of all enum entries, in the order they're declared. 
## Functions
value Of 
```kotlin
fun valueOf(value: String): Pipeline.TextHorizontalAlignment
```
Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.) 
values 
```kotlin
fun values(): Array<Pipeline.TextHorizontalAlignment>
```
Returns an array containing the constants of this enum type, in the order they're declared.