# DatePickerFormatter | PICO Spatial SDK

ui:design / com.pico.spatial.ui.design / DatePickerFormatter 
# DatePickerFormatter
```kotlin
interface DatePickerFormatter
```
A date formatter interface used by  DatePicker . 
Members 
## Functions
format Date 
```kotlin
abstract fun formatDate(dateMillis: Long?, locale: Locale, forContentDescription: Boolean = false): String?
```
Format a given  dateMillis  to a string representation of the date (i.e. Mar 27, 2021). 
format Month Year 
```kotlin
abstract fun formatMonthYear(monthMillis: Long?, locale: Locale): String?
```
Format a given  monthMillis  to a string representation of the month and the year (i.e. January 2023).