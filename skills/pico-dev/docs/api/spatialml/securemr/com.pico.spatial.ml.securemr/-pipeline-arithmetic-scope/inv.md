# inv | PICO Spatial SDK

spatialml:securemr / com.pico.spatial.ml.securemr / PipelineArithmeticScope / inv 
# inv
```kotlin
fun inv(value: Tensor): PipelineArithmeticScope.TensorArithmetic
```
Matrix inverse operation. Computes the inverse of a square matrix. 
#### Return
The expression of the inverse operation. 
#### Parameters
value 
the tensor to invert. 
#### Throws
Spatial MLException 
If the tensor is not square, or is not a matrix. 
```kotlin
fun inv(value: PipelineArithmeticScope.TensorArithmetic): PipelineArithmeticScope.TensorArithmetic
```
Matrix inverse operation. Computes the inverse of a matrix evaluated from the square matrix expression. 
#### Return
The expression of the inverse operation. 
#### Parameters
value 
the matrix evaluated from the tensor arithmetic expression to invert. 
#### Throws
Spatial MLException 
If the expression does not evaluate to a square matrix.