# switchSceneVisibility | PICO Spatial SDK

spatialml:securemr / com.pico.spatial.ml.securemr / Pipeline / switchSceneVisibility 
# switchSceneVisibility
```kotlin
fun switchSceneVisibility(sceneEntity: Tensor, visible: Tensor)
```
Control the visibility of an already-loaded scene graph tensor. 
#### Parameters
scene Entity 
the scene-graph tensor to be controlled. Must be a scene-graph tensor. 
visible 
a tensor to control the visibility. If it is evaluated to be true, the scene graph will be visible in the SpatialML container. Otherwise, invisible from the SpatialML container. The tensor will be regarded as true if 
- 
it is a scene-graph tensor containing a successfully loaded scene graph, or 
- 
it is a tensor which contains non-zero bytes. 
#### Throws
Spatial MLException 
If the usage is not allowed by the SpatialML run-time Framework, or if the framework encounters internal error and cannot perform the requested behavior.