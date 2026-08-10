# lookAt | PICO Spatial SDK

foundation / com.pico.spatial.core.math / Matrix4 / Companion / lookAt 
# lookAt
```kotlin
@JvmStatic
```fun  lookAt ( eye :  Vector3 ,  target :  Vector3 ,  up :  Vector3 ) :  Matrix4 
Creates and returns a 4x4 view matrix that transforms coordinates from world space to camera (view) space. This is a standard "look-at" matrix, robustly handling common edge cases. 
The resulting matrix defines a view where the camera is positioned at  eye , looks towards  target , and its orientation is influenced by the  up  vector (which typically defines the "world's up" direction). The camera is oriented to look down its local negative Z-axis in a right-handed coordinate system. 
Edge cases handled: 
- 
If  eye  and  target  are coincident ( distance < 1e-6f ), an identity matrix is returned. 
- 
up  must be a non-negligible vector ( length > 1e-6f ), otherwise, an  IllegalArgumentException  is thrown. 
- 
If  up  is collinear with the viewing direction ( target - eye ), a stable orthogonal basis is computed by choosing an alternative "up" direction. 
The matrix is suitable for post-multiplying column vectors (e.g.,  P_view = ViewMatrix * P_world ). 
#### Return
A new  Matrix4  view matrix. Returns an identity matrix if  eye  and  target  are coincident. 
#### Parameters
eye 
The position of the camera (the "eye" point) in world space. 
target 
The point in world space that the camera is looking at. 
up 
A vector indicating the general "up" direction in the world (e.g.,  Vector3(0f, 1f, 0f)  for Y-up). Must be a non-zero vector (length greater than  1e-6f ). 
#### Throws
Illegal Argument Exception 
if  up 's length is less than or equal to  1e-6f .