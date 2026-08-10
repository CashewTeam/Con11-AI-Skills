# newPipeline | PICO Spatial SDK

spatialml:securemr / com.pico.spatial.ml.securemr / SpatialMLSession / newPipeline 
# newPipeline
```kotlin
fun newPipeline(): Pipeline
```
Create a new pipeline within the context of current framework session. 
#### Return
the newly created Pipeline handle, to which you can hook pipeline tensors and operators to implement complex algorithms. 
#### See also
Pipeline 
#### Throws
Spatial MLException 
If the usage is not allowed by the SpatialML run-time Framework, or if the framework encounter internal error and cannot perform the requested behavior.