# SpatialContainerStateEvent | PICO Spatial SDK

core / com.pico.spatial.core.container / SpatialContainerStateEvent 
# SpatialContainerStateEvent
```kotlin
enum SpatialContainerStateEvent : Enum<SpatialContainerStateEvent>
```
Represents the events that trigger state transitions for a  SpatialContainer . These events describe changes in the  SpatialContainer 's  SpatialContainerState , which are triggered by focus, overlapping and occlusion, or camera visibility transitions. The events can be used to track and react to state changes in real-time. 
## State Machine
The state machine transitions between states based on the following events: 

```
| Current State |    Event   | Next State |  Transition Description                                ||---------------|------------|------------|--------------------------------------------------------||Any            |ON_FOCUSED  |Focused     |The container gains focus.                              ||Focused        |ON_UNFOCUSED|Unfocused   |The container loses focus.                              ||Any            |ON_SIGHTED  |Sighted     |The container enters the camera's field of view.        ||Sighted        |ON_UNSIGHTED|Unsighted   |The container leaves the camera's field of view.        ||Staged         |ON_UNSTAGED |Unstaged    |The container is no longer fully visible or is occluded.||Unstaged       |ON_SIGHTED  |Sighted     |The container re-enters the camera's field of view.     ||Unstaged       |ON_STAGED   |Staged      |The container becomes fully visible and not occluded.   |
```
Definitions: 
- 
Sighted : The  SpatialContainer  is within the camera's field of view. 
- 
Unsighted : The  SpatialContainer  is outside the camera's field of view. 
- 
Staged : The  SpatialContainer  is fully visible and not occluded. 
- 
Unstaged : The  SpatialContainer  is no longer fully visible or is occluded. 
- 
Focused : The  SpatialContainer  gains focus. 
- 
Unfocused : The  SpatialContainer  loses focus. 
Members Entries 
## Entries
ON_FOCUSED 
```kotlin
ON_FOCUSED
```
Event indicates that the  SpatialContainer  gains focus. 
ON_UNFOCUSED 
```kotlin
ON_UNFOCUSED
```
Event indicates that the  SpatialContainer  loses focus. 
ON_SIGHTED 
```kotlin
ON_SIGHTED
```
Event indicates that the  SpatialContainer  enters the camera's field of view. 
ON_UNSIGHTED 
```kotlin
ON_UNSIGHTED
```
Event indicates that the  SpatialContainer  leaves the camera's field of view. 
ON_STAGED 
```kotlin
ON_STAGED
```
Event indicates that the  SpatialContainer  becomes staged (is fully visible and not occluded). 
ON_UNSTAGED 
```kotlin
ON_UNSTAGED
```
Event indicates that the  SpatialContainer  becomes unstaged (is no longer fully visible or is occluded). 
## Properties
entries 
```kotlin
val entries: EnumEntries<SpatialContainerStateEvent>
```
Returns a representation of an immutable list of all enum entries, in the order they're declared. 
## Functions
value Of 
```kotlin
fun valueOf(value: String): SpatialContainerStateEvent
```
Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.) 
values 
```kotlin
fun values(): Array<SpatialContainerStateEvent>
```
Returns an array containing the constants of this enum type, in the order they're declared.