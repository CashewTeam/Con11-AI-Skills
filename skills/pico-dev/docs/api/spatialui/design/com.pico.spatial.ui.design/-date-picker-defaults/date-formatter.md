# dateFormatter | PICO Spatial SDK

ui:design / com.pico.spatial.ui.design / DatePickerDefaults / dateFormatter 
# dateFormatter
```kotlin
fun dateFormatter(yearSelectionSkeleton: String = YearMonthSkeleton, selectedDateSkeleton: String = YearAbbrMonthDaySkeleton, selectedDateDescriptionSkeleton: String = YearMonthWeekdayDaySkeleton): DatePickerFormatter
```
The date formatter will apply the best possible localized form of the given skeleton and Locale. A skeleton is similar to, and uses the same format characters as, a Unicode  UTS #35  pattern. 
One difference is that order is irrelevant. For example, "MMMMd" will return "MMMM d" in the  en_US  locale, but "d. MMMM" in the  de_CH  locale. 
#### Return
Returns a  DatePickerFormatter . 
#### Parameters
year Selection Skeleton 
a date format skeleton used to format the date picker's year selection menu button (e.g. "March 2021"). 
selected Date Skeleton 
a date format skeleton used to format a selected date (e.g. "Mar 27, 2021") 
selected Date Description Skeleton 
a date format skeleton used to format a selected date to be used as content description for screen readers (e.g. "Saturday, March 27, 2021")