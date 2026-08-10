# destroy | PICO Spatial SDK

core / com.pico.spatial.core.ecs / Entity / destroy 
# destroy
```kotlin
@MainThread
```fun  destroy ( recursively :  Boolean  =  true ) :  Boolean 
Destroys this entity and, by default, all its children recursively. 
If you do not call  destroy()  explicitly and there are no remaining strong references to this object, its native resources will be released automatically during garbage collection. Developers do not need to manage native memory manually in that case. 
If  recursively  is false, this call destroys only the current Entity. All child Entities are detached and their parent reference is set to  null . If those children are not held by any other strong reference, they follow the same auto-release strategy: their native memory will be released once the objects are garbage-collected. Developers do not need to manage this manually. 
Destroying an entity is a relatively expensive operation. Avoid polling and destroying many target entities in the same frame. For high-frequency destruction scenarios, collect entities first and destroy them in batches at a suitable time, or spread destruction across frames when possible, to reduce frame stutters. 
#### Return
true  if the destruction succeeds;  false  otherwise. 
#### Parameters
recursively 
Whether to destroy child entities recursively. The default value is  true .