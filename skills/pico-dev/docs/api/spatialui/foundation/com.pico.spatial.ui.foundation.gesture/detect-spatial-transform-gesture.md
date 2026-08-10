# detectSpatialTransformGesture | PICO Spatial SDK

ui:foundation / com.pico.spatial.ui.foundation.gesture / detectSpatialTransformGesture 
# detectSpatialTransformGesture
```kotlin
suspend fun PointerInputScope.detectSpatialTransformGesture(context: Context, targetedToEntity: TargetEntity? = null, constraintsRotationAxis: RotationAxis3D? = null, onTransformBegin: () -> Unit = {}, onTransformEnd: () -> Unit = {}, onTransformCancel: () -> Unit = {}, onTransform: (value: SpatialTransformValue) -> Unit)
```
Detect spatial transform gesture. it includes translation, rotation, and scaling. it is detected when the user performs a gesture on a 3D model or in the spatial environment. when the gesture is detected, the  onTransform  callback will be invoked. when the gesture is canceled, the  onTransformCancel  callback will be invoked. In the  onTransform  callback, the  SpatialTransformValue  will provide the transform value, it includes centroid, translation, rotation, scaling, interaction kind and target entity.the centroid is the center point of the pointers. the translation value is the distance between the current pointer position and the previous pointer position. the rotation value is the angle between the current pointer position and the previous pointer position. the scaling value is the distance between the current pointer position and the previous pointer position. the interaction kind is the kind of interaction that triggers the transform gesture. the target entity is the entity to which the transform gesture is targeted. If null, the transform gesture is not targeted to any entity. 
#### Parameters
context 
The context of the application. 
targeted To Entity 
The entity to which the gesture is targeted. If null, the gesture is not targeted to any entity. 
constraints Rotation Axis 
The axis around which the rotation gesture is constrained. If null, the rotation gesture is not constrained. 
on Transform Begin 
The callback to invoke when the transform gesture begins. 
on Transform End 
The callback to invoke when the transform gesture ends. 
on Transform Cancel 
The callback to invoke when the transform gesture is canceled. 
on Transform 
The callback to invoke when the transform gesture is updated. 
#### Samples
```
import androidx.compose.foundation.layout.offset
import androidx.compose.foundation.layout.size
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableFloatStateOf
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Modifier
import androidx.compose.ui.input.pointer.pointerInput
import androidx.compose.ui.platform.LocalContext
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
import com.pico.spatial.ui.foundation.effect3d.scale3D
import com.pico.spatial.ui.foundation.geometry.Rotation3D
import com.pico.spatial.ui.foundation.gesture.TargetEntity
import com.pico.spatial.ui.foundation.gesture.detectSpatialTransformGesture
import com.pico.spatial.ui.foundation.layout.zOffset
import com.pico.spatial.ui.geometry.Offset3D
import kotlin.math.roundToInt

fun main() { 
   //sampleStart 
   val context = LocalContext.current
var rotation by remember { mutableStateOf(Rotation3D.identity()) }
var pan by remember { mutableStateOf(Offset3D.Zero) }
var scale by remember { mutableFloatStateOf(1f) }
SpatialModelView(
    modifier =
        Modifier.offset { IntOffset(x = pan.x.roundToInt(), y = pan.y.roundToInt()) }
            .zOffset { pan.z }
            .scale3D(scale)
            .rotate3D { rotation }
            .size(200.dp)
            .pointerInput(Unit) {
                detectSpatialTransformGesture(
                    context = context,
                    targetedToEntity = TargetEntity.any(),
                ) {
                    rotation = rotation.rotateBy(it.rotation)
                    pan += it.dragAmount
                    scale *= it.scaleValue
                }
            },
    source = Source.assets("alarm.usdz"),
) 
   //sampleEnd
}
```
```
import androidx.compose.foundation.layout.offset
import androidx.compose.foundation.layout.size
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableFloatStateOf
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Modifier
import androidx.compose.ui.input.pointer.pointerInput
import androidx.compose.ui.platform.LocalContext
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
import com.pico.spatial.ui.foundation.effect3d.scale3D
import com.pico.spatial.ui.foundation.geometry.Rotation3D
import com.pico.spatial.ui.foundation.gesture.TargetEntity
import com.pico.spatial.ui.foundation.gesture.detectSpatialTransformGesture
import com.pico.spatial.ui.foundation.layout.zOffset
import com.pico.spatial.ui.geometry.Offset3D
import kotlin.math.roundToInt

fun main() { 
   //sampleStart 
   val context = LocalContext.current
var rotation by remember { mutableStateOf(Rotation3D.identity()) }
var pan by remember { mutableStateOf(Offset3D.Zero) }
var scale by remember { mutableFloatStateOf(1f) }

SpatialView(
    modifier =
        Modifier.size(200.dp).pointerInput(Unit) {
            detectSpatialTransformGesture(
                context = context,
                targetedToEntity = TargetEntity.any(),
            ) {
                rotation = rotation.rotateBy(it.rotation)
                pan += it.dragAmount
                scale *= it.scaleValue
            }
        },
    initial = { content, _ ->
        val entity = Entity()
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
        val convertVector3 =
            content.convertPosition(
                pan.toVector3(),
                ViewCoordinateSpace.Global,
                content.localSpatialCoordinateSpace,
            )

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
            ?.setPosition(convertVector3)
            ?.setScaleVector(Vector3(scale, scale, scale))
    },
) 
   //sampleEnd
}
```