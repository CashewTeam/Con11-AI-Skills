# MotionTrackerConnectionState | PICO Spatial SDK

tracking / com.pico.spatial.tracking.motion / MotionTrackerConnectionState 
# MotionTrackerConnectionState
```kotlin
enum MotionTrackerConnectionState : Enum<MotionTrackerConnectionState>
```
Motion tracker connection state. 
Members Entries 
## Entries
DISCONNECTED 
```kotlin
DISCONNECTED
```
The tracker is disconnected. 
CONNECTED 
```kotlin
CONNECTED
```
The tracker is connected. 
UNKNOWN 
```kotlin
UNKNOWN
```
Unknown connection state. 
## Properties
entries 
```kotlin
val entries: EnumEntries<MotionTrackerConnectionState>
```
Returns a representation of an immutable list of all enum entries, in the order they're declared. 
value 
```kotlin
val value: Int
```
The integer value of the connection state. 
## Functions
value Of 
```kotlin
fun valueOf(value: String): MotionTrackerConnectionState
```
Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.) 
values 
```kotlin
fun values(): Array<MotionTrackerConnectionState>
```
Returns an array containing the constants of this enum type, in the order they're declared.