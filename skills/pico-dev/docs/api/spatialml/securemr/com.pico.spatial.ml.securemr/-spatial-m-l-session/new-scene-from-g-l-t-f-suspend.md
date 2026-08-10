# newSceneFromGLTFSuspend | PICO Spatial SDK

spatialml:securemr / com.pico.spatial.ml.securemr / SpatialMLSession / newSceneFromGLTFSuspend 
# newSceneFromGLTFSuspend
```kotlin
suspend fun newSceneFromGLTFSuspend(gltfSceneAsset: String): GlobalTensor
```
Async version of  newSceneFromGLTF . 
#### Return
the newly create tensor, which represents the SpatialML scene so that you can use  Pipeline 's methods to update the scene according to intermedia results in the pipeline. 
#### Parameters
gltf Scene Asset 
The path in the app's asset to the glTF file. 
#### Throws
IOException 
when file is failed to be read as a scene. 
Spatial MLException 
If the usage is not allowed by the SpatialML run-time Framework, or if the framework encounter internal error and cannot perform the requested behavior.