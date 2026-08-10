# ShadowClippingPlaneType | PICO Spatial SDK

core / com.pico.spatial.core.ecs.light / ShadowClippingPlaneType 
# ShadowClippingPlaneType
```kotlin
sealed class ShadowClippingPlaneType
```
Specifies how the clipping planes used for shadow rendering are determined. 
#### Inheritors
Auto Fixed Members 
## Constructors
Shadow Clipping Plane Type 
```kotlin
protected constructor()
```
## Types
Auto 
```kotlin
object Auto : ShadowClippingPlaneType
```
Automatically determines the shadow clipping planes. 
Fixed 
```kotlin
class Fixed(val zNear: Float = 0.01f, val zFar: Float = 10.0f) : ShadowClippingPlaneType
```
Uses fixed clipping planes for shadow rendering.