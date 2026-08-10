# detectSpatialTapGesture | PICO Spatial SDK

ui:foundation / com.pico.spatial.ui.foundation.gesture / detectSpatialTapGesture 
# detectSpatialTapGesture
```kotlin
suspend fun PointerInputScope.detectSpatialTapGesture(context: Context, targetedToEntity: TargetEntity? = null, onTap: (value: SpatialTapValue) -> Unit)
```
Gesture detector that detects spatial tap gesture.  onTap  will be invoked when a spatial tap gesture happens with a  SpatialTapValue  that holds data for the tap gesture, such as the position3D and entity. Compared to compose tap gesture detector, spatial tap gesture is useful for 3D interaction. Such as detect a gesture on a 3D model or 3D rotation view. 
Entity  is not interactable by default. To make an  Entity  interactable, you should both add a  InteractableComponent  and a  CollisionComponent  to this entity. 
When  targetedToEntity  is set, means that this gesture detector is bind to  Entity  that match  TargetEntity 's rule. 
#### Parameters
context 
Android context. You can get context by  LocalContext .current. 
targeted To Entity 
Indicate how this gesture detector bind to Entity. If is null, both 2D and 3D interaction event can be detected by this gesture. 
on Tap 
Invoke when a spatial tap gesture happens. 
#### Samples
```
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.size
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Modifier
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
import com.pico.spatial.ui.foundation.effect3d.rotate3D
import com.pico.spatial.ui.foundation.geometry.RotationAxis3D
import com.pico.spatial.ui.foundation.gesture.TargetEntity
import com.pico.spatial.ui.foundation.gesture.detectSpatialTapGesture
import com.pico.spatial.ui.foundation.layout.offset

fun main() { 
   //sampleStart 
   val context = LocalContext.current
Box(
    modifier =
        Modifier.size(200.dp)
            .offset(z = 100.dp)
            .rotate3D(degree = 30f, axis = RotationAxis3D.XY)
            .pointerInput(Unit) {
                detectSpatialTapGesture(context) { println("tap at ${it.position}") }
            }
) 
   //sampleEnd
}
```
```
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.size
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Modifier
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
import com.pico.spatial.ui.foundation.effect3d.rotate3D
import com.pico.spatial.ui.foundation.geometry.RotationAxis3D
import com.pico.spatial.ui.foundation.gesture.TargetEntity
import com.pico.spatial.ui.foundation.gesture.detectSpatialTapGesture
import com.pico.spatial.ui.foundation.layout.offset

fun main() { 
   //sampleStart 
   val context = LocalContext.current
// 1. define a variable to record the last tap entity
var lastTapEntity by remember { mutableStateOf<Entity?>(null) }
SpatialView(
    modifier =
        Modifier.fillMaxSize().pointerInput(Unit) {
            // 2. detect tap gesture
            detectSpatialTapGesture(context, targetedToEntity = TargetEntity.any()) {
                // 3. update the last tap entity
                lastTapEntity = it.targetEntity
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
        content.entities.forEach { entity ->
            // 4. update the scale of the entity
            @Suppress("MagicNumber") val scale = if (entity == lastTapEntity) 1.3f else 1f
            entity.components[TransformComponent::class.java]?.setScaleVector(
                Vector3(scale, scale, scale)
            )
        }
    },
) 
   //sampleEnd
}
```