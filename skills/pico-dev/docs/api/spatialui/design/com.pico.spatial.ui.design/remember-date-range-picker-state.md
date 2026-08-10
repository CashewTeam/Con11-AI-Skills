# rememberDateRangePickerState | PICO Spatial SDK

ui:design / com.pico.spatial.ui.design / rememberDateRangePickerState 
# rememberDateRangePickerState
```kotlin
@Composable
```fun  rememberDateRangePickerState ( initialSelectedStartDateMillis :  Long ?  =  null ,  initialSelectedEndDateMillis :  Long ?  =  null ,  initialDisplayedMonthMillis :  Long ?  =  initialSelectedStartDateMillis ) :  DateRangePickerState 
Creates a  DateRangePickerState  for a  DateRangePicker  that is remembered across compositions. 
#### Parameters
initial Selected Start Date Millis 
timestamp in  UTC  milliseconds from the epoch that represents an initial selection of a start date. Provide a  null  to indicate no selection. 
initial Selected End Date Millis 
timestamp in  UTC  milliseconds from the epoch that represents an initial selection of an end date. Provide a  null  to indicate no selection. 
initial Displayed Month Millis 
timestamp in  UTC  milliseconds from the epoch that represents an initial selection of a month to be displayed to the user. By default, in case an  initialSelectedStartDateMillis  is provided, the initial displayed month would be the month of the selected date. Otherwise, in case  null  is provided, the displayed month would be the current one.