# PipelineTensor | PICO Spatial SDK

spatialml:securemr / com.pico.spatial.ml.securemr / PipelineTensor 
# PipelineTensor
```kotlin
@RequiresApi(value = 27)
```abstract  class  PipelineTensor ( val  rootPipeline :  Pipeline ,  hasMemory :  Boolean ,  config :  Tensor.InitInfo )  :  Tensor 
A PipelineTensor is a tensor that is bound to a  Pipeline . It has the same lifecycle as the  Pipeline  it is subordinate to. Depending on whether it has local memory, it can categorized into two subclasses:  PipelineTensorLocal  or  PipelineTensorPlaceholder . The former has local memory allocated to it, while the latter has no underlying memory, and works as a run-time reference. 
#### Parameters
root Pipeline 
the pipeline in which the tensor is created. 
has Memory 
whether the tensor should have local memory allocated inside the pipeline If true, the tensor is regarded as a pipeline local tensor; otherwise, a pipeline placeholder, which is accessible inside the pipeline, but must refer to a compatible global tensor when the pipeline is submitted for run. 
config 
the tensor's configuration. 
#### See also
Pipeline Tensor Local Pipeline Tensor Placeholder 
#### Throws
Spatial MLException 
If the usage is not allowed by the SpatialML run-time Framework, or if the framework encounter internal error and cannot perform the requested behavior. 
#### Inheritors
PipelineTensorLocal PipelineTensorPlaceholder Members 
## Constructors
Pipeline Tensor 
```kotlin
constructor(rootPipeline: Pipeline, hasMemory: Boolean, config: Tensor.InitInfo)
```
## Properties
root Pipeline 
```kotlin
val rootPipeline: Pipeline
```
## Functions
get 
```kotlin
operator fun get(indices: PipelineTensor): PipelineTensorSlice
```
Create a slice using bracket operators from a tensor. This operator overload allows SpatialML framework users to apply tensors output from previous steps as a  dynamic  slices. 
```kotlin
operator fun get(vararg indexAndSkips: IntProgression): PipelineTensorSlice
```
Create a slice using bracket operators from IntProgression. Different from the overloaded method that uses  IntRange  as inputs,  IntProgression  allows skip and backward iteration. Similarly, there must be the same number of  IntProgression  inputs as the number of this tensor's dimensions 
```kotlin
operator fun get(vararg indices: IntRange): PipelineTensorSlice
```
Create a slice using bracket operators from  IntRange s like  0..5, 1..2 
reset Tensor Value 
```kotlin
protected open override fun resetTensorValue()
```
Callback when the tensor resource is reset