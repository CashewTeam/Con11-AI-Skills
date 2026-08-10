# submit | PICO Spatial SDK

spatialml:securemr / com.pico.spatial.ml.securemr / Pipeline / submit 
# submit
```kotlin
fun submit(parameters: Map<PipelineTensorPlaceholder, GlobalTensor>, condition: GlobalTensor?, waitFor: Pipeline.RunTask?): Pipeline.RunTask
```
Submit the pipeline for  one  run. Note: the method only submits the run as a task, and SpatialML framework will schedule the task based on its  waitFor  task, the  GlobalTensor  it will access, and the current computation resource availability. 
#### Return
the  RunTask  handle representing the submitted pipeline run, which can be used as the  waitFor  parameter of another pipeline submission. 
#### Parameters
parameters 
the mapping from the pipeline's local  PipelineTensorPlaceholder s to the referred  GlobalTensor s. The mapping is the parameters of this run, and will only be valid for this run. This allows you to change the tensors as parameters for different pipeline runs to reuse the same pipeline for different inputs/outputs. 
condition 
the condition tensor, when the pipeline is about to run, if the condition tensor is false (i.e., all zero), the run will be aborted. 
wait For 
the predecessor pipeline run this pipeline run must wait. Only the  waitFor  pipeline run is ended or aborted, can this pipeline run be executed.  Note  the  waitFor  pipeline run must be a  RunTask  submitted from another  Pipeline , because the run tasks  always  wait for the previous tasks submitted from the same pipeline. 
#### Throws
Spatial MLException 
If the usage is not allowed by the SpatialML run-time Framework, or if the framework encounters internal error and cannot perform the requested behavior.