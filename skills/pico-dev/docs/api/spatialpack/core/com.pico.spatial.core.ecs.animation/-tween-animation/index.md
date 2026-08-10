# TweenAnimation | PICO Spatial SDK

core / com.pico.spatial.core.ecs.animation / TweenAnimation 
# TweenAnimation
```kotlin
class TweenAnimation : SpatialAnimation
```
Represents a type of animation for "from-to-by" behavior. 
PICO Spatial SDK supports four combinations of  TweenAnimation : FromTo, FromBy, To, and By. If any other combinations are constructed, they will not function as intended because the system cannot perform interpolation calculations with the given data. 
Additionally, a corresponding BindTarget is required for applying an animation to an entity. For instance, to change an entity's position, use  bindTarget = AnimationBindTarget.bindPosition()  to indicate that the animation should modify the entity's position values. In this case, the type of input parameter for fromValue, toValue, and byValue should be Vector3. Refer to the documentation of the static functions in  AnimationBindTarget  for the types of input parameter required by different types of bindTarget. 
### Code sample:

```
// Create a position animation for an entity.val animation = TweenAnimation.createTweenAnimation(    bindTarget = AnimationBindTarget.bindPosition(),    to = Vector3(-7F, 5.5F, -11F),    repeatMode = RepeatMode.RESTART,    repeatCount = 100,    duration = 2F)val animationResource = AnimationResource.generateWithTweenAnimation(animation)val entity = Entity()entity.playAnimation(animationResource)// Create a base color animation for an entity.val colorAnimation = TweenAnimation.createTweenAnimation(    bindTarget = AnimationBindTarget.bindMaterial(0, MaterialTarget.BASE_COLOR),    from = Color4.fromLinearHex("5CCF6BFF"), // Starting color    to = Color4.BLUE,                        // Ending color    repeatMode = RepeatMode.RESTART,    repeatCount = 100,    duration = 2F)val colorAnimationResource = AnimationResource.generateWithTweenAnimation(colorAnimation)entity.playAnimation(colorAnimationResource)
```Members 
## Types
Companion 
```kotlin
object Companion
```
The companion of  TweenAnimation . 
## Properties
ease Type 
```kotlin
var easeType: EaseType
```
The  EaseType  of the animation. This defines the rate of change of the animation over time, allowing for effects such as acceleration, deceleration, or linear motion. It affects the smoothness, style, and realism of the animation. 
## Functions
additive 
```kotlin
fun additive(additive: Boolean): TweenAnimation
```
Sets if this animation is additive. 
bind Target 
```kotlin
fun bindTarget(animationBindTarget: AnimationBindTarget): TweenAnimation
```
Sets the  AnimationBindTarget  of the animation. 
delay 
```kotlin
fun delay(delay: Float): TweenAnimation
```
Sets the delay before the animation starts, in seconds. 
duration 
```kotlin
fun duration(duration: Float): TweenAnimation
```
Sets the duration of the animation. 
ease Type 
```kotlin
fun easeType(easeType: EaseType): TweenAnimation
```
Sets the ease type of the animation. 
equals 
```kotlin
open operator override fun equals(other: Any?): Boolean
```hash Code 
```kotlin
open override fun hashCode(): Int
```name 
```kotlin
fun name(name: String): TweenAnimation
```
Sets the name of the animation. 
offset 
```kotlin
fun offset(offset: Float): TweenAnimation
```
Sets the offset time of animation. 
repeat Count 
```kotlin
fun repeatCount(repeatCount: Int): TweenAnimation
```
Sets how many times the animation should repeat. 
repeat Mode 
```kotlin
fun repeatMode(repeatMode: RepeatMode): TweenAnimation
```
Sets the repeat mode of animation. 
speed 
```kotlin
fun speed(speed: Float): TweenAnimation
```
Sets the speed of the animation. 
to String 
```kotlin
open override fun toString(): String
```trim Duration 
```kotlin
fun trimDuration(trimDuration: Float): TweenAnimation
```
Sets the duration of the animation to trim, in seconds. 
trim End 
```kotlin
fun trimEnd(trimEnd: Float): TweenAnimation
```
Sets the end time (in seconds) at which to trim the animation. 
trim Start 
```kotlin
fun trimStart(trimStart: Float): TweenAnimation
```
Sets the start time (in seconds) from which to begin trimming the animation.