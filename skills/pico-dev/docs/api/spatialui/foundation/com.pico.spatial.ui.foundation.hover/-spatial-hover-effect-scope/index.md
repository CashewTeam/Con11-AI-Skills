# SpatialHoverEffectScope | PICO Spatial SDK

ui:foundation / com.pico.spatial.ui.foundation.hover / SpatialHoverEffectScope 
# SpatialHoverEffectScope
```kotlin
@Immutable
```interface  SpatialHoverEffectScope 
The scope of  spatialHoverEffect  DSL 
#### Inheritors
SpatialHoverEffectRootScope Members 
## Functions
alpha 
```kotlin
abstract fun alpha(@FloatRange(from = 0.0, to = 1.0) alpha: Float)
```
Sets transparency of the view 
clip Shape 
```kotlin
abstract fun clipShape(shape: RoundedCornerShape, size: IntSize, offset: IntOffset = IntOffset.Zero)
```
Clip the view with given  shape ,  size  and  offset 
offset 
```kotlin
abstract fun offset(offset: DpOffset)
```
```kotlin
abstract fun offset(x: Dp = 0.dp, y: Dp = 0.dp)
```
Sets the offset of the view 
rotate 
```kotlin
abstract fun rotate(degree: Float, origin: TransformOrigin = TransformOrigin.Center)
```
Rotate the view along z-axis by given  degree  and  origin 
scale 
```kotlin
abstract fun scale(scale: Float, origin: TransformOrigin = TransformOrigin.Center)
```
Scale the view by given  scale  and  origin 
```kotlin
abstract fun scale(scaleX: Float, scaleY: Float, origin: TransformOrigin = TransformOrigin.Center)
```
Scale the view by given  scaleX  and  scaleY  and  origin