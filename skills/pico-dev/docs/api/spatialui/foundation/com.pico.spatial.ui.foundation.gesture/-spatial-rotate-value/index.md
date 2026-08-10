# SpatialRotateValue | PICO Spatial SDK

ui:foundation / com.pico.spatial.ui.foundation.gesture / SpatialRotateValue 
# SpatialRotateValue
```kotlin
class SpatialRotateValue(val centroid: NormalizedPoint3D, val rotation: Rotation3D, val leftInteractionKind: InteractionKind, val rightInteractionKind: InteractionKind, val targetEntity: Entity? = null)
```
Class that holds the value of a rotate gesture. 
Members 
## Constructors
Spatial Rotate Value 
```kotlin
constructor(centroid: NormalizedPoint3D, rotation: Rotation3D, leftInteractionKind: InteractionKind, rightInteractionKind: InteractionKind, targetEntity: Entity? = null)
```
## Properties
centroid 
```kotlin
val centroid: NormalizedPoint3D
```
The centroid of the rotate gesture in normalized space. 
left Interaction Kind 
```kotlin
val leftInteractionKind: InteractionKind
```
The interaction kind of the left pointer. 
right Interaction Kind 
```kotlin
val rightInteractionKind: InteractionKind
```
The interaction kind of the right pointer. 
rotation 
```kotlin
val rotation: Rotation3D
```
The rotation of the rotate gesture, when gesture is rotating. Every rotation delta returned is relative to the last rotation. For lifecycle callbacks such as  onRotateStart ,  onRotateEnd , and  onRotateCancel , this value is  Rotation3D.identity . 
target Entity 
```kotlin
val targetEntity: Entity?
```
If the scale gesture happens on a 3d model,  targetEntity  will be the  Entity  of the 3d model. Otherwise,  targetEntity  will be null. 
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