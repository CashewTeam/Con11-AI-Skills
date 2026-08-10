# setTexture | PICO Spatial SDK

core / com.pico.spatial.core.ecs.resource / VideoMaterial / setTexture 
# setTexture
```kotlin
@ExperimentalSpatialApi
```fun  setTexture ( texture :  TextureResource ) 
Sets the  TextureResource  of the  VideoMaterial  in the following modes:  VideoDimensionMode.MONO ,  VideoDimensionMode.SIDE_BY_SIDE , and  VideoDimensionMode.TOP_AND_DOWN . 
This method is typically used to set the cover image of the video. 
Remember to release the texture after use by calling  TextureResource.close . 
#### Parameters
texture 
The  TextureResource  object representing the texture to be applied to the  VideoMaterial . 
```kotlin
@ExperimentalSpatialApi
```fun  setTexture ( textureLeft :  TextureResource ,  textureRight :  TextureResource ) 
Sets the  TextureResource  of the  VideoMaterial  in  VideoDimensionMode.MULTIPLE_VIEW . 
This method is typically used to set the cover image of the video. 
Remember to release the textures after use by calling  TextureResource.close . 
#### Parameters
texture Left 
The  TextureResource  object representing the texture to be applied to the  VideoMaterial  for the left eye. 
texture Right 
The  TextureResource  object representing the texture to be applied to the  VideoMaterial  for the right eye.