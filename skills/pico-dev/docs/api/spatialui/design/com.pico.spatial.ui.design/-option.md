# Option | PICO Spatial SDK

ui:design / com.pico.spatial.ui.design / Option 
# Option
```kotlin
@Composable
```fun  Option ( selected :  Boolean ,  onSelectChange :  ( selected :  Boolean )  ->  Unit ,  modifier :  Modifier  =  Modifier ,  icon :  @ Composable ( )  ->  Unit ?  =  null ,  colors :  OptionColors  =  OptionDefaults.optionColors() ,  enabled :  Boolean  =  true ,  gap :  Dp  =  OptionDefaults.Gap ,  shape :  Shape  =  OptionDefaults.Shape ,  contentPadding :  PaddingValues  =  OptionDefaults.ContentPadding ,  interactionSource :  MutableInteractionSource  =  remember { MutableInteractionSource() } ,  content :  @ Composable ( )  ->  Unit ) 
Option is a stylized button component defined by PICO design witch has a  selected  state. And usually has a  Text  and optional leading  icon . 
#### Parameters
selected 
Whether the state is on or off. 
on Select Change 
Callback to be invoked when checked state changed, usually by a click action. 
modifier 
The modifier to be applied to the layout. 
icon 
The optional leading icon. It is tint by  OptionColors  by default. 
colors 
Defines the colors used by  Option .See also  OptionDefaults.optionColors . 
enabled 
Whether the option is enabled. 
gap 
The gap between  icon  and  content 
shape 
The shape used by  Option . 
content Padding 
The padding used by  Option 
interaction Source 
MutableInteractionSource  that will be used to dispatch hover and press events. 
content 
The content of  Option . Usually a  Text 
#### Samples
```
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.res.painterResource
import com.pico.spatial.ui.design.Icon
import com.pico.spatial.ui.design.Option
import com.pico.spatial.ui.design.Text

fun main() { 
   //sampleStart 
   var checked by remember { mutableStateOf(false) }
Option(
    selected = checked,
    onSelectChange = { checked = !checked },
    icon = {
        Icon(
            painter = painterResource(R.drawable.ic_sample_circle_placeholder),
            contentDescription = null,
        )
    },
) {
    Text("label")
} 
   //sampleEnd
}
```