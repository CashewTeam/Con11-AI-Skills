# times | PICO Spatial SDK

foundation / com.pico.spatial.core.math / Matrix3 / times 
# times
```kotlin
operator fun times(scale: Float): Matrix3
```
Overloads the  *  operator to perform element-wise multiplication of this matrix by a scalar value. 
Each component of the resulting matrix is the product of the corresponding component of this matrix and the  scale  factor. 
#### Return
A new  Matrix3  representing the result of the scalar multiplication. 
#### Parameters
scale 
The scalar  Float  value to multiply this matrix by. 
```kotlin
operator fun times(other: Matrix3): Matrix3
```
Overloads the  *  operator to perform matrix multiplication of this matrix by another  Matrix3  ( this * other ). 
Matrix multiplication is not commutative; the order of operands matters. If this matrix represents transformation  A  and  other  represents transformation  B , then  A * B  represents applying transformation  B  first, then transformation  A . 
Each element  (i,j)  of the resulting matrix is the dot product of the  i -th row of this matrix and the  j -th column of the  other  matrix. 
#### Return
A new  Matrix3  representing the product of this matrix and  other . 
#### Parameters
other 
The  Matrix3  to multiply this matrix by (the right-hand side matrix). 
```kotlin
operator fun times(other: Vector3): Vector3
```
Overloads the  *  operator to transform a 3D vector by this matrix. 
This performs a standard matrix-vector multiplication, where the  vector  is treated as a column vector. The result is a new  Vector3  representing the transformed vector. 
result.x = m00*vector.x + m01*vector.y + m02*vector.z result.y = m10*vector.x + m11*vector.y + m12*vector.z result.z = m20*vector.x + m21*vector.y + m22*vector.z 
This operation can be used to apply rotations, scaling, or shearing represented by this matrix to a point or direction vector. 
#### Return
A new  Vector3  representing the result of the transformation. 
#### Parameters
other 
The  Vector3  to be transformed by this matrix.