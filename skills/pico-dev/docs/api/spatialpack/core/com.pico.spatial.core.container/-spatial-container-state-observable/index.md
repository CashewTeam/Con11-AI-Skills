# SpatialContainerStateObservable | PICO Spatial SDK

core / com.pico.spatial.core.container / SpatialContainerStateObservable 
# SpatialContainerStateObservable
```kotlin
open class SpatialContainerStateObservable(owner: SpatialContainerStateOwner)
```
Used to receive  SpatialContainer 's  SpatialContainerState  change and dispatch it to observers. 
Members 
## Constructors
Spatial Container State Observable 
```kotlin
constructor(owner: SpatialContainerStateOwner)
```
## Properties
current State 
```kotlin
var currentState: SpatialContainerState
```
The current  SpatialContainerState  of the  SpatialContainerStateObservable . 
init State 
```kotlin
protected val initState: SpatialContainerState
```
The initial  SpatialContainerState  of the  SpatialContainerStateObservable . 
## Functions
add Observer 
```kotlin
fun addObserver(observer: SpatialContainerStateObserver)
```
Add an observer for a spatial container's state. 
handle State 
```kotlin
open fun handleState(state: SpatialContainerState)
```
Override this function to get the new  SpatialContainerState  when it changes. 
refresh State 
```kotlin
fun refreshState(context: Context)
```
Manually refreshes the state of the  SpatialContainer  when state change events are missed. For example, you can call this function when default  WindowContainer 's state has changed before the first  android.app.Activity  listens to it. 
remove Observer 
```kotlin
fun removeObserver(observer: SpatialContainerStateObserver)
```
Remove the observer for  SpatialContainerStateObserver .