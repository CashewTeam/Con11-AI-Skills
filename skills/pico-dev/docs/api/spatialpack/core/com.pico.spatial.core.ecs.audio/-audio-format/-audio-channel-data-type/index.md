# AudioChannelDataType | PICO Spatial SDK

core / com.pico.spatial.core.ecs.audio / AudioFormat / AudioChannelDataType 
# AudioChannelDataType
```kotlin
enum AudioChannelDataType : Enum<AudioFormat.AudioChannelDataType>
```
The AudioChannelDataType audio type, which can be either signed 8-bit, signed 16-bit, signed 24-bit, signed 32-bit, or 32-bit floating point. 
Members Entries 
## Entries
UNKNOWN 
```kotlin
UNKNOWN
```
Invalid data type. 
INT8 
```kotlin
INT8
```
Signed 8-bit integer. 
INT16 
```kotlin
INT16
```
Signed 16-bit integer. 
INT24 
```kotlin
INT24
```
Signed 24-bit integer. 
INT32 
```kotlin
INT32
```
Signed 32-bit integer. 
FLOAT32 
```kotlin
FLOAT32
```
32-bit floating point. 
## Properties
entries 
```kotlin
val entries: EnumEntries<AudioFormat.AudioChannelDataType>
```
Returns a representation of an immutable list of all enum entries, in the order they're declared. 
## Functions
value Of 
```kotlin
fun valueOf(value: String): AudioFormat.AudioChannelDataType
```
Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.) 
values 
```kotlin
fun values(): Array<AudioFormat.AudioChannelDataType>
```
Returns an array containing the constants of this enum type, in the order they're declared.