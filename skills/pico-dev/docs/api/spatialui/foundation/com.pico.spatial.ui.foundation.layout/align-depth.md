# alignDepth | PICO Spatial SDK

ui:foundation / com.pico.spatial.ui.foundation.layout / alignDepth 
# alignDepth
```kotlin
@Stable
```fun  Modifier . alignDepth ( alignment :  DepthAlignment  =  DepthAlignment.DepthCenter ) :  Modifier 
Modifier to align the element along the depth axis (usually the Z-axis) of a three-dimensional coordinate system. the default alignment is  DepthAlignment.DepthCenter 
#### Return
Modifier 
#### Parameters
alignment 
The depth alignment to be applied to the element. Default is  DepthAlignment.DepthCenter . 
#### Samples
```
import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.size
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp
import com.pico.spatial.ui.foundation.layout.DepthAlignment
import com.pico.spatial.ui.foundation.layout.alignDepth
import com.pico.spatial.ui.foundation.layout.depth
import com.pico.spatial.ui.foundation.layout.requiredDepth

fun main() { 
   //sampleStart 
   var depthAlign by remember { mutableStateOf(DepthAlignment.DepthCenter) }
Box(
    Modifier.size(100.dp).requiredDepth(100.dp).alignDepth(depthAlign).clickable {
        depthAlign =
            when (depthAlign) {
                DepthAlignment.DepthFront -> DepthAlignment.DepthCenter
                DepthAlignment.DepthCenter -> DepthAlignment.DepthBack
                DepthAlignment.DepthBack -> DepthAlignment.DepthFront
                else -> DepthAlignment.DepthCenter
            }
    }
) {
    repeat(3) { Box(Modifier.size(50.dp).depth(10.dp).alignDepth(depthAlign)) }
} 
   //sampleEnd
}
```