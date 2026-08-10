# times | PICO Spatial SDK

foundation / com.pico.spatial.core.math / Matrix4 / times 
# times
```kotlin
operator fun times(scale: Float): Matrix4
```
Overloads the  *  operator to perform element-wise multiplication of this matrix by a scalar value. 
Each component of the resulting matrix is the product of the corresponding component of this matrix and the  scale  factor. 
#### Return
A new  Matrix4  representing the result of the scalar multiplication. 
#### Parameters
scale 
The scalar  Float  value to multiply this matrix by. 
```kotlin
operator fun times(other: Matrix4): Matrix4
```
Times two  Matrix4  instances. 
#### Return
The new  Matrix4  instance by timing the current  Matrix4  instance and the input  Matrix4  instance. 
#### Parameters
other 
Another  Matrix4  instance that will be timed. 
```kotlin
operator fun times(other: Vector4): Vector4
```
Overloads the  *  operator to transform a 4D vector by this matrix. 
This performs a standard matrix-vector multiplication, where the  vector  is treated as a column vector ( result = this_matrix * vector ). The result is a new  Vector4  representing the transformed vector. 
Each component of the result vector is the dot product of a row of this matrix and the input  vector . For example:  result.x = m00*vector.x + m01*vector.y + m02*vector.z + m03*vector.w 
This operation is fundamental for applying 3D transformations (like translation, rotation, scaling, and projection) to points and vectors represented in homogeneous coordinates. 
#### Return
A new  Vector4  representing the result of the transformation. 
#### Parameters
other 
The  Vector4  to be transformed by this matrix.