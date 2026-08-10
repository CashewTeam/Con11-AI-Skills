# depthIn | PICO Spatial SDK

ui:foundation / com.pico.spatial.ui.foundation.layout / depthIn 
# depthIn
```kotlin
@Stable
```fun  Modifier . depthIn ( min :  Dp  =  Dp.Unspecified ,  max :  Dp  =  Dp.Unspecified ) :  Modifier 
Constrain the depth of the content to be between  min dp and  max dp as permitted by the incoming measurement  Constraints3D . If the incoming constraints are more restrictive the requested size will obey the incoming constraints and attempt to be as close as possible to the preferred size. 
#### Return
The  Modifier  with expected offset value. 
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