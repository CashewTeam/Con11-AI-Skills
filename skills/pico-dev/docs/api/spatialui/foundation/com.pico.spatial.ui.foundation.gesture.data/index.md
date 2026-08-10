# com.pico.spatial.ui.foundation.gesture.data | PICO Spatial SDK

ui:foundation / com.pico.spatial.ui.foundation.gesture.data 
# Package-level declarations
Types 
## Types
Input Device Pose 
```kotlin
@Immutable
```class  InputDevicePose ( val  rawPosition :  Offset3D ,  val  rawRotation :  Rotation3D ) 
Pose of input device. 
Interaction Kind 
```kotlin
enum InteractionKind : Enum<InteractionKind>
```
InteractionKind is used to describe the kind of interaction that is currently being performed.