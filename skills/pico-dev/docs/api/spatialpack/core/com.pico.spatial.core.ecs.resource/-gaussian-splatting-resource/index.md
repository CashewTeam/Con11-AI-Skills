# GaussianSplattingResource | PICO Spatial SDK

core / com.pico.spatial.core.ecs.resource / GaussianSplattingResource 
# GaussianSplattingResource
```kotlin
class GaussianSplattingResource : Resource
```
A high-level representation of a Gaussian splatting resource. 
Members 
## Constructors
Gaussian Splatting Resource 
```kotlin
constructor(path: String, loadType: LoadType = LoadType.FROM_ASSETS)
```
Constructs a Gaussian splatting resource via file path. 
## Types
Companion 
```kotlin
object Companion
```
The companion object of  GaussianSplattingResource . 
## Functions
close 
```kotlin
open override fun close()
```
You need to manually release the resource to free the memory it occupies.