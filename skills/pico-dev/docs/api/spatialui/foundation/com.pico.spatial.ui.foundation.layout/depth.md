# depth | PICO Spatial SDK

ui:foundation / com.pico.spatial.ui.foundation.layout / depth 
# depth
```kotlin
@Stable
```fun  Modifier . depth ( depth :  Dp  =  Dp.Unspecified ) :  Modifier 
Declare the preferred depth of the content to be exactly  depth dp. The incoming measurement  Constraints3D  may override this value, forcing the content to be either smaller or larger. 
#### Return
The  Modifier  with expected offset value. Example usage: 
#### Samples
```
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.text.BasicText
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.tooling.preview.Preview
import androidx.compose.ui.unit.dp
import com.pico.spatial.ui.foundation.layout.depth
import com.pico.spatial.ui.foundation.layout.depthIn
import com.pico.spatial.ui.foundation.layout.requiredDepth
import com.pico.spatial.ui.foundation.layout.requiredDepthIn

fun main() { 
   //sampleStart 
   Column {
    Box(modifier = Modifier.depth(100.dp)) {
        BasicText(text = "depth", color = { Color.Yellow })
    }

    Box(modifier = Modifier.depthIn(100.dp, 200.dp)) {
        BasicText(text = "depthIn", color = { Color.Yellow })
    }

    Box(modifier = Modifier.requiredDepth(100.dp)) {
        BasicText(text = "requiredDepth", color = { Color.Yellow })
    }

    Box(modifier = Modifier.requiredDepthIn(100.dp, 200.dp)) {
        BasicText(text = "requiredDepth", color = { Color.Yellow })
    }
} 
   //sampleEnd
}
```
```kotlin
val LayoutCoordinates.depth: Int
```
The depth of this layout in the 3D coordinates space. when monitor the layout depth change, the depth will be updated. get the current depth in 3D coordinates space. 
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