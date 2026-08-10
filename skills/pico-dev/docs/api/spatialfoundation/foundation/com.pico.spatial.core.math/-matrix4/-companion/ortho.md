# ortho | PICO Spatial SDK

foundation / com.pico.spatial.core.math / Matrix4 / Companion / ortho 
# ortho
```kotlin
@JvmStatic
```fun  ortho ( left :  Float ,  right :  Float ,  bottom :  Float ,  top :  Float ,  near :  Float ,  far :  Float ) :  Matrix4 
Creates and returns a 4x4 orthographic projection matrix. 
This matrix transforms coordinates from view space (defined by the frustum  left, right, bottom, top, near, far ) to clip space. The transformation maps the specified view volume to a canonical cube, typically with coordinates ranging from -1 to 1 in X, Y, and Z (Normalized Device Coordinates - NDC). 
This implementation produces a matrix suitable for a right-handed view space (where the camera typically looks down the -Z axis) and maps the depth range defined by  near  and  far  (positive distances from the viewpoint) to  [-1, 1]  in NDC. 
The matrix is designed to be post-multiplied by column vectors (e.g.,  P_clip = ProjectionMatrix * P_view ). 
#### Return
A new  Matrix4  orthographic projection matrix. 
#### Parameters
left 
The coordinate for the left vertical clipping plane. 
right 
The coordinate for the right vertical clipping plane. Must be greater than  left . 
bottom 
The coordinate for the bottom horizontal clipping plane. Must be less than  top . 
top 
The coordinate for the top horizontal clipping plane. Must be greater than  bottom . 
near 
The distance to the near depth clipping plane. Must be positive and less than  far . 
far 
The distance to the far depth clipping plane. Must be positive and greater than  near . 
#### Throws
Illegal Argument Exception 
if  left >= right ,  bottom >= top , or  near >= far .