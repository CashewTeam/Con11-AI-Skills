# Companion | PICO Spatial SDK

core / com.pico.spatial.core.ecs.resource / MeshInstancesResource / Companion 
# Companion
```kotlin
object Companion
```
The companion object for  MeshInstancesResource . 
Members 
## Functions
create 
```kotlin
@JvmStatic
```fun  create ( name :  String  =  "MeshInstancesResource" ) :  MeshInstancesResource 
Creates a new  MeshInstancesResource  with the specified name. 
```kotlin
@JvmStatic
```fun  create ( name :  String  =  "MeshInstancesResource" ,  customDataCount :  Int ) :  MeshInstancesResource 
Creates a new  MeshInstancesResource  with the specified name and custom float data slots per instance. 
```kotlin
@JvmStatic
```fun  create ( name :  String  =  "MeshInstancesResource" ,  list :  List < MeshInstancesResource.Instance > ) :  MeshInstancesResource 
Creates a new  MeshInstancesResource  with the specified name and instances. When there are too many instances that need to be created at one time, using this function will achieve better performance. 
```kotlin
@JvmStatic
```fun  create ( name :  String  =  "MeshInstancesResource" ,  customDataCount :  Int ,  list :  List < MeshInstancesResource.Instance > ) :  MeshInstancesResource 
Creates a new  MeshInstancesResource  with the specified name, instances and explicit custom float data slots.