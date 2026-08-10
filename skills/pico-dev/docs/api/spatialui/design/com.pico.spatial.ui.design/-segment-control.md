# SegmentControl | PICO Spatial SDK

ui:design / com.pico.spatial.ui.design / SegmentControl 
# SegmentControl
```kotlin
@Composable
```fun  SegmentControl ( modifier :  Modifier  =  Modifier ,  backgroundColor :  Color  =  SegmentControlDefaults.backgroundColor ,  itemSpace :  Dp  =  SegmentControlDefaults.ItemSpace ,  contentPadding :  Dp  =  SegmentControlDefaults.ContainerPadding ,  cornerRadius :  Dp  =  SegmentControlDefaults.Small.containerCornerRadius() ,  content :  @ Composable RowScope . ( )  ->  Unit ) 
Segment control with Texts or Icons 
A composable function that creates a rich segment control. The rich segment control combines both icons and text items, allowing users to switch the selected state by clicking on the items. 
#### Parameters
modifier 
The modifier to be applied to the segment control, defaulting to  Modifier . 
background Color 
The background color of the segment control, defaulting to  SegmentControlDefaults.backgroundColor . 
item Space 
The spacing between items in the segment control, defaulting to 4.dp. 
content Padding 
The inner padding of the segment control, defaulting to 4.dp. 
corner Radius 
The RoundedCornerShape cornerRadius of the segment control, defaulting to 0.dp. 
content 
A composable function that provides the content of the segment control. It is expected to contain multiple  SegmentItem  instances. 
#### Samples
```
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
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
import androidx.compose.ui.text.style.TextAlign
import androidx.compose.ui.tooling.preview.Preview
import androidx.compose.ui.unit.dp
import com.pico.spatial.ui.design.SegmentControl
import com.pico.spatial.ui.design.SegmentControlDefaults
import com.pico.spatial.ui.design.SegmentItem
import com.pico.spatial.ui.design.Text
import com.pico.spatial.ui.design.containerCornerRadius
import com.pico.spatial.ui.design.itemContentPadding
import com.pico.spatial.ui.design.textStyle

fun main() { 
   //sampleStart 
   var selectIndex by remember { mutableStateOf(0) }
SegmentControl(cornerRadius = SegmentControlDefaults.Rich.containerCornerRadius()) {
    repeat(5) { index ->
        SegmentItem(
            icon = { AnyIcon(iconSize = 24.dp) },
            title = {
                Text(
                    "Label",
                    modifier = Modifier.width(91.dp).height(18.dp),
                    textAlign = TextAlign.Center,
                )
            },
            selected = selectIndex == index,
            onClick = { selectIndex = index },
            textStyle = SegmentControlDefaults.Rich.textStyle(),
        )
    }
} 
   //sampleEnd
}
```