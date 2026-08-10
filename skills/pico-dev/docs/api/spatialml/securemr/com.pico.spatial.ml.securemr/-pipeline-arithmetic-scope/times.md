# times | PICO Spatial SDK

spatialml:securemr / com.pico.spatial.ml.securemr / PipelineArithmeticScope / times 
# times
```kotlin
operator fun Tensor.times(other: Tensor): PipelineArithmeticScope.TensorArithmetic
```
Matrix multiplication. The left-hand-side and the right-hand-side tensors will be multiplied using matrix multiplication rules. 
#### Return
The expression of the multiplication operation. 
#### Parameters
other 
the tensor multiplied with this tensor. 
#### Throws
Spatial MLException 
If the tensors do not have compatible shapes for matrix multiplication, or this tensor or the  other  tensor is not a matrix. 
```kotlin
operator fun Tensor.times(other: PipelineArithmeticScope.TensorArithmetic): PipelineArithmeticScope.TensorArithmetic
```
Matrix multiplication. The left-hand-side tensor and the matrix evaluated from the right-hand-side expression will be multiplied using matrix multiplication rules. 
#### Return
The expression of the multiplication operation. 
#### Parameters
other 
the matrix evaluated from the tensor arithmetic expression multiplied with this tensor. 
#### Throws
Spatial MLException 
If the tensor and expression do not have compatible shapes for matrix multiplication, or this tensor is not a matrix. 
```kotlin
operator fun PipelineArithmeticScope.TensorArithmetic.times(other: Tensor): PipelineArithmeticScope.TensorArithmetic
```
Matrix multiplication. The matrix evaluated from the left-hand-side expression and the right-hand-side tensor will be multiplied using matrix multiplication. 
#### Return
The expression of the multiplication operation. 
#### Parameters
other 
the tensor multiplied with the matrix evaluated from this expression. 
#### Throws
Spatial MLException 
If the expression and tensor do not have compatible shapes for matrix multiplication, or the  other  tensor is not a matrix. 
```kotlin
operator fun PipelineArithmeticScope.TensorArithmetic.times(other: PipelineArithmeticScope.TensorArithmetic): PipelineArithmeticScope.TensorArithmetic
```
Matrix multiplication. The matrices evaluated from the left-hand-side and the right-hand-side expressions will be multiplied using matrix multiplication. 
#### Return
The expression of the multiplication operation. 
#### Parameters
other 
the matrix evaluated from the tensor arithmetic expression multiplied with the matrix evaluated from this expression. 
#### Throws
Spatial MLException 
If the expressions do not have compatible shapes for matrix multiplication. 
```kotlin
operator fun PipelineArithmeticScope.TensorArithmetic.times(other: Double): PipelineArithmeticScope.TensorArithmetic
```
Scalar multiplication. The matrix evaluated from the tensor expression will be multiplied element-by-element with a scalar value. 
#### Return
The expression of the multiplication operation. 
#### Parameters
other 
the scalar value multiplied with the matrix evaluated from this expression. 
```kotlin
operator fun Tensor.times(other: Double): PipelineArithmeticScope.TensorArithmetic
```
Scalar multiplication. The tensor will be multiplied element-by-element with a scalar value. 
#### Return
The expression of the multiplication operation. 
#### Parameters
other 
the scalar value multiplied with this tensor. 
#### Throws
Spatial MLException 
If this tensor is not a matrix. 
```kotlin
operator fun Double.times(other: PipelineArithmeticScope.TensorArithmetic): PipelineArithmeticScope.TensorArithmetic
```
Scalar multiplication. A scalar value will be multiplied element-by-element with the matrix evaluated from the tensor expression. 
#### Return
The expression of the multiplication operation. 
#### Parameters
other 
the matrix evaluated from the tensor expression multiplied with this scalar value. 
```kotlin
operator fun Double.times(other: Tensor): PipelineArithmeticScope.TensorArithmetic
```
Scalar multiplication. A scalar value will be multiplied element-by-element with the tensor. 
#### Return
The expression of the multiplication operation. 
#### Parameters
other 
the tensor multiplied with this scalar value. 
#### Throws
Spatial MLException 
If the  other  tensor is not a matrix.