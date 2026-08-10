# FRONT | PICO Spatial SDK

core / com.pico.spatial.core.ecs.light / ShadowFaceCullingMode / FRONT 
# FRONT
```kotlin
FRONT
```
Culls front-facing triangles during shadow rendering. 
Only back-facing triangles (away from the light) are rendered into the shadow map. Front-facing triangles are culled before rasterization. 
Renders: Back faces only 
Pros: 
- 
Significantly reduces shadow acne (self-shadowing artifacts) 
- 
Often used with shadow biasing techniques 
Cons: 
- 
May cause shadows to appear detached from objects ("Peter Panning") 
- 
Can miss shadows on thin geometry 
- 
Requires careful tuning to avoid visual artifacts 
Best for: Advanced scenarios where shadow acne is problematic and detachment artifacts are acceptable. Typically combined with depth bias adjustments. 
Note: This trades one type of artifact for another. Use only when  BACK  produces unacceptable shadow acne.