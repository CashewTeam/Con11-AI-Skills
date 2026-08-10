# AnimationPlayConfig | PICO Spatial SDK

core / com.pico.spatial.core.ecs.animation / AnimationPlayConfig / AnimationPlayConfig 
# AnimationPlayConfig
```kotlin
constructor(transitionDuration: Float = 0.0f, transitionMode: AnimationTransitionMode = AnimationTransitionMode.DEFAULT, blendLayer: Int = -1, blendWeight: Float = 1.0f)
```
Creates a configuration. 
#### Parameters
transition Duration 
Transition duration in seconds.     - 0 means switch immediately.     - Values greater than 0 will linearly blend from the current state to the target state       over the specified time.     - Negative values are clamped to 0f. 
transition Mode 
The transition mode used for playing the animation. When set to  AnimationTransitionMode.DEFAULT , skeletal animations will use the CROSSFADE mode, while other animations will use the COMPOSE mode. 
blend Layer 
The blend layer used for playing the animation. A value of -1 means the animation is played on the default blend layer. 
blend Weight 
The blend weight used for playing the animation. Controls how much this animation contributes to the final blended result. Valid range is 0, 1, values outside the range will be clamped, and the default value 1 means full contribution.