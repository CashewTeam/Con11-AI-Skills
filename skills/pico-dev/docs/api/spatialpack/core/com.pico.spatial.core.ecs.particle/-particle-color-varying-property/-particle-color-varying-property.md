# ParticleColorVaryingProperty | PICO Spatial SDK

core / com.pico.spatial.core.ecs.particle / ParticleColorVaryingProperty / ParticleColorVaryingProperty 
# ParticleColorVaryingProperty
```kotlin
constructor(type: ParticleVaryingPropertyType = ParticleVaryingPropertyType.CONSTANT, value: Color4 = Color4(1f, 1f, 1f, 1f), range: Color4 = Color4(1f, 1f, 1f, 1f))
```
Constructs a new  ParticleColorVaryingProperty  with the specified type, value, and range. 
#### Parameters
type 
The  type  of the color property. Defaults to  ParticleVaryingPropertyType.CONSTANT . 
value 
The  value  of the color property. Defaults to Color4(1f, 1f, 1f, 1f). 
range 
The  range  of the color property. Defaults to Color4(1f, 1f, 1f, 1f). 
```kotlin
constructor(another: ParticleColorVaryingProperty)
```
Constructs a new  ParticleColorVaryingProperty  by copying the values from another  ParticleColorVaryingProperty . 
#### Parameters
another 
The  ParticleColorVaryingProperty  to copy values from.