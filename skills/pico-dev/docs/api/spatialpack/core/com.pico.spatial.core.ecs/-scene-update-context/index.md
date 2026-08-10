# SceneUpdateContext | PICO Spatial SDK

core / com.pico.spatial.core.ecs / SceneUpdateContext 
# SceneUpdateContext
```kotlin
class SceneUpdateContext
```
The context used to update scene. 
It is used to query  Entity  and  Component . 
Members 
## Properties
delta Time 
```kotlin
val deltaTime: Float
```
The delta time than the last updating. 
scene 
```kotlin
val scene: Scene
```
The  Scene  used to query Entities and Components.