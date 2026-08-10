# SpatialContainer | PICO Spatial SDK

core / com.pico.spatial.core.container / SpatialContainer 
# SpatialContainer
```kotlin
sealed class SpatialContainer(val name: String, containerId: Int) : SpatialContainerStateOwner
```
The base class of a  SpatialContainer . It can be a  WindowContainer  or a  Stage . 
#### Parameters
name 
The name of the  SpatialContainer . Different types of  SpatialContainer s can share the same name, the same type of  SpatialContainer s should use unique names when defined in  android.app.Application  scope. 
container Id 
The unique ID of the  SpatialContainer . 
Members 
## Constructors
Spatial Container 
```kotlin
protected constructor(name: String, containerId: Int)
```
## Properties
name 
```kotlin
open override val name: String
```state Observable 
```kotlin
open override val stateObservable: SpatialContainerStateObservable
```
For receiving the  SpatialContainerState  of  SpatialContainer  and dispatching it to observers. 
type 
```kotlin
abstract val type: SpatialContainerType
```
The type of the  SpatialContainer . 
## Functions
equals 
```kotlin
open operator override fun equals(other: Any?): Boolean
```hash Code 
```kotlin
open override fun hashCode(): Int
```on Create 
```kotlin
open fun onCreate()
```
The callback for the creation of  SpatialContainer . 
on Destroy 
```kotlin
open fun onDestroy()
```
Called when the  SpatialContainer  is destroyed. 
to String 
```kotlin
open override fun toString(): String
```