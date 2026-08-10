# R_FLOAT_DYNAMIC | PICO Spatial SDK

spatialml:securemr / com.pico.spatial.ml.securemr / Tensor / DataType / Image / R_FLOAT_DYNAMIC 
# R_FLOAT_DYNAMIC
```kotlin
R_FLOAT_DYNAMIC
```
32-bit pixel, interpreted as one single-precision floating-point value only. 
The difference between this and  R_FLOAT  is: a tensor declared using this data type will be a "dynamic-texture" tensor, which means the tensor can be used as a texture for rendering. If the content of such a "dynamic-texture" tensor is updated, the texture will be updated automatically and synchronously, which is the reason why it is called  dynamic -texture.