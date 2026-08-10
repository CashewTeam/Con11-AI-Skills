# ParticleColorVaryingProperty | PICO Spatial SDK

core / com.pico.spatial.core.ecs.particle / ParticleColorVaryingProperty 
# ParticleColorVaryingProperty
```kotlin
class ParticleColorVaryingProperty
```
Represents a color property for particles that can be constant or random. 
Depending on the  ParticleVaryingPropertyType , the  value  and  range  fields are interpreted differently: 
- 
CONSTANT :  value  is the fixed color.  range  is ignored. 
- 
RANDOM :  value  and  range  define the bounds of a random color range. 
Members 
## Constructors
Particle Color Varying Property 
```kotlin
constructor(type: ParticleVaryingPropertyType = ParticleVaryingPropertyType.CONSTANT, value: Color4 = Color4(1f, 1f, 1f, 1f), range: Color4 = Color4(1f, 1f, 1f, 1f))
```
Constructs a new  ParticleColorVaryingProperty  with the specified type, value, and range. 
```kotlin
constructor(another: ParticleColorVaryingProperty)
```
Constructs a new  ParticleColorVaryingProperty  by copying the values from another  ParticleColorVaryingProperty . 
## Properties
range 
```kotlin
val range: Color4
```
The range of the color property. It's the second value used for random color range. 
type 
```kotlin
val type: ParticleVaryingPropertyType
```
The type of the color property. Specifies how the property should behave, either constant or random. 
value 
```kotlin
val value: Color4
```
The value of the color property. It is the only Color4 value when describing a constant color, or the first value when describing a random color range. 
## Functions
equals 
```kotlin
open operator override fun equals(other: Any?): Boolean
```hash Code 
```kotlin
open override fun hashCode(): Int
```to String 
```kotlin
open override fun toString(): String
```