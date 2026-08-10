# onProvideData | PICO Spatial SDK

tracking / com.pico.spatial.tracking / DataProvider / DataListener / onProvideData 
# onProvideData
```kotlin
abstract fun onProvideData(data: T)
```
Called when new data is available. 
This callback is not called on the main thread. Avoid manipulating UI, entities, or components directly in this callback. 
#### Parameters
data 
The latest data.