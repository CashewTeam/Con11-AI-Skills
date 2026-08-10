# PICOKeyboardAnchor | PICO Spatial SDK

sense / com.pico.spatial.sense.keyboard / PICOKeyboardAnchor 
# PICOKeyboardAnchor
```kotlin
class PICOKeyboardAnchor : Anchor
```
Encapsulates the spatial pose and state of a tracked PICO keyboard entity. 
Members 
## Properties
anchor UUID 
```kotlin
val anchorUUID: UUID
```
Unique identifier for the tracked anchor. 
category 
```kotlin
val category: PICOKeyboardCategory
```
Category of the tracked entity, such as keyboard or touchpad. 
is Ready 
```kotlin
val isReady: Boolean
```
Whether the keyboard entity is ready for use. 
is Tracking 
```kotlin
val isTracking: Boolean
```
Whether tracking quality is currently valid. 
transform 
```kotlin
val transform: Transform
```
Spatial transform of the anchor in the current space. 
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