# NONE | PICO Spatial SDK

core / com.pico.spatial.core.ecs.light / ShadowFaceCullingMode / NONE 
# NONE
```kotlin
NONE
```
Disables face culling during shadow rendering. 
All triangle faces (both front and back) are rendered into the shadow map. No faces are culled. 
Renders: Both front and back faces 
Pros: 
- 
Most geometrically accurate shadows 
- 
Essential for double-sided materials 
- 
Correct for thin geometry where both sides are visible 
Cons: 
- 
Highest fragment processing cost (~2× render cost) 
- 
Increased risk of shadow acne from interior surfaces 
- 
May require more aggressive depth biasing 
Best for: Thin geometry (foliage, cloth, hair, paper), transparent objects, or any double-sided materials where both sides cast visible shadows. 
Performance note: Use sparingly. Consider  BACK  for background foliage or distant objects where the accuracy difference is imperceptible.