# SceneGraphProperty | PICO Spatial SDK

spatialml:securemr / com.pico.spatial.ml.securemr / SceneGraphProperty 
# SceneGraphProperty
```kotlin
sealed class SceneGraphProperty
```
Specifying the component and the field to be updated in  Pipeline.updateSceneGraphProperty . 
For example, to update the local transform of the target entity, you may 

```
val session: Session = ... // create a new sessionsession!!.newPipeline().run {     val scene = newPlaceholderLike(...) // a local placeholder referring the scene to be updated     val newMatrixTensor = newPipelineLocalTensor(         Tensor.MultiDimensionalInitInfo(Tensor.DataType.FLOAT32, intArrayOf(4, 4))     )     ...     updateComponent(         scene,         "/entity/child/grandchild",  // path of the target entity in the scene         Transform.LocalMatrix,         newMatrixTensor     )}
```
Another example is to update the material of a target entity. Let's say the entity has 4 materials, and we would like to update the base color of the 3rd: 

```
val session: Session = ... // create a new sessionsession!!.newPipeline().run {     val scene = newPlaceholderLike(...) // a local placeholder referring the scene to be updated     val redColor = PipelineLocalTensor(this, Color.valueOf(Color.RED))     ...     updateComponent(         scene, // a local PipelineTensorPlaceholder for the scene to be updated         "/entity/child/grandchild",  // path of the target entity in the scene         PBRMaterials[2].BaseColor,         redColor     )}
```
#### Parameters
component Name 
the name of the component being updated. 
property 
the name of the property in Component  componentName  to be updated. 
#### Inheritors
Transform CameraAnchor Text Members 
## Types
Camera Anchor 
```kotlin
sealed class CameraAnchor : SceneGraphProperty
```
Update the camera anchor component of an entity.  CameraAnchor  component is an hidden component for SpatialML container only. It allows you to use a transform matrix with respect to the camera coordinate space, to override the local transform updated by  SceneGraphProperty.Transform . 
PBRMaterials 
```kotlin
object PBRMaterials
```
Update the Physical-Based Rendering (PBR) material properties of an entity. For an entity holding multiple materials, by default the material indexed 0 will be updated. To specify a different material in the entity, you can specify the material index like  PBRMaterials[2].BaseColor . 
Text 
```kotlin
sealed class Text : SceneGraphProperty
```
Update a property of one entity's Text component. If the entity has not been added a text component to, updating its text component property will create one for the entity. The component will render text at the origin of the entity's local coordination system. 
Transform 
```kotlin
sealed class Transform : SceneGraphProperty
```
Update a property of one entity's TransformComponent. 
## Properties
property 
```kotlin
protected val property: String
```
## Functions
to String 
```kotlin
open override fun toString(): String
```