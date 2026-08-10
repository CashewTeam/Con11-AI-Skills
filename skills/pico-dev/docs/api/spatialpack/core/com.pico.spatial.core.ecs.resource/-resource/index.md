# Resource | PICO Spatial SDK

core / com.pico.spatial.core.ecs.resource / Resource 
# Resource
```kotlin
open class Resource : Closeable
```
Represents a 3D content resource. 
#### Inheritors
AnimationResource AudioAsset AudioMixerGroupResource GaussianSplattingResource Material MeshInstancesResource MeshResource PhysicsMaterialResource ShapeResource SurfaceRenderTexture TextureResource Members 
## Properties
valid 
```kotlin
@get:JvmName(name = "isValid")
```val  valid :  Boolean 
The resource is valid. 
## Functions
close 
```kotlin
@CallSuper
```open  override  fun  close ( ) 
You need to manually release the resource to free the memory it occupies. 
equals 
```kotlin
operator override fun equals(other: Any?): Boolean
```hash Code 
```kotlin
override fun hashCode(): Int
```to Global 
```kotlin
fun toGlobal()
```
Converts the resource to a global resource. 
to String 
```kotlin
open override fun toString(): String
```