# FRONT | PICO Spatial SDK

core / com.pico.spatial.core.ecs.resource / MaterialCullingMode / FRONT 
# FRONT
```kotlin
FRONT
```
Culls front-facing triangles. 
Only back-facing triangles (facing away from the camera) are rendered. Front-facing triangles are culled before rasterization. 
Best for: Inverse rendering effects, certain volumetric rendering techniques, or debugging winding order issues.