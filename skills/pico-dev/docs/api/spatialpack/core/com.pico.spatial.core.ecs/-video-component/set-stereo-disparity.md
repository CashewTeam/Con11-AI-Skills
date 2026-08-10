# setStereoDisparity | PICO Spatial SDK

core / com.pico.spatial.core.ecs / VideoComponent / setStereoDisparity 
# setStereoDisparity
```kotlin
fun setStereoDisparity(stereoDisparity: Float)
```
Sets the stereo disparity for 3D video. Only effective for 3D (non-mono) videos when DisplayMode is Stereo. The valid range is -40.0f, 40.0f. 
#### Parameters
stereo Disparity 
The stereo disparity value to set. Must be in range -40.0f, 40.0f.