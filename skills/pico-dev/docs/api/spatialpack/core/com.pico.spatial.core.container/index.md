# com.pico.spatial.core.container | PICO Spatial SDK

core / com.pico.spatial.core.container 
# Package-level declarations
Types Functions 
## Types
Space State 
```kotlin
enum SpaceState : Enum<SpaceState>
```
Represents the types of spaces in which the application is currently running, including  UNKNOWN ,  SHARED_SPACE , and  FULL_SPACE . 
Spatial Container 
```kotlin
sealed class SpatialContainer(val name: String, containerId: Int) : SpatialContainerStateOwner
```
The base class of a  SpatialContainer . It can be a  WindowContainer  or a  Stage . 
Spatial Container State 
```kotlin
interface SpatialContainerState
```
The state of  SpatialContainer . 
Spatial Container State Event 
```kotlin
enum SpatialContainerStateEvent : Enum<SpatialContainerStateEvent>
```
Represents the events that trigger state transitions for a  SpatialContainer . These events describe changes in the  SpatialContainer 's  SpatialContainerState , which are triggered by focus, overlapping and occlusion, or camera visibility transitions. The events can be used to track and react to state changes in real-time. 
Spatial Container State Observable 
```kotlin
open class SpatialContainerStateObservable(owner: SpatialContainerStateOwner)
```
Used to receive  SpatialContainer 's  SpatialContainerState  change and dispatch it to observers. 
Spatial Container State Observer 
```kotlin
interface SpatialContainerStateObserver
```
The observer for  SpatialContainerState . 
Spatial Container State Owner 
```kotlin
interface SpatialContainerStateOwner
```
For making the  SpatialContainer  as the owner of  SpatialContainerStateObserver . 
Spatial Container Type 
```kotlin
enum SpatialContainerType : Enum<SpatialContainerType>
```
The types of  SpatialContainer . 
Spatial View Content 
```kotlin
class SpatialViewContent : SpatialViewEntityManager, SpatialCoordinateSpaceConverter, SpatialViewEventManager
```
The content of a  SpatialView . Almost all functions towards 3D content in SpatialView are abilities of  SpatialViewContent , such as entity management, coordinate converting, and event subscription. 
Spatial View Entity Collection 
```kotlin
open class SpatialViewEntityCollection : Collection<Entity>
```
A  SpatialView  needs a  SpatialViewEntityCollection  to manage entities. 
Spatial View Entity Manager 
```kotlin
interface SpatialViewEntityManager
```
Interface to define content of  SpatialView  and operations about the content. 
Spatial View Event Manager 
```kotlin
interface SpatialViewEventManager
```
Provides event subscription for a  SpatialView 's content. 
## Functions
enforce Full Space 
```kotlin
fun Context.enforceFullSpace(pid: Int, uid: Int, message: String?)
```
Throws an  IllegalStateException  if the application identified by the given process and user ID is not running in a full space. Nothing will happen if your application is not running on PICO's spatial platform. 
enforce Self Full Space 
```kotlin
fun Context.enforceSelfFullSpace(message: String?)
```
Throws an  IllegalStateException  if your application is not running in a full space. Nothing will happen if your application is not running on PICO's spatial platform. 
get Self Space State 
```kotlin
fun Context.getSelfSpaceState(): SpaceState
```
Determines whether the application is running in a shared space or a full space. 
get Space State 
```kotlin
fun Context.getSpaceState(pid: Int, uid: Int): SpaceState
```
Determines whether the application identified by the given process and user ID is running in a shared space or a full space.