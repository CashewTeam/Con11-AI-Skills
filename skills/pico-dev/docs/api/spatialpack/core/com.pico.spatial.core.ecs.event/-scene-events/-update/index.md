# Update | PICO Spatial SDK

core / com.pico.spatial.core.ecs.event / SceneEvents / Update 
# Update
```kotlin
class Update : Event
```
Event raised after the scene is updated. 
Members 
## Properties
delta Time 
```kotlin
val deltaTime: Float
```
The time elapsed since the last update. 
scene 
```kotlin
val scene: Scene
```
The target scene. 
## Functions
to String 
```kotlin
open override fun toString(): String
```