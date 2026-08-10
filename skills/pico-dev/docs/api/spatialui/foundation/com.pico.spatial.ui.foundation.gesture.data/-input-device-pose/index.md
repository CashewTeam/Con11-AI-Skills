# InputDevicePose | PICO Spatial SDK

ui:foundation / com.pico.spatial.ui.foundation.gesture.data / InputDevicePose 
# InputDevicePose
```kotlin
@Immutable
```class  InputDevicePose ( val  rawPosition :  Offset3D ,  val  rawRotation :  Rotation3D ) 
Pose of input device. 
Members 
## Constructors
Input Device Pose 
```kotlin
constructor(rawPosition: Offset3D, rawRotation: Rotation3D)
```
## Types
Companion 
```kotlin
object Companion
```
companion object of InputDevicePose. 
## Properties
raw Position 
```kotlin
val rawPosition: Offset3D
```
The raw position of input device. 
raw Rotation 
```kotlin
val rawRotation: Rotation3D
```
The raw rotation of input device. 
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