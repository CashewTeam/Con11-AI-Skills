# Image | PICO Spatial SDK

spatialml:securemr / com.pico.spatial.ml.securemr / Tensor / DataType / Image 
# Image
```kotlin
enum Image : Enum<Tensor.DataType.Image>
```
Extended data types for tensors to store images or textures. Such a data type can be of multiple channels, such as R8G8B8_U, which means each element in the tensor (in other word, each pixel in the tensor) has 24 bit, as a 3-channel value, where each channel is interpreted as a single 8-bit unsigned integer. 
Members Entries 
## Entries
R8_U 
```kotlin
R8_U
```
8-bit pixel, interpreted as one unsigned integer value only. 
R8_U_DYNAMIC 
```kotlin
R8_U_DYNAMIC
```
8-bit pixel, interpreted as one unsigned integer value only. 
R8G8_U 
```kotlin
R8G8_U
```
16-bit pixel, interpreted as two 8-bit unsigned integer value (8 bits for RED, 8 bits for GREEN). 
R8G8_U_DYNAMIC 
```kotlin
R8G8_U_DYNAMIC
```
16-bit pixel, interpreted as two 8-bit unsigned integer value (8 bits for RED, 8 bits for GREEN). 
R8G8B8_U 
```kotlin
R8G8B8_U
```
24-bit pixel, interpreted as three 8-bit unsigned integer value (8 bits for RED, 8 bits for GREEN and 8 bits for BLUE). 
R8G8B8_U_DYNAMIC 
```kotlin
R8G8B8_U_DYNAMIC
```
24-bit pixel, interpreted as three 8-bit unsigned integer value (8 bits for RED, 8 bits for GREEN and 8 bits for BLUE). 
R8G8B8A8_U 
```kotlin
R8G8B8A8_U
```
32-bit pixel, interpreted as four 8-bit unsigned integer value (8 bits for RED, 8 bits for GREEN, 8 bits for BLUE and 8 bits for ALPHA). 
R8G8B8A8_U_DYNAMIC 
```kotlin
R8G8B8A8_U_DYNAMIC
```
32-bit pixel, interpreted as four 8-bit unsigned integer value (8 bits for RED, 8 bits for GREEN, 8 bits for BLUE and 8 bits for ALPHA). 
R16_U 
```kotlin
R16_U
```
16-bit pixel, interpreted as one unsigned integer value only. 
R16G16_U 
```kotlin
R16G16_U
```
32-bit pixel, interpreted as two 16-bit unsigned integer value (16 bits for RED, 16 bits for GREEN). 
R16G16B16_U 
```kotlin
R16G16B16_U
```
48-bit pixel, interpreted as three 16-bit unsigned integer value (16 bits for RED, 16 bits for GREEN and 16 bits for BLUE). 
R16G16B16A16_U 
```kotlin
R16G16B16A16_U
```
64-bit pixel, interpreted as four 16-bit unsigned integer value (16 bits for RED, 16 bits for GREEN, 16 bits for BLUE and 16 bits for ALPHA). 
R8_S 
```kotlin
R8_S
```
8-bit pixel, interpreted as one signed integer value only. 
R8G8_S 
```kotlin
R8G8_S
```
16-bit pixel, interpreted as two 8-bit signed integer value (8 bits for RED, 8 bits for GREEN). 
R8G8B8_S 
```kotlin
R8G8B8_S
```
24-bit pixel, interpreted as three 8-bit signed integer value (8 bits for RED, 8 bits for GREEN and 8 bits for BLUE). 
R8G8B8A8_S 
```kotlin
R8G8B8A8_S
```
32-bit pixel, interpreted as four 8-bit signed integer value (8 bits for RED, 8 bits for GREEN, 8 bits for BLUE and 8 bits for ALPHA). 
R16_S 
```kotlin
R16_S
```
16-bit pixel, interpreted as one signed integer value only. 
R16G16_S 
```kotlin
R16G16_S
```
32-bit pixel, interpreted as two 16-bit signed integer value (16 bits for RED, 16 bits for GREEN). 
R16G16B16_S 
```kotlin
R16G16B16_S
```
48-bit pixel, interpreted as three 16-bit signed integer value (16 bits for RED, 16 bits for GREEN and 16 bits for BLUE). 
R16G16B16A16_S 
```kotlin
R16G16B16A16_S
```
64-bit pixel, interpreted as four 16-bit signed integer value (16 bits for RED, 16 bits for GREEN, 16 bits for BLUE and 16 bits for ALPHA). 
R32_S 
```kotlin
R32_S
```
32-bit pixel, interpreted as one signed integer value only. 
R32G32_S 
```kotlin
R32G32_S
```
64-bit pixel, interpreted as two 32-bit signed integer value (32 bits for RED, 32 bits for GREEN). 
R32G32B32_S 
```kotlin
R32G32B32_S
```
96-bit pixel, interpreted as three 32-bit signed integer value (32 bits for RED, 32 bits for GREEN and 8 bits for BLUE). 
R32G32B32A32_S 
```kotlin
R32G32B32A32_S
```
108-bit pixel, interpreted as four 32-bit signed integer value (32 bits for RED, 32 bits for GREEN, 32 bits for BLUE and 32 bits for ALPHA). 
R_FLOAT 
```kotlin
R_FLOAT
```
32-bit pixel, interpreted as one single-precision floating-point value only. 
R_FLOAT_DYNAMIC 
```kotlin
R_FLOAT_DYNAMIC
```
32-bit pixel, interpreted as one single-precision floating-point value only. 
RG_FLOAT 
```kotlin
RG_FLOAT
```
64-bit pixel, interpreted as two 32-bit single-precision floating-point value (32 bits for RED, 32 bits for GREEN). 
RGB_FLOAT 
```kotlin
RGB_FLOAT
```
96-bit pixel, interpreted as three 32-bit single-precision floating-point value (32 bits for RED, 32 bits for GREEN and 32 bits for BLUE). 
RGBA_FLOAT 
```kotlin
RGBA_FLOAT
```
108-bit pixel, interpreted as four 32-bit single-precision floating-point value (32 bits for RED, 32 bits for GREEN, 32 bits for BLUE and 32 bits for ALPHA). 
R_DOUBLE 
```kotlin
R_DOUBLE
```
64-bit pixel, interpreted as one double-precision floating-point value only. 
RG_DOUBLE 
```kotlin
RG_DOUBLE
```
128-bit pixel, interpreted as two 64-bit double-precision floating-point value (64 bits for RED, 32 bits for GREEN). 
RGB_DOUBLE 
```kotlin
RGB_DOUBLE
```
192-bit pixel, interpreted as three 64-bit double-precision floating-point value (64 bits for RED, 64 bits for GREEN and 64 bits for BLUE). 
RGBA_DOUBLE 
```kotlin
RGBA_DOUBLE
```
256-bit pixel, interpreted as four 64-bit double-precision floating-point value (64 bits for RED, 64 bits for GREEN, 8 bits for BLUE and 64 bits for ALPHA). 
## Properties
entries 
```kotlin
val entries: EnumEntries<Tensor.DataType.Image>
```
Returns a representation of an immutable list of all enum entries, in the order they're declared. 
## Functions
value Of 
```kotlin
fun valueOf(value: String): Tensor.DataType.Image
```
Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.) 
values 
```kotlin
fun values(): Array<Tensor.DataType.Image>
```
Returns an array containing the constants of this enum type, in the order they're declared.