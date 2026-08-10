# DateRangePicker | PICO Spatial SDK

ui:design / com.pico.spatial.ui.design / DateRangePicker 
# DateRangePicker
```kotlin
@Composable
```fun  DateRangePicker ( onStartSelected :  ( startDateInMillis :  Long )  ->  Unit ,  onEndSelected :  ( endDateInMillis :  Long ? )  ->  Unit ,  modifier :  Modifier  =  Modifier ,  state :  DateRangePickerState  =  rememberDateRangePickerState() ,  dateFormatter :  DatePickerFormatter  =  remember { DatePickerDefaults.dateFormatter() } ,  colors :  DatePickerColors  =  DatePickerDefaults.datePickerColors() ,  headerStyle :  HeaderStyle  =  HeaderStyle.Navigation(true) ) 
Date range pickers let people select a range of dates and can be embedded into Dialogs. 
#### Parameters
on Start Selected 
callback invoked when start date is selected 
on End Selected 
callback invoked when end date is selected 
modifier 
the  Modifier  to be applied to this date range picker 
state 
state of the date range picker. See  rememberDateRangePickerState . 
date Formatter 
a  DatePickerFormatter  that provides formatting skeletons for dates display transforms it into a date range input 
colors 
DatePickerColors  that will be used to resolve the colors used for this date range picker in different states. 
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
   var start: Long? by remember { mutableStateOf(null) }
var end: Long? by remember { mutableStateOf(null) }
Column(modifier = Modifier.fillMaxSize(), verticalArrangement = Arrangement.Top) {
    DateRangePicker(onStartSelected = { start = it }, onEndSelected = { end = it })
    Text(
        "Selected date range: ${start.formatToText()} -- ${end.formatToText()}",
        color = Color.White,
    )
} 
   //sampleEnd
}
```