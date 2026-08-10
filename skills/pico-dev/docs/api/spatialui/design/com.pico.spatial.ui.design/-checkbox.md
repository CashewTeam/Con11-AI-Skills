# Checkbox | PICO Spatial SDK

ui:design / com.pico.spatial.ui.design / Checkbox 
# Checkbox
```kotlin
@Composable
```fun  Checkbox ( checked :  Boolean ,  onCheckedChange :  ( Boolean )  ->  Unit ? ,  modifier :  Modifier  =  Modifier ,  enabled :  Boolean  =  true ,  contentSize :  CheckboxContentSize  =  CheckBoxDefaults.Regular ,  colors :  CheckboxColor  =  CheckBoxDefaults.checkboxColors() ,  interactionSource :  MutableInteractionSource  =  remember { MutableInteractionSource() } ) 
Checkboxes allow users to select one or more items from a set. Checkboxes can turn an option on or off. 
#### Parameters
checked 
whether Checkbox is checked or unchecked 
on Checked Change 
callback to be invoked when checkbox is being clicked, therefore the change of checked state is requested. If null, then this is passive and relies entirely on a higher-level component to control the "checked" state. 
modifier 
Modifier to be applied to the layout of the checkbox 
enabled 
whether the component is enabled or grayed out 
content Size 
The content size of the CheckBox. 
colors 
CheckboxColor  that will be used to determine the color of the checkmark / box / border in different states. 
interaction Source 
the  MutableInteractionSource  representing the stream of  Interaction s for this Checkbox. You can create and pass in your own remembered  MutableInteractionSource  if you want to observe  Interaction s and customize the appearance / behavior of this Checkbox in different  Interaction s. 
#### See also
Tri State Checkbox 
if you require support for an indeterminate state, or more advanced color customization between states. 
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
import androidx.compose.ui.state.ToggleableState
import androidx.compose.ui.tooling.preview.Preview
import androidx.compose.ui.unit.dp
import com.pico.spatial.ui.design.Checkbox
import com.pico.spatial.ui.design.Text
import com.pico.spatial.ui.design.TriStateCheckbox

fun main() { 
   //sampleStart 
   var checked by remember { mutableStateOf(true) }
Checkbox(
    modifier = Modifier.semantics { contentDescription = "Demo" },
    checked = checked,
    onCheckedChange = { checked = !it },
) 
   //sampleEnd
}
```