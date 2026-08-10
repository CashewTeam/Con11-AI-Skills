# tween | PICO Spatial SDK

ui:foundation / com.pico.spatial.ui.foundation.hover / tween 
# tween
```kotlin
fun SpatialHoverEffectRootScope.tween(durationMillis: Int = AnimationConstants.DefaultDurationMillis, delayMillis: Int = 0, bezier: CubicBezier): SpatialHoverAnimation
```
Creates  Tween  animation for spatial hover effect. 
#### Return
a  SpatialHoverAnimation  with given  durationMillis  and  bezier . 
#### Parameters
duration Millis delay Millis bezier 
```kotlin
fun SpatialHoverEffectRootScope.tween(durationMillis: Int = AnimationConstants.DefaultDurationMillis, delayMillis: Int = 0, easing: Easing = FastOutSlowInEasing): SpatialHoverAnimation
```
Creates  Tween  animation for spatial hover effect. 
#### Return
a  SpatialHoverAnimation  with given  durationMillis ,  delayMillis  and  easing . 
#### Parameters
duration Millis delay Millis easing 
only support  CubicBezierEasing , if given  Easing  is not  CubicBezierEasing , will use  FastOutSlowInEasing  as default.