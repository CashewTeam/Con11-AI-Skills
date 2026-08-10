# ThumbstickValue | PICO Spatial SDK

tracking / com.pico.spatial.tracking.controller / ThumbstickValue 
# ThumbstickValue
```kotlin
class ThumbstickValue
```
2D value for a controller thumbstick. 
- 
Range: x, y ∈ -1.0, 1.0 
- 
Semantics: x is horizontal, y is vertical (exact orientation depends on device mapping) 
- 
Frame model: current-frame snapshot; apply your own smoothing/debouncing if needed. 
Members 
## Constructors
Thumbstick Value 
```kotlin
constructor(x: Float, y: Float)
```
## Properties
x 
```kotlin
val x: Float
```
The x-axis value of the thumbstick, ranging from -1.0 to 1.0. 
y 
```kotlin
val y: Float
```
The y-axis value of the thumbstick, ranging from -1.0 to 1.0. 
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