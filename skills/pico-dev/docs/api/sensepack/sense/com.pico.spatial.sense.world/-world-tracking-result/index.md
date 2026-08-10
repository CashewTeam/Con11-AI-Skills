# WorldTrackingResult | PICO Spatial SDK

sense / com.pico.spatial.sense.world / WorldTrackingResult 
# WorldTrackingResult
```kotlin
@RequiredFullSpace
```sealed  class  WorldTrackingResult < out  T > 
Encapsulates the outcome of an operation, providing a type-safe mechanism to handle successes or errors in a unified manner. 
#### Parameters
T 
The type of data returned for successful operations. 
#### Inheritors
Success Error Members 
## Constructors
World Tracking Result 
```kotlin
protected constructor()
```
## Types
Error 
```kotlin
class Error : WorldTrackingResult<Nothing>
```
Represents an error for an operation. 
Success 
```kotlin
class Success<out T> : WorldTrackingResult<T>
```
Represents a success for an operation.