# PipelineTensor | PICO Spatial SDK

spatialml:securemr / com.pico.spatial.ml.securemr / PipelineTensor / PipelineTensor 
# PipelineTensor
```kotlin
constructor(rootPipeline: Pipeline, hasMemory: Boolean, config: Tensor.InitInfo)
```
#### Parameters
root Pipeline 
the pipeline in which the tensor is created. 
has Memory 
whether the tensor should have local memory allocated inside the pipeline If true, the tensor is regarded as a pipeline local tensor; otherwise, a pipeline placeholder, which is accessible inside the pipeline, but must refer to a compatible global tensor when the pipeline is submitted for run. 
config 
the tensor's configuration.