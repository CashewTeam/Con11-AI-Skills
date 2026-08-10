# RoughnessTexture | PICO Spatial SDK

spatialml:securemr / com.pico.spatial.ml.securemr / SceneGraphProperty / PBRMaterials / IndexedPBRMaterial / RoughnessTexture 
# RoughnessTexture
```kotlin
val RoughnessTexture: SceneGraphProperty
```
Update the roughness property of the PBR material at specified  index . 
If this property is used as the  Pipeline.updateSceneGraphProperty 's  targetProperty  parameter, the  data  tensor parameter must be a multi-dimensional tensor, whose  dynamicTexture  is set to be  True  when the tensor is initialized. 
Additionally, as the tensor is used as the roughness texture, its pixels should each only have one channel.