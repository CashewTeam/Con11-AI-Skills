# perspective | PICO Spatial SDK

foundation / com.pico.spatial.core.math / Matrix4 / Companion / perspective 
# perspective
```kotlin
@JvmStatic
```fun  perspective ( fovYDegrees :  Float ,  aspectRatio :  Float ,  nearPlane :  Float ,  farPlane :  Float ) :  Matrix4 
Creates and returns a 4x4 perspective projection matrix. 
This matrix transforms coordinates from view space to clip space, simulating depth perception where objects further away appear smaller. It defines a frustum-shaped view volume and maps it to a canonical cube, typically with coordinates ranging from -1 to 1 in X, Y, and Z (Normalized Device Coordinates - NDC). 
This implementation produces a matrix suitable for a right-handed view space (where the camera typically looks down its negative Z-axis) and maps the depth range  [nearPlane, farPlane]  (positive distances from the viewpoint) to  [-1, 1]  in NDC Z. 
The matrix is designed to be post-multiplied by column vectors (e.g.,  P_clip = ProjectionMatrix * P_view ). 
#### Return
A new  Matrix4  perspective projection matrix. 
#### Parameters
fov YDegrees 
The vertical field of view angle, in  degrees . Must be  > 0  and  < 180 . 
aspect Ratio 
The aspect ratio of the viewport (width / height). Must be  > 0 . 
near Plane 
The distance to the near clipping plane. Must be positive. 
far Plane 
The distance to the far clipping plane. Must be positive and greater than  nearPlane . 
#### Throws
Illegal Argument Exception 
if any input parameter is out of its valid range.