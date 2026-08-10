# Timepicker | PICO Spatial SDK

ui:design / com.pico.spatial.ui.design / Timepicker 
# Timepicker
```kotlin
@Composable
```fun  Timepicker ( modifier :  Modifier  =  Modifier ,  config :  TimepickerConfig  =  TimepickerConfig.create(
            hour = TimepickerElement.hours(),
            minute = TimepickerElement.minutes(),
            second = TimepickerElement.seconds(),
        ) ,  onHoursChanged :  ( Int )  ->  Unit  =  {} ,  onMinutesChanged :  ( Int )  ->  Unit  =  {} ,  onSecondsChanged :  ( Int )  ->  Unit  =  {} ,  gap :  Dp  =  TimepickerDefaults.DefaultGap ,  colors :  WheelPickerColors  =  WheelPickerDefaults.wheelPickerColors() ) 
A components for choose hours/minutes/seconds based on  WheelPicker 
#### Parameters
modifier 
The  Modifier  used by the TimePicker. 
config 
a config to defined what element will be shown. 
on Hours Changed 
will be called when hour changed. 
on Minutes Changed 
will be called when minute changed. 
on Seconds Changed 
will be called when second changed. 
gap 
Gap between each element, default is  TimepickerDefaults.DefaultGap . 
colors 
A  WheelPickerColors  to customize the appearance of pickers. 
#### Samples
```
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.tooling.preview.Preview
import com.pico.spatial.ui.design.Timepicker
import com.pico.spatial.ui.design.TimepickerConfig
import com.pico.spatial.ui.design.TimepickerElement

fun main() { 
   //sampleStart 
   var hour by remember { mutableStateOf("") }
var minute by remember { mutableStateOf("") }
var sec by remember { mutableStateOf("") }
Timepicker(
    config =
        TimepickerConfig.create(
            TimepickerElement.hours("H"),
            TimepickerElement.minutes("M"),
            TimepickerElement.seconds("S"),
        ),
    onHoursChanged = { hour = it.toString() },
    onMinutesChanged = { minute = it.toString() },
    onSecondsChanged = { sec = it.toString() },
) 
   //sampleEnd
}
```