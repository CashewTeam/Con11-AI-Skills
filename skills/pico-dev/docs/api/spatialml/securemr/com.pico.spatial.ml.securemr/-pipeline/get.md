# get | PICO Spatial SDK

spatialml:securemr / com.pico.spatial.ml.securemr / Pipeline / get 
# get
```kotlin
operator fun GlobalTensor.get(vararg indices: IntRange): PipelineTensorSlice
```
Convenient method to directly create a slice of a GlobalTensor using bracket operators from  IntRange s like  0..5, 1..2 . 
Note  Cannot be called on tensors of scene graph usage. 
#### Return
the slice of this pipeline tensor corresponding to the  IntRange  array. 
#### Parameters
indices 
the slices on each dimension, must have the same number of IntRange as the number of this tensor's dimensions. 
#### See also
Pipeline Tensor. get 
#### Throws
Spatial MLException 
If the usage is not allowed by the SpatialML run-time Framework, or if the framework encounters internal error and cannot perform the requested behavior. 
```kotlin
operator fun GlobalTensor.get(vararg indexAndSkips: IntProgression): PipelineTensorSlice
```
Convenient method to directly create a slice of a GlobalTensor using bracket operators from  IntProgression . Different from the overloaded method that uses  IntRange  as inputs,  IntProgression  allows skip and backward iteration. Similarly, there must be the same number of  IntProgression  inputs as the number of this tensor's dimensions 
Note  Cannot be called on tensors of scene graph usage. 
#### Return
the slice of this pipeline tensor corresponding to the  IntProgression  array. 
#### Parameters
index And Skips 
the slice (start, end and skip) along each dimension. 
#### See also
Pipeline Tensor. get 
#### Throws
Spatial MLException 
If the usage is not allowed by the SpatialML run-time Framework, or if the framework encounters internal error and cannot perform the requested behavior. 
```kotlin
operator fun GlobalTensor.get(indices: PipelineTensor): PipelineTensorSlice
```
Convenient method to directly create a slice of a GlobalTensor using bracket operators from a tensor. This operator overload allows SpatialML framework users to apply tensors output from previous steps as a  dynamic  slices. 
Note  Cannot be called on tensors of scene graph usage. 
#### Return
the slice of this pipeline, using another tensor as the slicing indices. 
#### Parameters
indices 
the slice tensor, must be created using  Tensor.SliceInitInfo . 
#### See also
Pipeline Tensor. get 
#### Throws
Spatial MLException 
If the usage is not allowed by the SpatialML run-time Framework, or if the framework encounters internal error and cannot perform the requested behavior. 
```kotlin
operator fun PipelineTensorSlice.get(channelSliceTensor: Tensor): PipelineTensorSlice
```
Create a slice on channels using bracket operators from a slice tensor. 
Note  Cannot be called on tensors of scene graph usage. 
#### Return
reference to this slice, with the channel slice being updated according to the input  IntRange . 
#### Parameters
channel Slice Tensor 
the slice tensor onto channels, which should be a tensor created using  Tensor.SliceInitInfo . Its content should specify which channels of the original tensor's pixels will be taken. 
#### Throws
Spatial MLException 
If the usage is not allowed by the SpatialML run-time Framework, or if the framework encounters internal error and cannot perform the requested behavior.