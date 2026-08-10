# SymbolicCircularProgressIndicator | PICO Spatial SDK

ui:design / com.pico.spatial.ui.design / SymbolicCircularProgressIndicator 
# SymbolicCircularProgressIndicator
```kotlin
@Composable
```fun  SymbolicCircularProgressIndicator ( progress :  ( )  ->  Float ,  progressSymbol :  @ Composable ( )  ->  Unit ? ,  modifier :  Modifier  =  Modifier ,  colors :  ProgressColors  =  CircularProgressDefaults.circleProgressColors() ,  progressSize :  CircularProgressSize  =  CircularProgressDefaults.Small ,  strokeWidth :  Dp  =  progressSize.strokeWidth() ,  edgeStyle :  ProgressIndicatorEdgeStyle  =  ProgressIndicatorEdgeStyle.RoundCorner ) 
Progress indicators display the length of a process. When  progress  is 1.0f, a complete animation will be display. A  progressSymbol  is optional for you to display the progress details 
#### Parameters
progress 
The progress of this progress indicator, where 0.0 represents no progress and 1.0 represents full progress. Values outside of this range are coerced into the range. 
progress Symbol 
optional symbol content, such as a downloading icon or pause icon 
modifier 
the  Modifier  to be applied to this progress indicator 
colors 
The color for the progress indicator. 
progress Size 
the size param of this component 
stroke Width 
progress stroke width 
edge Style 
the style use for the ends of this progress indicator. 
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
   SymbolicCircularProgressIndicator(
    progress = { 0.3f },
    progressSize = CircularProgressDefaults.Regular,
    progressSymbol = {
        Icon(
            painter = painterResource(id = R.drawable.ic_sample_download),
            contentDescription = null,
        )
    },
) 
   //sampleEnd
}
```