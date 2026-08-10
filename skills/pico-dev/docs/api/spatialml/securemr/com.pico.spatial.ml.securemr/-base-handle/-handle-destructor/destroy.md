# destroy | PICO Spatial SDK

spatialml:securemr / com.pico.spatial.ml.securemr / BaseHandle / HandleDestructor / destroy 
# destroy
```kotlin
abstract fun destroy()
```
The method that each implementation of  BaseHandle  should provide, to clear up its own resources during destruction. 
Note : because the method will be called after the implementation class is gone, so  no  members of the implementation class shall be used inside  destroy() . Instead, you may need to capture the needed members (such as the opaque handle ID) inside its inheritance of  HandleDestructor .