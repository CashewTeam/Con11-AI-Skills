# zOffset | PICO Spatial SDK

ui:foundation / com.pico.spatial.ui.foundation.layout / zOffset 
# zOffset
```kotlin
fun Modifier.zOffset(offset: Density.() -> Float): Modifier
```
Offset content by  offset  px 
This modifier is designed to be used for offsets that change, possibly due to user interactions. It avoids recomposition when the offset is changing, and also adds a graphics layer that prevents unnecessary redrawing of the context when the offset is changing. 
#### Return
The  Modifier  with expected zOffset value. 
#### See also
graphics Layer 
#### Samples
```
import androidx.compose.animation.core.animateDpAsState
import androidx.compose.foundation.background
import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.size
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.unit.dp
import com.pico.spatial.ui.foundation.layout.offset
import com.pico.spatial.ui.foundation.layout.zOffset

fun main() { 
   //sampleStart 
   var isFloating by remember { mutableStateOf(false) }

val offsetZInDp by
    animateDpAsState(targetValue = if (isFloating) 100.dp else 0.dp, label = "offsetZ")

Box(
    modifier =
        Modifier.zOffset { offsetZInDp.toPx() }
            .size(100.dp)
            .background(color = Color.Black)
            .clickable { isFloating = !isFloating }
) 
   //sampleEnd
}
```