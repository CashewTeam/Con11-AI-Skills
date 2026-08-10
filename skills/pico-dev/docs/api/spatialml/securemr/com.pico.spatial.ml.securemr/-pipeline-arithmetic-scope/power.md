# power | PICO Spatial SDK

spatialml:securemr / com.pico.spatial.ml.securemr / PipelineArithmeticScope / power 
# power
```kotlin
fun Tensor.power(exponent: Tensor): PipelineArithmeticScope.TensorArithmetic
```
Matrix power operation. The tensor will be raised to the power of the exponent tensor. 
#### Return
The expression of the power operation. 
#### Parameters
exponent 
the tensor containing the exponent value. The tensor must be a matrix of shape 1x1, i.e., containing exactly one value. 
#### Throws
Spatial MLException 
If the exponent tensor does not contain exactly one value, or this tensor is not a matrix. 
```kotlin
fun Tensor.power(exponent: PipelineArithmeticScope.TensorArithmetic): PipelineArithmeticScope.TensorArithmetic
```
Matrix power operation. The tensor will be raised to the power of the matrix evaluated from the exponent expression element-by-element. 
#### Return
The expression of the power operation. 
#### Parameters
exponent 
the matrix evaluated from the tensor arithmetic expression containing the exponent value, which must evaluated to a 1x1 matrix, i.e., containing exactly one value. 
#### Throws
Spatial MLException 
If the exponent expression does not evaluate to exactly one value, or this tensor is not a matrix. 
```kotlin
fun PipelineArithmeticScope.TensorArithmetic.power(exponent: Tensor): PipelineArithmeticScope.TensorArithmetic
```
Matrix power operation. The matrix evaluated from the tensor expression will be raised to the power of the exponent tensor element-by-element. 
#### Return
The expression of the power operation. 
#### Parameters
exponent 
the tensor containing the exponent value. The tensor must be a matrix of shape 1x1, i.e., containing exactly one value. 
#### Throws
Spatial MLException 
If the exponent tensor does not contain exactly one value. 
```kotlin
fun PipelineArithmeticScope.TensorArithmetic.power(exponent: PipelineArithmeticScope.TensorArithmetic): PipelineArithmeticScope.TensorArithmetic
```
Matrix power operation. The matrix evaluated from the tensor expression will be raised to the power of the matrix evaluated from the exponent expression element-by-element. 
#### Return
The expression of the power operation. 
#### Parameters
exponent 
the matrix evaluated from the tensor arithmetic expression containing the exponent value. The expression must be evaluated to a tensor of shape 1x1, i.e., containing exactly one value. 
#### Throws
Spatial MLException 
If the exponent expression does not evaluate to exactly one value. 
```kotlin
fun Double.power(exponent: Tensor): PipelineArithmeticScope.TensorArithmetic
```
Scalar power operation. A scalar value will be raised to the power of the exponent tensor. 
#### Return
The expression of the power operation. 
#### Parameters
exponent 
the tensor containing the exponent value. 
#### Throws
Spatial MLException 
If the exponent tensor does not contain exactly one value, or the exponent tensor is not a matrix. 
```kotlin
fun Double.power(exponent: PipelineArithmeticScope.TensorArithmetic): PipelineArithmeticScope.TensorArithmetic
```
Scalar power operation. A scalar value will be raised to the power of the matrix evaluated from the exponent expression. 
#### Return
The expression of the power operation. 
#### Parameters
exponent 
the matrix evaluated from the tensor arithmetic expression containing the exponent value. The expression must be evaluated to a matrix of shape 1x1, i.e., containing of exactly one value. 
#### Throws
Spatial MLException 
If the exponent expression does not evaluate to exactly one value. 
```kotlin
fun PipelineArithmeticScope.TensorArithmetic.power(other: Double): PipelineArithmeticScope.TensorArithmetic
```
Scalar power operation. The matrix evaluated from the tensor expression will be raised to the power of a scalar value element-by-element. 
#### Return
The expression of the power operation. 
#### Parameters
other 
the scalar exponent value. 
```kotlin
fun Tensor.power(other: Double): PipelineArithmeticScope.TensorArithmetic
```
Scalar power operation. The tensor will be raised to the power of a scalar value element-by-element. 
#### Return
The expression of the power operation. 
#### Parameters
other 
the scalar exponent value. 
#### Throws
Spatial MLException 
If this tensor is not a matrix.