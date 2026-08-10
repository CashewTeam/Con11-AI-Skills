# PipelineTensorSlice | PICO Spatial SDK

spatialml:securemr / com.pico.spatial.ml.securemr / PipelineTensorSlice / PipelineTensorSlice 
# PipelineTensorSlice
```kotlin
constructor(originTensor: PipelineTensor, sliceTensor: PipelineTensor)
```
#### Parameters
origin Tensor 
the original tensor to be sliced, i.e., element source. 
slice Tensor 
the slice tensor on dimensions. 
```kotlin
constructor(originalTensor: PipelineTensor, indexAndSkips: Array<out IntProgression>)
```
Create an slice onto a tensor from Kotlin's IntRanges, with an integer as the skip, rather than a pre-define  Tensor  of slice usage. With this constructor, you can easily create a slice from Kotlin's  IntProgression . 
#### Parameters
original Tensor 
the tensor as slice source. 
index And Skips 
the slice with  IntProgression  for start, end and skip on each dimension of the  originalTensor . 
#### Throws
Spatial MLException 
If the usage is not allowed by the SpatialML run-time Framework, or if the framework encounters internal error and cannot perform the requested behavior. 
```kotlin
constructor(originalTensor: PipelineTensor, indices: Array<out IntRange>)
```
Create an slice onto a tensor from Kotlin's IntRanges, rather than a pre-defined  Tensor  of slice usage. With this constructor, you can easily create a slice of an existing tensor using  originTensor[0..5, 0..-1]  etc. 
#### Parameters
original Tensor 
the tensor as slice source. 
indices 
the slices (start and end) for each dimension on the  originalTensor . 
#### Throws
Spatial MLException 
If the usage is not allowed by the SpatialML run-time Framework, or if the framework encounters internal error and cannot perform the requested behavior.