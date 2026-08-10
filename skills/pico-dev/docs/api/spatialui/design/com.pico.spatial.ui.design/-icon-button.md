# IconButton | PICO Spatial SDK

ui:design / com.pico.spatial.ui.design / IconButton 
# IconButton
```kotlin
@Composable
```fun  IconButton ( onClick :  ( )  ->  Unit ,  modifier :  Modifier  =  Modifier ,  colors :  ButtonColors  =  IconButtonDefaults.iconButtonColors() ,  size :  ButtonSize  =  IconButtonDefaults.Regular ,  shape :  Shape  =  IconButtonDefaults.DefaultShape ,  enabled :  Boolean  =  true ,  interactionSource :  MutableInteractionSource  =  remember { MutableInteractionSource() } ,  content :  @ Composable ( )  ->  Unit ) 
Icon button defined by PICO design 
#### Parameters
on Click 
is called when user clicks on the element 
modifier 
The modifier to be applied to the layout 
colors 
The  ButtonColors  used by button to resolve background color and content color in different states, see  IconButtonDefaults.iconButtonColors 
size 
size used by  IconButton 
shape 
the content will be clipped to this  Shape . Default is CircleShape 
enabled 
Controls the enabled state. When  false ,  onClick , and this modifier appears disabled for accessibility services 
interaction Source 
MutableInteractionSource  that will be used to dispatch  PressInteraction.Press  when this clickable is pressed. Only the initial (first) press will be recorded and dispatched with  MutableInteractionSource . 
content 
the content of this icon button, typically an  Icon 
#### Samples
```
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.tooling.preview.Preview
import androidx.compose.ui.unit.Dp
import androidx.compose.ui.unit.dp
import com.pico.spatial.ui.design.ButtonColors
import com.pico.spatial.ui.design.ButtonSize
import com.pico.spatial.ui.design.IconButton
import com.pico.spatial.ui.design.IconButtonDefaults
import com.pico.spatial.ui.design.PicoTheme

fun main() { 
   //sampleStart 
   IconButton(onClick = {}) { AnyIcon(iconSize = 20.dp) } 
   //sampleEnd
}
```
```
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.tooling.preview.Preview
import androidx.compose.ui.unit.Dp
import androidx.compose.ui.unit.dp
import com.pico.spatial.ui.design.ButtonColors
import com.pico.spatial.ui.design.ButtonSize
import com.pico.spatial.ui.design.IconButton
import com.pico.spatial.ui.design.IconButtonDefaults
import com.pico.spatial.ui.design.PicoTheme

fun main() { 
   //sampleStart 
   IconButton(
    onClick = {},
    colors =
        IconButtonDefaults.iconButtonColors(
            containerColor = Color(color = 0xFFFF4D4D),
            contentColor = Color.White,
        ),
) {
    AnyIcon(iconSize = 20.dp)
} 
   //sampleEnd
}
```