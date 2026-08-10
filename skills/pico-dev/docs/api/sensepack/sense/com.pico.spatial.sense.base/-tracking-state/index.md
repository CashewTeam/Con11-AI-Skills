# TrackingState | PICO Spatial SDK

sense / com.pico.spatial.sense.base / TrackingState 
# TrackingState
```kotlin
enum TrackingState : Enum<TrackingState>
```
Represents the various states of the tracking manager during its lifecycle. This enum is used to indicate the current operational state of the tracking manager. 
Members Entries 
## Entries
NONE 
```kotlin
NONE
```
The default state, indicating that the tracking manager has not been initialized yet. Typically, this is the starting state before any setup or configuration is performed. 
INITIALIZED 
```kotlin
INITIALIZED
```
Indicates that the tracking manager has been successfully initialized. At this stage, the manager is ready to start tracking but is not actively running yet. 
RUNNING 
```kotlin
RUNNING
```
Indicates that the tracking manager is actively running and performing tracking operations. In this state, tracking data is being processed and updated in real-time. 
PAUSED 
```kotlin
PAUSED
```
Indicates that the tracking manager is temporarily paused. In this state, tracking operations are halted, but the manager retains its state and can resume tracking without requiring reinitialization. 
STOPPED 
```kotlin
STOPPED
```
Indicates that the tracking manager has been stopped. Once stopped, the manager may require reinitialization to start tracking again. This state typically signifies the end of tracking operations. 
INVALID 
```kotlin
INVALID
```
Indicates that the tracking manager is in an invalid state. This may occur due to errors or unexpected conditions, and the manager may not be able to perform any operations until the issue is resolved. 
UNKNOWN 
```kotlin
UNKNOWN
```
Unknown state. 
## Properties
entries 
```kotlin
val entries: EnumEntries<TrackingState>
```
Returns a representation of an immutable list of all enum entries, in the order they're declared. 
value 
```kotlin
val value: Int
```
The integer value of the tracking state. 
## Functions
value Of 
```kotlin
fun valueOf(value: String): TrackingState
```
Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.) 
values 
```kotlin
fun values(): Array<TrackingState>
```
Returns an array containing the constants of this enum type, in the order they're declared.