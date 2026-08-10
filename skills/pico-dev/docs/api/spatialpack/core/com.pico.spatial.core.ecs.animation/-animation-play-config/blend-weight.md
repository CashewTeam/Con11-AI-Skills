# blendWeight | PICO Spatial SDK

core / com.pico.spatial.core.ecs.animation / AnimationPlayConfig / blendWeight 
# blendWeight
```kotlin
val blendWeight: Float
```
The blend weight value to use for playing the animation. 
Controls how much this animation contributes to the final blended animation result. Valid range is 0, 1. Values outside the range will be clamped to 0, 1. 
The default value is 1, which means the animation will contribute fully to the blended result. If set to 0, the animation has no effect on the final result. Values between 0, 1: the animation is mixed proportionally with other active animations.