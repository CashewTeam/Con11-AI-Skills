# Blend | PICO Spatial SDK

core / com.pico.spatial.core.ecs / ImageBasedLightSource / Blend / Blend 
# Blend
```kotlin
constructor(firstResource: TextureResource, secondResource: TextureResource, blendPercentage: Float = 0.5f)
```
#### Parameters
first Resource 
The primary environment texture. 
second Resource 
The secondary environment texture to blend with. 
blend Percentage 
The blend ratio, where  0.0  = 100% first texture,  1.0  = 100% second texture. The default value is  0.5  (equal blend).