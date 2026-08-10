# requiredDepth | PICO Spatial SDK

ui:foundation / com.pico.spatial.ui.foundation.layout / requiredDepth 
# requiredDepth
```kotlin
@Stable
```fun  Modifier . requiredDepth ( depth :  Dp ) :  Modifier 
Declare the depth of the content to be exactly  depth dp. The incoming measurement  Constraints3D  will not override this value. If the content chooses a size that does not satisfy the incoming  Constraints3D , the parent layout will be reported a size coerced in the  Constraints3D , and the position of the content will be automatically offset to be centered on the space assigned to the child by the parent layout under the assumption that  Constraints3D  were respected. 
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