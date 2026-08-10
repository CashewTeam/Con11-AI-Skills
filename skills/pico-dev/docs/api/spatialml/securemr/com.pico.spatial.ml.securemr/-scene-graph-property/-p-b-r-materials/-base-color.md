# BaseColor | PICO Spatial SDK

spatialml:securemr / com.pico.spatial.ml.securemr / SceneGraphProperty / PBRMaterials / BaseColor 
# BaseColor
```kotlin
val BaseColor: SceneGraphProperty
```
Update the base color property of the PBR material at default index 0. 
If this property is used as the  Pipeline.updateSceneGraphProperty 's  targetProperty  parameter, the  data  tensor parameter must be a single color value, i.e., a tensor declared using  Tensor.ColorArrayInitInfo  with size = 1.