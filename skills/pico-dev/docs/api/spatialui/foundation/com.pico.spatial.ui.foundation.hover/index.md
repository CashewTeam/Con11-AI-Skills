# com.pico.spatial.ui.foundation.hover | PICO Spatial SDK

ui:foundation / com.pico.spatial.ui.foundation.hover 
# Package-level declarations
Types Functions Properties 
## Types
Cubic Bezier 
```kotlin
interface CubicBezier
```
Cubic Bezier curve. 
Spatial Hover Animation 
```kotlin
sealed interface SpatialHoverAnimation
```
Defines SpatialHoverEffects how to animate between active & inactive states 
Spatial Hover Effect Context 
```kotlin
interface SpatialHoverEffectContext
```
Holds the context of  spatialHoverEffect 
Spatial Hover Effect Group 
```kotlin
class SpatialHoverEffectGroup
```
Represents a group for managing spatial hover effects. Each instance has a unique group ID for identifying the group. 
Spatial Hover Effect Root Scope 
```kotlin
interface SpatialHoverEffectRootScope : SpatialHoverEffectScope
```
The root scope of  spatialHoverEffect  DSL, here can call  animation 
Spatial Hover Effect Scope 
```kotlin
@Immutable
```interface  SpatialHoverEffectScope 
The scope of  spatialHoverEffect  DSL 
## Properties
Linear Easing 
```kotlin
val LinearEasing: CubicBezier
```
Linear bezier curve. 
Rectangle Shape 
```kotlin
val RectangleShape: RoundedCornerShape
```
For  SpatialHoverEffectScope.clipShape  convenience, a  RoundedCornerShape  with 0 radius. 
## Functions
Cubic Bezier 
```kotlin
@Stable
```fun  CubicBezier ( a :  Float ,  b :  Float ,  c :  Float ,  d :  Float ) :  CubicBezier disable Spatial Hover Effect 
```kotlin
fun Modifier.disableSpatialHoverEffect(disabled: Boolean): Modifier
```
Disable all child nodes' hover effect effects. 
spatial Hover Effect 
```kotlin
@Stable
```fun  Modifier . spatialHoverEffect ( block :  SpatialHoverEffectRootScope . ( SpatialHoverEffectContext )  ->  Unit ) :  Modifier 
Defines how view should change when a pointer hover or eye looks at the view Unlike  androidx.compose.foundation.hoverable , the SpatialHoverEffect is applied out of process, so it can not be visible to app process 
```kotlin
fun Modifier.spatialHoverEffect(style: SpatialHoverStyle = SpatialHoverStyle.Default, enabled: Boolean = true): Modifier
```
Applies a spatial hover effect to the element. 
spatial Hover Effect Group 
```kotlin
fun Modifier.spatialHoverEffectGroup(): Modifier
```
Adds a default HoverEffectGroup to all effects defined on descendant views, and activates the group whenever this view or any descendant views are hovered. 
```kotlin
fun Modifier.spatialHoverEffectGroup(group: SpatialHoverEffectGroup, enable: Boolean = true): Modifier
```
Adds a HoverEffectGroup to all effects defined on descendant views, and activates the group whenever this view or any descendant views are hovered. 
spring 
```kotlin
fun SpatialHoverEffectRootScope.spring(dampingRatio: Float = HoverAnimationDefaults.DefaultDumpingRatio, stiffness: Float = HoverAnimationDefaults.DefaultStiffness, delayMillis: Int = 0): SpatialHoverAnimation
```
Creates  Spring  animation. 
to Cubic Bezier 
```kotlin
fun Easing.toCubicBezier(default: () -> CubicBezier = { LinearEasing }): CubicBezier
```
Helper for converts  CubicBezierEasing  to  CubicBezier . 
tween 
```kotlin
fun SpatialHoverEffectRootScope.tween(durationMillis: Int = AnimationConstants.DefaultDurationMillis, delayMillis: Int = 0, easing: Easing = FastOutSlowInEasing): SpatialHoverAnimation
```
```kotlin
fun SpatialHoverEffectRootScope.tween(durationMillis: Int = AnimationConstants.DefaultDurationMillis, delayMillis: Int = 0, bezier: CubicBezier): SpatialHoverAnimation
```
Creates  Tween  animation for spatial hover effect.