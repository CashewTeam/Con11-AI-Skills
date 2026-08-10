# Event | PICO Spatial SDK

sense / com.pico.spatial.sense.base / AnchorUpdate / Event 
# Event
```kotlin
enum Event : Enum<AnchorUpdate.Event>
```
Enumerates the possible types of anchor update events. 
Members Entries 
## Entries
ADDED 
```kotlin
ADDED
```
Indicates that the anchor was added. 
UPDATED 
```kotlin
UPDATED
```
Indicates that the anchor was updated. 
REMOVED 
```kotlin
REMOVED
```
Indicates that the anchor was removed. 
LOADED 
```kotlin
LOADED
```
Indicates that the anchor was loaded. 
UNKNOWN 
```kotlin
UNKNOWN
```
Reserved value for forward compatibility. 
## Properties
entries 
```kotlin
val entries: EnumEntries<AnchorUpdate.Event>
```
Returns a representation of an immutable list of all enum entries, in the order they're declared. 
value 
```kotlin
val value: Int
```
The integer value of the event type. 
## Functions
value Of 
```kotlin
fun valueOf(value: String): AnchorUpdate.Event
```
Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.) 
values 
```kotlin
fun values(): Array<AnchorUpdate.Event>
```
Returns an array containing the constants of this enum type, in the order they're declared.