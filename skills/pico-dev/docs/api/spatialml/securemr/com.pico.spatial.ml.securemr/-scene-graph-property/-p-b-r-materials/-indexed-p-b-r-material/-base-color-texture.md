# BaseColorTexture | PICO Spatial SDK

spatialml:securemr / com.pico.spatial.ml.securemr / SceneGraphProperty / PBRMaterials / IndexedPBRMaterial / BaseColorTexture 
# BaseColorTexture
```kotlin
val BaseColorTexture: SceneGraphProperty
```
Update the base color texture property of the PBR material at specified  index . 
If this property is used as the  Pipeline.updateSceneGraphProperty 's  targetProperty  parameter, the  data  tensor parameter must be a multi-dimensional tensor, whose  dynamicTexture  is set to be  True  when the tensor is initialized.