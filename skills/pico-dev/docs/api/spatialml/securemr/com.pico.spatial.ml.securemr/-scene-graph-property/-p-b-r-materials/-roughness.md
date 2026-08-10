# Roughness | PICO Spatial SDK

spatialml:securemr / com.pico.spatial.ml.securemr / SceneGraphProperty / PBRMaterials / Roughness 
# Roughness
```kotlin
val Roughness: SceneGraphProperty
```
Update the roughness property of the PBR material at default index 0. 
If this property is used as the  Pipeline.updateSceneGraphProperty 's  targetProperty  parameter, the  data  tensor parameter must be a single floating-point scalar value, i.e., a tensor declared using  Tensor.FloatArrayInitInfo  or  Tensor.DoubleArrayInitInfo  with size 1 (equivalent to a  Tensor.ScalarInitInfo  with size 1 and datatype =  Tensor.DataType.FLOAT64  or  Tensor.DataType.FLOAT32 , but not recommended).