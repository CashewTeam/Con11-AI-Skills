# LookAtTargetType | PICO Spatial SDK

core / com.pico.spatial.core.ecs / LookAtTargetType 
# LookAtTargetType
```kotlin
enum LookAtTargetType : Enum<LookAtTargetType>
```
Enumeration defining target types for the  LookAtComponent  in 3D spatial simulation. Specifies what an entity should face when implementing "look at" behavior. 
Members Entries 
## Entries
NONE 
```kotlin
NONE
```
No target; the entity will not face any specific object, which is the default behavior. 
VIEWER 
```kotlin
VIEWER
```
Targets the viewer (user's head-mounted display). 
ENTITY 
```kotlin
ENTITY
```
Targets a specific entity. The entity will face the target entity by orienting towards its position, and this behavior remains effective even when the target entity is in different containers. 
UNKNOWN 
```kotlin
UNKNOWN
```
Reserved value for forward compatibility. 
## Properties
entries 
```kotlin
val entries: EnumEntries<LookAtTargetType>
```
Returns a representation of an immutable list of all enum entries, in the order they're declared. 
value 
```kotlin
val value: Int
```
The integer value of the target type. 
## Functions
value Of 
```kotlin
fun valueOf(value: String): LookAtTargetType
```
Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.) 
values 
```kotlin
fun values(): Array<LookAtTargetType>
```
Returns an array containing the constants of this enum type, in the order they're declared.