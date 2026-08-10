# VideoDimensionMode | PICO Spatial SDK

core / com.pico.spatial.core.ecs.video / VideoDimensionMode 
# VideoDimensionMode
```kotlin
enum VideoDimensionMode : Enum<VideoDimensionMode>
```
Represents the video dimension mode of the material. 
VideoDimensionMode determines how the material compose the video frame for stereoscopic rendering. Default:MONO. 
Members Entries 
## Entries
MONO 
```kotlin
MONO
```
MONO indicates the video dimension mode is a normal (monoscopic) video, where the content for the left and right eyes is identical. This mode supports 2D, 2D 180, and 2D 360 videos. 
TOP_AND_DOWN 
```kotlin
TOP_AND_DOWN
```
TOP_AND_DOWN indicates the video dimension mode is vertically structured into two parts. For example, if the decoded image resolution is 3840 x 1920, both the left and right eye images have a resolution of 3840 x 960. This mode supports 2D top and bottom, 3D 180 top and bottom, and 3D 360 top and bottom videos. 
SIDE_BY_SIDE 
```kotlin
SIDE_BY_SIDE
```
SIDE_BY_SIDE indicates the video dimension mode is horizontally structured into two parts. For example, if the decoded image resolution is 3840 x 1920, both left and right eye images have a resolution of 1920 x 1920. This mode supports 2D side by side, 3D 180 side by side, and 3D 360 side by side videos. 
MULTIPLE_VIEW 
```kotlin
MULTIPLE_VIEW
```
MULTIPLE_VIEW indicates the video dimension mode uses a double buffer structure, meaning there is one buffer dedicated for each eye. This mode is typically used for MV-HEVC video format. For example, if the decoded image resolution is 3840 x 1920, both the left and right eye images have a resolution of 3840 x 1920. 
UNKNOWN 
```kotlin
UNKNOWN
```
Reserved value for forward compatibility. 
## Properties
entries 
```kotlin
val entries: EnumEntries<VideoDimensionMode>
```
Returns a representation of an immutable list of all enum entries, in the order they're declared. 
value 
```kotlin
val value: Int
```
The integer value of the dimension mode. 
## Functions
value Of 
```kotlin
fun valueOf(value: String): VideoDimensionMode
```
Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.) 
values 
```kotlin
fun values(): Array<VideoDimensionMode>
```
Returns an array containing the constants of this enum type, in the order they're declared.