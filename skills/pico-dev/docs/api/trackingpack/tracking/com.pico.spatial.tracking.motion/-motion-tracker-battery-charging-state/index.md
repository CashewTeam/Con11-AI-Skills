# MotionTrackerBatteryChargingState | PICO Spatial SDK

tracking / com.pico.spatial.tracking.motion / MotionTrackerBatteryChargingState 
# MotionTrackerBatteryChargingState
```kotlin
enum MotionTrackerBatteryChargingState : Enum<MotionTrackerBatteryChargingState>
```
Motion tracker battery charging state. 
Members Entries 
## Entries
UNCHARGED 
```kotlin
UNCHARGED
```
The battery is not charging. 
TRICKLE_CHARGING 
```kotlin
TRICKLE_CHARGING
```
The battery is trickle charging. 
CHARGING 
```kotlin
CHARGING
```
The battery is charging. 
CHARGE_COMPLETED 
```kotlin
CHARGE_COMPLETED
```
The battery is charging and fully charged. 
UNKNOWN 
```kotlin
UNKNOWN
```
Unknown charging state. 
## Properties
entries 
```kotlin
val entries: EnumEntries<MotionTrackerBatteryChargingState>
```
Returns a representation of an immutable list of all enum entries, in the order they're declared. 
value 
```kotlin
val value: Int
```
The integer value of the charging state. 
## Functions
value Of 
```kotlin
fun valueOf(value: String): MotionTrackerBatteryChargingState
```
Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.) 
values 
```kotlin
fun values(): Array<MotionTrackerBatteryChargingState>
```
Returns an array containing the constants of this enum type, in the order they're declared.