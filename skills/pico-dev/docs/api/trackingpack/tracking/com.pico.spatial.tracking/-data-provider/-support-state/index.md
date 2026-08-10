# SupportState | PICO Spatial SDK

tracking / com.pico.spatial.tracking / DataProvider / SupportState 
# SupportState
```kotlin
enum SupportState : Enum<DataProvider.SupportState>
```
Indicates whether the current type of data is supported now. 
Members Entries 
## Entries
NONE 
```kotlin
NONE
```
For compatibility, will not be return normally. 
SUPPORTED 
```kotlin
SUPPORTED
```
The current type of data is supported now. 
DEVICE_NOT_SUPPORTED 
```kotlin
DEVICE_NOT_SUPPORTED
```
The current type of data is not supported on the current device now, possibly because the device is not connected or not in use yet. The state will automatically change to  SupportState.SUPPORTED  when the date is supported. 
NOT_IN_FULL_SPACE 
```kotlin
NOT_IN_FULL_SPACE
```
Receiving current type of data need application running in full space, but it is in shared space now. It will auto change to  SupportState.SUPPORTED  when it is running in full space. 
WITHOUT_PERMISSION 
```kotlin
WITHOUT_PERMISSION
```
Receiving this type of data requires a specific permission, which has not been granted yet. The state will automatically change to  SupportState.SUPPORTED  once the permission is granted. 
UNKNOWN 
```kotlin
UNKNOWN
```
Unknown support state. 
## Properties
entries 
```kotlin
val entries: EnumEntries<DataProvider.SupportState>
```
Returns a representation of an immutable list of all enum entries, in the order they're declared. 
value 
```kotlin
val value: Int
```
The integer value of the support state. 
## Functions
value Of 
```kotlin
fun valueOf(value: String): DataProvider.SupportState
```
Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.) 
values 
```kotlin
fun values(): Array<DataProvider.SupportState>
```
Returns an array containing the constants of this enum type, in the order they're declared.