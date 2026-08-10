# detectDragGestures | PICO Spatial SDK

ui:foundation / com.pico.spatial.ui.foundation.gesture / detectDragGestures 
# detectDragGestures
```kotlin
suspend fun PointerInputScope.detectDragGestures(onDragStart: (Offset) -> Unit = {}, onDragEnd: () -> Unit = {}, onDragCancel: () -> Unit = {}, context: Context, targetedToEntity: TargetEntity?, onDrag: (change: PointerInputChange, dragAmount: Offset) -> Unit)
```
Gesture detector that waits for pointer down and touch slop in any direction and then calls  onDrag  for each drag event. It follows the touch slop detection of  awaitTouchSlopOrCancellation  but will consume the position change automatically once the touch slop has been crossed. 
Entity  is not interactable by default. To make an  Entity  interactable, you should both add a  InteractableComponent  and a  CollisionComponent  to this entity. 
When  targetedToEntity  is set, means that this gesture detector is bind to  Entity  that match  TargetEntity 's rule. 
onDragStart  called when the touch slop has been passed and includes an  Offset  representing the last known pointer position relative to the containing element. The  Offset  can be outside the actual bounds of the element itself meaning the numbers can be negative or larger than the element bounds if the touch target is smaller than the  ViewConfiguration.minimumTouchTargetSize . 
onDragEnd  is called after all pointers are up and  onDragCancel  is called if another gesture has consumed pointer input, canceling this gesture. 
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
                detectDragGestures(context = context, targetedToEntity = TargetEntity.any()) {
                    change,
                    dragAmount ->
                    // do something here
                    println("ondrag, delta: x = ${dragAmount.x}, y = ${dragAmount.y}")
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