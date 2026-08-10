# RunTask | PICO Spatial SDK

spatialml:securemr / com.pico.spatial.ml.securemr / Pipeline / RunTask 
# RunTask
```kotlin
class RunTask(pipeline: Pipeline, placeholderMap: Map<PipelineTensorPlaceholder, GlobalTensor>, condition: GlobalTensor?, waitFor: Pipeline.RunTask?)
```
The handle to one submitted pipeline run task. 
#### Throws
Spatial MLException 
If the usage is not allowed by the SpatialML run-time Framework, or if the framework encounters internal error and cannot perform the requested behavior. 
Members 
## Constructors
Run Task 
```kotlin
constructor(pipeline: Pipeline, placeholderMap: Map<PipelineTensorPlaceholder, GlobalTensor>, condition: GlobalTensor?, waitFor: Pipeline.RunTask?)
```