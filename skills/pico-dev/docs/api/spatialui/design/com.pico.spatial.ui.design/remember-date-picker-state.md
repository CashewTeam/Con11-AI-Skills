# rememberDatePickerState | PICO Spatial SDK

ui:design / com.pico.spatial.ui.design / rememberDatePickerState 
# rememberDatePickerState
```kotlin
@Composable
```fun  rememberDatePickerState ( initialSelectedDateMillis :  Long ?  =  null ,  initialDisplayedMonthMillis :  Long ?  =  initialSelectedDateMillis ) :  DatePickerState 
Creates a  DatePickerState  for a  DatePicker  that is remembered across compositions. 
#### Parameters
initial Selected Date Millis 
timestamp in  UTC  milliseconds from the epoch that represents an initial selection of a date. Provide a  null  to indicate no selection. 
initial Displayed Month Millis 
timestamp in  UTC  milliseconds from the epoch that represents an initial selection of a month to be displayed to the user. By default, in case an  initialSelectedDateMillis  is provided, the initial displayed month would be the month of the selected date. Otherwise, in case  null  is provided, the displayed month would be the current one.