# MeshInstancesResource | PICO Spatial SDK

core / com.pico.spatial.core.ecs.resource / MeshInstancesResource 
# MeshInstancesResource
```kotlin
class MeshInstancesResource : Resource
```
A resource for model components that enables GPU instancing for models and materials. 
It helps render a large number of models in a scene by reducing CPU draw calls and supports reusing instance data for better performance. 
Members 
## Types
Companion 
```kotlin
object Companion
```
The companion object for  MeshInstancesResource . 
Instance 
```kotlin
class Instance
```
Represents a single instance with an ID and a transform. 
## Properties
count 
```kotlin
val count: Int
```
The number of instances in the resource. 
custom Data Count 
```kotlin
val customDataCount: Int
```
The number of custom float values reserved per instance. Range: 0, 16. 
is Empty 
```kotlin
val isEmpty: Boolean
```
Whether the resource is empty. 
## Functions
add 
```kotlin
fun add(instance: MeshInstancesResource.Instance): Boolean
```
Adds a new instance to the resource. 
close 
```kotlin
open override fun close()
```
You need to manually release the resource to free the memory it occupies. 
get 
```kotlin
fun get(id: String): MeshInstancesResource.Instance?
```
Gets an instance from the resource. 
get All Ids 
```kotlin
fun getAllIds(): List<String>
```
Gets all instance IDs from the resource. 
get Name 
```kotlin
fun getName(): String
```
Gets the name of the resource. 
remove 
```kotlin
fun remove(id: String): Boolean
```
Removes an instance from the resource. 
remove All 
```kotlin
fun removeAll()
```
Removes all instances from the resource. 
update 
```kotlin
fun update(id: String, transform: Transform): Boolean
```
Updates an instance in the resource. 
```kotlin
fun update(id: String, transform: Transform, customFloatData: FloatArray): Boolean
```
Updates an instance in the resource with both transform and custom float data.