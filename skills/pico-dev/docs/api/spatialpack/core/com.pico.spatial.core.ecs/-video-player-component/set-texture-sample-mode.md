# setTextureSampleMode | PICO Spatial SDK

core / com.pico.spatial.core.ecs / VideoPlayerComponent / setTextureSampleMode 
# setTextureSampleMode
```kotlin
fun setTextureSampleMode(textureSampleMode: VideoTextureSampleMode)
```
Sets the  VideoTextureSampleMode  for the  VideoPlayerComponent  instance. Default is NONE. Typically used together with  setTextureSampleName . 
Note: 
- 
VideoTextureSampleMode.NONE  indicates no texture will be broadcast from this video     component. 
- 
VideoTextureSampleMode.RAW  broadcasts the raw texture from this video component. 
- 
VideoTextureSampleMode.RAW_AND_BLURRED  blurs the raw texture and broadcasts it from this     video component. 
#### Parameters
texture Sample Mode 
The  VideoTextureSampleMode  to set.