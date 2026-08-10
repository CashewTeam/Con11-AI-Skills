# RemovableChip | PICO Spatial SDK

ui:design / com.pico.spatial.ui.design / RemovableChip 
# RemovableChip
```kotlin
@Composable
```fun  RemovableChip ( label :  @ Composable ( )  ->  Unit ,  onLeadingClick :  ( )  ->  Unit ,  onTrailingRemoveClick :  ( )  ->  Unit ,  visible :  Boolean ,  modifier :  Modifier  =  Modifier ,  leadingIcon :  @ Composable ( )  ->  Unit ?  =  null ,  enabled :  Boolean  =  true ,  colors :  ChipColors  =  ChipsDefaults.chipColors() ,  chipSize :  ChipSize  =  ChipsDefaults.Small ,  contentPadding :  PaddingValues  =  chipSize.removeChipPadding(leadingIcon != null) ,  contentGap :  Dp  =  chipSize.contentGap() ,  shape :  Shape  =  RoundedCornerShape(chipSize.cornerRadius()) ,  interactionSource :  MutableInteractionSource  =  remember { MutableInteractionSource() } ) 
A chip which is removable 
#### Parameters
label 
the content of the ButtonChip, typically a  Text . Text color is defined by  ChipColors.contentColor . 
on Leading Click 
called when the leading is clicked. 
on Trailing Remove Click 
called when the trailing remove icon is clicked. 
visible 
defines whether the chip should be visible. 
modifier 
Modifier to be applied to the chip. 
leading Icon 
Optional icon at the start of the chip, preceding the content text. 
enabled 
When disabled, chip will not respond to user input. It will also appear visually disabled to accessibility services. 
colors 
the colors for content including  label , leadingIcon  and background of chip. 
chip Size 
the size of chip. 
content Padding 
padding for content of this chip. 
content Gap 
the gap between  leadingIcon  and  label . 
shape 
the shape of this chip. 
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
   Row(verticalAlignment = Alignment.CenterVertically, modifier = Modifier.height(70.dp)) {
    var visible by remember { mutableStateOf(true) }
    var clickValue by remember { mutableIntStateOf(0) }
    Column {
        Text(
            text = "Trailing Click  to ${if (visible) "hide" else "show"} Chip",
            modifier =
                Modifier.background(Color.Yellow)
                    .clickable { visible = !visible }
                    .padding(horizontal = 8.dp)
                    .width(135.dp),
        )
        Text(text = "Leading Click Action: $clickValue")
    }
    // chip
    RemovableChip(
        label = { Text(text = "Chip") },
        onLeadingClick = { clickValue += 1 },
        onTrailingRemoveClick = { visible = false },
        visible = visible,
        leadingIcon = { AnyIcon(iconSize = 12.dp) },
    )
} 
   //sampleEnd
}
```