# ColorType | PICO Spatial SDK

spatialml:securemr / com.pico.spatial.ml.securemr / Tensor / ColorType 
# ColorType
```kotlin
enum ColorType : Enum<Tensor.ColorType>
```
The color type (combining  DataType  and number of channels) used to define a color array. 
#### See also
Tensor. Color Array Init Info Members Entries 
## Entries
R8G8B8_UINT 
```kotlin
R8G8B8_UINT
```
UINT8 3-channel (RGB) color type 
R16G16B16_UINT 
```kotlin
R16G16B16_UINT
```
UINT16 3-channel (RGB) color type 
R32G32B32_FLOAT 
```kotlin
R32G32B32_FLOAT
```
Single-precision float 3-channel (RGB) color type 
R64G64B64_FLOAT 
```kotlin
R64G64B64_FLOAT
```
Double-precision float 3-channel (RGB) color type 
R8G8B8A8_UINT 
```kotlin
R8G8B8A8_UINT
```
UINT8 4-channel (RGBA) color type 
R16G16B16A16_UINT 
```kotlin
R16G16B16A16_UINT
```
UINT16 4-channel (RGBA) color type 
R32G32B32A32_FLOAT 
```kotlin
R32G32B32A32_FLOAT
```
Single-precision float 4-channel (RGBA) color type 
R64G64B64A64_FLOAT 
```kotlin
R64G64B64A64_FLOAT
```
Double-precision float 4-channel (RGBA) color type 
## Properties
entries 
```kotlin
val entries: EnumEntries<Tensor.ColorType>
```
Returns a representation of an immutable list of all enum entries, in the order they're declared. 
## Functions
value Of 
```kotlin
fun valueOf(value: String): Tensor.ColorType
```
Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.) 
values 
```kotlin
fun values(): Array<Tensor.ColorType>
```
Returns an array containing the constants of this enum type, in the order they're declared.