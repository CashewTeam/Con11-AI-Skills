# com.pico.spatial.core.ecs.resource | PICO Spatial SDK

core / com.pico.spatial.core.ecs.resource 
# Package-level declarations
Types 
## Types
Animation Resource 
```kotlin
class AnimationResource : Resource
```
The type of animation resource. 
Asset Bundle 
```kotlin
class AssetBundle : Closeable
```
An  AssetBundle  is a packaged collection of resources. 
Audio Asset 
```kotlin
open class AudioAsset : Resource
```
The abstract audio resource class for all audio resources including  AudioResource , AudioGroupResource . 
Audio Group Resource 
```kotlin
class AudioGroupResource : AudioAsset
```
The  AudioAsset  type for audio group. 
Audio Mixer Group Resource 
```kotlin
class AudioMixerGroupResource : Resource
```
Manages a group of audio resources. 
Audio Resource 
```kotlin
class AudioResource : AudioAsset
```
The  Resource  type for audio. 
Blending Mode 
```kotlin
enum BlendingMode : Enum<BlendingMode>
```
Represents the blending mode of the material. 
Gaussian Splatting Resource 
```kotlin
class GaussianSplattingResource : Resource
```
A high-level representation of a Gaussian splatting resource. 
Material 
```kotlin
open class Material : Resource
```
Represents the material properties of a mesh instance, such as color and texture. 
Material Converter 
```kotlin
typealias MaterialConverter = (Material) -> Material?
```Material Culling Mode 
```kotlin
enum MaterialCullingMode : Enum<MaterialCullingMode>
```
Specifies the face culling mode used when rendering a material. 
Material Data Converter 
```kotlin
typealias MaterialDataConverter = (Material) -> MaterialData?
```Mesh Instances Resource 
```kotlin
class MeshInstancesResource : Resource
```
A resource for model components that enables GPU instancing for models and materials. 
Mesh Model 
```kotlin
class MeshModel @JvmOverloads constructor(val positions: List<Vector3>, val triangleIndices: List<Int>, val normals: List<Vector3>? = null, val tangents: List<Vector4>? = null, val uv0: List<Vector2>? = null, val uv1: List<Vector2>? = null, val colors: List<Color4>? = null)
```
A container for mesh geometry data. 
Mesh Resource 
```kotlin
class MeshResource : Resource
```
A high-level representation of a collection of vertices and edges that define a shape. All models imported into the engine are measured in meters. 
Physically Based Material 
```kotlin
class PhysicallyBasedMaterial : Material
```
A material that simulates the appearance of real-world objects. 
Physics Material Resource 
```kotlin
class PhysicsMaterialResource : Resource
```
A resource type used to define the properties of physics materials, such as friction and restitution. 
Polygon Fill Mode 
```kotlin
enum PolygonFillMode : Enum<PolygonFillMode>
```
Fill modes for rendering polygons. 
Portal Material 
```kotlin
class PortalMaterial : Material
```
A material that turns a mesh into a portal to a portable world. 
Resource 
```kotlin
open class Resource : Closeable
```
Represents a 3D content resource. 
Resource Loading Exception 
```kotlin
class ResourceLoadingException(errorCode: Int, message: String) : Exception
```
Exception thrown when an error occurs during resource or entity loading. 
Shader Graph Material 
```kotlin
class ShaderGraphMaterial : Material
```
Provides methods to query and modify material parameters for dynamic customization at runtime. 
Shape Resource 
```kotlin
class ShapeResource : Resource
```
Represents a shape resource. 
Surface Render Texture 
```kotlin
class SurfaceRenderTexture : Resource
```
Managed SurfaceRenderTexture resource for Android media rendering; this resource obeys the lifecycle management of  Resource . Calling  toGlobal()  can make it reusable. 
Texture Color Space 
```kotlin
enum TextureColorSpace : Enum<TextureColorSpace>
```
The color space of the texture. 
Texture Create Option 
```kotlin
class TextureCreateOption
```
Options for creating a  TextureResource . 
Texture Encoding 
```kotlin
enum TextureEncoding : Enum<TextureEncoding>
```
The encoding of texture. 
Texture Mipmap Mode 
```kotlin
enum TextureMipmapMode : Enum<TextureMipmapMode>
```
The mipmap mode of the texture. 
Texture Resource 
```kotlin
class TextureResource : Resource
```
A representation of a texture. 
Unlit Material 
```kotlin
class UnlitMaterial : Material
```
A material type that renders without being affected by scene lighting. 
Video Material 
```kotlin
class VideoMaterial : Material
```
A material specialized for rendering spatial videos.