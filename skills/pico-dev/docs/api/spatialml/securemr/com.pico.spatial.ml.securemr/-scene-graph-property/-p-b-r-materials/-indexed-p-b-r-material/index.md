# IndexedPBRMaterial | PICO Spatial SDK

spatialml:securemr / com.pico.spatial.ml.securemr / SceneGraphProperty / PBRMaterials / IndexedPBRMaterial 
# IndexedPBRMaterial
```kotlin
class IndexedPBRMaterial
```
To update a certain material at the specified index. To specify such a indexed material of the target entity to be updated, you can use the  []  operator of  PBRMaterials . For example, 

```
val pipeline1: Pipeline = ...pipeline1.updateComponent(..., PBRMaterials[2].Roughness)
```
#### Parameters
index 
the material index among the target entity's all materials. 
Members 
## Properties
Base Color 
```kotlin
val BaseColor: SceneGraphProperty
```
Update the base color property of the PBR material at specified  index . 
Base Color Texture 
```kotlin
val BaseColorTexture: SceneGraphProperty
```
Update the base color texture property of the PBR material at specified  index . 
Metallic 
```kotlin
val Metallic: SceneGraphProperty
```
Update the metallic property of the PBR material at specified  index . 
Metallic Texture 
```kotlin
val MetallicTexture: SceneGraphProperty
```
Update the metallic property of the PBR material at specified  index . 
Roughness 
```kotlin
val Roughness: SceneGraphProperty
```
Update the roughness property of the PBR material at specified  index . 
Roughness Texture 
```kotlin
val RoughnessTexture: SceneGraphProperty
```
Update the roughness property of the PBR material at specified  index .