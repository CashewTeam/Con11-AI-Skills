# com.pico.spatial.sense.base | PICO Spatial SDK

sense / com.pico.spatial.sense.base 
# Package-level declarations
Types 
## Types
Anchor 
```kotlin
open class Anchor
```
The base class for all anchors, such as WorldAnchor, MeshAnchor, PlaneAnchor, etc. 
Anchor Update 
```kotlin
@RequiredFullSpace
```class  AnchorUpdate < T  :  Anchor > 
Represents an update event for a world anchor. 
Anchor Update Subscriber 
```kotlin
fun interface AnchorUpdateSubscriber<T : Anchor>
```
AnchorUpdateSubscriber is a subscriber for anchor update events. 
Semantic Label Type 
```kotlin
enum SemanticLabelType : Enum<SemanticLabelType>
```
Represents the semantic label type of mesh anchor. 
Tracking State 
```kotlin
enum TrackingState : Enum<TrackingState>
```
Represents the various states of the tracking manager during its lifecycle. This enum is used to indicate the current operational state of the tracking manager.