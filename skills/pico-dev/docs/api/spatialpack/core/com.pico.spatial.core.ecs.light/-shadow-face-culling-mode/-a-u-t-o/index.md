# AUTO | PICO Spatial SDK

core / com.pico.spatial.core.ecs.light / ShadowFaceCullingMode / AUTO 
# AUTO
```kotlin
AUTO
```
Automatically inherits the culling mode from the associated material. 
The rendering backend queries the object's MaterialCullingMode during shadow pass preparation and maps it to a shadow culling mode. This maintains visual consistency between material rendering and shadow casting. 
## Mapping Rules
| MaterialCullingMode | → | ShadowFaceCullingMode | Behavior |
|---|---|---|---|
| BACK | → | BACK | Render front faces only |
| FRONT | → | FRONT | Render back faces only |
| NONE | → | NONE | Render both sides |
| FRONT_AND_BACK | → | No shadows | Object casts no shadows |

Note on FRONT_AND_BACK: When a material has cullingMode = FRONT_AND_BACK (culls all faces), the object is invisible and thus cannot cast shadows. This mode is functionally equivalent to disabling shadow casting via castsShadowEnabled = false, so no explicit FRONT_AND_BACK enum constant is provided in ShadowFaceCullingMode. 
Pros: 
- 
Recommended default — maintains coherence between material and shadows 
- 
Automatically adapts when material properties change 
- 
No manual synchronization required 
Performance impact: Varies based on the resolved mode at runtime. 
Best for: Most scenarios. Override only when you need explicit control over shadow rendering independent of material appearance (e.g., forcing  BACK  for performance on foliage that uses  NONE  for material rendering). 
#### See also
Material Culling Mode