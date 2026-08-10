# SpatialHoverEffectRootScope | PICO Spatial SDK

ui:foundation / com.pico.spatial.ui.foundation.hover / SpatialHoverEffectRootScope 
# SpatialHoverEffectRootScope
```kotlin
interface SpatialHoverEffectRootScope : SpatialHoverEffectScope
```
The root scope of  spatialHoverEffect  DSL, here can call  animation 
Members Members & Extensions 
## Functions
animation 
```kotlin
abstract fun animation(animation: SpatialHoverAnimation = tween(), block: SpatialHoverEffectScope.() -> Unit)
```
Specify the  animation  for sub-scope effects 
spring 
```kotlin
fun SpatialHoverEffectRootScope.spring(dampingRatio: Float = HoverAnimationDefaults.DefaultDumpingRatio, stiffness: Float = HoverAnimationDefaults.DefaultStiffness, delayMillis: Int = 0): SpatialHoverAnimation
```
Creates  Spring  animation. 
tween 
```kotlin
fun SpatialHoverEffectRootScope.tween(durationMillis: Int = AnimationConstants.DefaultDurationMillis, delayMillis: Int = 0, easing: Easing = FastOutSlowInEasing): SpatialHoverAnimation
```
```kotlin
fun SpatialHoverEffectRootScope.tween(durationMillis: Int = AnimationConstants.DefaultDurationMillis, delayMillis: Int = 0, bezier: CubicBezier): SpatialHoverAnimation
```
Creates  Tween  animation for spatial hover effect.