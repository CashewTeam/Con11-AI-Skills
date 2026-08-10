# BodyTrackingStatus | PICO Spatial SDK

tracking / com.pico.spatial.tracking.body / BodyTrackingStatus 
# BodyTrackingStatus
```kotlin
enum BodyTrackingStatus : Enum<BodyTrackingStatus>
```
Status of body tracking. 
Members Entries 
## Entries
NONE 
```kotlin
NONE
```
No status. 
INVALID 
```kotlin
INVALID
```
Invalid status, maybe not calibrated yet. 
VALID 
```kotlin
VALID
```
Valid status. 
LIMITED 
```kotlin
LIMITED
```
Limited status, maybe calibration is not good or tracker is not visible by hmd. 
UNKNOWN 
```kotlin
UNKNOWN
```
Unknown status. 
## Properties
entries 
```kotlin
val entries: EnumEntries<BodyTrackingStatus>
```
Returns a representation of an immutable list of all enum entries, in the order they're declared. 
value 
```kotlin
val value: Int
```
The integer value of the tracking status. 
## Functions
value Of 
```kotlin
fun valueOf(value: String): BodyTrackingStatus
```
Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.) 
values 
```kotlin
fun values(): Array<BodyTrackingStatus>
```
Returns an array containing the constants of this enum type, in the order they're declared.