# com.pico.spatial.core.ecs.light | PICO Spatial SDK

core / com.pico.spatial.core.ecs.light 
# Package-level declarations
Types 
## Types
Shadow Clipping Plane Type 
```kotlin
sealed class ShadowClippingPlaneType
```
Specifies how the clipping planes used for shadow rendering are determined. 
Shadow Face Culling Mode 
```kotlin
enum ShadowFaceCullingMode : Enum<ShadowFaceCullingMode>
```
Defines the face culling strategy applied during shadow map rendering. 
Shadow Projection Type 
```kotlin
sealed class ShadowProjectionType
```
Specifies how the projection used for shadow rendering is determined.