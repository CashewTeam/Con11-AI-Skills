# readbackAsTextureResource | PICO Spatial SDK

spatialml:readback / com.pico.spatial.ml.readback / readbackAsTextureResource 
# readbackAsTextureResource
```kotlin
@RequiresApi(value = 27)
```fun  GlobalTensor . readbackAsTextureResource ( ) :  TextureResource 
If a  GlobalTensor  is a dynamic-texture one, you can use this method to read it back as a  TextureResource -compatible dynamic texture. You can use the dynamic texture as maps in your application's material, so that when the tensor's content is changed by SpatialML framework, the materials using the returned dynamic texture will all be updated automatically. 
If the current SpatialML session to which the  GlobalTensor  belongs utilizes the see-through camera data in any of its pipelines, the application  must  have the Android camera permission granted by users. 
If the current SpatialML session to which the  GlobalTensor  belongs utilizes the spatial-data data in any of its pipelines, the application  must  have the PICO spatial data permission granted by users. 
#### Return
Dynamic texture resource from the tensor. 
#### Throws
Spatial MLException 
if the application does not have the required permission(s), or if the  GlobalTensor  is invalid, or cannot be read back, such as a tensor created with  Tensor.SceneGraphInitInfo  config.