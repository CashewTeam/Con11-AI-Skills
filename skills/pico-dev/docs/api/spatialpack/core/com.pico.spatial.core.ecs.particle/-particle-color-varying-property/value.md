# value | PICO Spatial SDK

core / com.pico.spatial.core.ecs.particle / ParticleColorVaryingProperty / value 
# value
```kotlin
val value: Color4
```
The value of the color property. It is the only Color4 value when describing a constant color, or the first value when describing a random color range. 
This field is interpreted differently depending on the  type  of the property: 
- 
CONSTANT : This is the fixed color. 
- 
RANDOM : This defines one bound of the random color range. The random color would be generated in color range value, range.