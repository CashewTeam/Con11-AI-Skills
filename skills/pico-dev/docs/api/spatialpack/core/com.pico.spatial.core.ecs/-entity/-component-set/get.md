# get | PICO Spatial SDK

core / com.pico.spatial.core.ecs / Entity / ComponentSet / get 
# get
```kotlin
@MainThread
```operator  fun  < T  :  Component >  get ( componentType :  Class < T > ) :  T ? 
Gets the component of a specific type. 
#### Return
The component of the specified type, or null if the component does not exist. 
#### Parameters
T 
The generic  Component  type. 
component Type 
The type of component to get. 
```kotlin
inline fun <T : Component> get(): T?
```
Gets the component of the specific type. 
#### Return
The component of the specified type, or null if the component does not exist. 
#### Parameters
T 
The generic  Component  type.