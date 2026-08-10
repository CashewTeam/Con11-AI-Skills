# updateSceneGraphTextVerticalAlignment | PICO Spatial SDK

spatialml:securemr / com.pico.spatial.ml.securemr / Pipeline / updateSceneGraphTextVerticalAlignment 
# updateSceneGraphTextVerticalAlignment
```kotlin
fun updateSceneGraphTextVerticalAlignment(sceneEntity: Tensor, entityPath: String, verticalAlignment: Pipeline.TextVerticalAlignment)
```
Update data of vertical alignment of a text component in the scene graph using the alignment enum defined in  TextVerticalAlignment . 
This is equivalent to use the  updateSceneGraphProperty  with  targetProperty = SceneGraphProperty.Text.VerticalAlignment  and  data  being the a tensor carrying corresponding enum values. 
#### Parameters
scene Entity 
the scene-graph tensor to be updated. Must be a scene-graph tensor. 
entity Path 
the path to the entity within the scene graph whose component will be updated. A valid path always starts with  /  and will be in form like  /entity/childEntity/grandchildEntity/... , where  entity ,  childEntity ,  grandchildEntity  are all entity names in the scene graph. A single  /  refers to the entire scene entity. 
vertical Alignment 
the alignment enum to update the text component. 
#### Throws
Spatial MLException 
If the usage is not allowed by the SpatialML run-time Framework, or if the framework encounters internal error and cannot perform the requested behavior.