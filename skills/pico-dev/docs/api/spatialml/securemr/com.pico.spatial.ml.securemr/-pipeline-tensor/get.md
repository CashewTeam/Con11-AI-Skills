# get | PICO Spatial SDK

spatialml:securemr / com.pico.spatial.ml.securemr / PipelineTensor / get 
# get
```kotlin
operator fun get(vararg indices: IntRange): PipelineTensorSlice
```
Create a slice using bracket operators from  IntRange s like  0..5, 1..2 
Note  Cannot be called on tensors of scene graph usage. 
#### Return
the slice of this pipeline tensor corresponding to the  IntRange  array. 
#### Parameters
indices 
the slices on each dimension, must have the same number of IntRange as the number of this tensor's dimensions. 
#### Throws
Spatial MLException 
If the usage is not allowed by the SpatialML run-time Framework, or if the framework encounter internal error and cannot perform the requested behavior. 
```kotlin
operator fun get(vararg indexAndSkips: IntProgression): PipelineTensorSlice
```
Create a slice using bracket operators from IntProgression. Different from the overloaded method that uses  IntRange  as inputs,  IntProgression  allows skip and backward iteration. Similarly, there must be the same number of  IntProgression  inputs as the number of this tensor's dimensions 
Note  Cannot be called on tensors of scene graph usage. 
#### Return
the slice of this pipeline tensor corresponding to the  IntProgression  array. 
#### Parameters
index And Skips 
the slice (start, end and skip) along each dimension. 
#### Throws
Spatial MLException 
If the usage is not allowed by the SpatialML run-time Framework, or if the framework encounter internal error and cannot perform the requested behavior. 
```kotlin
operator fun get(indices: PipelineTensor): PipelineTensorSlice
```
Create a slice using bracket operators from a tensor. This operator overload allows SpatialML framework users to apply tensors output from previous steps as a  dynamic  slices. 
Note  Cannot be called on tensors of scene graph usage. 
#### Return
the slice of this pipeline, using another tensor as the slicing indices. 
#### Parameters
indices 
the slice tensor, must be created using  Tensor.SliceInitInfo . 
#### Throws
Spatial MLException 
If the usage is not allowed by the SpatialML run-time Framework, or if the framework encounter internal error and cannot perform the requested behavior.