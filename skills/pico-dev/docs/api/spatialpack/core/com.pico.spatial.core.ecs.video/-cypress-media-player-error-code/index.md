# CypressMediaPlayerErrorCode | PICO Spatial SDK

core / com.pico.spatial.core.ecs.video / CypressMediaPlayerErrorCode 
# CypressMediaPlayerErrorCode
```kotlin
enum CypressMediaPlayerErrorCode : Enum<CypressMediaPlayerErrorCode>
```
Represents the error code of CypressMediaPlayer. 
Members Entries 
## Entries
ERROR_UNKNOWN 
```kotlin
ERROR_UNKNOWN
```
Unknown error. 
ERROR_NO_MEMORY 
```kotlin
ERROR_NO_MEMORY
```
Out of memory error. 
ERROR_INVALID 
```kotlin
ERROR_INVALID
```
Invalid argument error. 
ERROR_SYSTEM 
```kotlin
ERROR_SYSTEM
```
System error, for example create thread failed. 
ERROR_AUDIO 
```kotlin
ERROR_AUDIO
```
Audio error. 
ERROR_VIDEO 
```kotlin
ERROR_VIDEO
```
Video error. 
ERROR_STREAM 
```kotlin
ERROR_STREAM
```
Stream info not found error. 
ERROR_DEMUXER 
```kotlin
ERROR_DEMUXER
```
Demuxer read failed error. 
ERROR_DECODER 
```kotlin
ERROR_DECODER
```
Decoder not found error. 
ERROR_IO 
```kotlin
ERROR_IO
```
IO error. 
## Properties
code 
```kotlin
val code: Int
```
The error code. 
entries 
```kotlin
val entries: EnumEntries<CypressMediaPlayerErrorCode>
```
Returns a representation of an immutable list of all enum entries, in the order they're declared. 
## Functions
value Of 
```kotlin
fun valueOf(value: String): CypressMediaPlayerErrorCode
```
Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.) 
values 
```kotlin
fun values(): Array<CypressMediaPlayerErrorCode>
```
Returns an array containing the constants of this enum type, in the order they're declared.