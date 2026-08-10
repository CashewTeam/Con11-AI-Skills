# ToggleIconButton | PICO Spatial SDK

ui:design / com.pico.spatial.ui.design / ToggleIconButton 
# ToggleIconButton
```kotlin
@Composable
```fun  ToggleIconButton ( checked :  Boolean ,  onCheckedChange :  ( Boolean )  ->  Unit ,  modifier :  Modifier  =  Modifier ,  colors :  ToggleButtonColors  =  ToggleIconButtonDefaults.toggleIconButtonColors() ,  size :  ButtonSize  =  ToggleIconButtonDefaults.Min ,  shape :  Shape  =  ToggleIconButtonDefaults.DefaultShape ,  enabled :  Boolean  =  true ,  interactionSource :  MutableInteractionSource  =  remember { MutableInteractionSource() } ,  content :  @ Composable ( )  ->  Unit ) 
Toggleable icon button defined by PICO design 
#### Parameters
checked 
whether the state is on or off 
on Checked Change 
callback to be invoked when toggleable is clicked, therefore the change of the state in requested 
modifier 
The modifier to be applied to the layout 
colors 
The  ToggleButtonColors  used by button to resolve background color and content color in different states 
size 
size used by  IconButton 
shape 
the content will be clipped to this  Shape . 
enabled 
whether this  toggleable  will handle input events and appear enabled for semantics purposes 
interaction Source 
MutableInteractionSource  that will be used to dispatch  PressInteraction.Press  when this clickable is pressed. Only the initial (first) press will be recorded and dispatched with  MutableInteractionSource . 
content 
the content of this icon button, typically an  Icon 
#### Samples
```
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.RowScope
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Modifier
import androidx.compose.ui.tooling.preview.Preview
import androidx.compose.ui.unit.dp
import com.pico.spatial.ui.design.ToggleIconButton

fun main() { 
   //sampleStart 
   var isChecked by remember { mutableStateOf(false) }
ToggleIconButton(checked = isChecked, onCheckedChange = { isChecked = !isChecked }) {
    AnyIcon()
} 
   //sampleEnd
}
```