# setDisplayMode | PICO Spatial SDK

core / com.pico.spatial.core.ecs / VideoComponent / setDisplayMode 
# setDisplayMode
```kotlin
fun setDisplayMode(displayMode: DisplayMode)
```
Sets the display mode of the  VideoComponent . 
The display mode does not work for 2D videos. 
#### Parameters
display Mode 
The display mode of the  VideoComponent , which can be set to  DisplayMode.NONE ,  DisplayMode.MONO , or  DisplayMode.STEREO . The default value is  DisplayMode.NONE .  DisplayMode.MONO  is used to display the video in a single view with no stereo effect.  DisplayMode.STEREO  is used to display the video in a stereo view with stereo effect. 
#### See also
Display Mode