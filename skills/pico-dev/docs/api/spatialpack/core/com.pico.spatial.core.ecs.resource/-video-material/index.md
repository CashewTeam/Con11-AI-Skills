# VideoMaterial | PICO Spatial SDK

core / com.pico.spatial.core.ecs.resource / VideoMaterial 
# VideoMaterial
```kotlin
class VideoMaterial : Material
```
A material specialized for rendering spatial videos. 
This material supports immersive spatial video experiences by providing essential tools to achieve a variety of visual effects. Additionally, a  ShaderGraphMaterial  can be attached to apply rendering effects directly to the texture used by VideoMaterial during rendering. 
Notes: 
- 
When a  ShaderGraphMaterial  is attached, it should be detached once it is no longer needed by the current  VideoMaterial . Any previously attached  ShaderGraphMaterial  will be automatically released unless it has been marked as a global resource via the `.toGlobal()' method as shown in the following example: 

```
val bundle = AssetBundle.load("asset://your_shaderGraphMaterial_name.bundle")val shaderMat = ShaderGraphMaterial.loadFromAssetBundle(bundle, "relative_path_in_AssetBundle")shaderMat.toGlobal()videoMaterial.attachShaderGraphMaterial(shaderMat)
```
- 
Detaching a  ShaderGraphMaterial  will release it if it is not marked as a global resource. To make a material global, call  .toGlobal()  like shown in the example above. 
#### See also
Shader Graph Material Members 
## Constructors
Video Material 
```kotlin
constructor(blendingMode: BlendingMode, videoDimensionMode: VideoDimensionMode, cullingMode: MaterialCullingMode, defaultColor: Color4 = Color4.BLACK)
```
Creates a  VideoMaterial  with the specified  BlendingMode ,  VideoDimensionMode , and  MaterialCullingMode . 
## Functions
attach Shader Graph Material 
```kotlin
fun attachShaderGraphMaterial(shaderGraphMaterial: ShaderGraphMaterial): Boolean
```
Attaches a valid  ShaderGraphMaterial  to the VideoMaterial. 
bind Surface Render Texture 
```kotlin
fun bindSurfaceRenderTexture(surfaceRenderTexture: SurfaceRenderTexture)
```
Bind a  SurfaceRenderTexture  instance with current video material. 
detach Shader Graph Material 
```kotlin
fun detachShaderGraphMaterial()
```
Detaches the previously attached ShaderGraphMaterial from the VideoMaterial. 
get Bind Surface Render Texture 
```kotlin
fun getBindSurfaceRenderTexture(): SurfaceRenderTexture?
```
Gets the bound  SurfaceRenderTexture  of the VideoMaterial. 
get Culling Mode 
```kotlin
fun getCullingMode(): MaterialCullingMode
```
Gets the  MaterialCullingMode  of the  VideoMaterial . 
get Depth Test 
```kotlin
fun getDepthTest(): Boolean
```
Gets the state of depth testing for the  VideoMaterial . 
get Depth Write 
```kotlin
fun getDepthWrite(): Boolean
```
Gets the state of depth writing for the  VideoMaterial . 
get Dimension Mode 
```kotlin
fun getDimensionMode(): VideoDimensionMode
```
Gets the  VideoDimensionMode  of the  VideoMaterial . 
get Shader Graph Material 
```kotlin
fun getShaderGraphMaterial(): ShaderGraphMaterial?
```
Gets the attached  ShaderGraphMaterial  of the VideoMaterial. 
set Culling Mode 
```kotlin
fun setCullingMode(cullingMode: MaterialCullingMode)
```
Sets the  MaterialCullingMode  of the  VideoMaterial . 
set Depth Test 
```kotlin
fun setDepthTest(depthTest: Boolean)
```
Enables or disables depth testing for the  VideoMaterial . 
set Depth Write 
```kotlin
fun setDepthWrite(depthWrite: Boolean)
```
Enables or disables depth writing for the  VideoMaterial . 
set Dimension Mode 
```kotlin
fun setDimensionMode(videoDimensionMode: VideoDimensionMode)
```
Sets the  VideoDimensionMode  of the  VideoMaterial . 
set Texture 
```kotlin
@ExperimentalSpatialApi
```fun  setTexture ( texture :  TextureResource ) 
Sets the  TextureResource  of the  VideoMaterial  in the following modes:  VideoDimensionMode.MONO ,  VideoDimensionMode.SIDE_BY_SIDE , and  VideoDimensionMode.TOP_AND_DOWN . 
```kotlin
@ExperimentalSpatialApi
```fun  setTexture ( textureLeft :  TextureResource ,  textureRight :  TextureResource ) 
Sets the  TextureResource  of the  VideoMaterial  in  VideoDimensionMode.MULTIPLE_VIEW . 
unbind Surface Render Texture 
```kotlin
fun unbindSurfaceRenderTexture()
```
Unbind surface render texture with current video material.