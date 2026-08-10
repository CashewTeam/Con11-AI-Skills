# StageStyle | PICO Spatial SDK

ui:platform / com.pico.spatial.ui.platform.containers / StageStyle 
# StageStyle
```kotlin
enum StageStyle : Enum<StageStyle>
```
Stage 's styles 
Members Entries 
## Entries
Automatic 
```kotlin
Automatic
```
Style will be determinate by os 
Mixed 
```kotlin
Mixed
```
Mixed your virtual content with video passthrough 
Progressive 
```kotlin
Progressive
```
User can adjust immersion ratio from 0% to 100% 
Full 
```kotlin
Full
```
App takeover all display, video passthrough will be turned off 
## Properties
entries 
```kotlin
val entries: EnumEntries<StageStyle>
```
Returns a representation of an immutable list of all enum entries, in the order they're declared. 
## Functions
value Of 
```kotlin
fun valueOf(value: String): StageStyle
```
Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.) 
values 
```kotlin
fun values(): Array<StageStyle>
```
Returns an array containing the constants of this enum type, in the order they're declared.