# SpatialMLSession | PICO Spatial SDK

spatialml:securemr / com.pico.spatial.ml.securemr / SpatialMLSession 
# SpatialMLSession
```kotlin
@RequiresApi(value = 27)
```class  SpatialMLSession  :  BaseHandle 
A handle to each session of SpatialML framework usage. For each session, a dedicated SpatialML container for securely rendering mixed-reality components will be allocated. 
One session handle must be linked to a  SpatialMLInstance , on which the framework session's lifecycle depends. 
#### Parameters
instance 
the  SpatialMLInstance  the session is associated with. 
config 
the configuration during initialization. 
#### Throws
Spatial MLException 
If the usage is not allowed by the SpatialML run-time Framework, or if the framework encounter internal error and cannot perform the requested behavior. 
Members 
## Types
Companion 
```kotlin
object Companion
```
Companion for  SpatialMLSession . 
Init Info 
```kotlin
class InitInfo(val imageWidth: Int, val imageHeight: Int, val containerWidth: Int, val containerHeight: Int, val containerDepth: Int)
```
Configuration structure for framework session handle. 
## Properties
destructor 
```kotlin
open override val destructor: BaseHandle.HandleDestructor
```
The  BaseHandle 's implementation's destructor. 
## Functions
new Global Tensor 
```kotlin
fun newGlobalTensor(config: Tensor.InitInfo): GlobalTensor
```
Create new global tensors within the context of current framework session. 
new Pipeline 
```kotlin
fun newPipeline(): Pipeline
```
Create a new pipeline within the context of current framework session. 
new Scene From GLTF 
```kotlin
fun newSceneFromGLTF(gltfSceneMemory: SharedMemory): GlobalTensor
```
Create an SpatialML scene from a glTF file already loaded into SharedMemory. 
```kotlin
fun newSceneFromGLTF(gltfSceneAsset: String): GlobalTensor
```
Create an SpatialML scene from a glTF file in asset. 
new Scene From GLTFSuspend 
```kotlin
suspend fun newSceneFromGLTFSuspend(gltfSceneAsset: String): GlobalTensor
```
Async version of  newSceneFromGLTF .