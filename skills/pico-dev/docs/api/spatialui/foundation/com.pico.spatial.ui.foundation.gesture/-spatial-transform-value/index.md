# SpatialTransformValue | PICO Spatial SDK

ui:foundation / com.pico.spatial.ui.foundation.gesture / SpatialTransformValue 
# SpatialTransformValue
```kotlin
@Immutable
```class  SpatialTransformValue ( val  centroid :  NormalizedPoint3D ,  val  dragAmount :  Offset3D ,  val  scaleValue :  Float ,  val  rotation :  Rotation3D ,  val  leftInteractionKind :  InteractionKind ,  val  rightInteractionKind :  InteractionKind ,  val  targetEntity :  Entity ?  =  null ) 
Value class for spatial transform gesture. 
Members 
## Constructors
Spatial Transform Value 
```kotlin
constructor(centroid: NormalizedPoint3D, dragAmount: Offset3D, scaleValue: Float, rotation: Rotation3D, leftInteractionKind: InteractionKind, rightInteractionKind: InteractionKind, targetEntity: Entity? = null)
```
## Properties
centroid 
```kotlin
val centroid: NormalizedPoint3D
```
The centroid point of the transform gesture in normalized space. 
drag Amount 
```kotlin
val dragAmount: Offset3D
```
The drag amount of the transform gesture in normalized space. 
left Interaction Kind 
```kotlin
val leftInteractionKind: InteractionKind
```
The interaction kind of the left hand. 
right Interaction Kind 
```kotlin
val rightInteractionKind: InteractionKind
```
The interaction kind of the right hand. 
rotation 
```kotlin
val rotation: Rotation3D
```
The rotation value of the transform gesture. 
scale Value 
```kotlin
val scaleValue: Float
```
The scale value of the transform gesture. 
target Entity 
```kotlin
val targetEntity: Entity?
```
The target entity of the transform gesture. 
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