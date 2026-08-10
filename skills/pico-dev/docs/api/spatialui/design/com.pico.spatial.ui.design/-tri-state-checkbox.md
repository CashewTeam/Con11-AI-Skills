# TriStateCheckbox | PICO Spatial SDK

ui:design / com.pico.spatial.ui.design / TriStateCheckbox 
# TriStateCheckbox
```kotlin
@Composable
```fun  TriStateCheckbox ( state :  ToggleableState ,  modifier :  Modifier  =  Modifier ,  onClick :  ( )  ->  Unit ?  =  null ,  enabled :  Boolean  =  true ,  contentSize :  CheckboxContentSize  =  CheckBoxDefaults.Regular ,  colors :  CheckboxColor  =  CheckBoxDefaults.checkboxColors() ,  interactionSource :  MutableInteractionSource  =  remember { MutableInteractionSource() } ) 
Checkboxes can have a parent-child relationship with other checkboxes. When the parent checkbox is checked, all child checkboxes are checked. If a parent checkbox is unchecked, all child checkboxes are unchecked. If some, but not all, child checkboxes are checked, the parent checkbox becomes an indeterminate checkbox. 
#### Parameters
state 
whether TriStateCheckbox is checked, unchecked or in indeterminate state 
modifier 
Modifier to be applied to the layout of the checkbox 
on Click 
callback to be invoked when checkbox is being clicked, therefore the change of ToggleableState state is requested. If null, then this is passive and relies entirely on a higher-level component to control the state. 
enabled 
whether the component is enabled or grayed out 
content Size 
The content size of the CheckBox. 
colors 
CheckboxColor  that will be used to determine the color of the checkmark / box / border in different states. 
interaction Source 
the  MutableInteractionSource  representing the stream of  Interaction s for this TriStateCheckbox. You can create and pass in your own remembered  MutableInteractionSource  if you want to observe  Interaction s and customize the appearance / behavior of this TriStateCheckbox in different  Interaction s. 
#### See also
Checkbox 
if you want a simple component that represents Boolean state 
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
   Column(
    modifier = Modifier.fillMaxWidth().background(Color(color = 0xFF2F2F2F)).padding(12.dp)
) {
    listOf(ToggleableState.On, ToggleableState.Off, ToggleableState.Indeterminate).forEach {
        CheckBoxColumn(it)
        Spacer(modifier = Modifier.size(40.dp))
    }
} 
   //sampleEnd
}
```