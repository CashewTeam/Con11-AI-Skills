# minus | PICO Spatial SDK

spatialml:securemr / com.pico.spatial.ml.securemr / PipelineArithmeticScope / minus 
# minus
```kotlin
operator fun Tensor.minus(other: Tensor): PipelineArithmeticScope.TensorArithmetic
```
Arithmetic subtraction. The right-hand-side tensor will be subtracted from the left-hand-side tensor element-by-element. 
#### Return
The expression of the subtraction operation. 
#### Parameters
other 
the tensor subtracted from this tensor. 
#### Throws
Spatial MLException 
If the tensors do not have the same shape, or this tensor or the  other  tensor is not a matrix. 
```kotlin
operator fun Tensor.minus(other: PipelineArithmeticScope.TensorArithmetic): PipelineArithmeticScope.TensorArithmetic
```
Arithmetic subtraction. The matrix evaluated from the right-hand-side expression will be subtracted from the left-hand-side tensor element-by-element. 
#### Return
The expression of the subtraction operation. 
#### Parameters
other 
the matrix evaluated from the tensor arithmetic expression subtracted from this tensor. 
#### Throws
Spatial MLException 
If the tensor and expression do not have the same shape, or this tensor is not a matrix. 
```kotlin
operator fun PipelineArithmeticScope.TensorArithmetic.minus(other: Tensor): PipelineArithmeticScope.TensorArithmetic
```
Arithmetic subtraction. The right-hand-side tensor will be subtracted from the matrix evaluated from the left-hand-side expression element-by-element. 
#### Return
The expression of the subtraction operation. 
#### Parameters
other 
the tensor subtracted from the matrix evaluated from this expression. 
#### Throws
Spatial MLException 
If the expression and tensor do not have the same shape, or the  other  tensor is not a matrix. 
```kotlin
operator fun PipelineArithmeticScope.TensorArithmetic.minus(other: PipelineArithmeticScope.TensorArithmetic): PipelineArithmeticScope.TensorArithmetic
```
Arithmetic subtraction. The matrix evaluated from the right-hand-side expression will be subtracted from the matrix evaluated from the left-hand-side expression element-by-element. 
#### Return
The expression of the subtraction operation. 
#### Parameters
other 
the matrix evaluated from the tensor arithmetic expression subtracted from the matrix evaluated from this expression. 
#### Throws
Spatial MLException 
If the expressions do not have the same shape. 
```kotlin
operator fun PipelineArithmeticScope.TensorArithmetic.minus(other: Double): PipelineArithmeticScope.TensorArithmetic
```
Arithmetic subtraction. A scalar value will be subtracted from the matrix evaluated from the tensor expression element-by-element. 
#### Return
The expression of the subtraction operation. 
#### Parameters
other 
the scalar value subtracted from the matrix evaluated from this expression. 
```kotlin
operator fun Tensor.minus(other: Double): PipelineArithmeticScope.TensorArithmetic
```
Arithmetic subtraction. A scalar value will be subtracted from the tensor element-by-element. 
#### Return
The expression of the subtraction operation. 
#### Parameters
other 
the scalar value subtracted from this tensor. 
#### Throws
Spatial MLException 
If this tensor is not a matrix. 
```kotlin
operator fun Double.minus(other: PipelineArithmeticScope.TensorArithmetic): PipelineArithmeticScope.TensorArithmetic
```
Arithmetic subtraction. The matrix evaluated from the tensor expression will be subtracted from a scalar value element-by-element. 
#### Return
The expression of the subtraction operation. 
#### Parameters
other 
the matrix evaluated from the tensor expression subtracted from this scalar value. 
```kotlin
operator fun Double.minus(other: Tensor): PipelineArithmeticScope.TensorArithmetic
```
Arithmetic subtraction. The tensor will be subtracted from a scalar value element-by-element. 
#### Return
The expression of the subtraction operation. 
#### Parameters
other 
the tensor subtracted from this scalar value. 
#### Throws
Spatial MLException 
If the  other  tensor is not a matrix.