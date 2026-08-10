# setSpatialContent | PICO Spatial SDK

ui:platform / com.pico.spatial.ui.platform.stub.delegate / SpatialActivityDelegate / setSpatialContent 
# setSpatialContent
```kotlin
abstract fun setSpatialContent()
```
Set the spatial content to a custom activity. Like  Activity.setContentView , this method should be called at  Activity.onCreate . Be noticed that, when using a  SpatialActivityDelegate , you should not call  Activity.setContentView  or ComponentActivity.setContent anymore.