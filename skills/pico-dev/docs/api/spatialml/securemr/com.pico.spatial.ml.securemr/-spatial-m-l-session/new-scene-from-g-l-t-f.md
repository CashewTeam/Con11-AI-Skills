# newSceneFromGLTF | PICO Spatial SDK

spatialml:securemr / com.pico.spatial.ml.securemr / SpatialMLSession / newSceneFromGLTF 
# newSceneFromGLTF
```kotlin
fun newSceneFromGLTF(gltfSceneMemory: SharedMemory): GlobalTensor
```
Create an SpatialML scene from a glTF file already loaded into SharedMemory. 
#### Return
the newly create tensor, which represents the SpatialML scene so that you can use.  Pipeline 's methods to update the scene according to intermedia results in the pipeline. 
#### Parameters
gltf Scene Memory 
The shared memory contains the scene described in glTF format. Callers will be responsible to close the SharedMemory after the return of this method to avoid memory leak. 
#### See also
Global Tensor 
#### Throws
Spatial MLException 
If the usage is not allowed by the SpatialML run-time Framework, or if the framework encounter internal error and cannot perform the requested behavior. 
```kotlin
fun newSceneFromGLTF(gltfSceneAsset: String): GlobalTensor
```
Create an SpatialML scene from a glTF file in asset. 
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