# stateObservable | PICO Spatial SDK

core / com.pico.spatial.core.container / SpatialContainer / stateObservable 
# stateObservable
```kotlin
open override val stateObservable: SpatialContainerStateObservable
```
For receiving the  SpatialContainerState  of  SpatialContainer  and dispatching it to observers. 
You can use this observable to add your observer, for example: 

```
stateObservable.addObserver(object : SpatialContainerStateObserver {     override fun onEvent(source: SpatialContainerStateOwner, event: SpatialStateEvent) {         // do something     }})
```
#### Throws
Illegal State Exception 
This exception is thrown if the  SpatialContainer  is not registered.