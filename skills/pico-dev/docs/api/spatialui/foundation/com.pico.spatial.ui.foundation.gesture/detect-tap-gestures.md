# detectTapGestures | PICO Spatial SDK

ui:foundation / com.pico.spatial.ui.foundation.gesture / detectTapGestures 
# detectTapGestures
```kotlin
suspend fun PointerInputScope.detectTapGestures(context: Context, targetedToEntity: TargetEntity?, onDoubleTap: (Offset) -> Unit? = null, onLongPress: (Offset) -> Unit? = null, onPress: suspend PressGestureScope.(Offset) -> Unit = NoPressGesture, onTap: (Offset) -> Unit? = null)
```
Detects tap, double-tap, and long press gestures and calls  onTap ,  onDoubleTap , and  onLongPress , respectively, when detected.  onPress  is called when the press is detected and the  PressGestureScope.tryAwaitRelease  and  PressGestureScope.awaitRelease  can be used to detect when pointers have released or the gesture was canceled. The first pointer down and final pointer up are consumed, and in the case of long press, all changes after the long press is detected are consumed. 
Entity  is not interactable by default. To make an  Entity  interactable, you should both add a  InteractableComponent  and a  CollisionComponent  to this entity. 
When  targetedToEntity  is set, means that this gesture detector is bind to  Entity  that match  TargetEntity 's rule. 
Each function parameter receives an  Offset  representing the position relative to the containing element. The  Offset  can be outside the actual bounds of the element itself meaning the numbers can be negative or larger than the element bounds if the touch target is smaller than the  ViewConfiguration.minimumTouchTargetSize . 
When  onDoubleTap  is provided, the tap gesture is detected only after the  ViewConfiguration.doubleTapMinTimeMillis  has passed and  onDoubleTap  is called if the second tap is started before  ViewConfiguration.doubleTapTimeoutMillis . If  onDoubleTap  is not provided, then  onTap  is called when the pointer up has been received. 
After the initial  onPress , if the pointer moves out of the input area, the position change is consumed, or another gesture consumes the down or up events, the gestures are considered canceled. That means  onDoubleTap ,  onLongPress , and  onTap  will not be called after a gesture has been canceled. 
If the first down event is consumed somewhere else, the entire gesture will be skipped, including  onPress . 
#### Parameters
context 
Android context. You can get context by  LocalContext .current. 
targeted To Entity 
Indicate how this gesture detector bind to Entity. If is null, both 2D and 3D interaction event can be detected by this gesture. 
on Double Tap 
Double tab callback 
on Long Press 
Long press callback 
on Press 
Invoked when press down 
on Tap 
Tap callback 
#### Samples
```
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Modifier
import androidx.compose.ui.input.pointer.pointerInput
import androidx.compose.ui.platform.LocalContext
import com.pico.spatial.core.ecs.CollisionComponent
import com.pico.spatial.core.ecs.Entity
import com.pico.spatial.core.ecs.InteractableComponent
import com.pico.spatial.core.ecs.TransformComponent
import com.pico.spatial.core.ecs.ViewCoordinateSpace
import com.pico.spatial.core.ecs.resource.PhysicsMaterialResource
import com.pico.spatial.core.ecs.resource.ShapeResource
import com.pico.spatial.ui.foundation.content.SpatialView
import com.pico.spatial.ui.foundation.gesture.TargetEntity
import com.pico.spatial.ui.foundation.gesture.data.InputDevicePose
import com.pico.spatial.ui.foundation.gesture.detectDragGestures
import com.pico.spatial.ui.foundation.gesture.detectDragGesturesAfterLongPress
import com.pico.spatial.ui.foundation.gesture.detectHorizontalDragGestures
import com.pico.spatial.ui.foundation.gesture.detectSpatialPointerEvent
import com.pico.spatial.ui.foundation.gesture.detectTapGestures
import com.pico.spatial.ui.foundation.gesture.detectVerticalDragGestures

fun main() { 
   //sampleStart 
   val context = LocalContext.current
SpatialView(
    modifier =
        Modifier.fillMaxSize() // make it as large as possible to receive touch event
            .pointerInput(Unit) {
                detectTapGestures(context = context, targetedToEntity = TargetEntity.any()) {
                    // do something here
                    println("tap invoked!")
                }
            }
) { content, _ ->
    val entity = Entity()
    // Entity is not interactable by default. To make an entity interactable, you should both
    // add a
    // [InputTargetComponent] and a [CollisionComponent].
    entity.components.set(InteractableComponent())
    entity.components.set(
        CollisionComponent(
            collisionShape = listOf(ShapeResource.createSphere(radius = 0.3f)),
            physicsMaterial = PhysicsMaterialResource(),
        )
    )
    content.addEntity(entity)
} 
   //sampleEnd
}
```