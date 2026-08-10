# SegmentItem | PICO Spatial SDK

ui:design / com.pico.spatial.ui.design / SegmentItem 
# SegmentItem
```kotlin
@Composable
```fun  RowScope . SegmentItem ( selected :  Boolean ,  onClick :  ( )  ->  Unit ,  modifier :  Modifier  =  Modifier ,  interactionSource :  MutableInteractionSource  =  remember { MutableInteractionSource() } ,  textStyle :  TextStyle  =  SegmentControlDefaults.Small.textStyle() ,  colors :  SegmentControlColors  =  SegmentControlDefaults.colors() ,  title :  @ Composable ( )  ->  Unit ?  =  null ,  icon :  @ Composable ( )  ->  Unit ?  =  null ,  contentPadding :  PaddingValues  =  SegmentControlDefaults.Small.itemContentPadding() ,  gap :  Dp  =  SegmentControlDefaults.ItemGap ) 
A composable function that creates a basic segment item. The segment item can be used as a building block for creating the text and icon segment controls. 
#### Parameters
selected 
A boolean value indicating whether the segment item is selected. 
on Click 
The callback function to be invoked when the segment item is clicked. 
modifier 
The modifier to be applied to the segment item, defaulting to  Modifier . 
interaction Source 
The interaction source to be used for haptic feedback, defaulting to  remember  a new  MutableInteractionSource . 
text Style 
The text style to be applied to the segment item, defaulting to SegmentControlDefaults.Small.textStyle(). 
colors 
The colors to be applied to the segment item, defaulting to SegmentControlDefaults.colors(). 
title 
The title to be displayed in the segment item, typically a  Text . 
icon 
The icon to be displayed in the segment item, typically a  Icon . 
content Padding 
The inner padding of the segment item, defaulting to SegmentControlDefaults.Small.itemPadding(). 
gap 
The gap between the icon and the text, defaulting to 0.dp. 
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
val options = listOf("Home", "Mine", "Favorite", "Setting", "About")
SegmentControl {
    options.forEachIndexed { index, option ->
        SegmentItem(
            title = { Text(option, modifier = Modifier.height(16.dp)) },
            selected = selectIndex == index,
            onClick = { selectIndex = index },
        )
    }
} 
   //sampleEnd
}
```
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
SegmentControl {
    repeat(5) { index ->
        SegmentItem(
            icon = { AnyIcon(iconSize = 16.dp) },
            onClick = { selectIndex = index },
            selected = selectIndex == index,
        )
    }
} 
   //sampleEnd
}
```