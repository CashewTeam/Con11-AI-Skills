# WorldScale | PICO Spatial SDK

ui:foundation / com.pico.spatial.ui.foundation.dsl / WorldScale 
# WorldScale
```kotlin
enum WorldScale : Enum<WorldScale>
```
The way how a  WindowContainer  will be scaled in the world. Available options include: 
- 
Automatic : how the  WindowContainer  will be scaled is decided by the system automatically. Currently, it's the same as Dynamic. 
- 
Dynamic : Dynamic scale means the  WindowContainer  will scale larger as it moves further away, maintaining the same angular size. 
- 
Fixed : Fixed scale means the  WindowContainer  will keep its physical size in the world. 
Will be Automatic by default. 
Members Entries 
## Entries
Automatic 
```kotlin
Automatic
```
the scale mode where the  WindowContainer  will be scaled is decided by the system automatically. Currently, it's the same as Dynamic. 
Dynamic 
```kotlin
Dynamic
```
Dynamic scale means the  WindowContainer  will scale larger as it moves further away, maintaining the same angular size. 
Fixed 
```kotlin
Fixed
```
Fixed scale means the  WindowContainer  will keep its physical size in the world. 
## Properties
entries 
```kotlin
val entries: EnumEntries<WorldScale>
```
Returns a representation of an immutable list of all enum entries, in the order they're declared. 
## Functions
value Of 
```kotlin
fun valueOf(value: String): WorldScale
```
Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.) 
values 
```kotlin
fun values(): Array<WorldScale>
```
Returns an array containing the constants of this enum type, in the order they're declared.