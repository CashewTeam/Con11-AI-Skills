# CaptionBarType | PICO Spatial SDK

ui:platform / com.pico.spatial.ui.platform.resize / CaptionBarType 
# CaptionBarType
```kotlin
enum CaptionBarType : Enum<CaptionBarType>
```
Declares the caption bar display behavior for  com.pico.spatial.core.container.WindowContainer 
Members Entries 
## Entries
Default 
```kotlin
Default
```
Keep caption bar permanently visible at all times 
AutomaticHide 
```kotlin
AutomaticHide
```
Automatically hides caption bar after an idle period 
## Properties
entries 
```kotlin
val entries: EnumEntries<CaptionBarType>
```
Returns a representation of an immutable list of all enum entries, in the order they're declared. 
## Functions
value Of 
```kotlin
fun valueOf(value: String): CaptionBarType
```
Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.) 
values 
```kotlin
fun values(): Array<CaptionBarType>
```
Returns an array containing the constants of this enum type, in the order they're declared.