# WindowSizeBehaviors | PICO Spatial SDK

ui:foundation / com.pico.spatial.ui.foundation.window / WindowSizeBehaviors 
# WindowSizeBehaviors
```kotlin
enum WindowSizeBehaviors : Enum<WindowSizeBehaviors>
```
Window size behaviors 
Members Entries 
## Entries
Adaptive 
```kotlin
Adaptive
```
Window size is adaptive to the content. 
MatchContainerWidth 
```kotlin
MatchContainerWidth
```
Window width matches the container width, and height is adaptive to the content. 
MatchContainerHeight 
```kotlin
MatchContainerHeight
```
Window height matches the container height, and width is adaptive to the content. 
## Properties
entries 
```kotlin
val entries: EnumEntries<WindowSizeBehaviors>
```
Returns a representation of an immutable list of all enum entries, in the order they're declared. 
## Functions
value Of 
```kotlin
fun valueOf(value: String): WindowSizeBehaviors
```
Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.) 
values 
```kotlin
fun values(): Array<WindowSizeBehaviors>
```
Returns an array containing the constants of this enum type, in the order they're declared.