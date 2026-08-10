# R8_U_DYNAMIC | PICO Spatial SDK

spatialml:securemr / com.pico.spatial.ml.securemr / Tensor / DataType / Image / R8_U_DYNAMIC 
# R8_U_DYNAMIC
```kotlin
R8_U_DYNAMIC
```
8-bit pixel, interpreted as one unsigned integer value only. 
The difference between this and  R8_U  is: a tensor declared using this data type will be a "dynamic-texture" tensor, which means the tensor can be used as a texture for rendering. If the content of such a "dynamic-texture" tensor is updated, the texture will be updated automatically and synchronously, which is the reason why it is called  dynamic -texture.