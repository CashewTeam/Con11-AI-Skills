# ShadowProjectionType | PICO Spatial SDK

core / com.pico.spatial.core.ecs.light / ShadowProjectionType 
# ShadowProjectionType
```kotlin
sealed class ShadowProjectionType
```
Specifies how the projection used for shadow rendering is determined. 
#### Inheritors
Auto Fixed Members 
## Constructors
Shadow Projection Type 
```kotlin
protected constructor()
```
## Types
Auto 
```kotlin
class Auto(val maximumDistance: Float = 5.0f) : ShadowProjectionType
```
Automatically determines the shadow projection based on the current camera configuration, constrained by a maximum distance. 
Fixed 
```kotlin
class Fixed(val zNear: Float = 0.01f, val zFar: Float = 10.0f, val orthographicWidth: Float = 10.0f, val orthographicHeight: Float = 10.0f) : ShadowProjectionType
```
Uses fixed parameters to define the shadow projection.