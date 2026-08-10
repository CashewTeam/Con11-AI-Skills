# TensorUsage | PICO Spatial SDK

spatialml:securemr / com.pico.spatial.ml.securemr / Tensor / TensorUsage 
# TensorUsage
```kotlin
enum TensorUsage : Enum<Tensor.TensorUsage>
```
Enum to declare tensor's usage. By default, the tensor shall all be of multi-dimensional usage, which creates non-structured data arrays. Such a tensor observes the conventional definition of tensors in linear algebra, where the values it contains are non-structured. 
Tensors of other usage types extend the use scenarios of tensor objects, from conventional mathematics and physics applications to a general abstraction of any structured data in Spatial SecureMR. Here, we say the data of these tensors with  extended definitions  are "structured", as values at different indices inside the tensor are assigned with different meanings and subject to pre-determined limitations. 
For example, a tensor of POINT usage will have two/three values per element: meaning the X, Y (and Z) components respective. Similarly, a tensor of COLOR usage will have three/four values per element instead, storing R, G, B (and A) components. 
NOTE  Nevertheless, you are not suppose to use these enums directly. Instead, you will find the subclasses of  InitInfo  handy. 
#### See also
Tensor. InitInfo Tensor. Multi Dimensional Init Info Tensor. Special Usage Init Info Tensor. Point2Array Init Info Tensor. Point3Array Init Info Tensor. Scalar Init Info Tensor. Slice Init Info Tensor. Time Stamp Init Info Tensor. Scene Graph Init Info Tensor. Color Array Init Info Members Entries 
## Entries
MULTI_DIMENSIONAL 
```kotlin
MULTI_DIMENSIONAL
```
Multi-dimensional usage, i.e., tensors under mathematics or physics definition 
POINT 
```kotlin
POINT
```
A point array tensor, the data in the tensor will be interpreted as an array of 2D or 3D points. 
SCALAR_ARRAY 
```kotlin
SCALAR_ARRAY
```
A scalar array, the data in the tensor will be regarded as an array of scalars, useful for indices, counters, etc. 
SLICE 
```kotlin
SLICE
```
A slice array, the data in the tensor will be interpreted as an array of 
COLORS 
```kotlin
COLORS
```
A color array, the data in the tensor will be interpreted as an array of 
TIMESTAMP 
```kotlin
TIMESTAMP
```
A timestamp 
SCENE_GRAPH 
```kotlin
SCENE_GRAPH
```
The data in the tensor shall be interpreted as numerical values, but as a structured scene graph. 
## Properties
entries 
```kotlin
val entries: EnumEntries<Tensor.TensorUsage>
```
Returns a representation of an immutable list of all enum entries, in the order they're declared. 
## Functions
value Of 
```kotlin
fun valueOf(value: String): Tensor.TensorUsage
```
Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.) 
values 
```kotlin
fun values(): Array<Tensor.TensorUsage>
```
Returns an array containing the constants of this enum type, in the order they're declared.