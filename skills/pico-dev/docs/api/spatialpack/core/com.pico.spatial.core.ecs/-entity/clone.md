# clone | PICO Spatial SDK

core / com.pico.spatial.core.ecs / Entity / clone 
# clone
```kotlin
@MainThread
```fun  clone ( cloneOptions :  Entity.CloneOptions  =  CloneOptions() ) :  Entity ? 
Creates and returns a copy of this entity based on the specified cloning options. 
The cloned entity will have the same name and cloneable components as the original one. And the entity tree information will not be copied. 
#### Return
The cloned entity instance. 
Note: Clone is a time-consuming operation. Since this function can only be invoked on the main thread, cloning a deeply nested entity tree or a large number of entities may cause main thread stuttering. It is recommended to limit the depth and quantity of entities to reduce performance overhead. When the number of clone operations exceeds 15,000, performance issues may occur. 
#### Parameters
clone Options 
The custom cloning process, such as whether the cloning should be recursive and if the material instance should be shared.