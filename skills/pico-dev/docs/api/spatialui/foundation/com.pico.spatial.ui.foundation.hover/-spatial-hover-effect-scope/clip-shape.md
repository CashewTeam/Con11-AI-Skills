# clipShape | PICO Spatial SDK

ui:foundation / com.pico.spatial.ui.foundation.hover / SpatialHoverEffectScope / clipShape 
# clipShape
```kotlin
abstract fun clipShape(shape: RoundedCornerShape, size: IntSize, offset: IntOffset = IntOffset.Zero)
```
Clip the view with given  shape ,  size  and  offset 
#### Parameters
shape 
the shape of clip 
size 
the size of  shape 
offset 
the offset of  shape , default is  IntOffset.Zero , means the shape is start from the top-left corner of the view 
#### Samples
```
import androidx.compose.foundation.background
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.shape.CircleShape
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.unit.IntOffset
import androidx.compose.ui.unit.IntSize
import androidx.compose.ui.unit.center
import androidx.compose.ui.unit.dp
import com.pico.spatial.ui.foundation.hover.RectangleShape
import com.pico.spatial.ui.foundation.hover.spatialHoverEffect
import com.pico.spatial.ui.foundation.hover.tween
import kotlin.math.min

fun main() { 
   //sampleStart 
   // Demonstrate a Box with clip and alpha changes during hover active and inactive
Box(
    Modifier.spatialHoverEffect {
        val isActive = it.isActive
        val size = it.size
        // clip with a default animation
        clipShape(
            shape = if (isActive) RoundedCornerShape(20.dp) else RoundedCornerShape(0),
            size =
                IntSize(
                    if (isActive) {
                        size.width
                    } else size.width / 2,
                    size.height,
                ),
            IntOffset(0, 0),
        )

        // scale with a default animation
        scale(scale = if (isActive) 2f else 1f)

        // 2. alpha with a default animation
        alpha(if (isActive) 1f else 0f)
        // 3. with a specified animation
        animation(animation = tween(delayMillis = 200)) {
            // some effect
        }
    }
) 
   //sampleEnd
}
```