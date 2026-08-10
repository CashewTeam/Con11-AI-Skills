# scale3D | PICO Spatial SDK

ui:foundation / com.pico.spatial.ui.foundation.effect3d / scale3D 
# scale3D
```kotlin
fun Modifier.scale3D(scaleX: Float, scaleY: Float, scaleZ: Float, pivot: NormalizedPoint3D = NormalizedPoint3D.Center): Modifier
```
Scales the composable by the given  scaleX ,  scaleY  and  scaleZ  factors, around the given  pivot  point. 
#### Return
Modifier  with scale3d 
#### Parameters
scale X 
The scale factor to apply on the X axis. 
scale Y 
The scale factor to apply on the Y axis. 
scale Z 
The scale factor to apply on the Z axis. 
pivot 
The pivot point to scale around. Default is  NormalizedPoint3D.Center 
Usage of this API renders this composable into a separate graphics layer. 
#### See also
graphics Layer 
#### Samples
```
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.text.BasicText
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.tooling.preview.Preview
import com.pico.spatial.core.ecs.Entity
import com.pico.spatial.ui.foundation.content.Source
import com.pico.spatial.ui.foundation.content.SpatialView
import com.pico.spatial.ui.foundation.content.loadFrom
import com.pico.spatial.ui.foundation.effect3d.scale3D
import com.pico.spatial.ui.foundation.geometry.NormalizedPoint3D
import com.pico.spatial.ui.foundation.geometry.Scale3D
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.withContext

fun main() { 
   //sampleStart 
   SpatialView(
    modifier =
        Modifier.scale3D(
            scaleX = 0.5f,
            scaleY = 0.5f,
            scaleZ = 0.5f,
            pivot = NormalizedPoint3D.Center,
        ),
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
        AttachmentPanel(id = "attachment1") { BasicText(text = "Scale 3D") }
    },
) 
   //sampleEnd
}
```
```kotlin
fun Modifier.scale3D(block: () -> Scale3D): Modifier
```
Scales the composable by the given  Scale3D  factors, around the given pivot point. 
#### Return
Modifier  with scale3d 
#### Parameters
block 
The  Scale3D  to apply to the composable 
Usage of this API renders this composable into a separate graphics layer. 
#### See also
graphics Layer 
#### Samples
```
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.text.BasicText
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.tooling.preview.Preview
import com.pico.spatial.core.ecs.Entity
import com.pico.spatial.ui.foundation.content.Source
import com.pico.spatial.ui.foundation.content.SpatialView
import com.pico.spatial.ui.foundation.content.loadFrom
import com.pico.spatial.ui.foundation.effect3d.scale3D
import com.pico.spatial.ui.foundation.geometry.NormalizedPoint3D
import com.pico.spatial.ui.foundation.geometry.Scale3D
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.withContext

fun main() { 
   //sampleStart 
   SpatialView(
    modifier =
        Modifier.scale3D {
            Scale3D(
                scaleX = 0.5f,
                scaleY = 0.5f,
                scaleZ = 0.5f,
                pivot = NormalizedPoint3D.Center,
            )
        },
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
        AttachmentPanel(id = "attachment1") { BasicText(text = "Scale 3D with block") }
    },
) 
   //sampleEnd
}
```
```kotlin
fun Modifier.scale3D(scale: Float, pivot: NormalizedPoint3D = NormalizedPoint3D.Center): Modifier
```
Scales the composable by the given  scale  factor, around the given  pivot  point. 
#### Return
Modifier  with scale3d 
#### Parameters
scale 
The scale factor to apply on the X, Y and Z axis 
pivot 
The pivot point to scale around. Default is  NormalizedPoint3D.Center 
Usage of this API renders this composable into a separate graphics layer. 
#### See also
graphics Layer 
#### Samples
```
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.text.BasicText
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.tooling.preview.Preview
import com.pico.spatial.core.ecs.Entity
import com.pico.spatial.ui.foundation.content.Source
import com.pico.spatial.ui.foundation.content.SpatialView
import com.pico.spatial.ui.foundation.content.loadFrom
import com.pico.spatial.ui.foundation.effect3d.scale3D
import com.pico.spatial.ui.foundation.geometry.NormalizedPoint3D
import com.pico.spatial.ui.foundation.geometry.Scale3D
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.withContext

fun main() { 
   //sampleStart 
   SpatialView(
    modifier = Modifier.scale3D(scale = 0.5f, pivot = NormalizedPoint3D.Center),
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
        AttachmentPanel(id = "attachment1") { BasicText(text = "Scale 3D effect with xyz") }
    },
) 
   //sampleEnd
}
```