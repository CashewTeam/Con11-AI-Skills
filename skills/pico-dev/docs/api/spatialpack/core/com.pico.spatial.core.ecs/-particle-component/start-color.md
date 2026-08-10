# startColor | PICO Spatial SDK

core / com.pico.spatial.core.ecs / ParticleComponent / startColor 
# startColor
```kotlin
var startColor: ParticleColorVaryingProperty
```
The initial color of particles at spawn. 
Behavior depends on  startColor.type : 
- 
CONSTANT : All particles use the same color defined by  startColor.value . 
- 
RANDOM : Each particle has a random color chosen from the range  [startColor.value, startColor.range] .