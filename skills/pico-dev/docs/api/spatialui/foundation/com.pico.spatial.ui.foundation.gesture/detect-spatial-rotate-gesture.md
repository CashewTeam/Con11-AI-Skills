# detectSpatialRotateGesture | PICO Spatial SDK

ui:foundation / com.pico.spatial.ui.foundation.gesture / detectSpatialRotateGesture 
# detectSpatialRotateGesture
```kotlin
suspend fun PointerInputScope.detectSpatialRotateGesture(context: Context, targetedToEntity: TargetEntity? = null, constraintsRotationAxis: RotationAxis3D? = null, onRotateStart: (value: SpatialRotateValue) -> Unit = {}, onRotateEnd: (value: SpatialRotateValue) -> Unit = {}, onRotateCancel: (value: SpatialRotateValue) -> Unit = {}, onRotate: (value: SpatialRotateValue) -> Unit)
```
Gesture detector that detects a spatial rotate and calls  onRotate  for each event with a 3D rotate value, see  SpatialRotateValue . Usually, you can apply this gesture detector to a composable view, and apply the 3D rotate value to a 2D view, through Modifier.rotate3d or Modifier.graphicsLayer, or to a 3D model  Entity  through TransformComponent.  Entity  is not interactable by default. To make an  Entity  interactable, you should both add a InteractableComponent and a CollisionComponent to this entity. Params  targetedToEntity  determines how the gesture is bound to entities or not. Null means that this gesture can detect rotate event happens on 2D view and 3D model within this view. See at  TargetEntity  for more details. 
#### Parameters
context 
The context to access system services. 
targeted To Entity 
The entity to which the gesture is targeted. If null, the gesture is not targeted to any entity. 
constraints Rotation Axis 
The axis around which the rotation is constrained. If null, the rotation is not constrained. 
on Rotate Start 
The callback to be invoked when the rotate gesture starts. It provides the current rotate context with  SpatialRotateValue.rotation  set to  Rotation3D.identity . 
on Rotate End 
The callback to be invoked when the rotate gesture ends. It provides the last valid matched rotate context with  SpatialRotateValue.rotation  set to  Rotation3D.identity . 
on Rotate Cancel 
The callback to be invoked when the rotate gesture is canceled. It provides the last valid matched rotate context with  SpatialRotateValue.rotation  set to  Rotation3D.identity . 
on Rotate 
The callback to be invoked when the rotate gesture is changed. 
#### Samples
```
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
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
import com.pico.spatial.core.ecs.ViewCoordinateSpace
import com.pico.spatial.core.ecs.resource.PhysicsMaterialResource
import com.pico.spatial.core.ecs.resource.ShapeResource
import com.pico.spatial.ui.foundation.content.Source
import com.pico.spatial.ui.foundation.content.SpatialModelView
import com.pico.spatial.ui.foundation.content.SpatialView
import com.pico.spatial.ui.foundation.effect3d.rotate3D
import com.pico.spatial.ui.foundation.geometry.Rotation3D
import com.pico.spatial.ui.foundation.gesture.TargetEntity
import com.pico.spatial.ui.foundation.gesture.detectSpatialRotateGesture

fun main() { 
   //sampleStart 
   val context = LocalContext.current
var rotation by remember { mutableStateOf(Rotation3D.identity()) }
SpatialModelView(
    modifier =
        Modifier.fillMaxSize()
            .pointerInput(Unit) {
                detectSpatialRotateGesture(
                    context = context,
                    targetedToEntity = TargetEntity.any(),
                ) {
                    rotation = rotation.rotateBy(it.rotation.toQuaternion())
                }
            }
            .rotate3D { rotation },
    source = Source.assets("alarm.usdz"),
) 
   //sampleEnd
}
```
```
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
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
import com.pico.spatial.core.ecs.ViewCoordinateSpace
import com.pico.spatial.core.ecs.resource.PhysicsMaterialResource
import com.pico.spatial.core.ecs.resource.ShapeResource
import com.pico.spatial.ui.foundation.content.Source
import com.pico.spatial.ui.foundation.content.SpatialModelView
import com.pico.spatial.ui.foundation.content.SpatialView
import com.pico.spatial.ui.foundation.effect3d.rotate3D
import com.pico.spatial.ui.foundation.geometry.Rotation3D
import com.pico.spatial.ui.foundation.gesture.TargetEntity
import com.pico.spatial.ui.foundation.gesture.detectSpatialRotateGesture

fun main() { 
   //sampleStart 
   val context = LocalContext.current
var rotation by remember { mutableStateOf(Rotation3D.identity()) }
Box(
    modifier =
        Modifier.fillMaxSize()
            .pointerInput(Unit) {
                detectSpatialRotateGesture(context = context) {
                    rotation = rotation.rotateBy(it.rotation.toQuaternion())
                }
            }
            .rotate3D { rotation }
) 
   //sampleEnd
}
```