# SpatialPointerInfo | PICO Spatial SDK

ui:foundation / com.pico.spatial.ui.foundation.gesture / SpatialPointerInfo 
# SpatialPointerInfo
```kotlin
@Stable
```class  SpatialPointerInfo ( pointerInputChange :  PointerInputChange ,  spaceExtraInfo :  SpacePointerInfo ? ,  entity :  Entity ?  =  null ) 
A spatial event data generated from an input. 
Members 
## Constructors
Spatial Pointer Info 
```kotlin
constructor(pointerInputChange: PointerInputChange, spaceExtraInfo: SpacePointerInfo?, entity: Entity? = null)
```
## Properties
input Device Pose 
```kotlin
val inputDevicePose: InputDevicePose
```
The pose of the input device at the time of the event. 
kind 
```kotlin
val kind: InteractionKind
```
The kind of interaction that is currently being performed. 
pointer Id 
```kotlin
val pointerId: PointerId
```
id of this pointer 
position3D 
```kotlin
val position3D: Offset3D
```
The 3D position of the pointer in the coordinate space of the view. 
pressed 
```kotlin
val pressed: Boolean
```
true  if the pointer event is considered "pressed." For example, finger touching the screen or a mouse button is pressed  pressed  would be  true . 
targeted Entity 
```kotlin
val targetedEntity: Entity?
```
The entity target for this touch, if one exists. 
uptime Millis 
```kotlin
val uptimeMillis: Long
```
The time of the current pointer event, in milliseconds. 
x 
```kotlin
val x: Float
```
X coordinate of the pointer at view local 
y 
```kotlin
val y: Float
```
Y coordinate of the pointer at view local 
z 
```kotlin
val z: Float
```
Z coordinate of the pointer at view local 
## Functions
equals 
```kotlin
open operator override fun equals(other: Any?): Boolean
```hash Code 
```kotlin
open override fun hashCode(): Int
```is Down Event 
```kotlin
fun isDownEvent(): Boolean
```
For example,  MotionEvent.ACTION_DOWN  or  MotionEvent.ACTION_POINTER_DOWN 
is Up Event 
```kotlin
fun isUpEvent(): Boolean
```
For example,  MotionEvent.ACTION_UP  or  MotionEvent.ACTION_POINTER_UP 
to String 
```kotlin
open override fun toString(): String
```