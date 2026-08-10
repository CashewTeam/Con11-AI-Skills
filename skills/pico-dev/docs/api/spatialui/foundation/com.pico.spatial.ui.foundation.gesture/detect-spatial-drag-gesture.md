# detectSpatialDragGesture | PICO Spatial SDK

ui:foundation / com.pico.spatial.ui.foundation.gesture / detectSpatialDragGesture 
# detectSpatialDragGesture
```kotlin
suspend fun PointerInputScope.detectSpatialDragGesture(context: Context, targetedToEntity: TargetEntity? = null, onDragStart: (location: Offset3D, dragValue: SpatialDragValue) -> Unit = { _, _ -> }, onDragEnd: (dragValue: SpatialDragValue) -> Unit = {}, onDragCancel: (dragValue: SpatialDragValue) -> Unit = {}, onDrag: (dragValue: SpatialDragValue) -> Unit)
```
Gesture detector that detects a spatial drag and calls  onDrag  for each event with a 3D drag amount, see  SpatialDragValue . Usually, you can apply this gesture detector to a composable view, and apply the 3D drag value to a 2D view, through Modifier.offset and Modifier.zOffset, or to a 3D model  Entity  through  TransformComponent .  Entity  is not interactable by default. To make an  Entity  interactable, you should both add a  InteractableComponent  and a  CollisionComponent  to this entity. Params  targetedToEntity  determines how the gesture is bound to entities or not. Null means that this gesture can detect drag event happens on 2D view and 3D model within this view. See at  TargetEntity  for more details. 
#### Parameters
context 
Android context. You can get context by  LocalContext .current. 
targeted To Entity 
The entity that this gesture is bound to. 
on Drag Start 
The callback that is called when the drag gesture starts. The first parameter is the drag start location, and the second parameter provides the current drag context with  SpatialDragValue.dragAmount  set to  Offset3D.Zero . 
on Drag End 
The callback that is called when the drag gesture ends. It provides the last valid drag context with  SpatialDragValue.dragAmount  set to  Offset3D.Zero . 
on Drag Cancel 
The callback that is called when the drag gesture is canceled. It provides the last valid drag context with  SpatialDragValue.dragAmount  set to  Offset3D.Zero . 
on Drag 
The callback that is called for each drag event. 
#### Samples
```
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.offset
import androidx.compose.foundation.layout.size
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.input.pointer.pointerInput
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.platform.LocalDensity
import androidx.compose.ui.unit.Density
import androidx.compose.ui.unit.IntOffset
import androidx.compose.ui.unit.dp
import com.pico.spatial.core.ecs.CollisionComponent
import com.pico.spatial.core.ecs.Entity
import com.pico.spatial.core.ecs.InteractableComponent
import com.pico.spatial.core.ecs.TransformComponent
import com.pico.spatial.core.ecs.ViewCoordinateSpace
import com.pico.spatial.core.ecs.resource.PhysicsMaterialResource
import com.pico.spatial.core.ecs.resource.ShapeResource
import com.pico.spatial.core.math.Vector3
import com.pico.spatial.ui.foundation.content.Source
import com.pico.spatial.ui.foundation.content.SpatialModelView
import com.pico.spatial.ui.foundation.content.SpatialView
import com.pico.spatial.ui.foundation.effect3d.rotate3D
import com.pico.spatial.ui.foundation.geometry.Rotation3D
import com.pico.spatial.ui.foundation.gesture.TargetEntity
import com.pico.spatial.ui.foundation.gesture.detectSpatialDragGesture
import com.pico.spatial.ui.foundation.layout.zOffset
import com.pico.spatial.ui.geometry.Offset3D
import com.pico.spatial.ui.platform.LengthUnit
import com.pico.spatial.ui.platform.LocalPhysicalLengthConverter
import com.pico.spatial.ui.platform.PhysicalLengthConverter
import kotlin.math.roundToInt

fun main() { 
   //sampleStart 
   Box(modifier = Modifier.fillMaxSize(), contentAlignment = Alignment.Center) {
    val context = LocalContext.current
    var offset3D by remember { mutableStateOf(Offset3D.Zero) }
    Box(
        modifier =
            Modifier.size(250.dp)
                .offset { IntOffset(x = offset3D.x.roundToInt(), y = offset3D.y.roundToInt()) }
                .zOffset { offset3D.z }
                .pointerInput(Unit) {
                    detectSpatialDragGesture(context) { spatialDragValue ->
                        offset3D += spatialDragValue.dragAmount
                    }
                }
    )
} 
   //sampleEnd
}
```
```
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.offset
import androidx.compose.foundation.layout.size
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.input.pointer.pointerInput
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.platform.LocalDensity
import androidx.compose.ui.unit.Density
import androidx.compose.ui.unit.IntOffset
import androidx.compose.ui.unit.dp
import com.pico.spatial.core.ecs.CollisionComponent
import com.pico.spatial.core.ecs.Entity
import com.pico.spatial.core.ecs.InteractableComponent
import com.pico.spatial.core.ecs.TransformComponent
import com.pico.spatial.core.ecs.ViewCoordinateSpace
import com.pico.spatial.core.ecs.resource.PhysicsMaterialResource
import com.pico.spatial.core.ecs.resource.ShapeResource
import com.pico.spatial.core.math.Vector3
import com.pico.spatial.ui.foundation.content.Source
import com.pico.spatial.ui.foundation.content.SpatialModelView
import com.pico.spatial.ui.foundation.content.SpatialView
import com.pico.spatial.ui.foundation.effect3d.rotate3D
import com.pico.spatial.ui.foundation.geometry.Rotation3D
import com.pico.spatial.ui.foundation.gesture.TargetEntity
import com.pico.spatial.ui.foundation.gesture.detectSpatialDragGesture
import com.pico.spatial.ui.foundation.layout.zOffset
import com.pico.spatial.ui.geometry.Offset3D
import com.pico.spatial.ui.platform.LengthUnit
import com.pico.spatial.ui.platform.LocalPhysicalLengthConverter
import com.pico.spatial.ui.platform.PhysicalLengthConverter
import kotlin.math.roundToInt

fun main() { 
   //sampleStart 
   val context = LocalContext.current
val converter = LocalPhysicalLengthConverter.current
val density = LocalDensity.current
var offset3D by remember { mutableStateOf(Offset3D.Zero) }
var rotation by remember { mutableStateOf(Rotation3D.identity()) }
SpatialView(
    modifier =
        Modifier.fillMaxSize().pointerInput(Unit) {
            detectSpatialDragGesture(context = context, targetedToEntity = TargetEntity.any()) {
                offset3D += it.dragAmount
                rotation = it.inputDevicePose.rawRotation
            }
        },
    initial = { content, _ ->
        val entity = Entity()
        // Entity is not interactable by default. To make an entity interactable, you should
        // both
        // add a
        // [InteractableComponent] and a [CollisionComponent].
        entity.components.set(InteractableComponent())
        entity.components.set(
            CollisionComponent(
                collisionShape = listOf(ShapeResource.createSphere(radius = 0.3f)),
                physicsMaterial = PhysicsMaterialResource(),
            )
        )
        content.addEntity(entity)
    },
    update = { content, _ ->
        val convertQuat =
            content.convertRotation(
                rotation.toQuaternion(),
                ViewCoordinateSpace.Global,
                content.localSpatialCoordinateSpace,
            )

        content.entities
            .first()
            .components[TransformComponent::class.java]
            ?.setQuaternion(convertQuat)
            ?.setPosition(
                Vector3(
                    x = convertPxToMeter(offset3D.x, density, converter),
                    y = convertPxToMeter(-offset3D.y, density, converter),
                    z = convertPxToMeter(offset3D.z, density, converter),
                )
            )
    },
) 
   //sampleEnd
}
```