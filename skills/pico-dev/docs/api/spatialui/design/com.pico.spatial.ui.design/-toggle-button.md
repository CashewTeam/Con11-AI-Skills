# ToggleButton | PICO Spatial SDK

ui:design / com.pico.spatial.ui.design / ToggleButton 
# ToggleButton
```kotlin
@Composable
```fun  ToggleButton ( checked :  Boolean ,  onCheckedChange :  ( Boolean )  ->  Unit ,  modifier :  Modifier  =  Modifier ,  colors :  ToggleButtonColors  =  ToggleButtonDefaults.toggleButtonColors() ,  size :  ButtonSize  =  ToggleButtonDefaults.Min ,  enabled :  Boolean  =  true ,  interactionSource :  MutableInteractionSource  =  remember { MutableInteractionSource() } ,  leadingIcon :  @ Composable ( )  ->  Unit ?  =  null ,  trailingIcon :  @ Composable ( )  ->  Unit ?  =  null ,  contentPadding :  PaddingValues  =  ButtonDefaults.paddingForButtonSize(
            size,
            haveIcon = leadingIcon != null || trailingIcon != null,
        ) ,  shape :  Shape  =  ButtonDefaults.shapeForButtonSize(size) ,  gap :  Dp  =  ButtonDefaults.gapForButtonSize(
            size,
            haveIcon = leadingIcon != null || trailingIcon != null,
        ) ,  content :  @ Composable RowScope . ( )  ->  Unit ) 
A stylized toggleable button component defined by PICO design which could be used easily by pass pre-defined  ButtonSize  and  ToggleButtonColors . Each pre-defined  ButtonSize  has related  PaddingValues , Shape , gap  and  TextStyle . 
#### Parameters
checked 
whether the state is on or off 
on Checked Change 
callback to be invoked when toggleable is clicked, therefore the change of the state in requested 
modifier 
The modifier to be applied to the layout 
colors 
The  ToggleButtonColors  used by button to resolve background color and content color in different states, see  ToggleButtonDefaults.toggleButtonColors 
size 
a  ButtonSize , see  ToggleButtonDefaults.toggleButtonSize 
enabled 
Controls the enabled state. When  false ,  onCheckedChange , and this modifier 
interaction Source 
MutableInteractionSource  that will be used to dispatch  PressInteraction.Press  when this clickable is pressed. Only the initial (first) press will be will appear disabled for accessibility services 
leading Icon 
a leading icon before the content, typically an  Icon , default tint is  ToggleButtonColors.contentColor 
trailing Icon 
a trailing icon after the content, typically an  Icon , default tint is  ToggleButtonColors.contentColor 
content Padding 
The  PaddingValues  will be applied between the container and the content 
shape 
the content will be clipped to this  Shape . 
gap 
The gap between icons and content, only take effects with  leadingIcon  and  trailingIcon  set recorded and dispatched with  MutableInteractionSource . 
content 
The content of the button, typically a  Text , Text color is  ToggleButtonColors.contentColor 
#### Samples
```
import androidx.compose.foundation.border
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.RowScope
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.width
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.tooling.preview.Preview
import androidx.compose.ui.unit.dp
import com.pico.spatial.ui.design.Text
import com.pico.spatial.ui.design.ToggleButton
import com.pico.spatial.ui.design.ToggleButtonDefaults

fun main() { 
   //sampleStart 
   var isChecked by remember { mutableStateOf(false) }
ToggleButton(
    isChecked,
    onCheckedChange = { isChecked = it },
    size = ToggleButtonDefaults.Small,
    leadingIcon = { AnyIcon() },
) {
    Text("Favorite")
} 
   //sampleEnd
}
```