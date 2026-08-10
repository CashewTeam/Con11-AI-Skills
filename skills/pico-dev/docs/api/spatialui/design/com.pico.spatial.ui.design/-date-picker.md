# DatePicker | PICO Spatial SDK

ui:design / com.pico.spatial.ui.design / DatePicker 
# DatePicker
```kotlin
@Composable
```fun  DatePicker ( onDateSelected :  ( selectedDateMillis :  Long )  ->  Unit ,  modifier :  Modifier  =  Modifier ,  state :  DatePickerState  =  rememberDatePickerState() ,  dateFormatter :  DatePickerFormatter  =  remember { DatePickerDefaults.dateFormatter() } ,  colors :  DatePickerColors  =  DatePickerDefaults.datePickerColors() ,  headerStyle :  HeaderStyle  =  HeaderStyle.Navigation(true) ) 
DatePicker is a component that allows users to select a date. 
#### Parameters
on Date Selected 
Callback invoked when date is selected. 
modifier 
The  Modifier  to be applied to this date picker. 
state 
State of the date picker. See  rememberDatePickerState . 
date Formatter 
A  DatePickerFormatter  that provides formatting skeletons for dates display transforms it into a date input. 
colors 
DatePickerColors  that will be used to resolve the colors used for this date picker in different states. 
header Style 
Controls the header style of the date picker. See  HeaderStyle . 
#### Samples
```
import android.annotation.SuppressLint
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.tooling.preview.Preview
import androidx.compose.ui.unit.dp
import com.pico.spatial.ui.design.Button
import com.pico.spatial.ui.design.ButtonDefaults
import com.pico.spatial.ui.design.DatePicker
import com.pico.spatial.ui.design.DateRangePicker
import com.pico.spatial.ui.design.HeaderStyle
import com.pico.spatial.ui.design.Text
import com.pico.spatial.ui.design.rememberDatePickerState
import com.pico.spatial.ui.design.rememberDateRangePickerState
import com.pico.spatial.ui.design.windows.DatePickerDialog
import java.text.SimpleDateFormat
import java.util.Date

fun main() { 
   //sampleStart 
   Column(verticalArrangement = Arrangement.spacedBy(8.dp)) {
    var millis: Long? by remember { mutableStateOf(null) }
    DatePicker(onDateSelected = { millis = it })
    Text("Selected date: ${millis.formatToText()} ", color = Color.White)
} 
   //sampleEnd
}
```