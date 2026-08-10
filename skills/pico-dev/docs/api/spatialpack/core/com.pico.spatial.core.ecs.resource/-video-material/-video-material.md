# VideoMaterial | PICO Spatial SDK

core / com.pico.spatial.core.ecs.resource / VideoMaterial / VideoMaterial 
# VideoMaterial
```kotlin
constructor(blendingMode: BlendingMode, videoDimensionMode: VideoDimensionMode, cullingMode: MaterialCullingMode, defaultColor: Color4 = Color4.BLACK)
```
Creates a  VideoMaterial  with the specified  BlendingMode ,  VideoDimensionMode , and  MaterialCullingMode . 
#### Parameters
blending Mode 
The  BlendingMode  to use.  BlendingMode.ADD ,  BlendingMode.FADE , and  BlendingMode.MASKED  are not supported. 
video Dimension Mode 
The  VideoDimensionMode  to use. 
culling Mode 
The  MaterialCullingMode  to use. 
default Color 
The default color of the  VideoMaterial . The default value is  Color4.BLACK . If set to  Color4.TRANSPARENT , ensure  blendingMode  is set to  BlendingMode.TRANSPARENT . 
#### See also
Video Component 
. 
Video Player Component 
.