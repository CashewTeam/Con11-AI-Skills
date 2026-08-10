# attachShaderGraphMaterial | PICO Spatial SDK

core / com.pico.spatial.core.ecs.resource / VideoMaterial / attachShaderGraphMaterial 
# attachShaderGraphMaterial
```kotlin
fun attachShaderGraphMaterial(shaderGraphMaterial: ShaderGraphMaterial): Boolean
```
Attaches a valid  ShaderGraphMaterial  to the VideoMaterial. 
Note: Once attached, the VideoMaterial will use the provided  ShaderGraphMaterial  for rendering. If another  ShaderGraphMaterial  was previously attached, it will be automatically released unless  .toGlobal()  was called on it beforehand like shown in the following example: 

```
val bundle = AssetBundle.load("asset://your_shaderGraphMaterial_name.bundle")val shaderMat = ShaderGraphMaterial.loadFromAssetBundle(bundle, "relative_path_in_AssetBundle")shaderMat.toGlobal()videoMaterial.attachShaderGraphMaterial(shaderMat)
```
Note: The  ShaderGraphMaterial  must be valid and not released before calling this method. 
#### Return
true if the attachment was successful; false otherwise. 
#### Parameters
shader Graph Material 
The  ShaderGraphMaterial  to attach. 
#### Throws
Illegal State Exception 
If this material or the given shader material is invalid.