# sizeIn3D | PICO Spatial SDK

ui:foundation / com.pico.spatial.ui.foundation.layout / sizeIn3D 
# sizeIn3D
```kotlin
val LayoutCoordinates.sizeIn3D: IntSize3D
```
The 3D size of this layout in the 3D coordinates space. when monitor the layout size change, the size will be updated. get the current size in 3D coordinates space. 
#### Samples
```
import android.util.Log
import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.size
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableIntStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Modifier
import androidx.compose.ui.layout.LayoutCoordinates
import androidx.compose.ui.layout.onGloballyPositioned
import androidx.compose.ui.unit.dp
import com.pico.spatial.ui.foundation.layout.depth
import com.pico.spatial.ui.foundation.layout.sizeIn3D

fun main() { 
   //sampleStart 
   var boxDepth by remember { mutableIntStateOf(0) }
Box(
    Modifier.size(100.dp)
        .depth(boxDepth.dp)
        .onGloballyPositioned {
            val size3D = it.sizeIn3D
            val depth = it.depth
            Log.i("LayoutCoordinatesSample", "sizeIn3D: $size3D, depth: $depth")
        }
        .clickable { boxDepth++ }
) 
   //sampleEnd
}
```