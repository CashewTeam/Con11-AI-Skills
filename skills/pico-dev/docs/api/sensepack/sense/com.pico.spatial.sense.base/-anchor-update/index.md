# AnchorUpdate | PICO Spatial SDK

sense / com.pico.spatial.sense.base / AnchorUpdate 
# AnchorUpdate
```kotlin
@RequiredFullSpace
```class  AnchorUpdate < T  :  Anchor > 
Represents an update event for a world anchor. 
Members 
## Types
Event 
```kotlin
enum Event : Enum<AnchorUpdate.Event>
```
Enumerates the possible types of anchor update events. 
## Properties
anchor 
```kotlin
val anchor: T
```
Depends on the type of anchor update, this can be a specific anchor type. 
event 
```kotlin
val event: AnchorUpdate.Event
```
The specific event type for this anchor update, derived from the event value.