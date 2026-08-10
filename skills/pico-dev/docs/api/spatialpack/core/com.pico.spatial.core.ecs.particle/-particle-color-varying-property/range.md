# range | PICO Spatial SDK

core / com.pico.spatial.core.ecs.particle / ParticleColorVaryingProperty / range 
# range
```kotlin
val range: Color4
```
The range of the color property. It's the second value used for random color range. 
This field is interpreted differently depending on the  type  of the property: 
- 
CONSTANT : This is ignored. 
- 
RANDOM : This defines the other bound of the random color range. The random color would be generated in color range value, range.