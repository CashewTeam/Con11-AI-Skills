# detectDragGesturesAfterLongPress | PICO Spatial SDK

ui:foundation / com.pico.spatial.ui.foundation.gesture / detectDragGesturesAfterLongPress 
# detectDragGesturesAfterLongPress
```kotlin
suspend fun PointerInputScope.detectDragGesturesAfterLongPress(onDragStart: (Offset) -> Unit = {}, onDragEnd: () -> Unit = {}, onDragCancel: () -> Unit = {}, context: Context, targetedToEntity: TargetEntity?, onDrag: (change: PointerInputChange, dragAmount: Offset) -> Unit)
```
Gesture detector that waits for pointer down and long press, after which it calls  onDrag  for each drag event. 
Entity  is not interactable by default. To make an  Entity  interactable, you should both add a  InteractableComponent  and a  CollisionComponent  to this entity. 
When  targetedToEntity  is set, means that this gesture detector is bind to  Entity  that match  TargetEntity 's rule. 
onDragStart  called when a long press is detected and includes an  Offset  representing the last known pointer position relative to the containing element. The  Offset  can be outside the actual bounds of the element itself meaning the numbers can be negative or larger than the element bounds if the touch target is smaller than the  ViewConfiguration.minimumTouchTargetSize . 
onDragEnd  is called after all pointers are up and  onDragCancel  is called if another gesture has consumed pointer input, canceling this gesture. This function will automatically consume all the position change after the long press. 
#### Parameters
on Drag Start 
Invoked when start drag. 
on Drag End 
Invoked when finish drag. 
on Drag Cancel 
Invoked when drag is canceled. 
context 
Android context. You can get context by  LocalContext .current. 
targeted To Entity 
Indicate how this gesture detector bind to Entity. If is null, both 2D and 3D interaction event can be detected by this gesture. 
on Drag 
Invoked when is dragging.