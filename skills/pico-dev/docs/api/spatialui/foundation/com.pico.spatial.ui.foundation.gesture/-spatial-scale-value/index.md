# SpatialScaleValue | PICO Spatial SDK

ui:foundation / com.pico.spatial.ui.foundation.gesture / SpatialScaleValue 
# SpatialScaleValue
```kotlin
class SpatialScaleValue(val centroid: NormalizedPoint3D, val scaleValue: Float, val leftInteractionKind: InteractionKind, val rightInteractionKind: InteractionKind, val targetEntity: Entity? = null)
```
Class that holds data for a spatial scale gesture. 
Members 
## Constructors
Spatial Scale Value 
```kotlin
constructor(centroid: NormalizedPoint3D, scaleValue: Float, leftInteractionKind: InteractionKind, rightInteractionKind: InteractionKind, targetEntity: Entity? = null)
```
## Properties
centroid 
```kotlin
val centroid: NormalizedPoint3D
```
The centroid of the two pointers that are currently performing the scale gesture. 
left Interaction Kind 
```kotlin
val leftInteractionKind: InteractionKind
```
The kind of interaction that is currently being performed by the left hand. 
right Interaction Kind 
```kotlin
val rightInteractionKind: InteractionKind
```
The kind of interaction that is currently being performed by the right hand. 
scale Value 
```kotlin
val scaleValue: Float
```
The scale value of the gesture. This is the difference between the current scale and the previous scale. For lifecycle callbacks such as  onScaleStart ,  onScaleEnd , and  onScaleCancel , this value is  1f . 
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