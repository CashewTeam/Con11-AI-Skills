# com.pico.spatial.core.ecs.animation | PICO Spatial SDK

core / com.pico.spatial.core.ecs.animation 
# Package-level declarations
Types 
## Types
Animation Bind Target 
```kotlin
class AnimationBindTarget
```
The properties that can be animated in tween animations. 
Animation Playback Controller 
```kotlin
@MainThread
```class  AnimationPlaybackController  :  Closeable 
A controller that manages animation playback. 
Animation Play Config 
```kotlin
class AnimationPlayConfig
```
Configuration for playing animations. 
Animation Transition Mode 
```kotlin
enum AnimationTransitionMode : Enum<AnimationTransitionMode>
```
The transition mode the play animation method performs between a current animation and a new animation. 
Ease Type 
```kotlin
enum EaseType : Enum<EaseType>
```
Provides functions or algorithms used for animation interpolation, which are used to control the rate of change of an animation object over the timeline. 
Material Target 
```kotlin
enum MaterialTarget : Enum<MaterialTarget>
```
Describes a reference to an animated material property. 
Orbit Animation 
```kotlin
class OrbitAnimation : SpatialAnimation
```
OrbitAnimation describes an orbital (revolution) animation of an object moving around a given axis. 
Repeat Mode 
```kotlin
enum RepeatMode : Enum<RepeatMode>
```
Controls how an animation behaves when it reaches the end. The animation's repeat count must be set to a positive integer or '-1' for this property to have an effect. 
Skeleton 
```kotlin
class Skeleton
```
Skeleton information. 
Skeleton Joint 
```kotlin
class SkeletonJoint
```
Data of a joint in a skeleton. 
Spatial Animation 
```kotlin
open class SpatialAnimation
```
Represents the foundational information required for an animation, including its name, target binding, duration, repeat mode, and other essential properties. 
Tween Animation 
```kotlin
class TweenAnimation : SpatialAnimation
```
Represents a type of animation for "from-to-by" behavior.