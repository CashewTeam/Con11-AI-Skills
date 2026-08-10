# DatePickerDefaults | PICO Spatial SDK

ui:design / com.pico.spatial.ui.design / DatePickerDefaults 
# DatePickerDefaults
```kotlin
object DatePickerDefaults
```
Contains default values used by the  DatePicker . 
Members 
## Functions
date Formatter 
```kotlin
fun dateFormatter(yearSelectionSkeleton: String = YearMonthSkeleton, selectedDateSkeleton: String = YearAbbrMonthDaySkeleton, selectedDateDescriptionSkeleton: String = YearMonthWeekdayDaySkeleton): DatePickerFormatter
```
The date formatter will apply the best possible localized form of the given skeleton and Locale. A skeleton is similar to, and uses the same format characters as, a Unicode  UTS #35  pattern. 
date Picker Colors 
```kotlin
@Composable
```fun  datePickerColors ( ) :  DatePickerColors 
Default colors for  DatePicker . 
date Piker Colors 
```kotlin
@Composable
```fun  datePikerColors ( primaryContentColor :  Color  =  Color.Unspecified ,  weekTextColor :  Color  =  Color.Unspecified ,  inactiveDateColor :  Color  =  Color.Unspecified ,  selectedDateBackgroundColor :  Color  =  Color.Unspecified ,  todayBackgroundColor :  Color  =  Color.Unspecified ,  todayTextColor :  Color  =  Color.Unspecified ,  rangeBackgroundColor :  Color  =  Color.Unspecified ) :  DatePickerColors 
Custom colors for  DatePicker .