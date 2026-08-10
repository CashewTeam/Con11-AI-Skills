# BodyTrackingMessage | PICO Spatial SDK

tracking / com.pico.spatial.tracking.body / BodyTrackingMessage 
# BodyTrackingMessage
```kotlin
enum BodyTrackingMessage : Enum<BodyTrackingMessage>
```
Message of body tracking. 
Members Entries 
## Entries
NONE 
```kotlin
NONE
```
No message. 
NO_ERROR 
```kotlin
NO_ERROR
```
No error. 
TRACKER_NOT_CALIBRATED 
```kotlin
TRACKER_NOT_CALIBRATED
```
Not calibrated yet. 
TRACKER_NUM_NOT_ENOUGH 
```kotlin
TRACKER_NUM_NOT_ENOUGH
```
Tracker connected not enough. 
TRACKER_STATE_NOT_SATISFIED 
```kotlin
TRACKER_STATE_NOT_SATISFIED
```
Tracker state not satisfied. 
TRACKER_PERSISTENT_INVISIBILITY 
```kotlin
TRACKER_PERSISTENT_INVISIBILITY
```
Tracker persistent invisibility. 
TRACKER_DATA_ERROR 
```kotlin
TRACKER_DATA_ERROR
```
Tracker data error. 
USER_CHANGE 
```kotlin
USER_CHANGE
```
User has changed. 
TRACKING_POSE_ERROR 
```kotlin
TRACKING_POSE_ERROR
```
Tracker pose error. 
UNKNOWN 
```kotlin
UNKNOWN
```
Unknown message. 
## Properties
entries 
```kotlin
val entries: EnumEntries<BodyTrackingMessage>
```
Returns a representation of an immutable list of all enum entries, in the order they're declared. 
value 
```kotlin
val value: Int
```
The integer value of the tracking message. 
## Functions
value Of 
```kotlin
fun valueOf(value: String): BodyTrackingMessage
```
Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.) 
values 
```kotlin
fun values(): Array<BodyTrackingMessage>
```
Returns an array containing the constants of this enum type, in the order they're declared.