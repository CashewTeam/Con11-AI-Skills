# newSceneFromGLTF | PICO Spatial SDK

spatialml:securemr / com.pico.spatial.ml.securemr / Pipeline / newSceneFromGLTF 
# newSceneFromGLTF
```kotlin
fun newSceneFromGLTF(gltfSceneMemory: SharedMemory): PipelineTensor
```
Create an SpatialML scene from a glTF file already loaded into SharedMemory. Similar to  SpatialMLSession.newSceneFromGLTF  but that one creates a global scene graph handle, so that multiple pipelines can share, whereas this method creates one scene graph local to the pipeline only. 
#### Return
the newly create tensor, which represents the SpatialML scene so that you can use  Pipeline 's methods to update the scene according to intermedia results in the pipeline. 
#### Parameters
gltf Scene Memory 
The shared memory contains the scene described in glTF format. Callers will be responsible to close the SharedMemory after the return of this method to avoid memory leak. 
#### See also
Spatial MLSession. new Scene From GLTF 
#### Throws
Spatial MLException 
If the usage is not allowed by the SpatialML run-time Framework, or if the framework encounters internal error and cannot perform the requested behavior.