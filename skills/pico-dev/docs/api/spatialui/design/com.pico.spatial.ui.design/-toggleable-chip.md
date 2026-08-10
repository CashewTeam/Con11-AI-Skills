# ToggleableChip | PICO Spatial SDK

ui:design / com.pico.spatial.ui.design / ToggleableChip 
# ToggleableChip
```kotlin
@Composable
```fun  ToggleableChip ( label :  @ Composable ( )  ->  Unit ,  isToggleOn :  Boolean ,  onClick :  ( )  ->  Unit ,  modifier :  Modifier  =  Modifier ,  leadingIcon :  @ Composable ( )  ->  Unit ?  =  null ,  trailingIcon :  @ Composable ( )  ->  Unit ?  =  null ,  enabled :  Boolean  =  true ,  chipSize :  ChipSize  =  ChipsDefaults.Small ,  colors :  ToggleableChipColors  =  ChipsDefaults.toggleableChipColors() ,  interactionSource :  MutableInteractionSource  =  remember { MutableInteractionSource() } ) 
Chip that is toggleable 
#### Parameters
label 
the content of the ButtonChip, typically a  Text . Text color is defined by  ChipColors.contentColor . 
is Toggle On 
whether Toggleable is on or off. 
on Click 
called when the chip is clicked. 
modifier 
Modifier to be applied to the chip 
leading Icon 
Optional icon at the start of the chip, preceding the content text. 
trailing Icon 
Optional icon at the end of the chip, following the content text. 
enabled 
When disabled, chip will not respond to user input. It will also appear visually disabled to accessibility services. 
chip Size 
the size of chip. 
colors 
color for content including  label , leadingIcon 
interaction Source 
the  MutableInteractionSource  representing the stream of Interactions for this chip. You can create and pass in your own remembered  MutableInteractionSource  if you want to observe Interactions and customize the appearance / behavior of this chip in different Interactions. 
#### Samples
```
import androidx.compose.foundation.background
import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.width
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableIntStateOf
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.tooling.preview.Preview
import androidx.compose.ui.unit.dp
import com.pico.spatial.ui.design.ButtonChip
import com.pico.spatial.ui.design.ChipsDefaults
import com.pico.spatial.ui.design.RemovableChip
import com.pico.spatial.ui.design.Text
import com.pico.spatial.ui.design.ToggleableChip

fun main() { 
   //sampleStart 
   Column(modifier = Modifier.padding(start = 12.dp)) {
    var selected by remember { mutableStateOf(false) }
    // chip sample
    ToggleableChip(
        label = { Text(text = "Chip") },
        isToggleOn = selected,
        onClick = { selected = !selected },
        leadingIcon = { AnyIcon(iconSize = 12.dp) },
        trailingIcon = { AnyIcon(iconSize = 12.dp) },
        colors = ChipsDefaults.toggleableChipColors(),
        chipSize = ChipsDefaults.Small,
    )
    Spacer(Modifier.height(10.dp))
    Text(
        text = "ToggleableState: $selected",
        modifier = Modifier.clickable { selected = !selected }.padding(top = 8.dp),
    )
} 
   //sampleEnd
}
```