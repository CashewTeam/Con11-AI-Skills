# isDynamicTexture | PICO Spatial SDK

spatialml:securemr / com.pico.spatial.ml.securemr / Tensor / InitInfo / isDynamicTexture 
# isDynamicTexture
```kotlin
val isDynamicTexture: Boolean
```
Whether this tensor is a dynamic-texture tensor. 
A dynamic-texture tensor is a multi-dimensional texture created with datatype:  DataType.Image.R8_U_DYNAMIC ,  DataType.Image.R8G8_U_DYNAMIC ,  DataType.Image.R8G8B8_U_DYNAMIC ,  DataType.Image.R8G8B8A8_U_DYNAMIC  or  DataType.Image.R_FLOAT_DYNAMIC . 
If  true , the tensor can thereafter be used as texture for rendering. Modifying the content of the tensor will automatically and synchronously update the texture. 
#### See also
Tensor. Multi Dimensional Init Info Tensor. DataType. Image