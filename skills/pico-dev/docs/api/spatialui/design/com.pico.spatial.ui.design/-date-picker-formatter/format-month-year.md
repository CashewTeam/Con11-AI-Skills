# formatMonthYear | PICO Spatial SDK

ui:design / com.pico.spatial.ui.design / DatePickerFormatter / formatMonthYear 
# formatMonthYear
```kotlin
abstract fun formatMonthYear(monthMillis: Long?, locale: Locale): String?
```
Format a given  monthMillis  to a string representation of the month and the year (i.e. January 2023). 
#### Return
The  String  that represents the time of give date and locale. If input time is invalid or it doesn't support this formatting, it will return null. 
#### Parameters
month Millis 
timestamp in  UTC  milliseconds from the epoch that represents the month 
locale 
a  Locale  to use when formatting the month and year