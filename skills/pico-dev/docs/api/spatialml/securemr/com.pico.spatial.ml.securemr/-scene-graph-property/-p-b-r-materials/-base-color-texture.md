# BaseColorTexture | PICO Spatial SDK

spatialml:securemr / com.pico.spatial.ml.securemr / SceneGraphProperty / PBRMaterials / BaseColorTexture 
# BaseColorTexture
```kotlin
val BaseColorTexture: SceneGraphProperty
```
Update the base color texture property of the PBR material at index 0. 
If this property is used as the  Pipeline.updateSceneGraphProperty 's  targetProperty  parameter, the  data  tensor parameter must be a multi-dimensional tensor, whose  dynamicTexture  is set to be  True  when the tensor is initialized.