# detectSpatialScaleGesture | PICO Spatial SDK

ui:foundation / com.pico.spatial.ui.foundation.gesture / detectSpatialScaleGesture 
# detectSpatialScaleGesture
```kotlin
suspend fun PointerInputScope.detectSpatialScaleGesture(context: Context, targetedToEntity: TargetEntity? = null, onScaleStart: (scale: SpatialScaleValue) -> Unit = {}, onScaleEnd: (scale: SpatialScaleValue) -> Unit = {}, onScaleCancel: (scale: SpatialScaleValue) -> Unit = {}, onScale: (scale: SpatialScaleValue) -> Unit)
```
Gesture detector that detects a spatial scale and calls  onScale  for each event with a 3D scale value, see  SpatialScaleValue . Usually, you can apply this gesture detector to a composable view, and apply the 3D scale value to a 2D view, through Modifier.scale or Modifier.graphicsLayer, or to a 3D model  Entity  through  TransformComponent .  Entity  is not interactable by default. To make an  Entity  interactable, you should both add a  InteractableComponent  and a  CollisionComponent  to this entity. Params  targetedToEntity  determines how the gesture is bound to entities or not. Null means that this gesture can detect scale event happens on 2D view and 3D model within this view. See at  TargetEntity  for more details. 
#### Parameters
context 
Android context. You can get context by  LocalContext .current. 
targeted To Entity 
The entity that this gesture is bound to. 
on Scale Start 
The callback that is called when the scale gesture starts. It provides the current scale context with  SpatialScaleValue.scaleValue  set to  1f . 
on Scale End 
The callback that is called when the scale gesture ends. It provides the last valid matched scale context with  SpatialScaleValue.scaleValue  set to  1f . 
on Scale Cancel 
The callback that is called when the scale gesture is canceled. It provides the last valid matched scale context with  SpatialScaleValue.scaleValue  set to  1f . 
on Scale 
The callback that is called for each scale event. 
#### Samples
```
import androidx.compose.foundation.background
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.size
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableFloatStateOf
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.scale
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.input.pointer.pointerInput
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.unit.dp
import com.pico.spatial.core.ecs.CollisionComponent
import com.pico.spatial.core.ecs.Entity
import com.pico.spatial.core.ecs.InteractableComponent
import com.pico.spatial.core.ecs.TransformComponent
import com.pico.spatial.core.ecs.resource.PhysicsMaterialResource
import com.pico.spatial.core.ecs.resource.ShapeResource
import com.pico.spatial.core.math.Vector3
import com.pico.spatial.ui.foundation.content.SpatialView
import com.pico.spatial.ui.foundation.effect3d.scale3D
import com.pico.spatial.ui.foundation.geometry.NormalizedPoint3D
import com.pico.spatial.ui.foundation.gesture.TargetEntity
import com.pico.spatial.ui.foundation.gesture.detectSpatialScaleGesture

fun main() { 
   //sampleStart 
   Box(modifier = Modifier.fillMaxSize(), contentAlignment = Alignment.Center) {
    val context = LocalContext.current
    var scale by remember { mutableFloatStateOf(1f) }
    var pivot by remember { mutableStateOf(NormalizedPoint3D.Center) }
    Box(
        modifier =
            Modifier.size(250.dp)
                .scale(scale)
                .background(Color.Red)
                .pointerInput(Unit) {
                    detectSpatialScaleGesture(context) {
                        scale *= it.scaleValue
                        pivot = it.centroid
                    }
                }
                .scale3D(scale = scale, pivot = pivot)
    )
} 
   //sampleEnd
}
```
```
import androidx.compose.foundation.background
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.size
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableFloatStateOf
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.scale
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.input.pointer.pointerInput
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.unit.dp
import com.pico.spatial.core.ecs.CollisionComponent
import com.pico.spatial.core.ecs.Entity
import com.pico.spatial.core.ecs.InteractableComponent
import com.pico.spatial.core.ecs.TransformComponent
import com.pico.spatial.core.ecs.resource.PhysicsMaterialResource
import com.pico.spatial.core.ecs.resource.ShapeResource
import com.pico.spatial.core.math.Vector3
import com.pico.spatial.ui.foundation.content.SpatialView
import com.pico.spatial.ui.foundation.effect3d.scale3D
import com.pico.spatial.ui.foundation.geometry.NormalizedPoint3D
import com.pico.spatial.ui.foundation.gesture.TargetEntity
import com.pico.spatial.ui.foundation.gesture.detectSpatialScaleGesture

fun main() { 
   //sampleStart 
   val context = LocalContext.current
var scale by remember { mutableFloatStateOf(1f) }
SpatialView(
    modifier =
        Modifier.fillMaxSize().pointerInput(Unit) {
            detectSpatialScaleGesture(
                context = context,
                targetedToEntity = TargetEntity.any(),
            ) {
                scale *= it.scaleValue
            }
        },
    initial = { content, _ ->
        val entity = Entity()
        // Entity is not interactable by default. To make an entity interactable, you should
        // both
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
    },
    update = { content, _ ->
        content.entities
            .first()
            .components[TransformComponent::class.java]
            ?.setScaleVector(Vector3(scale, scale, scale))
    },
) 
   //sampleEnd
}
```