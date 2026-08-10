# AnimationPlayConfig | PICO Spatial SDK

core / com.pico.spatial.core.ecs.animation / AnimationPlayConfig 
# AnimationPlayConfig
```kotlin
class AnimationPlayConfig
```
Configuration for playing animations. 
Members 
## Constructors
Animation Play Config 
```kotlin
constructor(transitionDuration: Float = 0.0f, transitionMode: AnimationTransitionMode = AnimationTransitionMode.DEFAULT, blendLayer: Int = -1, blendWeight: Float = 1.0f)
```
Creates a configuration. 
## Properties
blend Layer 
```kotlin
val blendLayer: Int
```
The blend layer value to use for playing the animation. 
blend Weight 
```kotlin
val blendWeight: Float
```
The blend weight value to use for playing the animation. 
transition Duration 
```kotlin
val transitionDuration: Float
```
Transition duration in seconds. 0 means switch immediately, values greater than 0 will linearly blend from the current state to the target state over the specified time. 
transition Mode 
```kotlin
val transitionMode: AnimationTransitionMode
```
The transition mode value to use for playing the animation.