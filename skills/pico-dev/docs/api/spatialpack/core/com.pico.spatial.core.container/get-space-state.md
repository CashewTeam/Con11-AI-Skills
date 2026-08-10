# getSpaceState | PICO Spatial SDK

core / com.pico.spatial.core.container / getSpaceState 
# getSpaceState
```kotlin
fun Context.getSpaceState(pid: Int, uid: Int): SpaceState
```
Determines whether the application identified by the given process and user ID is running in a shared space or a full space. 
#### Return
Return  SpaceState.SHARED_SPACE  if the current space is a shared space; return  SpaceState.FULL_SPACE  if the current space is a full space; return  SpaceState.UNKNOWN  if the application is not running on PICO's spatial platform. 
#### Parameters
pid 
The process ID, which must be positive. 
uid 
The user ID.