# BACK | PICO Spatial SDK

core / com.pico.spatial.core.ecs.light / ShadowFaceCullingMode / BACK 
# BACK
```kotlin
BACK
```
Culls back-facing triangles during shadow rendering. 
Only front-facing triangles (toward the light) are rendered into the shadow map. Back-facing triangles are culled before rasterization. 
Renders: Front faces only 
Pros: 
- 
Good balance between performance and correctness 
- 
Reduces self-shadowing artifacts (shadow acne) 
- 
Standard choice in most rendering engines 
Cons: 
- 
May miss shadows from interior surfaces of complex geometry 
Best for: Solid, opaque objects (characters, props, buildings). This is the recommended default for most 3D content.