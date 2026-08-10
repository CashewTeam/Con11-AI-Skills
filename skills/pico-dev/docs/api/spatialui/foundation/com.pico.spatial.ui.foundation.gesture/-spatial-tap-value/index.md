# SpatialTapValue | PICO Spatial SDK

ui:foundation / com.pico.spatial.ui.foundation.gesture / SpatialTapValue 
# SpatialTapValue
```kotlin
@Immutable
```class  SpatialTapValue ( val  position :  Offset3D ,  val  interactionKind :  InteractionKind ,  val  targetEntity :  Entity ?  =  null ) 
Class that holds the value of a tap gesture. 
#### Parameters
position 
The position in pixels where a spatial tap happens. And the position 3d value is under view local coordinate. 
interaction Kind 
The interaction kind of the tap gesture. 
target Entity 
The target entity of the tap gesture. When user tap 3d model, targetEntity is the 3d model entity. And it is null when user tap 2d view. 
Members 
## Constructors
Spatial Tap Value 
```kotlin
constructor(position: Offset3D, interactionKind: InteractionKind, targetEntity: Entity? = null)
```
## Properties
interaction Kind 
```kotlin
val interactionKind: InteractionKind
```position 
```kotlin
val position: Offset3D
```target Entity 
```kotlin
val targetEntity: Entity?
```
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