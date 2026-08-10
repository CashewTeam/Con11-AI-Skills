# frameSize | PICO Spatial SDK

core / com.pico.spatial.core.ecs.audio / AudioStreamBufferData / frameSize 
# frameSize
```kotlin
val frameSize: Long
```
Memory size of individual frame. 
Calculated as: channel count × bytes per sample. Example: 2 channels × 2 bytes (INT16) = 4 bytes per frame.