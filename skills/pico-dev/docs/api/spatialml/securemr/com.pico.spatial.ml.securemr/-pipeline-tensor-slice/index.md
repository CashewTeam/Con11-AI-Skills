# PipelineTensorSlice | PICO Spatial SDK

spatialml:securemr / com.pico.spatial.ml.securemr / PipelineTensorSlice 
# PipelineTensorSlice
```kotlin
@RequiresApi(value = 27)
```class  PipelineTensorSlice ( originTensor :  PipelineTensor ,  sliceTensor :  PipelineTensor ) 
A wrapper of the pipeline tensor, with a slice onto this tensor. The slice must be a tensor of SLICE_ARRAY usage. 
Note  this data structure is just a wrap for the convenience of taking slices from tensors, it does not really create tensor copy until you call  toPipelineTensor  or used it as an input to  Pipeline.copy  method. 
#### Parameters
origin Tensor 
the original tensor to be sliced, i.e., element source. 
slice Tensor 
the slice tensor on dimensions. 
#### Throws
Spatial MLException 
if the pipeline of the two tensors are not the same. 
Members 
## Constructors
Pipeline Tensor Slice 
```kotlin
constructor(originTensor: PipelineTensor, sliceTensor: PipelineTensor)
```
```kotlin
constructor(originalTensor: PipelineTensor, indexAndSkips: Array<out IntProgression>)
```
Create an slice onto a tensor from Kotlin's IntRanges, with an integer as the skip, rather than a pre-define  Tensor  of slice usage. With this constructor, you can easily create a slice from Kotlin's  IntProgression . 
```kotlin
constructor(originalTensor: PipelineTensor, indices: Array<out IntRange>)
```
Create an slice onto a tensor from Kotlin's IntRanges, rather than a pre-defined  Tensor  of slice usage. With this constructor, you can easily create a slice of an existing tensor using  originTensor[0..5, 0..-1]  etc. 
## Functions
get 
```kotlin
operator fun get(indexAndSkips: IntProgression): PipelineTensorSlice
```
Create a slice on channels using bracket operators from IntProgression. Different from the overloaded method that uses  IntRange  as inputs,  IntProgression  allows skip and backward iteration. Similarly, there must be the same number of  IntProgression  inputs as the number of this tensor's dimensions 
```kotlin
operator fun get(indices: IntRange): PipelineTensorSlice
```
Create a slice on channels using bracket operators from  IntRange  like  1..2 
to Pipeline Tensor 
```kotlin
fun toPipelineTensor(config: Tensor.InitInfo): PipelineTensor
```
A convenient way to copy elements from a slice to an intermedia tensor, to be used by other pipeline method.