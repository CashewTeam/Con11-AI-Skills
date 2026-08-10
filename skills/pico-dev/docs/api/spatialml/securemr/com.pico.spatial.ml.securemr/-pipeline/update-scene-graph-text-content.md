# updateSceneGraphTextContent | PICO Spatial SDK

spatialml:securemr / com.pico.spatial.ml.securemr / Pipeline / updateSceneGraphTextContent 
# updateSceneGraphTextContent
```kotlin
fun updateSceneGraphTextContent(sceneEntity: Tensor, entityPath: String, text: String)
```
Update data of text content of a text component in the scene graph using a text String. 
This is equivalent to 

```
pipeline.updateSceneGraphProperty(        sceneEntity,        entityPath,        SceneGraphProperty.Text.Content,        newLocalTensor(text))
```
#### Parameters
scene Entity 
the scene-graph tensor to be updated. Must be a scene-graph tensor. 
entity Path 
the path to the entity within the scene graph whose component will be updated. A valid path always starts with  /  and will be in form like  /entity/childEntity/grandchildEntity/... , where  entity ,  childEntity ,  grandchildEntity  are all entity names in the scene graph. A single  /  refers to the entire scene entity. 
text 
the text string to update the text component's text content. Internally, the string will be converted to a scalar array  PipelineTensorLocal  of  Tensor.DataType.UINT8 . 
#### Throws
Spatial MLException 
If the usage is not allowed by the SpatialML run-time Framework, or if the framework encounters internal error and cannot perform the requested behavior.