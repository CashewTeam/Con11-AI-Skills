# get | PICO Spatial SDK

spatialml:securemr / com.pico.spatial.ml.securemr / PipelineTensorSlice / get 
# get
```kotlin
operator fun get(indices: IntRange): PipelineTensorSlice
```
Create a slice on channels using bracket operators from  IntRange  like  1..2 
Note  Cannot be called on tensors of scene graph usage. 
#### Return
reference to this slice, with the channel slice being updated according to the input  IntRange . 
#### Parameters
indices 
the slice channels, must have the same number of IntRange as the number of this tensor's number of channel for each of its pixels. 
#### Throws
Spatial MLException 
If the usage is not allowed by the SpatialML run-time Framework, or if the framework encounters internal error and cannot perform the requested behavior. 
```kotlin
operator fun get(indexAndSkips: IntProgression): PipelineTensorSlice
```
Create a slice on channels using bracket operators from IntProgression. Different from the overloaded method that uses  IntRange  as inputs,  IntProgression  allows skip and backward iteration. Similarly, there must be the same number of  IntProgression  inputs as the number of this tensor's dimensions 
Note  Cannot be called on tensors of scene graph usage. 
#### Return
reference to this slice, with the channel slice being updated according to the input  IntProgression . 
#### Parameters
index And Skips 
the slice (start, end and skip) along each dimension. 
#### Throws
Spatial MLException 
If the usage is not allowed by the SpatialML run-time Framework, or if the framework encounters internal error and cannot perform the requested behavior.