# DatePickerDialog | PICO Spatial SDK

ui:design / com.pico.spatial.ui.design.windows / DatePickerDialog 
# DatePickerDialog
```kotlin
@Composable
```fun  DatePickerDialog ( onDismissRequest :  ( )  ->  Unit ,  modifier :  Modifier  =  Modifier ,  title :  @ Composable ( )  ->  Unit ?  =  null ,  positiveButton :  @ Composable ( )  ->  Unit ?  =  null ,  negativeButton :  @ Composable ( )  ->  Unit ?  =  null ,  properties :  DialogProperties  =  DatePickerDialogDefaults.DefaultDialogProperties ,  cornerRadius :  Dp  =  LocalTokensBearer.current.dimension.RadiusLarge ,  followViewpoints :  Set < ViewPoint >  =  ViewPoint.All ,  content :  @ Composable ( )  ->  Unit ) 
A dialog for displaying a  DatePicker  and  DateRangePicker . Date pickers let people select a date. 
#### Parameters
on Dismiss Request 
called when the user tries to dismiss the Dialog by clicking outside or pressing the back button. This is not called when the dismiss button is clicked. 
modifier 
the  Modifier  to be applied to this dialog's content. 
title 
dialog title 
positive Button 
button which is meant to confirm a proposed action, thus resolving what triggered the dialog. The dialog does not set up any events for this button, nor does it control its enablement, so those need to be set up by the caller. 
negative Button 
button which is meant to dismiss the dialog. The dialog does not set up any events for this button so they need to be set up by the caller. 
properties 
typically platform specific properties to further configure the dialog 
corner Radius 
round corner radius. 
follow Viewpoints 
The viewpoints that the dialog should follow. 
content 
the content of the dialog (i.e. a  DatePicker , for example) 
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
    var showDialog by remember { mutableStateOf(false) }
    var selectedTimeMillis: Long? by remember { mutableStateOf(null) }
    if (showDialog) {
        DatePickerDialog(
            onDismissRequest = { showDialog = false },
            title = { Text(text = "Pick date") },
            positiveButton = {
                Button(onClick = { showDialog = false }, size = ButtonDefaults.Regular) {
                    Text(text = "OK")
                }
            },
            negativeButton = {
                Button(
                    onClick = { showDialog = false },
                    size = ButtonDefaults.Regular,
                    colors =
                        ButtonDefaults.buttonColors(
                            containerColor = Color(color = 0x0A000000),
                            contentColor = Color.Black,
                        ),
                ) {
                    Text(text = "Cancel")
                }
            },
        ) {
            DatePicker(
                onDateSelected = { selectedTimeMillis = it },
                headerStyle = HeaderStyle.Dropdown,
            )
        }
    }
    Button(onClick = { showDialog = true }) { Text(text = "show date picker dialog") }
    Text("Selected date: ${selectedTimeMillis.formatToText()} ", color = Color.White)
} 
   //sampleEnd
}
```
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
    var showDialog by remember { mutableStateOf(false) }
    var start: Long? by remember { mutableStateOf(null) }
    var end: Long? by remember { mutableStateOf(null) }
    if (showDialog) {
        val state = rememberDateRangePickerState()
        DatePickerDialog(
            onDismissRequest = { showDialog = false },
            title = { Text(text = "Pick date") },
            positiveButton = {
                Button(
                    onClick = {
                        start = state.selectedStartDateMillis
                        end = state.selectedEndDateMillis
                        showDialog = false
                    },
                    size = ButtonDefaults.Regular,
                ) {
                    Text(text = "OK")
                }
            },
            negativeButton = {
                Button(
                    onClick = { showDialog = false },
                    size = ButtonDefaults.Regular,
                    colors =
                        ButtonDefaults.buttonColors(
                            containerColor = Color(color = 0x0A000000),
                            contentColor = Color.Black,
                        ),
                ) {
                    Text(text = "Cancel")
                }
            },
        ) {
            DateRangePicker(onStartSelected = {}, onEndSelected = {}, state = state)
        }
    }
    Button(onClick = { showDialog = true }) { Text(text = "show date range picker dialog") }
    Text(
        "Selected date range: ${start.formatToText()}  -- ${end.formatToText()}",
        color = Color.White,
    )
} 
   //sampleEnd
}
```
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
    var showDialog by remember { mutableStateOf(false) }
    var selectedTimeMillis: Long? by remember { mutableStateOf(null) }
    if (showDialog) {
        val state = rememberDatePickerState()
        DatePickerDialog(
            onDismissRequest = { showDialog = false },
            title = { Text(text = "Pick date range") },
            positiveButton = {
                Button(
                    onClick = {
                        selectedTimeMillis = state.selectedDateMillis
                        showDialog = false
                    },
                    size = ButtonDefaults.Regular,
                ) {
                    Text(text = "OK")
                }
            },
            negativeButton = {
                Button(
                    onClick = { showDialog = false },
                    size = ButtonDefaults.Regular,
                    colors =
                        ButtonDefaults.buttonColors(
                            containerColor = Color(color = 0x0A000000),
                            contentColor = Color.Black,
                        ),
                ) {
                    Text(text = "Cancel")
                }
            },
        ) {
            DatePicker(
                onDateSelected = {},
                state = state,
                headerStyle = HeaderStyle.Navigation(false),
            )
        }
    }
    Button(onClick = { showDialog = true }) { Text(text = "show date picker dialog") }
    Text("Selected date: ${selectedTimeMillis.formatToText()} ", color = Color.White)
} 
   //sampleEnd
}
```