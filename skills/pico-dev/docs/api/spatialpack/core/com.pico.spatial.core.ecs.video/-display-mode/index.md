# DisplayMode | PICO Spatial SDK

core / com.pico.spatial.core.ecs.video / DisplayMode 
# DisplayMode
```kotlin
enum DisplayMode : Enum<DisplayMode>
```
The DisplayMode sets how the  com.pico.spatial.core.ecs.VideoComponent  displays 3D source videos containing binocular parallax, such as SIDE_BY_SIDE, TOP_AND_DOWN, and MV-HEVC 3D format videos. 
- 
When set to MONO, the video is displayed as a single view without stereo effect. 
- 
When set to STEREO, the video is displayed with stereo effect in a stereo view. 
This setting serves as a toggle to control 3D display on or off. 
Members Entries 
## Entries
NONE 
```kotlin
NONE
```
The NONE display mode is the initial state of  com.pico.spatial.core.ecs.VideoComponent , VideoComponent will display the video by  VideoDimensionMode . This is the default value of  DisplayMode . 
MONO 
```kotlin
MONO
```
The MONO display mode,when the video is 3D video, the video will be displayed in a single view with no stereo effect. 
STEREO 
```kotlin
STEREO
```
The STEREO display mode,when the video is 3D video, the video will be displayed in a stereo view with stereo effect. 
UNKNOWN 
```kotlin
UNKNOWN
```
Reserved value for forward compatibility. 
## Properties
entries 
```kotlin
val entries: EnumEntries<DisplayMode>
```
Returns a representation of an immutable list of all enum entries, in the order they're declared. 
value 
```kotlin
val value: Int
```
The integer value of the  DisplayMode . 
## Functions
value Of 
```kotlin
fun valueOf(value: String): DisplayMode
```
Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.) 
values 
```kotlin
fun values(): Array<DisplayMode>
```
Returns an array containing the constants of this enum type, in the order they're declared.