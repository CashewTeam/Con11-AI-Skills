# VolumeAlignment | PICO Spatial SDK

ui:foundation / com.pico.spatial.ui.foundation.dsl / VolumeAlignment 
# VolumeAlignment
```kotlin
enum VolumeAlignment : Enum<VolumeAlignment>
```
Represents how a  WindowContainer  of form  Form.Volumetric  will align. 
This class provides predefined alignments via  VolumeAlignment.Gravity  and  VolumeAlignment.Tilted . 
Members Entries 
## Entries
Gravity 
```kotlin
Gravity
```
The alignment mode where the  WindowContainer  of form  Form.Volumetric  will be aligned to the gravity direction, keeping its base parallel to the floor. 
Tilted 
```kotlin
Tilted
```
The alignment mode where the  WindowContainer  of form  Form.Volumetric  will be aligned to a tilt direction, facing the user. 
## Properties
entries 
```kotlin
val entries: EnumEntries<VolumeAlignment>
```
Returns a representation of an immutable list of all enum entries, in the order they're declared. 
## Functions
value Of 
```kotlin
fun valueOf(value: String): VolumeAlignment
```
Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.) 
values 
```kotlin
fun values(): Array<VolumeAlignment>
```
Returns an array containing the constants of this enum type, in the order they're declared.