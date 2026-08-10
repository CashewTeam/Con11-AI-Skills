# start | PICO Spatial SDK

tracking / com.pico.spatial.tracking.body / BodyTrackingProvider / start 
# start
```kotlin
fun start(startInfo: BodyTrackingStartInfo): DataProvider.StartResult
```
Starts providing body tracking data using the specified  BodyTrackingStartInfo . 
- 
If calibration is required at startup, set  BodyTrackingStartInfo.needCalibration  to  true . 
- 
After starting, you can: 
- 
Get the latest data from latestData. 
- 
Register a DataListener via addListener to receive data. 
- 
Collect data from dataFlow. 
If the requested type of data is not available now,  StartResult.PENDING  will be returned. Data provision will automatically start once all requirements are satisfied. 
#### Return
StartResult.SUCCESS  if body tracking starts successfully;  StartResult.PENDING  if the current type of data is currently unavailable. 
#### Parameters
start Info 
Configuration for starting body tracking.