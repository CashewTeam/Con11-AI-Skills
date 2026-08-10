# hasComponent | PICO Spatial SDK

core / com.pico.spatial.core.ecs / EntityQueryCondition / Companion / hasComponent 
# hasComponent
```kotlin
@JvmStatic
```fun  < T  :  Component >  hasComponent ( componentClass :  Class < T > ) :  EntityQueryCondition 
Creates a condition to check whether an entity has a component of the specified type. 
#### Return
An  EntityQueryCondition  that encapsulates the condition for checking whether an entity has the specified component. 
#### Parameters
T 
The component type to check. 
component Class 
The  Class  object of the component.