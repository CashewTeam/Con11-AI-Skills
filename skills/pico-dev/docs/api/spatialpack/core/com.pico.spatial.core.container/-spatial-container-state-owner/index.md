# SpatialContainerStateOwner | PICO Spatial SDK

core / com.pico.spatial.core.container / SpatialContainerStateOwner 
# SpatialContainerStateOwner
```kotlin
interface SpatialContainerStateOwner
```
For making the  SpatialContainer  as the owner of  SpatialContainerStateObserver . 
#### Inheritors
SpatialContainer Members 
## Properties
name 
```kotlin
abstract val name: String
```
The name of the SpatialContainer. 
state Observable 
```kotlin
abstract val stateObservable: SpatialContainerStateObservable
```
The observable for SpatialContainer's state.