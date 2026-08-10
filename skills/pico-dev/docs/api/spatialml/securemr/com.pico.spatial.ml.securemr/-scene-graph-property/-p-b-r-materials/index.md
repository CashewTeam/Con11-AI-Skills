# PBRMaterials | PICO Spatial SDK

spatialml:securemr / com.pico.spatial.ml.securemr / SceneGraphProperty / PBRMaterials 
# PBRMaterials
```kotlin
object PBRMaterials
```
Update the Physical-Based Rendering (PBR) material properties of an entity. For an entity holding multiple materials, by default the material indexed 0 will be updated. To specify a different material in the entity, you can specify the material index like  PBRMaterials[2].BaseColor . 
Members 
## Types
Indexed PBRMaterial 
```kotlin
class IndexedPBRMaterial
```
To update a certain material at the specified index. To specify such a indexed material of the target entity to be updated, you can use the  []  operator of  PBRMaterials . For example, 
## Properties
Base Color 
```kotlin
val BaseColor: SceneGraphProperty
```
Update the base color property of the PBR material at default index 0. 
Base Color Texture 
```kotlin
val BaseColorTexture: SceneGraphProperty
```
Update the base color texture property of the PBR material at index 0. 
Metallic 
```kotlin
val Metallic: SceneGraphProperty
```
Update the metallic property of the PBR material at default index 0. 
Metallic Texture 
```kotlin
val MetallicTexture: SceneGraphProperty
```
Update the metallic property of the PBR material at index 0. 
Roughness 
```kotlin
val Roughness: SceneGraphProperty
```
Update the roughness property of the PBR material at default index 0. 
Roughness Texture 
```kotlin
val RoughnessTexture: SceneGraphProperty
```
Update the roughness property of the PBR material at index 0. 
## Functions
get 
```kotlin
operator fun get(materialIdx: Int): SceneGraphProperty.PBRMaterials.IndexedPBRMaterial
```
Specify which material to be updated.