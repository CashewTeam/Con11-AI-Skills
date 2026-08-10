# TitleBar | PICO Spatial SDK

ui:design / com.pico.spatial.ui.design / TitleBar 
# TitleBar
```kotlin
@Composable
```fun  TitleBar ( title :  @ Composable BoxScope . ( )  ->  Unit ,  modifier :  Modifier  =  Modifier ,  leadingActions :  @ Composable RowScope . ( )  ->  Unit ?  =  null ,  trailingActions :  @ Composable RowScope . ( )  ->  Unit ?  =  null ,  contentPadding :  PaddingValues  =  TitleBarDefaults.HorizontalPadding ,  leadingGap :  Dp  =  TitleBarDefaults.ActionsGap ,  trailingGap :  Dp  =  TitleBarDefaults.ActionsGap ,  titleAlignment :  TitleAlignment  =  TitleAlignment.Center ,  colors :  TitleBarColors  =  TitleBarDefaults.titleBarColors() ) 
app title bar 
#### Parameters
title 
Usually is a  Text . Custom title content is allowed. 
modifier 
Compose modifier. 
leading Actions 
The actions placed at the start of the bar. Usually place multiple  IconButton s with size  ButtonDefaults.Small . 
trailing Actions 
The actions placed at the end of the bar. Usually place multiple  IconButton s with size  ButtonDefaults.Small . 
content Padding 
The space to each edge of the content. 
leading Gap 
The space between  leadingActions . 
trailing Gap 
The space between  trailingActions . 
title Alignment 
The position of  title , default is  TitleAlignment.Center . 
colors 
The colors of the bar, see  TitleBarDefaults.titleBarColors . 
#### Samples
```
import androidx.compose.foundation.border
import androidx.compose.foundation.horizontalScroll
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.width
import androidx.compose.foundation.rememberScrollState
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.drawWithContent
import androidx.compose.ui.geometry.Offset
import androidx.compose.ui.geometry.Size
import androidx.compose.ui.graphics.BlendMode
import androidx.compose.ui.graphics.Brush
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.graphics.CompositingStrategy
import androidx.compose.ui.graphics.graphicsLayer
import androidx.compose.ui.text.style.TextOverflow
import androidx.compose.ui.tooling.preview.Preview
import androidx.compose.ui.unit.dp
import com.pico.spatial.ui.design.Button
import com.pico.spatial.ui.design.ButtonDefaults
import com.pico.spatial.ui.design.IconButton
import com.pico.spatial.ui.design.IconButtonDefaults
import com.pico.spatial.ui.design.PicoTheme
import com.pico.spatial.ui.design.SearchField
import com.pico.spatial.ui.design.Text
import com.pico.spatial.ui.design.TitleAlignment
import com.pico.spatial.ui.design.TitleBar
import com.pico.spatial.ui.design.TitleBarDefaults

fun main() { 
   //sampleStart 
   TitleBar(
    modifier = Modifier.width(ScreenWidth),
    title = { Text("Title Bar") },
    colors =
        TitleBarDefaults.titleBarColors(
            titleColor = Color.Red,
            leadingColor = Color.Green,
            trailingColor = Color.Blue,
        ),
    leadingActions = {
        Text(text = "Left")
        Text(text = "Left")
        Text(text = "Left")
    },
    trailingActions = {
        Text(text = "Right")
        Text(text = "Right")
        Text(text = "Right")
    },
) 
   //sampleEnd
}
```