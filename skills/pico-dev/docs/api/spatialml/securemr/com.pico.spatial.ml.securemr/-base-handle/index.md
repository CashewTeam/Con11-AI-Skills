# BaseHandle | PICO Spatial SDK

spatialml:securemr / com.pico.spatial.ml.securemr / BaseHandle 
# BaseHandle
```kotlin
interface BaseHandle
```
The base for all top-level SpatialML handles. 
#### See also
Spatial MLSession Global Tensor Pipeline 
#### Inheritors
GlobalTensor Pipeline SpatialMLSession Members 
## Types
Handle Destructor 
```kotlin
abstract class HandleDestructor(target: BaseHandle) : PhantomReference<BaseHandle>
```
As a  BaseHandle  may container native resources that must be released when the handle is out of scope, this class provides a structure to bundle the destruction callback with necessary data (like opaque IDs or internal handles) to be used during the destruction. 
## Properties
destructor 
```kotlin
abstract val destructor: BaseHandle.HandleDestructor
```
The  BaseHandle 's implementation's destructor.