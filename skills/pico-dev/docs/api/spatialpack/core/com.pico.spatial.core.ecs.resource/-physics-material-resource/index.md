# PhysicsMaterialResource | PICO Spatial SDK

core / com.pico.spatial.core.ecs.resource / PhysicsMaterialResource 
# PhysicsMaterialResource
```kotlin
class PhysicsMaterialResource : Resource
```
A resource type used to define the properties of physics materials, such as friction and restitution. 
Members 
## Constructors
Physics Material Resource 
```kotlin
constructor(staticFriction: Float = 0.6f, dynamicFriction: Float = 0.6f, restitution: Float = 0.0f)
```
Constructs a  PhysicsMaterialResource  by specifying parameters. 
## Functions
close 
```kotlin
open override fun close()
```
You need to manually release the resource to free the memory it occupies. 
get Dynamic Friction 
```kotlin
fun getDynamicFriction(): Float
```
Gets the dynamic friction of the physics material. 
get Restitution 
```kotlin
fun getRestitution(): Float
```
Gets the restitution of the physics material. 
get Static Friction 
```kotlin
fun getStaticFriction(): Float
```
Gets the static friction of the physics material. 
set Dynamic Friction 
```kotlin
fun setDynamicFriction(dynamicFriction: Float)
```
Sets the dynamic friction of the physics material. 
set Restitution 
```kotlin
fun setRestitution(restitution: Float)
```
Sets the restitution of the physics material. 
set Static Friction 
```kotlin
fun setStaticFriction(staticFriction: Float)
```
Sets the static friction of the physics material.