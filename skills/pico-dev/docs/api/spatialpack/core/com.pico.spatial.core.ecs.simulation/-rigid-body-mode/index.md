# RigidBodyMode | PICO Spatial SDK

core / com.pico.spatial.core.ecs.simulation / RigidBodyMode 
# RigidBodyMode
```kotlin
enum RigidBodyMode : Enum<RigidBodyMode>
```
Defines the rigid body modes of an object. 
Objects without a  RigidBodyComponent  are considered static by default. Once a  RigidBodyComponent  is added, the object becomes dynamic by default. 
Members Entries 
## Entries
KINEMATIC 
```kotlin
KINEMATIC
```
Kinematic mode. In this mode, the  RigidBodyComponent  is unaffected by gravity and does not respond to external forces. 
DYNAMIC 
```kotlin
DYNAMIC
```
Dynamic mode. In this mode, the  RigidBodyComponent  is affected by gravity and responds to external forces. 
UNKNOWN 
```kotlin
UNKNOWN
```
Reserved value for forward compatibility. 
## Properties
entries 
```kotlin
val entries: EnumEntries<RigidBodyMode>
```
Returns a representation of an immutable list of all enum entries, in the order they're declared. 
value 
```kotlin
val value: Int
```
The value of the RigidBodyMode. 
## Functions
value Of 
```kotlin
fun valueOf(value: String): RigidBodyMode
```
Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.) 
values 
```kotlin
fun values(): Array<RigidBodyMode>
```
Returns an array containing the constants of this enum type, in the order they're declared.