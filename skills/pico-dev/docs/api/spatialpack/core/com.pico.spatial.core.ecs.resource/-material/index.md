# Material | PICO Spatial SDK

core / com.pico.spatial.core.ecs.resource / Material 
# Material
```kotlin
open class Material : Resource
```
Represents the material properties of a mesh instance, such as color and texture. 
#### Inheritors
PhysicallyBasedMaterial PortalMaterial ShaderGraphMaterial UnlitMaterial VideoMaterial Members 
## Functions
close 
```kotlin
open override fun close()
```
You need to manually release the resource to free the memory it occupies.