# AmbisonicsType | PICO Spatial SDK

core / com.pico.spatial.core.ecs.audio / AmbisonicsType 
# AmbisonicsType
```kotlin
enum AmbisonicsType : Enum<AmbisonicsType>
```
Defines Ambisonics audio formats for spatial audio processing. 
This enum specifies supported Ambisonics configurations that determine how 3D audio data is encoded and decoded. The options follow industry-standard channel ordering and normalization schemes. 
## Key Features
- 
ACN Channel Ordering : Ambisonics Channel Number sequence (W, Y, Z, X, V, T, R, S...) 
- 
SN3D Normalization : Schmidt Semi-Normalized (SN3D) energy normalization 
- 
Order Support : Currently supports 1st and 2nd order Ambisonics 
## Usage
Required when configuring audio streams with  AudioChannelLayoutType.AMBISONICS : 

```
AudioStreamConfig(    channelLayoutType = AudioChannelLayoutType.AMBISONICS,    ambisonicType = AmbisonicsType.ACN_SN3D_2,    // ... other parameters)
```Members Entries 
## Entries
NONE 
```kotlin
NONE
```
No Ambisonics. 
ACN_SN3D_1 
```kotlin
ACN_SN3D_1
```
1st order Ambisonics (ACN channel order + SN3D normalization). 
ACN_SN3D_2 
```kotlin
ACN_SN3D_2
```
2nd order Ambisonics. 
UNKNOWN 
```kotlin
UNKNOWN
```
Reserved value for forward compatibility. 
## Properties
entries 
```kotlin
val entries: EnumEntries<AmbisonicsType>
```
Returns a representation of an immutable list of all enum entries, in the order they're declared. 
value 
```kotlin
val value: Int
```
The integer value of the Ambisonics type. 
## Functions
value Of 
```kotlin
fun valueOf(value: String): AmbisonicsType
```
Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.) 
values 
```kotlin
fun values(): Array<AmbisonicsType>
```
Returns an array containing the constants of this enum type, in the order they're declared.