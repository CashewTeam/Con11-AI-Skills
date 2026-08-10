# DataType | PICO Spatial SDK

spatialml:securemr / com.pico.spatial.ml.securemr / Tensor / DataType 
# DataType
```kotlin
enum DataType : Enum<Tensor.DataType>
```
Data type enums. 
Members Entries 
## Entries
UINT8 
```kotlin
UINT8
```
unsigned 8-bit integer 
INT8 
```kotlin
INT8
```
signed 8-bit integer 
UINT16 
```kotlin
UINT16
```
unsigned 16-bit integer 
INT16 
```kotlin
INT16
```
signed 16-bit integer 
INT32 
```kotlin
INT32
```
signed 32-bit integer 
FLOAT32 
```kotlin
FLOAT32
```
32-bit floating point 
FLOAT64 
```kotlin
FLOAT64
```
64-bit floating point 
GLTF_BINARY 
```kotlin
GLTF_BINARY
```
Special data tuple: storing the binary content of a glTF asset 
## Types
Image 
```kotlin
enum Image : Enum<Tensor.DataType.Image>
```
Extended data types for tensors to store images or textures. Such a data type can be of multiple channels, such as R8G8B8_U, which means each element in the tensor (in other word, each pixel in the tensor) has 24 bit, as a 3-channel value, where each channel is interpreted as a single 8-bit unsigned integer. 
## Properties
entries 
```kotlin
val entries: EnumEntries<Tensor.DataType>
```
Returns a representation of an immutable list of all enum entries, in the order they're declared. 
## Functions
value Of 
```kotlin
fun valueOf(value: String): Tensor.DataType
```
Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.) 
values 
```kotlin
fun values(): Array<Tensor.DataType>
```
Returns an array containing the constants of this enum type, in the order they're declared.