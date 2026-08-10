# SimpleCoachmark | PICO Spatial SDK

ui:design / com.pico.spatial.ui.design.windows / SimpleCoachmark 
# SimpleCoachmark
```kotlin
@Composable
```fun  CoachmarkScope . SimpleCoachmark ( text :  @ Composable ( )  ->  Unit ,  modifier :  Modifier  =  Modifier ,  button :  @ Composable ( )  ->  Unit ?  =  null ,  backgroundColor :  Color  =  CoachmarkDefaults.DefaultBackgroundColor ,  cornerSize :  Dp  =  LocalTokensBearer.current.dimension.RadiusMedium ) 
SimpleCoachmark  usually used to display brevity message for anchor UI. It typically contains text and an optional button. 
#### Parameters
text 
The composable content representing the text of the coachmark. 
modifier 
The  Modifier  to be applied to the coachmark layout. 
button 
An optional composable representing the button in the coachmark. 
background Color 
The background color of the coachmark. Defaults to  CoachmarkDefaults.DefaultBackgroundColor . 
corner Size 
The corner radius of the coachmark. 
#### Samples
```
import androidx.compose.foundation.Image
import androidx.compose.foundation.layout.size
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.layout.ContentScale
import androidx.compose.ui.res.painterResource
import androidx.compose.ui.text.style.TextOverflow
import androidx.compose.ui.unit.dp
import com.pico.spatial.ui.design.Button
import com.pico.spatial.ui.design.Icon
import com.pico.spatial.ui.design.IconButton
import com.pico.spatial.ui.design.IconButtonDefaults
import com.pico.spatial.ui.design.PicoTheme
import com.pico.spatial.ui.design.Text
import com.pico.spatial.ui.design.windows.CoachmarkBox
import com.pico.spatial.ui.design.windows.CoachmarkDefaults
import com.pico.spatial.ui.design.windows.CoachmarkDirection
import com.pico.spatial.ui.design.windows.ImageCoachmark
import com.pico.spatial.ui.design.windows.RichCoachmark
import com.pico.spatial.ui.design.windows.SimpleCoachmark

fun main() { 
   //sampleStart 
   var show by remember { mutableStateOf(false) }
CoachmarkBox(
    coachmark = {
        SimpleCoachmark(
            text = {
                Text(text = "Short text", maxLines = 1, overflow = TextOverflow.Ellipsis)
            },
            button = {
                CoachmarkDefaults.CoachmarkButton(onClick = { show = false }) {
                    Text(text = "Close")
                }
            },
        )
    },
    showCoachmark = show,
) {
    Button(onClick = { show = !show }) { Text(text = "simple") }
} 
   //sampleEnd
}
```