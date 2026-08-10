# enforceFullSpace | PICO Spatial SDK

core / com.pico.spatial.core.container / enforceFullSpace 
# enforceFullSpace
```kotlin
fun Context.enforceFullSpace(pid: Int, uid: Int, message: String?)
```
Throws an  IllegalStateException  if the application identified by the given process and user ID is not running in a full space. Nothing will happen if your application is not running on PICO's spatial platform. 
#### Parameters
pid 
The process ID, which must be positive. 
uid 
The user ID. 
message 
The message included in the exception if it is thrown. 
#### Throws
Illegal State Exception 
This exception is thrown if the current application is not running in a full space.