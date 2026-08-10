# R8G8B8_U_DYNAMIC | PICO Spatial SDK

spatialml:securemr / com.pico.spatial.ml.securemr / Tensor / DataType / Image / R8G8B8_U_DYNAMIC 
# R8G8B8_U_DYNAMIC
```kotlin
R8G8B8_U_DYNAMIC
```
24-bit pixel, interpreted as three 8-bit unsigned integer value (8 bits for RED, 8 bits for GREEN and 8 bits for BLUE). 
The difference between this and  R8G8B8_U  is: a tensor declared using this data type will be a "dynamic-texture" tensor, which means the tensor can be used as a texture for rendering. If the content of such a "dynamic-texture" tensor is updated, the texture will be updated automatically and synchronously, which is the reason why it is called  dynamic -texture.