# toSRGBByte | PICO Spatial SDK

foundation / com.pico.spatial.core.math / Color4 / toSRGBByte 
# toSRGBByte
```kotlin
fun toSRGBByte(): Vector4
```
Converts this  Color4  (sRGB/gamma-encoded channels in the 0..1 range) into 8-bit-per-channel sRGB (RGBA8) values. 
The returned  Vector4  stores components in the 0..255 range as floats (R, G, B, A), rounded to the nearest integer and clamped to 0, 255. Alpha is treated as linear and is quantized the same way. 
#### Return
A  Vector4  containing RGBA8 sRGB values (0..255).