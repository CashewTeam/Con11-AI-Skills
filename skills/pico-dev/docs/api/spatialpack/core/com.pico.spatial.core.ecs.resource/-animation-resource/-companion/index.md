# Companion | PICO Spatial SDK

core / com.pico.spatial.core.ecs.resource / AnimationResource / Companion 
# Companion
```kotlin
object Companion
```
The companion object of  AnimationResource . 
Members 
## Functions
generate 
```kotlin
@JvmStatic
```fun  generate ( animation :  SpatialAnimation ) :  AnimationResource 
Generates an  AnimationResource  instance based on the provided subclass of  SpatialAnimation . 
generate With Tween Animation 
```kotlin
@JvmStatic
```fun  generateWithTweenAnimation ( animation :  TweenAnimation ) :  AnimationResource 
Generates an  AnimationResource  instance for the from-to-by animation. 
group 
```kotlin
@JvmStatic
```fun  group ( with :  List < AnimationResource > ) :  AnimationResource 
Groups multiple  AnimationResource  objects into a single  AnimationResource . 
sequence 
```kotlin
@JvmStatic
```fun  sequence ( with :  List < AnimationResource > ) :  AnimationResource 
Creates a sequence of multiple  AnimationResource  objects in the given list order.