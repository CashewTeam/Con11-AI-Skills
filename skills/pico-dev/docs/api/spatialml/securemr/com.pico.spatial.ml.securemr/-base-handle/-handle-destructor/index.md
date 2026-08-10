# HandleDestructor | PICO Spatial SDK

spatialml:securemr / com.pico.spatial.ml.securemr / BaseHandle / HandleDestructor 
# HandleDestructor
```kotlin
abstract class HandleDestructor(target: BaseHandle) : PhantomReference<BaseHandle>
```
As a  BaseHandle  may container native resources that must be released when the handle is out of scope, this class provides a structure to bundle the destruction callback with necessary data (like opaque IDs or internal handles) to be used during the destruction. 
Members 
## Constructors
Handle Destructor 
```kotlin
constructor(target: BaseHandle)
```
## Functions
destroy 
```kotlin
abstract fun destroy()
```
The method that each implementation of  BaseHandle  should provide, to clear up its own resources during destruction.