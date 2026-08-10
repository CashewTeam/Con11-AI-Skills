# Slider | PICO Spatial SDK

ui:design / com.pico.spatial.ui.design / Slider 
# Slider
```kotlin
@Composable
```fun  Slider ( value :  Float ,  onValueChange :  ( newValue :  Float )  ->  Unit ,  modifier :  Modifier  =  Modifier ,  valueRange :  ClosedFloatingPointRange < Float >  =  0f..1f ,  onValueChangeFinished :  ( )  ->  Unit ?  =  null ,  enabled :  Boolean  =  true ,  interactionSource :  MutableInteractionSource  =  remember { MutableInteractionSource() } ,  sliderSpec :  SliderSpec  =  SliderDefaults.Regular ,  colors :  SliderColors  =  SliderDefaults.sliderColors() ) 
Continuous sliders allow users to make selections in valueRange 
Sliders reflect a range(0 to 1) of values along a bar, from which users may select a single value. They are ideal for adjusting settings such as volume, brightness, or applying image filters. 
#### Parameters
value 
current value of the Slider. Should be in valueRange, default from 0.0 to 1.0 . 
on Value Change 
lambda in which value should be updated 
modifier 
modifiers for the Slider layout 
value Range 
of values that this slider can take. The passed value will be coerced to this range. 
on Value Change Finished 
lambda to be invoked when value change has ended. This callback shouldn't be used to update the slider value (use  onValueChange  for that), but rather to know when the user has completed selecting a new value by ending a drag or a click. 
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
    var sliderValue by remember { mutableStateOf(0f) }
    Slider(
        value = sliderValue,
        onValueChange = { sliderValue = it },
        onValueChangeFinished = {
            // Because onValueChange will be call frequently when dragging
            // do something when drag or click finish, such as invoke network request.
        },
        sliderSpec = SliderDefaults.Regular,
    )
    Text(text = "$sliderValue")
} 
   //sampleEnd
}
```