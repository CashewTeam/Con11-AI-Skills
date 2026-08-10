# getSelfSpaceState | PICO Spatial SDK

core / com.pico.spatial.core.container / getSelfSpaceState 
# getSelfSpaceState
```kotlin
fun Context.getSelfSpaceState(): SpaceState
```
Determines whether the application is running in a shared space or a full space. 
#### Return
SpaceState.SHARED_SPACE  if the current space is a shared space;  SpaceState.FULL_SPACE  if the current space is a full space;  SpaceState.UNKNOWN  if the application is not running on PICO's spatial platform.