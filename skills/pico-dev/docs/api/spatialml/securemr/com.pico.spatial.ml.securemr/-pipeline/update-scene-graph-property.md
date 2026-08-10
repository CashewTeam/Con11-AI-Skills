# updateSceneGraphProperty | PICO Spatial SDK

spatialml:securemr / com.pico.spatial.ml.securemr / Pipeline / updateSceneGraphProperty 
# updateSceneGraphProperty
```kotlin
fun updateSceneGraphProperty(sceneEntity: Tensor, entityPath: String, targetProperty: SceneGraphProperty, data: Tensor)
```
Update data of a specified component property in the scene graph, using the values from a tensor. 
#### Parameters
scene Entity 
the scene-graph tensor to be updated. Must be a scene-graph tensor. 
entity Path 
the path to the entity within the scene graph whose component will be updated. A valid path always starts with  /  and will be in form like  /entity/childEntity/grandchildEntity/... , where  entity ,  childEntity ,  grandchildEntity  are all entity names in the scene graph. A single  /  refers to the entire scene entity. 
target Property 
specifying which component property of the target entity specified by  entityPath  will be updated by this operator. 
data 
the tensor whose data will be used to update the specified component field. Each different target component may have different requirements on the  data . You may refer to  SceneGraphProperty 's documentation for detailed compatibility. 
#### Throws
Spatial MLException 
If the usage is not allowed by the SpatialML run-time Framework, or if the framework encounters internal error and cannot perform the requested behavior.