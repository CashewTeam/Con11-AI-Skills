# div | PICO Spatial SDK

spatialml:securemr / com.pico.spatial.ml.securemr / PipelineArithmeticScope / div 
# div
```kotlin
operator fun Tensor.div(other: Tensor): PipelineArithmeticScope.TensorArithmetic
```
Elementwise division. The left-hand-side tensor will be divided by the right-hand-side tensor element-by-element. 
Note : the division performs elementwise division of matrices, if you want the inversion of matrix multiplication, you may use  tensor1 * inv(tensor2)  which multiply the inversion of a matrix. 
#### Return
The expression of the division operation. 
#### Parameters
other 
the tensor dividing this tensor. 
#### Throws
Spatial MLException 
If the tensors do not have the same shape, or this tensor or the  other  tensor is not a matrix. 
```kotlin
operator fun Tensor.div(other: PipelineArithmeticScope.TensorArithmetic): PipelineArithmeticScope.TensorArithmetic
```
Elementwise division. The left-hand-side tensor will be divided by the matrix evaluated from the right-hand-side expression element-by-element. 
Note : the division performs elementwise division of matrices, if you want the inversion of matrix multiplication, you may use  tensor1 * inv(tensor2)  which multiply the inversion of a matrix. 
#### Return
The expression of the division operation. 
#### Parameters
other 
the matrix evaluated from the tensor arithmetic expression dividing this tensor. 
#### Throws
Spatial MLException 
If the tensor and expression do not have the same shape, or this tensor is not a matrix. 
```kotlin
operator fun PipelineArithmeticScope.TensorArithmetic.div(other: Tensor): PipelineArithmeticScope.TensorArithmetic
```
Elementwise division. The matrix evaluated from the left-hand-side expression will be divided by the right-hand-side tensor element-by-element. 
Note : the division performs elementwise division of matrices, if you want the inversion of matrix multiplication, you may use  tensor1 * inv(tensor2)  which multiply the inversion of a matrix. 
#### Return
The expression of the division operation. 
#### Parameters
other 
the tensor dividing the matrix evaluated from this expression. 
#### Throws
Spatial MLException 
If the expression and tensor do not have the same shape, or the  other  tensor is not a matrix. 
```kotlin
operator fun PipelineArithmeticScope.TensorArithmetic.div(other: PipelineArithmeticScope.TensorArithmetic): PipelineArithmeticScope.TensorArithmetic
```
Elementwise division. The matrix evaluated from the left-hand-side expression will be divided by the matrix evaluated from the right-hand-side expression element-by-element. 
Note : the division performs elementwise division of matrices, if you want the inversion of matrix multiplication, you may use  tensor1 * inv(tensor2)  which multiply the inversion of a matrix. 
#### Return
The expression of the division operation. 
#### Parameters
other 
the matrix evaluated from the tensor arithmetic expression dividing the matrix evaluated from this expression. 
#### Throws
Spatial MLException 
If the expressions do not have the same shape. 
```kotlin
operator fun PipelineArithmeticScope.TensorArithmetic.div(other: Double): PipelineArithmeticScope.TensorArithmetic
```
Scalar division. The matrix evaluated from the tensor expression will be divided element-by-element by a scalar value. 
Note : the division performs elementwise division of matrices, if you want the inversion of matrix multiplication, you may use  tensor1 * inv(tensor2)  which multiply the inversion of a matrix. 
#### Return
The expression of the division operation. 
#### Parameters
other 
the scalar value dividing the matrix evaluated from this expression. 
```kotlin
operator fun Tensor.div(other: Double): PipelineArithmeticScope.TensorArithmetic
```
Scalar division. The tensor will be divided element-by-element by a scalar value. 
Note : the division performs elementwise division of matrices, if you want the inversion of matrix multiplication, you may use  tensor1 * inv(tensor2)  which multiply the inversion of a matrix. 
#### Return
The expression of the division operation. 
#### Parameters
other 
the scalar value dividing this tensor. 
#### Throws
Spatial MLException 
If this tensor is not a matrix.