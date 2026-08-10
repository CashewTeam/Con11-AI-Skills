# Directivity | PICO Spatial SDK

core / com.pico.spatial.core.ecs.audio / Directivity / Directivity 
# Directivity
```kotlin
constructor(@FloatRange(from = 0.0, to = 1.0) pattern: Float = 0.0f, @FloatRange(from = 0.0) sharpness: Float = 0.0f)
```
Constructor of audio directivity. 
#### Parameters
pattern 
The pattern of audio directivity. Value range: 0.0, 1.0. The default value is 0.0f. 
sharpness 
The sharpness of the directivity. Value range: 0.0, Float.MAX_VALUE. The default value is 0.0f.