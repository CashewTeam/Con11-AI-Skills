# has | PICO Spatial SDK

core / com.pico.spatial.core.ecs / Entity / ComponentSet / has 
# has
```kotlin
@MainThread
```fun  < T  :  Component >  has ( componentType :  Class < T > ) :  Boolean 
Checks if the component set contains the component of the specified type. 
#### Return
true  if the specified type of component exists;  false  otherwise. 
#### Parameters
T 
The generic  Component  type. 
component Type 
The type of component to check. 
```kotlin
inline fun <T : Component> has(): Boolean
```
Check if the componentSet contains a component of a specific type. 
#### Return
True if the component exists, false otherwise. 
#### Parameters
T 
The generic Component type.