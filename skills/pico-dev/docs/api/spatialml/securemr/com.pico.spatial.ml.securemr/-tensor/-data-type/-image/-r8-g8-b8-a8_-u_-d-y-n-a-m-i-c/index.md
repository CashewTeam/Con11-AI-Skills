# R8G8B8A8_U_DYNAMIC | PICO Spatial SDK

spatialml:securemr / com.pico.spatial.ml.securemr / Tensor / DataType / Image / R8G8B8A8_U_DYNAMIC 
# R8G8B8A8_U_DYNAMIC
```kotlin
R8G8B8A8_U_DYNAMIC
```
32-bit pixel, interpreted as four 8-bit unsigned integer value (8 bits for RED, 8 bits for GREEN, 8 bits for BLUE and 8 bits for ALPHA). 
The difference between this and  R8G8B8A8_U  is: a tensor declared using this data type will be a "dynamic-texture" tensor, which means the tensor can be used as a texture for rendering. If the content of such a "dynamic-texture" tensor is updated, the texture will be updated automatically and synchronously, which is the reason why it is called  dynamic -texture.