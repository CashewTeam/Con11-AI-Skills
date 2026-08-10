# fromLinearColor | PICO Spatial SDK

foundation / com.pico.spatial.core.math / Color4 / Companion / fromLinearColor 
# fromLinearColor
```kotlin
@JvmStatic
```fun  fromLinearColor ( linearColor :  Vector4 ) :  Color4 
Creates a  Color4  from a linear-light RGBA color. 
The input linearColor is interpreted as linear RGB (R, G, B). These channels are encoded to sRGB/gamma and stored in this  Color4  as normalized 0..1 values. Alpha is treated as linear and passed through (clamped to 0..1). 
#### Return
A  Color4  containing sRGB/gamma-encoded 0..1 channels. 
#### Parameters
linear Color 
Linear-light RGBA values. RGB is expected in 0..1.