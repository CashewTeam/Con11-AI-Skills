# AudioChannelLayout | PICO Spatial SDK

core / com.pico.spatial.core.ecs.audio / AudioChannelLayout 
# AudioChannelLayout
```kotlin
enum AudioChannelLayout : Enum<AudioChannelLayout>
```
Defines standard audio channel layouts for spatial audio configurations. 
This enum specifies industry-standard speaker arrangements for different audio playback environments. Used with  AudioStreamConfig  to define physical speaker positioning when using standard channel layouts, the system default is  AudioChannelLayout.OUTPUT_LAYOUT_STEREO . 
## Channel Layout Types
- 
AudioChannelLayoutType.STANDARD : Standard channel layout with predefined configurations. 
- 
AudioChannelLayoutType.AMBISONICS : Ambisonics layout for spherical harmonic-based audio rendering. 
## Channel Layout Specifications
- 
OUTPUT_LAYOUT_INVALID : Indicates uninitialized/invalid configuration. 
- 
OUTPUT_LAYOUT_MONO : Single channel audio (Center). 
- 
OUTPUT_LAYOUT_STEREO : 2-channel (Left + Right). 
- 
OUTPUT_LAYOUT_QUAD : 4-channel (Front-Left + Front-Right + Rear-Left + Rear-Right). 
- 
OUTPUT_LAYOUT_QUADSIDE : Alternative quadraphonic layout with side speakers. 
- 
OUTPUT_LAYOUT_5_1 : 6-channel surround (Front L/R, Center, LFE, Rear L/R). 
- 
OUTPUT_LAYOUT_6_1 : 7-channel surround, extended 6.1 surround sound layout (5.1 + rear center). 
- 
OUTPUT_LAYOUT_7_1 : 8-channel surround，Home theater 7.1 surround sound layout (5.1 + side left/side right). 
- 
OUTPUT_LAYOUT_5_1_2 : 8-channel Dolby Atmos® layout (5.1 base + 2 overhead). 
## Usage Example

```
// Configure for home theater systemAudioStreamConfig(    channelLayoutType = AudioChannelLayoutType.STANDARD,    channelLayout = AudioChannelLayout.OUTPUT_LAYOUT_5_1_2,    // ...other parameters)
```Members Entries 
## Entries
OUTPUT_LAYOUT_INVALID 
```kotlin
OUTPUT_LAYOUT_INVALID
```
Invalid output layout (uninitialized or error state). 
OUTPUT_LAYOUT_MONO 
```kotlin
OUTPUT_LAYOUT_MONO
```
Single audio channel layout. 
OUTPUT_LAYOUT_STEREO 
```kotlin
OUTPUT_LAYOUT_STEREO
```
Stereo channel layout (left/right). 
OUTPUT_LAYOUT_QUAD 
```kotlin
OUTPUT_LAYOUT_QUAD
```
Quadraphonic channel layout (front-left/front-right/rear-left/rear-right), also this is default layout. 
OUTPUT_LAYOUT_QUADSIDE 
```kotlin
OUTPUT_LAYOUT_QUADSIDE
```
Quad side channel layout (alternative quad configuration). 
OUTPUT_LAYOUT_5_1 
```kotlin
OUTPUT_LAYOUT_5_1
```
Standard 5.1 surround sound layout. 
OUTPUT_LAYOUT_6_1 
```kotlin
OUTPUT_LAYOUT_6_1
```
Extended 6.1 surround sound layout. 
OUTPUT_LAYOUT_7_1 
```kotlin
OUTPUT_LAYOUT_7_1
```
Home theater 7.1 surround sound layout (5.1 + side left/side right). 
OUTPUT_LAYOUT_5_1_2 
```kotlin
OUTPUT_LAYOUT_5_1_2
```
Dolby Atmos 5.1.2 channel layout with height channels. 
UNKNOWN 
```kotlin
UNKNOWN
```
Unknown layout. 
## Properties
entries 
```kotlin
val entries: EnumEntries<AudioChannelLayout>
```
Returns a representation of an immutable list of all enum entries, in the order they're declared. 
value 
```kotlin
val value: Int
```
The integer value of the channel layout. 
## Functions
value Of 
```kotlin
fun valueOf(value: String): AudioChannelLayout
```
Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.) 
values 
```kotlin
fun values(): Array<AudioChannelLayout>
```
Returns an array containing the constants of this enum type, in the order they're declared.