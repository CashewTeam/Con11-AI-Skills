# Transform | PICO Spatial SDK

spatialml:securemr / com.pico.spatial.ml.securemr / SceneGraphProperty / Transform 
# Transform
```kotlin
sealed class Transform : SceneGraphProperty
```
Update a property of one entity's TransformComponent. 
#### Parameters
property 
the name of the property. 
#### Inheritors
Position Rotation Scale LocalMatrix Members 
## Types
Local Matrix 
```kotlin
object LocalMatrix : SceneGraphProperty.Transform
```
Update the local matrix property of one entity's transform. If this property is used as the  Pipeline.updateSceneGraphProperty 's  targetProperty  parameter, the  data  tensor parameter must be: a multi-dimensional tensor of 2 dimensions:  4x4 , with  datatype  declared as  Tensor.DataType.FLOAT32 ,  Tensor.DataType.FLOAT64 ,  Tensor.DataType.Image.R_FLOAT ,  Tensor.DataType.Image.R_FLOAT_DYNAMIC  or  Tensor.DataType.Image.R_DOUBLE . 
Position 
```kotlin
object Position : SceneGraphProperty.Transform
```
Update the position property of one entity's transform. If this property is used as the  Pipeline.updateSceneGraphProperty 's  targetProperty  parameter, the  data  tensor parameter must be: 
Rotation 
```kotlin
object Rotation : SceneGraphProperty.Transform
```
Update the rotation property of one entity's transform. If this property is used as the  Pipeline.updateSceneGraphProperty 's  targetProperty  parameter, the  data  tensor parameter must be: 
Scale 
```kotlin
object Scale : SceneGraphProperty.Transform
```
Update the scale property of one entity's transform. If this property is used as the  Pipeline.updateSceneGraphProperty 's  targetProperty  parameter, the  data  tensor parameter must be: