# create | PICO Spatial SDK

core / com.pico.spatial.core.ecs.resource / MeshInstancesResource / Companion / create 
# create
```kotlin
@JvmStatic
```fun  create ( name :  String  =  "MeshInstancesResource" ) :  MeshInstancesResource 
Creates a new  MeshInstancesResource  with the specified name. 
#### Return
The  MeshInstancesResource  created. 
#### Parameters
name 
The name of the  MeshInstancesResource . 
#### Throws
Resource Loading Exception 
If any error occurs during the creation process. 
```kotlin
@JvmStatic
```fun  create ( name :  String  =  "MeshInstancesResource" ,  customDataCount :  Int ) :  MeshInstancesResource 
Creates a new  MeshInstancesResource  with the specified name and custom float data slots per instance. 
#### Return
The  MeshInstancesResource  created. 
#### Parameters
name 
The name of the  MeshInstancesResource . 
custom Data Count 
The number of custom float values reserved per instance. Range: 0, 16. 
#### Throws
Resource Loading Exception 
If any error occurs during the creation process. 
```kotlin
@JvmStatic
```fun  create ( name :  String  =  "MeshInstancesResource" ,  list :  List < MeshInstancesResource.Instance > ) :  MeshInstancesResource 
Creates a new  MeshInstancesResource  with the specified name and instances. When there are too many instances that need to be created at one time, using this function will achieve better performance. 
#### Return
The  MeshInstancesResource  created. 
#### Parameters
name 
The name of the  MeshInstancesResource . 
list 
The list of instances to add to the  MeshInstancesResource . 
#### Throws
Resource Loading Exception 
If any error occurs during the creation process. 
Illegal Argument Exception 
If there are duplicate instance IDs in the list. 
```kotlin
@JvmStatic
```fun  create ( name :  String  =  "MeshInstancesResource" ,  customDataCount :  Int ,  list :  List < MeshInstancesResource.Instance > ) :  MeshInstancesResource 
Creates a new  MeshInstancesResource  with the specified name, instances and explicit custom float data slots. 
This overload uses the builder path and sets  customDataCount  even if the input instances have fewer (or no) custom float values, which can be useful when you want to reserve slots for later updates. 
#### Return
The  MeshInstancesResource  created. 
#### Parameters
name 
The name of the  MeshInstancesResource . 
custom Data Count 
The number of custom float values reserved per instance. Range: 0, 16. 
list 
The list of instances to add to the  MeshInstancesResource . 
#### Throws
Resource Loading Exception 
If any error occurs during the creation process. 
Illegal Argument Exception 
If there are duplicate instance IDs in the list, or data size exceeds count.