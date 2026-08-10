# CircularProgressIndicator | PICO Spatial SDK

ui:design / com.pico.spatial.ui.design / CircularProgressIndicator 
# CircularProgressIndicator
```kotlin
@Composable
```fun  CircularProgressIndicator ( progress :  ( )  ->  Float ,  modifier :  Modifier  =  Modifier ,  colors :  ProgressColors  =  CircularProgressDefaults.circleProgressColors() ,  edgeStyle :  ProgressIndicatorEdgeStyle  =  ProgressIndicatorEdgeStyle.RoundCorner ,  progressSize :  CircularProgressSize  =  CircularProgressDefaults.Small ,  strokeWidth :  Dp  =  progressSize.strokeWidth() ) 
Progress indicators display the length of a process. 
By default there is no animation between  progress  values. You can use  animateFloatAsState  to provide the progress animation 
#### Parameters
progress 
The progress of this progress indicator, where 0.0 represents no progress and 1.0 represents full progress. Values outside of this range are coerced into the range. 
modifier 
the  Modifier  to be applied to this progress indicator 
colors 
The color of the progress indicator. 
edge Style 
the style use for the ends of this progress indicator. 
progress Size 
the size param of this component 
stroke Width 
The stroke width for the progress indicator. 
#### Samples
```
import androidx.compose.animation.core.animateFloatAsState
import androidx.compose.foundation.clickable
import androidx.compose.foundation.interaction.MutableInteractionSource
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.layout.width
import androidx.compose.runtime.Composable
import androidx.compose.runtime.LaunchedEffect
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableFloatStateOf
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.res.painterResource
import androidx.compose.ui.tooling.preview.Preview
import androidx.compose.ui.unit.dp
import com.pico.spatial.ui.design.Button
import com.pico.spatial.ui.design.CircularProgressDefaults
import com.pico.spatial.ui.design.CircularProgressIndicator
import com.pico.spatial.ui.design.Icon
import com.pico.spatial.ui.design.PicoTheme
import com.pico.spatial.ui.design.SymbolicCircularProgressIndicator
import com.pico.spatial.ui.design.Text
import kotlinx.coroutines.delay

fun main() { 
   //sampleStart 
   Column(modifier = Modifier.width(200.dp), horizontalAlignment = Alignment.CenterHorizontally) {
    var progress by remember { mutableStateOf(0f) }
    val progressAnimation by animateFloatAsState(targetValue = progress, label = "")
    // indicator
    CircularProgressIndicator(progress = { progressAnimation })
    Text(text = "currentProgress: $progress")
    Row {
        Button(onClick = { progress -= 0.2f }) { Text("-") }
        Spacer(modifier = Modifier.width(12.dp))
        Button(onClick = { progress += 0.2f }) { Text("+") }
    }
} 
   //sampleEnd
}
```
```kotlin
@Composable
```fun  CircularProgressIndicator ( modifier :  Modifier  =  Modifier ,  color :  Color  =  PicoTheme.colorScheme.labelPrimaryLight ,  progressSize :  CircularProgressSize  =  CircularProgressDefaults.Small ,  strokeWidth :  Dp  =  progressSize.strokeWidth() ) 
Progress indicators express an unspecified wait time, such as loading. 
#### Parameters
modifier 
the  Modifier  to be applied to this progress indicator 
color 
end color of the indicator. 
progress Size 
the size param of this component 
stroke Width 
The stroke width for the progress indicator. 
#### Samples
```
import androidx.compose.animation.core.animateFloatAsState
import androidx.compose.foundation.clickable
import androidx.compose.foundation.interaction.MutableInteractionSource
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.layout.width
import androidx.compose.runtime.Composable
import androidx.compose.runtime.LaunchedEffect
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableFloatStateOf
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.res.painterResource
import androidx.compose.ui.tooling.preview.Preview
import androidx.compose.ui.unit.dp
import com.pico.spatial.ui.design.Button
import com.pico.spatial.ui.design.CircularProgressDefaults
import com.pico.spatial.ui.design.CircularProgressIndicator
import com.pico.spatial.ui.design.Icon
import com.pico.spatial.ui.design.PicoTheme
import com.pico.spatial.ui.design.SymbolicCircularProgressIndicator
import com.pico.spatial.ui.design.Text
import kotlinx.coroutines.delay

fun main() { 
   //sampleStart 
   Row {
    Column {
        // loading
        CircularProgressIndicator(progressSize = CircularProgressDefaults.Small)
        Spacer(modifier = Modifier.height(12.dp))
        CircularProgressIndicator(progressSize = CircularProgressDefaults.Regular)
        Spacer(modifier = Modifier.height(12.dp))
        CircularProgressIndicator(progressSize = CircularProgressDefaults.Max)
        Spacer(modifier = Modifier.height(12.dp))
    }
    Spacer(modifier = Modifier.width(12.dp))
    Column {
        // Finish
        SymbolicCircularProgressIndicator(
            progress = { 1f },
            progressSymbol = {
                Icon(
                    modifier = Modifier.size(12.dp),
                    painter = painterResource(id = R.drawable.ic_sample_finish),
                    contentDescription = null,
                )
            },
            progressSize = CircularProgressDefaults.Small,
            colors =
                CircularProgressDefaults.circleProgressColors(
                    backgroundColor = PicoTheme.colorScheme.labelPrimaryLight,
                    indicatorColor = PicoTheme.colorScheme.labelPrimaryLight,
                ),
        )
        Spacer(modifier = Modifier.height(12.dp))
        // Finish
        SymbolicCircularProgressIndicator(
            progress = { 1f },
            progressSymbol = {
                Icon(
                    modifier = Modifier.size(16.dp),
                    painter = painterResource(id = R.drawable.ic_sample_finish),
                    contentDescription = null,
                )
            },
            progressSize = CircularProgressDefaults.Regular,
            colors =
                CircularProgressDefaults.circleProgressColors(
                    backgroundColor = PicoTheme.colorScheme.labelPrimaryLight,
                    indicatorColor = PicoTheme.colorScheme.labelPrimaryLight,
                ),
        )
        Spacer(modifier = Modifier.height(12.dp))
        // Finish
        SymbolicCircularProgressIndicator(
            progress = { 1f },
            progressSymbol = {
                Icon(
                    modifier = Modifier.size(24.dp),
                    painter = painterResource(id = R.drawable.ic_sample_finish),
                    contentDescription = null,
                )
            },
            progressSize = CircularProgressDefaults.Max,
            colors =
                CircularProgressDefaults.circleProgressColors(
                    backgroundColor = PicoTheme.colorScheme.labelPrimaryLight,
                    indicatorColor = PicoTheme.colorScheme.labelPrimaryLight,
                ),
        )
        Spacer(modifier = Modifier.height(12.dp))
    }
} 
   //sampleEnd
}
```