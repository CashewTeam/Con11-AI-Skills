# AudioChannelLayoutType | PICO Spatial SDK

core / com.pico.spatial.core.ecs.audio / AudioChannelLayoutType 
# AudioChannelLayoutType
```kotlin
enum AudioChannelLayoutType : Enum<AudioChannelLayoutType>
```
Defines the fundamental spatial audio rendering mode for audio streams. 
This enum determines how the audio system interprets channel data: 
- 
STANDARD: Traditional speaker-based layouts (e.g., stereo, 5.1 surround) 
- 
AMBISONICS: Spherical harmonic-based full 3D audio representation 
## Usage Guidelines
- 
Choose STANDARD when: 
- 
Targeting specific speaker configurations 
- 
Using conventional surround sound layouts 
- 
Needing compatibility with traditional audio systems 
- 
Choose AMBISONICS when: 
- 
Requiring full 3D spatial audio 
- 
Supporting VR/AR applications 
- 
Needing rotation-independent sound fields 
Example configuration: 

```
// For home theater setupAudioStreamConfig(    channelLayoutType = AudioChannelLayoutType.STANDARD,    channelLayout = AudioChannelLayout.OUTPUT_LAYOUT_7_1,    // ...)// For VR spatial audioAudioStreamConfig(    channelLayoutType = AudioChannelLayoutType.AMBISONICS,    ambisonicType = AmbisonicsType.ACN_SN3D_2,    // ...)
```
#### See also
Audio Channel Layout 
For standard layout configurations 
Ambisonics Type 
For Ambisonics format specifications 
Members Entries 
## Entries
STANDARD 
```kotlin
STANDARD
```
Traditional channel-based audio layouts. Requires: 
AMBISONICS 
```kotlin
AMBISONICS
```
Full-sphere 3D audio format. Requires: 
UNKNOWN 
```kotlin
UNKNOWN
```
Reserved value for forward compatibility. 
## Properties
entries 
```kotlin
val entries: EnumEntries<AudioChannelLayoutType>
```
Returns a representation of an immutable list of all enum entries, in the order they're declared. 
value 
```kotlin
val value: Int
```
The integer value of the layout type. 
## Functions
value Of 
```kotlin
fun valueOf(value: String): AudioChannelLayoutType
```
Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.) 
values 
```kotlin
fun values(): Array<AudioChannelLayoutType>
```
Returns an array containing the constants of this enum type, in the order they're declared.