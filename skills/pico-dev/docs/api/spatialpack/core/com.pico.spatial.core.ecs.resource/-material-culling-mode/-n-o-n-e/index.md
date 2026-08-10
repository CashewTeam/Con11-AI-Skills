# NONE | PICO Spatial SDK

core / com.pico.spatial.core.ecs.resource / MaterialCullingMode / NONE 
# NONE
```kotlin
NONE
```
Disables face culling. 
Both front-facing and back-facing triangles are rendered. 
Pros: 
- 
Essential for double-sided materials 
- 
Correct for thin geometry where both sides are visible 
Cons: 
- 
Higher fragment processing cost (~2× render cost) 
Best for: Thin geometry (foliage, cloth, hair, paper), transparent objects, or any materials where both sides should be visible.