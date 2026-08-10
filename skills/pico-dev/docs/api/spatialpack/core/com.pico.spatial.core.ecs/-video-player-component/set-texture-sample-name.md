# setTextureSampleName | PICO Spatial SDK

core / com.pico.spatial.core.ecs / VideoPlayerComponent / setTextureSampleName 
# setTextureSampleName
```kotlin
fun setTextureSampleName(textureSampleName: String)
```
Sets the texture sample name for the  VideoPlayerComponent  instance. 
When set, the video component broadcasts its texture using this name according to the  VideoTextureSampleMode , enabling the shader graph material to sample the texture using the same built-in video sample name. 
Typically used together with  setTextureSampleMode . 
Note: 
- 
Ensure the texture sample name matches the built-in video sample name in the shader graph material. 
- 
This setting applies only when  VideoTextureSampleMode.RAW  or  VideoTextureSampleMode.RAW_AND_BLURRED  is set. 
#### Parameters
texture Sample Name 
The texture sample name to set. Must be non-empty, contain only alphanumeric characters, and be at most 256 bytes long.