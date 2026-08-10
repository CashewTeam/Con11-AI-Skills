# CoachmarkBox | PICO Spatial SDK

ui:design / com.pico.spatial.ui.design.windows / CoachmarkBox 
# CoachmarkBox
```kotlin
@Composable
```fun  CoachmarkBox ( coachmark :  @ Composable CoachmarkScope . ( )  ->  Unit ,  modifier :  Modifier  =  Modifier ,  showCoachmark :  Boolean  =  true ,  direction :  CoachmarkDirection  =  CoachmarkDirection.ToEnd ,  gap :  Dp  =  CoachmarkDefaults.DefaultGap ,  content :  @ Composable BoxScope . ( )  ->  Unit ) 
CoachmarkBox  is a container for displaying a coachmark. 
#### Parameters
coachmark 
The composable content representing the coachmark. Usually is a  SimpleCoachmark  or  RichCoachmark  or  ImageCoachmark . 
modifier 
The  Modifier  to be applied to the coachmark box layout. 
show Coachmark 
Whether to show the coachmark. Defaults to true. 
direction 
The direction of the coachmark relative to anchor view that placed in  content . Defaults to  CoachmarkDirection.ToEnd . 
gap 
The gap between the coachmark and the anchor. Defaults to  CoachmarkDefaults.DefaultGap . 
content 
The composable content representing the anchor UI. 
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
        RichCoachmark(
            image = {
                Image(
                    painter = painterResource(id = R.drawable.img_sample_coachmark_image),
                    contentDescription = null,
                    contentScale = ContentScale.Crop,
                )
            },
            title = { Text(text = "Title(Optional)") },
            content = { Text(text = "Content") },
            buttons = {
                CoachmarkDefaults.CoachmarkButton(onClick = { show = false }) {
                    Text(text = "Cancel")
                }
                CoachmarkDefaults.CoachmarkButton(onClick = { show = false }) {
                    Text(text = "OK")
                }
            },
        )
    },
    showCoachmark = show,
) {
    Button(onClick = { show = !show }) { Text(text = "normal") }
} 
   //sampleEnd
}
```
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
        ImageCoachmark(
            image = {
                Image(
                    painter = painterResource(id = R.drawable.img_sample_coachmark_image),
                    contentDescription = null,
                    modifier = Modifier.size(width = 304.dp, height = 172.dp),
                )
            },
            button = {
                IconButton(
                    onClick = { show = false },
                    size = IconButtonDefaults.Min,
                    colors =
                        IconButtonDefaults.iconButtonColors(
                            containerColor = Color(color = 0x66FFFFFF),
                            contentColor = PicoTheme.colorScheme.labelPrimaryLight,
                        ),
                ) {
                    Icon(
                        painter =
                            painterResource(
                                com.pico.spatial.ui.design.R.drawable.ic_sui_chip_remove
                            ),
                        contentDescription = "Close",
                        modifier = Modifier.size(16.dp),
                    )
                }
            },
        )
    },
    showCoachmark = show,
) {
    Button(onClick = { show = !show }) { Text(text = "Rich") }
} 
   //sampleEnd
}
```
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
    showCoachmark = show,
    direction = CoachmarkDirection.Above,
    coachmark = { SimpleCoachmark(text = { Text("Hello world") }) },
) {
    Button(onClick = { show = !show }) { Text(text = "Direction") }
} 
   //sampleEnd
}
```