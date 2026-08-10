# SpatialAudioMode | PICO Spatial SDK

core / com.pico.spatial.audio / SpatialAudioTrackExtension / SpatialAudioMode 
# SpatialAudioMode
```kotlin
enum SpatialAudioMode : Enum<SpatialAudioTrackExtension.SpatialAudioMode>
```
Spatial audio rendering mode. 
Determines how the audio will be spatialized: 
- 
CHANNEL : No spatialization, traditional channel-based audio. 
- 
AMBIENT : Orientation-based mixing, audio follows listener orientation. 
- 
OBJECT : Full 3D positional audio with position and orientation. 
Members Entries 
## Entries
CHANNEL 
```kotlin
CHANNEL
```
Traditional channel-based audio (stereo, 5.1, etc.). No spatial processing applied. Audio plays as-is from the speakers. 
AMBIENT 
```kotlin
AMBIENT
```
Ambient audio that considers listener orientation. Audio is mixed based on listener's head orientation but has no positional component. 
OBJECT 
```kotlin
OBJECT
```
Full 3D positional audio with both position and orientation. Each sound source has its own 3D position and can be spatially rendered. 
## Properties
entries 
```kotlin
val entries: EnumEntries<SpatialAudioTrackExtension.SpatialAudioMode>
```
Returns a representation of an immutable list of all enum entries, in the order they're declared. 
## Functions
value Of 
```kotlin
fun valueOf(value: String): SpatialAudioTrackExtension.SpatialAudioMode
```
Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.) 
values 
```kotlin
fun values(): Array<SpatialAudioTrackExtension.SpatialAudioMode>
```
Returns an array containing the constants of this enum type, in the order they're declared.