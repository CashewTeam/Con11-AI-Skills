# enforceSelfFullSpace | PICO Spatial SDK

core / com.pico.spatial.core.container / enforceSelfFullSpace 
# enforceSelfFullSpace
```kotlin
fun Context.enforceSelfFullSpace(message: String?)
```
Throws an  IllegalStateException  if your application is not running in a full space. Nothing will happen if your application is not running on PICO's spatial platform. 
#### Throws
Illegal State Exception 
This exception is thrown if the current process is not running in a full space.