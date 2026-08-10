# toLinearColor | PICO Spatial SDK

foundation / com.pico.spatial.core.math / Color4 / toLinearColor 
# toLinearColor
```kotlin
fun toLinearColor(): Vector4
```
Decodes this  Color4  from sRGB/gamma-encoded 0..1 channels into linear RGB. 
The returned  Vector4  contains linear-light R, G, B in the 0..1 range. Alpha is passed through unchanged (alpha is treated as linear). 
#### Return
A  Vector4  holding linear-light RGBA values.