# SegmentSlider | PICO Spatial SDK

ui:design / com.pico.spatial.ui.design / SegmentSlider 
# SegmentSlider
```kotlin
@Composable
```fun  SegmentSlider ( initialStep :  Int ,  segmentCount :  Int ,  onStepChange :  ( newStep :  Int )  ->  Unit ,  modifier :  Modifier  =  Modifier ,  enabled :  Boolean  =  true ,  interactionSource :  MutableInteractionSource  =  remember { MutableInteractionSource() } ,  sliderSpec :  SliderSpec  =  SliderDefaults.Regular ,  colors :  SliderColors  =  SliderDefaults.sliderColors() ) 
Sliders allow users to make selections range from 0 to  segmentCount 
A tap on a segment jumps directly to the target step and plays the configured click audio. During dragging, each crossed step plays the configured drag-scale audio instead of tap audio. 
#### Parameters
initial Step 
current value of the Slider. Should be >= 0 and <=  segmentCount . 
segment Count 
the count of segments, means total steps 
on Step Change 
lambda in which value should be updated. It is invoked when a tap jumps to a new step or when dragging crosses into another step. 
modifier 
modifiers for the Slider layout 
enabled 
whether or not component is enabled and can be interacted with or not 
interaction Source 
the  MutableInteractionSource  representing the stream of  Interaction s for this Slider. You can create and pass in your own remembered  MutableInteractionSource  if you want to observe  Interaction s and customize the appearance / behavior of this Slider in different  Interaction s. 
slider Spec 
defines the size of elements for slider. Use  Modifier.width  to specify the slider width. 
colors 
SliderColors  that will be used to determine the color of the Slider parts in different states. 
#### Samples
```
import androidx.compose.foundation.background
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.width
import androidx.compose.foundation.layout.wrapContentSize
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.res.painterResource
import androidx.compose.ui.tooling.preview.Preview
import androidx.compose.ui.unit.dp
import com.pico.spatial.ui.design.Icon
import com.pico.spatial.ui.design.SegmentSlider
import com.pico.spatial.ui.design.Slider
import com.pico.spatial.ui.design.SliderDefaults
import com.pico.spatial.ui.design.SymbolSlider
import com.pico.spatial.ui.design.Text

fun main() { 
   //sampleStart 
   Column {
    var step by remember { mutableStateOf(2) }
    SegmentSlider(initialStep = step, segmentCount = 5, onStepChange = { step = it })
    Text(text = "$step")
} 
   //sampleEnd
}
```
```
import androidx.compose.foundation.background
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.width
import androidx.compose.foundation.layout.wrapContentSize
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.res.painterResource
import androidx.compose.ui.tooling.preview.Preview
import androidx.compose.ui.unit.dp
import com.pico.spatial.ui.design.Icon
import com.pico.spatial.ui.design.SegmentSlider
import com.pico.spatial.ui.design.Slider
import com.pico.spatial.ui.design.SliderDefaults
import com.pico.spatial.ui.design.SymbolSlider
import com.pico.spatial.ui.design.Text

fun main() { 
   //sampleStart 
   Column {
    val initial = 0
    var step by remember { mutableStateOf(initial) }
    SegmentSlider(
        initialStep = initial,
        segmentCount = 6,
        onStepChange = { step = it },
        sliderSpec = SliderDefaults.Regular,
    )
    Text(text = "$step")
} 
   //sampleEnd
}
```