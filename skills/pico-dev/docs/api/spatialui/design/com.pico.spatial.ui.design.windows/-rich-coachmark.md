# RichCoachmark | PICO Spatial SDK

ui:design / com.pico.spatial.ui.design.windows / RichCoachmark 
# RichCoachmark
```kotlin
@Composable
```fun  CoachmarkScope . RichCoachmark ( modifier :  Modifier  =  Modifier ,  image :  @ Composable ( )  ->  Unit ?  =  null ,  title :  @ Composable ( )  ->  Unit ?  =  null ,  buttons :  @ Composable RowScope . ( )  ->  Unit ?  =  null ,  backgroundColor :  Color  =  CoachmarkDefaults.DefaultBackgroundColor ,  cornerSize :  Dp  =  if (image != null) LocalTokensBearer.current.dimension.RadiusLarge
        else LocalTokensBearer.current.dimension.RadiusMedium ,  content :  @ Composable ( )  ->  Unit ) 
ImageCoachmark  usually used to display rich message for anchor UI. It typically contains an optional image, title, content and buttons. 
#### Parameters
modifier 
The  Modifier  to be applied to the coachmark layout. 
image 
The image of the coachmark. 
title 
The title of the coachmark. 
buttons 
The buttons of the coachmark. 
background Color 
The background color of the coachmark. Defaults to  CoachmarkDefaults.DefaultBackgroundColor . 
corner Size 
The corner radius of the coachmark. 
content 
The content of the coachmark. 
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