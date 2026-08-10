# DataListener | PICO Spatial SDK

tracking / com.pico.spatial.tracking / DataProvider / DataListener 
# DataListener
```kotlin
fun interface DataListener<T>
```
The listener for receiving data from a  DataProvider . 
Members 
## Functions
on Provide Data 
```kotlin
abstract fun onProvideData(data: T)
```
Called when new data is available.