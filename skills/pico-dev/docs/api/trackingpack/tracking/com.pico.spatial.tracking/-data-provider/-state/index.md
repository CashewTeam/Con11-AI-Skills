# State | PICO Spatial SDK

tracking / com.pico.spatial.tracking / DataProvider / State 
# State
```kotlin
enum State : Enum<DataProvider.State>
```
Represents the state of the current  DataProvider . 
Members Entries 
## Entries
CREATED 
```kotlin
CREATED
```
DataProvider  is created but not started yet. 
STARTED 
```kotlin
STARTED
```
DataProvider  is started. 
STOPPED 
```kotlin
STOPPED
```
DataProvider  is stopped. 
PENDING 
```kotlin
PENDING
```
DataProvider  is started, but the data is not supported now. The state will automatically change to  State.STARTED  when the data is supported. 
UNKNOWN 
```kotlin
UNKNOWN
```
Unknown state. 
## Properties
entries 
```kotlin
val entries: EnumEntries<DataProvider.State>
```
Returns a representation of an immutable list of all enum entries, in the order they're declared. 
value 
```kotlin
val value: Int
```
The integer value of the state. 
## Functions
value Of 
```kotlin
fun valueOf(value: String): DataProvider.State
```
Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.) 
values 
```kotlin
fun values(): Array<DataProvider.State>
```
Returns an array containing the constants of this enum type, in the order they're declared.