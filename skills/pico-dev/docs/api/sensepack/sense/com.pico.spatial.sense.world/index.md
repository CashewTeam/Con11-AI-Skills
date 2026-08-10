# com.pico.spatial.sense.world | PICO Spatial SDK

sense / com.pico.spatial.sense.world 
# Package-level declarations
Types 
## Types
World Anchor 
```kotlin
@RequiredFullSpace
```class  WorldAnchor  :  Anchor 
Represents a world anchor with a unique identifier (UUID), name, position, and rotation. 
World Tracking Manager 
```kotlin
@RequiredFullSpace
```object  WorldTrackingManager 
Provides world tracking functionalities, including managing and updating anchors. 
World Tracking Result 
```kotlin
@RequiredFullSpace
```sealed  class  WorldTrackingResult < out  T > 
Encapsulates the outcome of an operation, providing a type-safe mechanism to handle successes or errors in a unified manner.