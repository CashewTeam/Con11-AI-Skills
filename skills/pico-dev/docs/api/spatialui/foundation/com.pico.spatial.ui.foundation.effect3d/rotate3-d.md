# rotate3D | PICO Spatial SDK

ui:foundation / com.pico.spatial.ui.foundation.effect3d / rotate3D 
# rotate3D
```kotlin
fun Modifier.rotate3D(degree: Float, axis: RotationAxis3D, pivot: NormalizedPoint3D = NormalizedPoint3D.Center): Modifier
```
Rotates the composable around the given  axis  and  pivot  by  degree 
#### Return
Modifier  with rotate3d 
#### Parameters
degree 
The degree by which to rotate the composable 
axis 
The axis of rotation, see  RotationAxis3D 
pivot 
The  NormalizedPoint3D  relative the composable about which to perform the rotation 
Usage of this API renders this composable into a separate graphics layer. 
#### See also
graphics Layer 
#### Samples
```
import androidx.compose.animation.core.animateFloat
import androidx.compose.animation.core.infiniteRepeatable
import androidx.compose.animation.core.rememberInfiniteTransition
import androidx.compose.animation.core.tween
import androidx.compose.foundation.background
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.shape.CircleShape
import androidx.compose.foundation.text.BasicText
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.setValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Brush
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.tooling.preview.Preview
import androidx.compose.ui.unit.dp
import com.pico.spatial.ui.foundation.effect3d.rotate3D
import com.pico.spatial.ui.foundation.geometry.NormalizedPoint3D
import com.pico.spatial.ui.foundation.geometry.Rotation3D
import com.pico.spatial.ui.foundation.geometry.RotationAxis3D

fun main() { 
   //sampleStart 
   Box(
    modifier =
        Modifier.rotate3D(degree = 95f, axis = RotationAxis3D.Y)
            .size(200.dp)
            .background(
                brush =
                    Brush.radialGradient(
                        colors = listOf(Color.Green, Color.Red, Color.Yellow, Color.White)
                    ),
                shape = CircleShape,
            ),
    contentAlignment = Alignment.Center,
) {
    BasicText(text = "Rotated circle", color = { Color.White })
} 
   //sampleEnd
}
```
```kotlin
fun Modifier.rotate3D(block: () -> Rotation3D): Modifier
```
Rotates the composable around the given  Rotation3D 
This modifier is designed to be used for rotation that change, possibly due to user interactions. It avoids recomposition when the offset is changing, and also adds a graphics layer that prevents unnecessary redrawing of the context when the offset is changing. 
Usage of this API renders this composable into a separate graphics layer. 
#### Return
Modifier  with rotate3d 
#### Samples
```
import androidx.compose.animation.core.animateFloat
import androidx.compose.animation.core.infiniteRepeatable
import androidx.compose.animation.core.rememberInfiniteTransition
import androidx.compose.animation.core.tween
import androidx.compose.foundation.background
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.shape.CircleShape
import androidx.compose.foundation.text.BasicText
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.setValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Brush
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.tooling.preview.Preview
import androidx.compose.ui.unit.dp
import com.pico.spatial.ui.foundation.effect3d.rotate3D
import com.pico.spatial.ui.foundation.geometry.NormalizedPoint3D
import com.pico.spatial.ui.foundation.geometry.Rotation3D
import com.pico.spatial.ui.foundation.geometry.RotationAxis3D

fun main() { 
   //sampleStart 
   val degree by
    rememberInfiniteTransition("Rotation3D")
        .animateFloat(
            initialValue = 0f,
            targetValue = 360f,
            animationSpec = infiniteRepeatable(tween()),
            label = "degree",
        )

Box(
    modifier =
        Modifier.size(100.dp).background(Color.Green).rotate3D {
            Rotation3D(degree = degree, RotationAxis3D.Y, NormalizedPoint3D.Center)
        },
    contentAlignment = Alignment.Center,
) {
    //
} 
   //sampleEnd
}
```