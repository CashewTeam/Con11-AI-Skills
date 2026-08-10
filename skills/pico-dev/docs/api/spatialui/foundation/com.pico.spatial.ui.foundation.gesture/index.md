# com.pico.spatial.ui.foundation.gesture | PICO Spatial SDK

ui:foundation / com.pico.spatial.ui.foundation.gesture 
# Package-level declarations
Types Functions 
## Types
Spatial Drag Value 
```kotlin
@Immutable
```class  SpatialDragValue ( val  dragAmount :  Offset3D ,  val  interactionKind :  InteractionKind ,  val  inputDevicePose :  InputDevicePose ,  val  targetEntity :  Entity ?  =  null ) 
Class that holds data for a spatial drag gesture. 
Spatial Pointer Info 
```kotlin
@Stable
```class  SpatialPointerInfo ( pointerInputChange :  PointerInputChange ,  spaceExtraInfo :  SpacePointerInfo ? ,  entity :  Entity ?  =  null ) 
A spatial event data generated from an input. 
Spatial Rotate Value 
```kotlin
class SpatialRotateValue(val centroid: NormalizedPoint3D, val rotation: Rotation3D, val leftInteractionKind: InteractionKind, val rightInteractionKind: InteractionKind, val targetEntity: Entity? = null)
```
Class that holds the value of a rotate gesture. 
Spatial Scale Value 
```kotlin
class SpatialScaleValue(val centroid: NormalizedPoint3D, val scaleValue: Float, val leftInteractionKind: InteractionKind, val rightInteractionKind: InteractionKind, val targetEntity: Entity? = null)
```
Class that holds data for a spatial scale gesture. 
Spatial Tap Value 
```kotlin
@Immutable
```class  SpatialTapValue ( val  position :  Offset3D ,  val  interactionKind :  InteractionKind ,  val  targetEntity :  Entity ?  =  null ) 
Class that holds the value of a tap gesture. 
Spatial Transform Value 
```kotlin
@Immutable
```class  SpatialTransformValue ( val  centroid :  NormalizedPoint3D ,  val  dragAmount :  Offset3D ,  val  scaleValue :  Float ,  val  rotation :  Rotation3D ,  val  leftInteractionKind :  InteractionKind ,  val  rightInteractionKind :  InteractionKind ,  val  targetEntity :  Entity ?  =  null ) 
Value class for spatial transform gesture. 
Target Entity 
```kotlin
@Stable
```sealed  class  TargetEntity 
Indicate that how a gesture bind to entities 
## Functions
detect Drag Gestures 
```kotlin
suspend fun PointerInputScope.detectDragGestures(onDragStart: (Offset) -> Unit = {}, onDragEnd: () -> Unit = {}, onDragCancel: () -> Unit = {}, context: Context, targetedToEntity: TargetEntity?, onDrag: (change: PointerInputChange, dragAmount: Offset) -> Unit)
```
Gesture detector that waits for pointer down and touch slop in any direction and then calls  onDrag  for each drag event. It follows the touch slop detection of  awaitTouchSlopOrCancellation  but will consume the position change automatically once the touch slop has been crossed. 
detect Drag Gestures After Long Press 
```kotlin
suspend fun PointerInputScope.detectDragGesturesAfterLongPress(onDragStart: (Offset) -> Unit = {}, onDragEnd: () -> Unit = {}, onDragCancel: () -> Unit = {}, context: Context, targetedToEntity: TargetEntity?, onDrag: (change: PointerInputChange, dragAmount: Offset) -> Unit)
```
Gesture detector that waits for pointer down and long press, after which it calls  onDrag  for each drag event. 
detect Horizontal Drag Gestures 
```kotlin
suspend fun PointerInputScope.detectHorizontalDragGestures(onDragStart: (Offset) -> Unit = {}, onDragEnd: () -> Unit = {}, onDragCancel: () -> Unit = {}, context: Context, targetedToEntity: TargetEntity?, onHorizontalDrag: (change: PointerInputChange, dragAmount: Float) -> Unit)
```
Gesture detector that waits for pointer down and touch slop in the horizontal direction and then calls  onHorizontalDrag  for each horizontal drag event. It follows the touch slop detection of  awaitHorizontalTouchSlopOrCancellation , but will consume the position change automatically once the touch slop has been crossed. 
detect Spatial Drag Gesture 
```kotlin
suspend fun PointerInputScope.detectSpatialDragGesture(context: Context, targetedToEntity: TargetEntity? = null, onDragStart: (location: Offset3D, dragValue: SpatialDragValue) -> Unit = { _, _ -> }, onDragEnd: (dragValue: SpatialDragValue) -> Unit = {}, onDragCancel: (dragValue: SpatialDragValue) -> Unit = {}, onDrag: (dragValue: SpatialDragValue) -> Unit)
```
Gesture detector that detects a spatial drag and calls  onDrag  for each event with a 3D drag amount, see  SpatialDragValue . Usually, you can apply this gesture detector to a composable view, and apply the 3D drag value to a 2D view, through Modifier.offset and Modifier.zOffset, or to a 3D model  Entity  through  TransformComponent .  Entity  is not interactable by default. To make an  Entity  interactable, you should both add a  InteractableComponent  and a  CollisionComponent  to this entity. Params  targetedToEntity  determines how the gesture is bound to entities or not. Null means that this gesture can detect drag event happens on 2D view and 3D model within this view. See at  TargetEntity  for more details. 
detect Spatial Pointer Event 
```kotlin
suspend fun PointerInputScope.detectSpatialPointerEvent(context: Context, targetedToEntity: TargetEntity? = null, onEvent: (eventCollection: List<SpatialPointerInfo>) -> Boolean)
```
Gesture detector that detects spatial pointer interaction events.  onEvent  will be invoked when pointers down, moving and up. You can use this detector to implement custom gestures, such as spatial rotation or zoom. 
detect Spatial Rotate Gesture 
```kotlin
suspend fun PointerInputScope.detectSpatialRotateGesture(context: Context, targetedToEntity: TargetEntity? = null, constraintsRotationAxis: RotationAxis3D? = null, onRotateStart: (value: SpatialRotateValue) -> Unit = {}, onRotateEnd: (value: SpatialRotateValue) -> Unit = {}, onRotateCancel: (value: SpatialRotateValue) -> Unit = {}, onRotate: (value: SpatialRotateValue) -> Unit)
```
Gesture detector that detects a spatial rotate and calls  onRotate  for each event with a 3D rotate value, see  SpatialRotateValue . Usually, you can apply this gesture detector to a composable view, and apply the 3D rotate value to a 2D view, through Modifier.rotate3d or Modifier.graphicsLayer, or to a 3D model  Entity  through TransformComponent.  Entity  is not interactable by default. To make an  Entity  interactable, you should both add a InteractableComponent and a CollisionComponent to this entity. Params  targetedToEntity  determines how the gesture is bound to entities or not. Null means that this gesture can detect rotate event happens on 2D view and 3D model within this view. See at  TargetEntity  for more details. 
detect Spatial Scale Gesture 
```kotlin
suspend fun PointerInputScope.detectSpatialScaleGesture(context: Context, targetedToEntity: TargetEntity? = null, onScaleStart: (scale: SpatialScaleValue) -> Unit = {}, onScaleEnd: (scale: SpatialScaleValue) -> Unit = {}, onScaleCancel: (scale: SpatialScaleValue) -> Unit = {}, onScale: (scale: SpatialScaleValue) -> Unit)
```
Gesture detector that detects a spatial scale and calls  onScale  for each event with a 3D scale value, see  SpatialScaleValue . Usually, you can apply this gesture detector to a composable view, and apply the 3D scale value to a 2D view, through Modifier.scale or Modifier.graphicsLayer, or to a 3D model  Entity  through  TransformComponent .  Entity  is not interactable by default. To make an  Entity  interactable, you should both add a  InteractableComponent  and a  CollisionComponent  to this entity. Params  targetedToEntity  determines how the gesture is bound to entities or not. Null means that this gesture can detect scale event happens on 2D view and 3D model within this view. See at  TargetEntity  for more details. 
detect Spatial Tap Gesture 
```kotlin
suspend fun PointerInputScope.detectSpatialTapGesture(context: Context, targetedToEntity: TargetEntity? = null, onTap: (value: SpatialTapValue) -> Unit)
```
Gesture detector that detects spatial tap gesture.  onTap  will be invoked when a spatial tap gesture happens with a  SpatialTapValue  that holds data for the tap gesture, such as the position3D and entity. Compared to compose tap gesture detector, spatial tap gesture is useful for 3D interaction. Such as detect a gesture on a 3D model or 3D rotation view. 
detect Spatial Transform Gesture 
```kotlin
suspend fun PointerInputScope.detectSpatialTransformGesture(context: Context, targetedToEntity: TargetEntity? = null, constraintsRotationAxis: RotationAxis3D? = null, onTransformBegin: () -> Unit = {}, onTransformEnd: () -> Unit = {}, onTransformCancel: () -> Unit = {}, onTransform: (value: SpatialTransformValue) -> Unit)
```
Detect spatial transform gesture. it includes translation, rotation, and scaling. it is detected when the user performs a gesture on a 3D model or in the spatial environment. when the gesture is detected, the  onTransform  callback will be invoked. when the gesture is canceled, the  onTransformCancel  callback will be invoked. In the  onTransform  callback, the  SpatialTransformValue  will provide the transform value, it includes centroid, translation, rotation, scaling, interaction kind and target entity.the centroid is the center point of the pointers. the translation value is the distance between the current pointer position and the previous pointer position. the rotation value is the angle between the current pointer position and the previous pointer position. the scaling value is the distance between the current pointer position and the previous pointer position. the interaction kind is the kind of interaction that triggers the transform gesture. the target entity is the entity to which the transform gesture is targeted. If null, the transform gesture is not targeted to any entity. 
detect Tap Gestures 
```kotlin
suspend fun PointerInputScope.detectTapGestures(context: Context, targetedToEntity: TargetEntity?, onDoubleTap: (Offset) -> Unit? = null, onLongPress: (Offset) -> Unit? = null, onPress: suspend PressGestureScope.(Offset) -> Unit = NoPressGesture, onTap: (Offset) -> Unit? = null)
```
Detects tap, double-tap, and long press gestures and calls  onTap ,  onDoubleTap , and  onLongPress , respectively, when detected.  onPress  is called when the press is detected and the  PressGestureScope.tryAwaitRelease  and  PressGestureScope.awaitRelease  can be used to detect when pointers have released or the gesture was canceled. The first pointer down and final pointer up are consumed, and in the case of long press, all changes after the long press is detected are consumed. 
detect Vertical Drag Gestures 
```kotlin
suspend fun PointerInputScope.detectVerticalDragGestures(onDragStart: (Offset) -> Unit = {}, onDragEnd: () -> Unit = {}, onDragCancel: () -> Unit = {}, context: Context, targetedToEntity: TargetEntity?, onVerticalDrag: (change: PointerInputChange, dragAmount: Float) -> Unit)
```
Gesture detector that waits for pointer down and touch slop in the vertical direction and then calls  onVerticalDrag  for each vertical drag event. It follows the touch slop detection of  awaitVerticalTouchSlopOrCancellation , but will consume the position change automatically once the touch slop has been crossed.