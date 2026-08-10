# ImageCoachmark | PICO Spatial SDK

ui:design / com.pico.spatial.ui.design.windows / ImageCoachmark 
# ImageCoachmark
```kotlin
@Composable
```fun  CoachmarkScope . ImageCoachmark ( image :  @ Composable ( )  ->  Unit ,  modifier :  Modifier  =  Modifier ,  button :  @ Composable ( )  ->  Unit ?  =  null ,  backgroundColor :  Color  =  CoachmarkDefaults.DefaultBackgroundColor ,  cornerSize :  Dp  =  LocalTokensBearer.current.dimension.RadiusLarge ,  padding :  Dp  =  ImagePadding ) 
ImageCoachmark  usually used to display image for anchor UI. It typically contains an image and an optional button. 
#### Parameters
image 
The image of the coachmark. 
modifier 
The  Modifier  to be applied to the coachmark layout. 
button 
An optional composable representing the button in the coachmark. 
background Color 
The background color of the coachmark. Defaults to  CoachmarkDefaults.DefaultBackgroundColor . 
corner Size 
The corner radius of the coachmark. 
padding 
The padding of the image. Defaults to  CoachmarkDefaults.ImagePadding . 
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