# StartResult | PICO Spatial SDK

tracking / com.pico.spatial.tracking / DataProvider / StartResult 
# StartResult
```kotlin
enum StartResult : Enum<DataProvider.StartResult>
```
The result of  start , represent the state when  start  is called. 
Members Entries 
## Entries
SUCCESS 
```kotlin
SUCCESS
```
The current type of data is ready to be provided when  start  is called. 
PENDING 
```kotlin
PENDING
```
The current type of data is not supported when  start  is called. Data provision will start when all requirements are met. 
## Properties
entries 
```kotlin
val entries: EnumEntries<DataProvider.StartResult>
```
Returns a representation of an immutable list of all enum entries, in the order they're declared. 
## Functions
value Of 
```kotlin
fun valueOf(value: String): DataProvider.StartResult
```
Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.) 
values 
```kotlin
fun values(): Array<DataProvider.StartResult>
```
Returns an array containing the constants of this enum type, in the order they're declared.