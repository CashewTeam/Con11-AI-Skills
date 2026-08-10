# formatWithSkeleton | PICO Spatial SDK

ui:design / com.pico.spatial.ui.design.calendar / formatWithSkeleton 
# formatWithSkeleton
```kotlin
fun formatWithSkeleton(utcTimeMillis: Long, skeleton: String, locale: Locale = Locale.getDefault()): String
```
Formats a UTC timestamp into a string with a given date format skeleton. 
A skeleton is similar to, and uses the same format characters as described in  Unicode Technical Standard #35 
One difference is that order is irrelevant. For example, "MMMMd" will return "MMMM d" in the en_US locale, but "d. MMMM" in the de_CH locale. 
#### Return
The  String  that represents UTC timestamp with the given data format skeleton 
#### Parameters
utc Time Millis 
a UTC timestamp to format (milliseconds from epoch) 
skeleton 
a date format skeleton 
locale 
the  Locale  to use when formatting the given timestamp