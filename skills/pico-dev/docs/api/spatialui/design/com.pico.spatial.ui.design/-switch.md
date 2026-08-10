# Switch | PICO Spatial SDK

ui:design / com.pico.spatial.ui.design / Switch 
# Switch
```kotlin
@Composable
```fun  Switch ( checked :  Boolean ,  onCheckedChange :  ( Boolean )  ->  Unit ? ,  modifier :  Modifier  =  Modifier ,  enabled :  Boolean  =  true ,  colors :  SwitchColors  =  SwitchDefaults.switchColors() ,  interactionSource :  MutableInteractionSource  =  remember { MutableInteractionSource() } ) 
Switches toggle the state of a single item on or off. 
#### Parameters
checked 
whether or not this switch is checked. 
on Checked Change 
called when this switch is clicked. If  null , then this switch is not interactable, unless something else handles its input events and updates its state. 
modifier 
the  Modifier  to be applied to this switch. 
enabled 
controls the enabled state of this switch. When  false , this component does not respond to user input, and it appears visually disabled to accessibility services. 
colors 
SwitchColors  that will be used to resolve the colors used for this switch in different states. See  SwitchDefaults.switchColors . 
interaction Source 
the  MutableInteractionSource  representing the stream of  Interaction s for this switch. You can create and pass in your own  remember ed instance to observe  Interaction s and customize the appearance / behavior of this switch in different states. 
#### Samples
```
import androidx.compose.foundation.background
import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.size
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.semantics.contentDescription
import androidx.compose.ui.semantics.semantics
import androidx.compose.ui.tooling.preview.Preview
import androidx.compose.ui.unit.dp
import com.pico.spatial.ui.design.Switch
import com.pico.spatial.ui.design.Text

fun main() { 
   //sampleStart 
   var checked by remember { mutableStateOf(true) }
Switch(
    modifier = Modifier.semantics { contentDescription = "Demo" },
    checked = checked,
    onCheckedChange = { checked = it },
) 
   //sampleEnd
}
```