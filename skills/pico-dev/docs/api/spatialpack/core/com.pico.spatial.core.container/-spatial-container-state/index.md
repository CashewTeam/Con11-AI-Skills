# SpatialContainerState | PICO Spatial SDK

core / com.pico.spatial.core.container / SpatialContainerState 
# SpatialContainerState
```kotlin
interface SpatialContainerState
```
The state of  SpatialContainer . 
Members 
## Properties
is Focused 
```kotlin
abstract val isFocused: Boolean
```
Whether the state of  SpatialContainer  is  SpatialContainerStateEvent.ON_FOCUSED . 
is Onstage 
```kotlin
abstract val isOnstage: Boolean
```
Whether the state of  SpatialContainer  is  SpatialContainerStateEvent.ON_STAGED . 
is Sighted 
```kotlin
abstract val isSighted: Boolean
```
Whether the state of  SpatialContainer  is  SpatialContainerStateEvent.ON_SIGHTED . 
## Functions
equals 
```kotlin
abstract operator override fun equals(other: Any?): Boolean
```hash Code 
```kotlin
abstract override fun hashCode(): Int
```