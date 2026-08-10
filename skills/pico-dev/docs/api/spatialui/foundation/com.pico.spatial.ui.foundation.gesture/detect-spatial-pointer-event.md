# detectSpatialPointerEvent | PICO Spatial SDK

ui:foundation / com.pico.spatial.ui.foundation.gesture / detectSpatialPointerEvent 
# detectSpatialPointerEvent
```kotlin
suspend fun PointerInputScope.detectSpatialPointerEvent(context: Context, targetedToEntity: TargetEntity? = null, onEvent: (eventCollection: List<SpatialPointerInfo>) -> Boolean)
```
Gesture detector that detects spatial pointer interaction events.  onEvent  will be invoked when pointers down, moving and up. You can use this detector to implement custom gestures, such as spatial rotation or zoom. 
Entity  is not interactable by default. To make an  Entity  interactable, you should both add a  InteractableComponent  and a  CollisionComponent  to this entity. 
When  targetedToEntity  is set, means that this gesture detector is bind to  Entity  that match  TargetEntity 's rule. 
#### Parameters
context 
Android context. You can get context by  LocalContext .current. 
targeted To Entity 
Indicate how this gesture detector bind to Entity. If is null, both 2D and 3D interaction event can be detected by this gesture. 
on Event 
Invoke when press, moving and up. Multi fingers interaction is supported, so event collection is provided for developers. Return  true  means that this detector consume all of the pointers 
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
// state of InputDevicePose
var devicePose by remember { mutableStateOf(InputDevicePose.identity()) }
SpatialView(
    modifier =
        Modifier.fillMaxSize() // make it as large as possible to receive touch event
            .pointerInput(Unit) {
                detectSpatialPointerEvent(context) { eventCollection ->
                    // do something here
                    eventCollection.forEach { eventInfo ->
                        // get the latest input device pose
                        devicePose = eventInfo.inputDevicePose
                    }
                    true
                }
            },
    update = { content, _ ->
        val updateQuat =
            content.convertRotation(
                devicePose.rawRotation.toQuaternion(),
                ViewCoordinateSpace.Global,
                content.localSpatialCoordinateSpace,
            )
        content.entities
            .first()
            .components[TransformComponent::class.java]
            ?.setQuaternion(updateQuat)
    },
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