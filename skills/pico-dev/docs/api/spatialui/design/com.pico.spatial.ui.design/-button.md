# Button | PICO Spatial SDK

ui:design / com.pico.spatial.ui.design / Button 
# Button
```kotlin
@Composable
```fun  Button ( onClick :  ( )  ->  Unit ,  modifier :  Modifier  =  Modifier ,  enabled :  Boolean  =  true ,  size :  ButtonSize  =  ButtonDefaults.Regular ,  colors :  ButtonColors  =  ButtonDefaults.buttonColors() ,  leadingIcon :  @ Composable ( )  ->  Unit ?  =  null ,  trailingIcon :  @ Composable ( )  ->  Unit ?  =  null ,  contentPadding :  PaddingValues  =  ButtonDefaults.paddingForButtonSize(
            size,
            haveIcon = leadingIcon != null || trailingIcon != null,
        ) ,  shape :  Shape  =  ButtonDefaults.shapeForButtonSize(size) ,  gap :  Dp  =  ButtonDefaults.gapForButtonSize(
            size,
            haveIcon = leadingIcon != null || trailingIcon != null,
        ) ,  interactionSource :  MutableInteractionSource  =  remember { MutableInteractionSource() } ,  content :  @ Composable RowScope . ( )  ->  Unit ) 
A stylized button component defined by PICO design which can be easily used by passing pre-defined  ButtonSize  and  ButtonColors . Each pre-defined  ButtonSize  has related  PaddingValues , Shape , gap  and  TextStyle . 
#### Parameters
on Click 
is called when user clicks on the element 
modifier 
The modifier to be applied to the layout 
enabled 
Controls the enabled state. When  false ,  onClick , and this modifier appears disabled for accessibility services 
size 
a  ButtonSize , see  ButtonDefaults.buttonSize 
colors 
The  ButtonColors  used by button to resolve background color and content color in different states, see  ButtonDefaults.buttonColors 
leading Icon 
a leading icon before the content, typically an  Icon , default tint is  ButtonColors.contentColor 
trailing Icon 
a trailing icon after the content, typically an  Icon , default tint is  ButtonColors.contentColor 
content Padding 
The  PaddingValues  to be applied between the container and the content 
shape 
the content will be clipped to this  Shape . 
gap 
The gap between icons and content, only take effects with  leadingIcon  and  trailingIcon  set 
interaction Source 
MutableInteractionSource  that will be used to dispatch  PressInteraction.Press  when this clickable is pressed. Only the initial (first) press will be recorded and dispatched with  MutableInteractionSource . 
content 
The content of the button, typically a  Text . Text color is defined by  ButtonColors.contentColor 
#### Samples
```
import androidx.compose.foundation.border
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.layout.width
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.tooling.preview.Preview
import androidx.compose.ui.unit.dp
import com.pico.spatial.ui.design.Button
import com.pico.spatial.ui.design.ButtonColors
import com.pico.spatial.ui.design.ButtonDefaults
import com.pico.spatial.ui.design.ButtonSize
import com.pico.spatial.ui.design.PicoTheme
import com.pico.spatial.ui.design.Text

fun main() { 
   //sampleStart 
   Button(
    onClick = {
        // do something
    }
) {
    Text("A regular button")
} 
   //sampleEnd
}
```
```
import androidx.compose.foundation.border
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.layout.width
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.tooling.preview.Preview
import androidx.compose.ui.unit.dp
import com.pico.spatial.ui.design.Button
import com.pico.spatial.ui.design.ButtonColors
import com.pico.spatial.ui.design.ButtonDefaults
import com.pico.spatial.ui.design.ButtonSize
import com.pico.spatial.ui.design.PicoTheme
import com.pico.spatial.ui.design.Text

fun main() { 
   //sampleStart 
   Button(
    onClick = {
        // do something
    },
    size = ButtonDefaults.Small,
    leadingIcon = { AnyIcon() },
) {
    Text("Favorite")
} 
   //sampleEnd
}
```
```
import androidx.compose.foundation.border
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.layout.width
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.tooling.preview.Preview
import androidx.compose.ui.unit.dp
import com.pico.spatial.ui.design.Button
import com.pico.spatial.ui.design.ButtonColors
import com.pico.spatial.ui.design.ButtonDefaults
import com.pico.spatial.ui.design.ButtonSize
import com.pico.spatial.ui.design.PicoTheme
import com.pico.spatial.ui.design.Text

fun main() { 
   //sampleStart 
   Column(Modifier.width(300.dp).border(1.dp, Color.Red)) {
    Button(
        modifier = Modifier.fillMaxWidth(),
        onClick = {},
        size = ButtonDefaults.Max,
        leadingIcon = { AnyIcon(iconSize = 22.dp) },
    ) {
        Text("FillMaxWidth(Max)")
    }
} 
   //sampleEnd
}
```