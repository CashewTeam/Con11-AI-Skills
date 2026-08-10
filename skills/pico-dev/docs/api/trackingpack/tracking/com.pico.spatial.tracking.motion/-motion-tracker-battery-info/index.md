# MotionTrackerBatteryInfo | PICO Spatial SDK

tracking / com.pico.spatial.tracking.motion / MotionTrackerBatteryInfo 
# MotionTrackerBatteryInfo
```kotlin
class MotionTrackerBatteryInfo
```
Motion tracker battery info. 
Members 
## Properties
battery Level 
```kotlin
val batteryLevel: Float
```
The current battery level. Value range: 0, 1. 
charging State 
```kotlin
val chargingState: MotionTrackerBatteryChargingState
```
The current charging state. 
id 
```kotlin
val id: Long
```
The id of the motion tracker. 
## Functions
equals 
```kotlin
open operator override fun equals(other: Any?): Boolean
```hash Code 
```kotlin
open override fun hashCode(): Int
```to String 
```kotlin
open override fun toString(): String
```