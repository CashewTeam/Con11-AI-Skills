# BACK | PICO Spatial SDK

core / com.pico.spatial.core.ecs.resource / MaterialCullingMode / BACK 
# BACK
```kotlin
BACK
```
Culls back-facing triangles. 
Only front-facing triangles (facing toward the camera) are rendered. Back-facing triangles are culled before rasterization. 
Pros: 
- 
Best performance for closed, opaque objects 
- 
Standard choice in most rendering engines 
Best for: Solid, opaque objects (characters, props, buildings). This is the recommended default for most 3D content.