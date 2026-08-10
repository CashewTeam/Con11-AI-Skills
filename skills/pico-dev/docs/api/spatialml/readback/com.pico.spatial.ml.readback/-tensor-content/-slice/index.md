# Slice | PICO Spatial SDK

spatialml:readback / com.pico.spatial.ml.readback / TensorContent / Slice 
# Slice
```kotlin
class Slice(content: TensorContent, range: IntRange)
```
A handy class to easily read a range of the tensor's content. 
#### Parameters
content 
the tensor content. 
range 
which range of tensor's content will be read. 
Members 
## Constructors
Slice 
```kotlin
constructor(content: TensorContent, range: IntRange)
```
## Functions
as Byte Array 
```kotlin
fun asByteArray(): ByteArray
```
Ready the selected range from the tensor as  Byte s. The tensor must be a of  Tensor.DataType.INT8 , otherwise you cannot read its content as  ByteArray . 
as Double Array 
```kotlin
fun asDoubleArray(): DoubleArray
```
Ready the selected range from the tensor as doubles. The tensor must be a of  Tensor.DataType.FLOAT64 , otherwise you cannot read its content as  DoubleArray . 
as Float Array 
```kotlin
fun asFloatArray(): FloatArray
```
Ready the selected range from the tensor as floats. The tensor must be a of  Tensor.DataType.FLOAT32 , otherwise you cannot read its content as  FloatArray . 
as Int Array 
```kotlin
fun asIntArray(): IntArray
```
Ready the selected range from the tensor as integers. The tensor must be a of  Tensor.DataType.INT32 , otherwise you cannot read its content as  IntArray . 
as Short Array 
```kotlin
fun asShortArray(): ShortArray
```
Ready the selected range from the tensor as  Short s. The tensor must be a of  Tensor.DataType.INT16 , otherwise you cannot read its content as  ShortArray .