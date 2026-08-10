# start | PICO Spatial SDK

tracking / com.pico.spatial.tracking / DataProvider / start 
# start
```kotlin
abstract fun start(): DataProvider.StartResult
```
Starts providing tracking data. 
You can get the latest data from  latestData , register a  DataListener  via  addListener  to receive data, or get data from  dataFlow . 
If the current data type is not supported,  StartResult.PENDING  will be returned. Data provision will automatically start when all requirements are met. 
#### Return
StartResult.SUCCESS  if data provision starts successfully, or  StartResult.PENDING  if the current type of data is not supported now.