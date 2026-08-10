# formatDate | PICO Spatial SDK

ui:design / com.pico.spatial.ui.design / DatePickerFormatter / formatDate 
# formatDate
```kotlin
abstract fun formatDate(dateMillis: Long?, locale: Locale, forContentDescription: Boolean = false): String?
```
Format a given  dateMillis  to a string representation of the date (i.e. Mar 27, 2021). 
#### Return
The  String  that represents the time of give date and locale. If input date is invalid or it doesn't support this formatting, it will return null. 
#### Parameters
date Millis 
timestamp in  UTC  milliseconds from the epoch that represents the date 
locale 
a  Locale  to use when formatting the date 
for Content Description 
indicates that the requested formatting is for content description. In these cases, the output may include a more descriptive wording that will be passed to a screen readers.