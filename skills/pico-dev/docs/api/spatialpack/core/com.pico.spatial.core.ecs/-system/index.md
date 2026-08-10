# System | PICO Spatial SDK

core / com.pico.spatial.core.ecs / System 
# System
```kotlin
abstract class System
```
Represents a system in the Entity-Component-System (ECS) architecture. 
A  System  instance receives periodic update callbacks from the ECS runtime. 
Subclasses of  System  must provide a public no-argument constructor to make internal mechanism work. 
Members 
## Constructors
System 
```kotlin
constructor()
```
## Types
Companion 
```kotlin
object Companion
```
The companion object of  System . 
## Functions
update 
```kotlin
open fun update(context: SceneUpdateContext)
```
Called periodically by the ECS runtime to update this system.