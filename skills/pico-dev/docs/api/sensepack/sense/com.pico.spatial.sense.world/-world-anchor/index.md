# WorldAnchor | PICO Spatial SDK

sense / com.pico.spatial.sense.world / WorldAnchor 
# WorldAnchor
```kotlin
@RequiredFullSpace
```class  WorldAnchor  :  Anchor 
Represents a world anchor with a unique identifier (UUID), name, position, and rotation. 
This class is used to define an anchor in a 3D space with a specific position and orientation. Each anchor is assigned a UUID, which ensures its uniqueness within the application. You can utilize UUIDs to reload or manage anchors across application sessions as needed. 
Members 
## Properties
anchor UUID 
```kotlin
val anchorUUID: UUID
```
The UUID of the anchor, which ensures that each anchor is unique and identifiable within the application. 
name 
```kotlin
val name: String
```
The name of the anchor, which can be used to identify or categorize the anchor. 
transform 
```kotlin
val transform: Transform
```
The transform of the anchor, including its position, rotation, and scale. The default scale is always set to Vector3(1f, 1f, 1f). 
## Functions
equals 
```kotlin
open operator override fun equals(other: Any?): Boolean
```hash Code 
```kotlin
open override fun hashCode(): Int
```to String 
```kotlin
open override fun toString(): String
```