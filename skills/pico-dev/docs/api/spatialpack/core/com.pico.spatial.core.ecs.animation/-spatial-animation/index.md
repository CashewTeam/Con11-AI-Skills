# SpatialAnimation | PICO Spatial SDK

core / com.pico.spatial.core.ecs.animation / SpatialAnimation 
# SpatialAnimation
```kotlin
open class SpatialAnimation
```
Represents the foundational information required for an animation, including its name, target binding, duration, repeat mode, and other essential properties. 
Notes: 
- 
This class serves as a base for defining animation details and cannot directly create an animation resource. 
- 
To generate an  com.pico.spatial.core.ecs.resource.AnimationResource , use one of its specialized subclasses, such as  TweenAnimation ,  OrbitAnimation , etc. 
#### Inheritors
OrbitAnimation TweenAnimation Members 
## Types
Companion 
```kotlin
object Companion
```
The companion object of  SpatialAnimation . 
## Properties
additive 
```kotlin
var additive: Boolean
```
Whether to add this animation additively over the current one. 
animation Bind Target 
```kotlin
var animationBindTarget: AnimationBindTarget?
```
The  AnimationBindTarget  of the animation. Defines which aspect of the entity is animated (position, rotation, scale, or a material property). 
delay 
```kotlin
var delay: Float
```
The delay before the animation starts, in seconds. This allows for a pause before the animation begins, which can be useful for synchronizing animations or creating staggered effects. 
duration 
```kotlin
var duration: Float
```
The duration of the animation in seconds. This specifies how long the animation will take to complete one cycle. It is an essential property that affects the speed and timing of the animation. 
name 
```kotlin
var name: String
```
The name of the animation. This is a descriptive identifier for the animation, which can be used to reference or manage animations within a system. It helps in distinguishing between different animations applied to entities. 
offset 
```kotlin
var offset: Float
```
The offset time in seconds of the animation. This is used to start the animation at a specific time offset, which can be useful for aligning animations that start at non-zero times or for creating complex sequences. 
repeat Count 
```kotlin
var repeatCount: Int
```
The repeat count of the animation. This specifies how many times the animation should repeat. A value of -1 means it will play infinitely; a value of 0 means it will play once; a value greater than 0 indicates multiple repetitions. 
repeat Mode 
```kotlin
var repeatMode: RepeatMode
```
The  RepeatMode  of the animation. This determines how the animation behaves after completing a cycle. It can be set to repeat, reverse, or not repeat at all, allowing for various looping behaviors. 
speed 
```kotlin
var speed: Float
```
The speed of the animation. This multiplier affects how fast the animation plays. A value greater than 1 speeds up the animation, while a value between 0 and 1 slows it down. 
trim Duration 
```kotlin
var trimDuration: Float?
```
The duration of the animation to trim, in seconds. This defines the portion of the animation that remains after trimming the start and end. It helps in focusing on a specific segment of the animation. 
trim End 
```kotlin
var trimEnd: Float?
```
The ending time of the animation to trim, in seconds. This property allows for trimming the animation's end, effectively cutting out the final portion of the animation sequence. 
trim Start 
```kotlin
var trimStart: Float?
```
The starting time of the animation to trim, in seconds. This property allows for trimming the animation's start, effectively cutting out the initial portion of the animation sequence. 
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