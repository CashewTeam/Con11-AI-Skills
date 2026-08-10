# ParticleVaryingPropertyType | PICO Spatial SDK

core / com.pico.spatial.core.ecs.particle / ParticleVaryingPropertyType 
# ParticleVaryingPropertyType
```kotlin
enum ParticleVaryingPropertyType : Enum<ParticleVaryingPropertyType>
```
Defines how a particle property varies across particles. 
Members Entries 
## Entries
CONSTANT 
```kotlin
CONSTANT
```
The property has a constant value. 
RANDOM 
```kotlin
RANDOM
```
The property's value is randomly selected from two values. 
UNKNOWN 
```kotlin
UNKNOWN
```
Reserved value for forward compatibility. 
## Properties
entries 
```kotlin
val entries: EnumEntries<ParticleVaryingPropertyType>
```
Returns a representation of an immutable list of all enum entries, in the order they're declared. 
value 
```kotlin
val value: Int
```
The serialized value of the type. 
## Functions
value Of 
```kotlin
fun valueOf(value: String): ParticleVaryingPropertyType
```
Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.) 
values 
```kotlin
fun values(): Array<ParticleVaryingPropertyType>
```
Returns an array containing the constants of this enum type, in the order they're declared.