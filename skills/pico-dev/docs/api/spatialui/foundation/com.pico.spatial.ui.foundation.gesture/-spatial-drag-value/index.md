# SpatialDragValue | PICO Spatial SDK

ui:foundation / com.pico.spatial.ui.foundation.gesture / SpatialDragValue 
# SpatialDragValue
```kotlin
@Immutable
```class  SpatialDragValue ( val  dragAmount :  Offset3D ,  val  interactionKind :  InteractionKind ,  val  inputDevicePose :  InputDevicePose ,  val  targetEntity :  Entity ?  =  null ) 
Class that holds data for a spatial drag gesture. 
Members 
## Constructors
Spatial Drag Value 
```kotlin
constructor(dragAmount: Offset3D, interactionKind: InteractionKind, inputDevicePose: InputDevicePose, targetEntity: Entity? = null)
```
## Properties
drag Amount 
```kotlin
val dragAmount: Offset3D
```
3D offset representing the distance moved since the last drag event (delta X, Y, Z) in pixels. Use this to update the position of 2D views (via Modifier.offset and Modifier.zOffset) or 3D entities (via  TransformComponent ). For lifecycle callbacks such as  onDragStart ,  onDragEnd , and  onDragCancel , this value is  Offset3D.Zero . 
input Device Pose 
```kotlin
val inputDevicePose: InputDevicePose
```
Contains the position and orientation of the input device (e.g., controller, hand) at the moment of the drag event, useful for advanced interaction logic. 
interaction Kind 
```kotlin
val interactionKind: InteractionKind
```
Specifies the type of input interaction triggering the drag (e.g., hand tracking, controller input), helping distinguish between different input sources. 
target Entity 
```kotlin
val targetEntity: Entity?
```
The 3D  Entity  being dragged (if the drag targets a 3D model with  InteractableComponent  and  CollisionComponent ). Null if dragging a 2D Compose view. 
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