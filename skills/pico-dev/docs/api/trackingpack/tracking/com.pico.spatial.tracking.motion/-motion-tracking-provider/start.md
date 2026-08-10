# start | PICO Spatial SDK

tracking / com.pico.spatial.tracking.motion / MotionTrackingProvider / start 
# start
```kotlin
fun start(startInfo: MotionTrackingStartInfo): DataProvider.StartResult
```
Starts providing motion tracking data using the specified  MotionTrackingStartInfo . 
You can request the exact number of motion trackers via  MotionTrackingStartInfo.requestDeviceCount , and receive the result through  addRequestCompleteListener . 
Note that the user may not connect the exact requested number of trackers. You should check the request result via  TrackerRequestCompleteListener.onRequestComplete . 
After starting, you can get the latest data from  latestData , register a  DataListener  using  addListener  to receive data, or get data from  dataFlow . 
If the current type of data is not available,  StartResult.PENDING  will be returned. Data provision will automatically start once all requirements are satisfied. 
#### Return
StartResult.SUCCESS  if motion tracking starts successfully, or  StartResult.PENDING  if the current type of data is not supported. 
#### Parameters
start Info 
The configuration for starting motion tracking.