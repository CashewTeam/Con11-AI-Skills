# SpatialView | PICO Spatial SDK

ui:foundation / com.pico.spatial.ui.foundation.content / SpatialView 
# SpatialView
```kotlin
@Composable
```fun  SpatialView ( modifier :  Modifier  =  Modifier ,  update :  ( content :  SpatialViewContent ,  attachments :  SpatialViewAttachments )  ->  Unit ?  =  null ,  attachments :  AttachmentPanelBuilder . ( )  ->  Unit ?  =  null ,  initial :  suspend  ( content :  SpatialViewContent ,  attachments :  SpatialViewAttachments )  ->  Unit ) 
The container for 3D content. 
#### Parameters
modifier 
The  Modifier  instance used by Jetpack Compose to configure SpatialView layout and state. It will take effect on the 2D part of SpatialView such as background rendering, and the 3D part of SpatialViewContent, such as Entity's opacity, transform, etc. 
update 
Every time the compose state which is read in this function changes, the update will be invoked by the compose runtime. Will be invoked once after initial is called. 
attachments 
A builder function to add compose UI attachments to  SpatialView . You can retrieve an attachment entity in  initial  through the same id if it exists, and then bind the attachment entity to a 3D model entity. (For now, nesting SpatialView within AttachmentPanel is not supported, this feature may be supported in future releases.) 
initial 
A function only invoked once after  SpatialView  is attached to the UI node. You can init and configure your 3D content in this function, such as adding  Entity , binding attachment to Entity 
#### Samples
```
import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.text.BasicText
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableFloatStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp
import com.pico.spatial.core.ecs.Entity
import com.pico.spatial.core.ecs.TransformComponent
import com.pico.spatial.core.math.Vector3
import com.pico.spatial.ui.foundation.content.Source
import com.pico.spatial.ui.foundation.content.SpatialView
import com.pico.spatial.ui.foundation.content.loadFrom
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.withContext

fun main() { 
   //sampleStart 
   SpatialView { content, attachments ->
    val entity = withContext(Dispatchers.IO) { Entity.load("asset://model.glb") }
    content.addEntity(entity)
} 
   //sampleEnd
}
```
```
import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.text.BasicText
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableFloatStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp
import com.pico.spatial.core.ecs.Entity
import com.pico.spatial.core.ecs.TransformComponent
import com.pico.spatial.core.math.Vector3
import com.pico.spatial.ui.foundation.content.Source
import com.pico.spatial.ui.foundation.content.SpatialView
import com.pico.spatial.ui.foundation.content.loadFrom
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.withContext

fun main() { 
   //sampleStart 
   SpatialView(
    initial = { content, attachments ->
        // load main entity from assets
        val entity = withContext(Dispatchers.IO) { Entity.loadFrom(Source.assets("model.glb")) }
        // step2: query attachment entity by id if exist
        attachments.entity("attachment1")?.let {
            // step3: bind attach
            entity.addChild(it)
        }
        // add entity to content
        content.addEntity(entity)
    },
    attachments = {
        // step1: declare a attachment with a unified id
        AttachmentPanel(id = "attachment1") { BasicText(text = "im compose ui") }
    },
) 
   //sampleEnd
}
```
```
import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.text.BasicText
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableFloatStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp
import com.pico.spatial.core.ecs.Entity
import com.pico.spatial.core.ecs.TransformComponent
import com.pico.spatial.core.math.Vector3
import com.pico.spatial.ui.foundation.content.Source
import com.pico.spatial.ui.foundation.content.SpatialView
import com.pico.spatial.ui.foundation.content.loadFrom
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.withContext

fun main() { 
   //sampleStart 
   Column {
    var scale by remember { mutableFloatStateOf(1.0f) }
    SpatialView(
        initial = { content, _ ->
            // load main entity from assets
            val entity = withContext(Dispatchers.IO) { Entity.load("asset://model.glb") }
            // add entity to content
            content.addEntity(entity)
        },
        update = { content, _ ->
            // ECS operation
            val component =
                content.entities.firstOrNull()?.components?.get<TransformComponent>()
            component!!.setScaleVector(scaleVector = Vector3(x = scale, y = scale, z = scale))
        },
    )
    // scale state will be update by click Box,
    Box(modifier = Modifier.size(30.dp).clickable { scale += SCALE_STEP_LENGTH })
} 
   //sampleEnd
}
```