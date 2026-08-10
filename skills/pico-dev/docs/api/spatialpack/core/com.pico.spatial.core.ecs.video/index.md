# com.pico.spatial.core.ecs.video | PICO Spatial SDK

core / com.pico.spatial.core.ecs.video 
# Package-level declarations
Types 
## Types
Cypress Media Player 
```kotlin
class CypressMediaPlayer : Closeable
```
Controls video playback in combination with  VideoPlayerComponent . 
Cypress Media Player Callback 
```kotlin
interface CypressMediaPlayerCallback
```
Defines callbacks for  CypressMediaPlayer  events such as playback state changes, errors, and completion. 
Cypress Media Player Error Code 
```kotlin
enum CypressMediaPlayerErrorCode : Enum<CypressMediaPlayerErrorCode>
```
Represents the error code of CypressMediaPlayer. 
Display Mode 
```kotlin
enum DisplayMode : Enum<DisplayMode>
```
The DisplayMode sets how the  com.pico.spatial.core.ecs.VideoComponent  displays 3D source videos containing binocular parallax, such as SIDE_BY_SIDE, TOP_AND_DOWN, and MV-HEVC 3D format videos. 
Texture Usage Flag 
```kotlin
object TextureUsageFlag
```
Defines texture usage flags for controlling how texture buffers are utilized in video processing. 
Video Dimension Mode 
```kotlin
enum VideoDimensionMode : Enum<VideoDimensionMode>
```
Represents the video dimension mode of the material. 
Video Texture Sample Mode 
```kotlin
enum VideoTextureSampleMode : Enum<VideoTextureSampleMode>
```
Represents the video texture sample mode of the material. VideoTextureSampleMode determines how the material samples the video texture. Default:NONE.