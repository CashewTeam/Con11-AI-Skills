# LinearProgressIndicator | PICO Spatial SDK

ui:design / com.pico.spatial.ui.design / LinearProgressIndicator 
# LinearProgressIndicator
```kotlin
@Composable
```fun  LinearProgressIndicator ( progress :  ( )  ->  Float ,  modifier :  Modifier  =  Modifier ,  colors :  ProgressColors  =  LinearProgressDefaults.linearProgressColors() ,  edgeStyle :  ProgressIndicatorEdgeStyle  =  ProgressIndicatorEdgeStyle.RoundCorner ,  height :  LinearProgressHeight  =  LinearProgressDefaults.Small ) 
Progress indicators express an unspecified wait time or display the length of a process. By default there is no animation between  progress  values. 
#### Parameters
progress 
The progress of this progress indicator, where 0.0 represents no progress and 1.0 represents full progress. Values outside of this range are coerced into the range. 
modifier 
the  Modifier  to be applied to this progress indicator 
colors 
The colors for the progress indicator 
edge Style 
the style use for the ends of this progress indicator. 
height 
the height of this progress indicator. 
#### Samples
```
import androidx.compose.animation.core.Spring
import androidx.compose.animation.core.animateFloatAsState
import androidx.compose.animation.core.spring
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.layout.width
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Modifier
import androidx.compose.ui.tooling.preview.Preview
import androidx.compose.ui.unit.dp
import com.pico.spatial.ui.design.Button
import com.pico.spatial.ui.design.LinearProgressDefaults
import com.pico.spatial.ui.design.LinearProgressIndicator
import com.pico.spatial.ui.design.Text

fun main() { 
   //sampleStart 
   var count by remember { mutableStateOf(0) }
val progress = { count.toFloat() / 100 }

Column {
    LinearProgressIndicator(progress = progress)
    Spacer(modifier = Modifier.height(10.dp))
    LinearProgressIndicator(progress = progress, height = LinearProgressDefaults.Small)
    Spacer(modifier = Modifier.height(10.dp))
    LinearProgressIndicator(progress = progress, height = LinearProgressDefaults.Regular)
    Spacer(modifier = Modifier.height(10.dp))
    LinearProgressIndicator(
        progress = progress,
        modifier = Modifier.size(width = 200.dp, height = 20.dp),
    )
    Spacer(modifier = Modifier.height(10.dp))
    Text(text = "currentProgress: ${progress.invoke()}")
    Row {
        Button(onClick = { count = (count - 10).coerceIn(0..100) }) { Text("-") }
        Spacer(modifier = Modifier.width(12.dp))
        Button(onClick = { count = (count + 10).coerceIn(0..100) }) { Text("+") }
    }
} 
   //sampleEnd
}
```