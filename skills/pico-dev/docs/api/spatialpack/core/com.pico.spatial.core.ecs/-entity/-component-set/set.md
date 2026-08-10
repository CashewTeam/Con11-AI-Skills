# set | PICO Spatial SDK

core / com.pico.spatial.core.ecs / Entity / ComponentSet / set 
# set
```kotlin
@MainThread
```operator  fun  < T  :  Component >  set ( componentType :  Class < T > ,  component :  T ) 
Sets a component as the specified type. If a component of the same type already exists, it will be replaced. 
#### Parameters
T 
The generic  Component  type. 
component Type 
The type of component to set. 
component 
The component to set as the specified type. 
```kotlin
inline fun <T : Component> set(component: T)
```
Sets a component of the specified type. If a component of the same type already exists, it will be replaced. 
#### Parameters
T 
The generic  Component  type. 
component 
The component to set of the specified type. 
```kotlin
@MainThread
```fun  set ( components :  List < Component > ) 
Sets multiple components. If the array contains components of the same type, the last one in the array will replace the previous ones. 
#### Parameters
components 
The component collection to set.