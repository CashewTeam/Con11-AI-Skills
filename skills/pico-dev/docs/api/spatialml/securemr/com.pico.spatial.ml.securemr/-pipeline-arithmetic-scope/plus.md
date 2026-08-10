# plus | PICO Spatial SDK

spatialml:securemr / com.pico.spatial.ml.securemr / PipelineArithmeticScope / plus 
# plus
```kotlin
operator fun Tensor.plus(other: Tensor): PipelineArithmeticScope.TensorArithmetic
```
Arithmetic addition. The left-hand-side and the right-hand-side will be added element-by-element. 
#### Return
The expression of the addition operation. 
#### Parameters
other 
the tensor added to this tensor. 
#### Throws
Spatial MLException 
If the tensors do not have the same shape, or this tensor or the  other  tensor is not a matrix. 
```kotlin
operator fun Tensor.plus(other: PipelineArithmeticScope.TensorArithmetic): PipelineArithmeticScope.TensorArithmetic
```
Arithmetic addition. The left-hand-side tensor and the matrix evaluated from the right-hand-side expression will be added element-by-element. 
#### Return
The expression of the addition operation. 
#### Parameters
other 
the matrix evaluated from the tensor arithmetic expression added to this tensor. 
#### Throws
Spatial MLException 
If the tensor and expression do not have the same shape, or this tensor is not a matrix. 
```kotlin
operator fun PipelineArithmeticScope.TensorArithmetic.plus(other: Tensor): PipelineArithmeticScope.TensorArithmetic
```
Arithmetic addition. The matrix evaluated from the left-hand-side expression and the right-hand-side tensor will be added element-by-element. 
#### Return
The expression of the addition operation. 
#### Parameters
other 
the tensor added to the matrix evaluated from this expression. 
#### Throws
Spatial MLException 
If the expression and tensor do not have the same shape, or the  other  tensor is not a matrix. 
```kotlin
operator fun PipelineArithmeticScope.TensorArithmetic.plus(other: PipelineArithmeticScope.TensorArithmetic): PipelineArithmeticScope.TensorArithmetic
```
Arithmetic addition. The matrices evaluated from the left-hand-side and the right-hand-side expressions will be added element-by-element. 
#### Return
The expression of the addition operation. 
#### Parameters
other 
the matrix evaluated from the tensor arithmetic expression added to the matrix evaluated from this expression. 
#### Throws
Spatial MLException 
If the expressions do not have the same shape. 
```kotlin
operator fun Tensor.plus(other: Double): PipelineArithmeticScope.TensorArithmetic
```
Arithmetic addition. The tensor will be added element-by-element with a scalar value. 
#### Return
The expression of the addition operation. 
#### Parameters
other 
the scalar value added to this tensor. 
#### Throws
Spatial MLException 
If this tensor is not a matrix. 
```kotlin
operator fun PipelineArithmeticScope.TensorArithmetic.plus(other: Double): PipelineArithmeticScope.TensorArithmetic
```
Arithmetic addition. The matrix evaluated from the tensor expression will be added element-by-element with a scalar value. 
#### Return
The expression of the addition operation. 
#### Parameters
other 
the scalar value added to the matrix evaluated from this expression. 
```kotlin
operator fun Double.plus(other: Tensor): PipelineArithmeticScope.TensorArithmetic
```
Arithmetic addition. A scalar value will be added element-by-element to the tensor. 
#### Return
The expression of the addition operation. 
#### Parameters
other 
the tensor to which the scalar value is added. 
#### Throws
Spatial MLException 
If the  other  tensor is not a matrix. 
```kotlin
operator fun Double.plus(other: PipelineArithmeticScope.TensorArithmetic): PipelineArithmeticScope.TensorArithmetic
```
Arithmetic addition. A scalar value will be added element-by-element to the matrix evaluated from the tensor expression. 
#### Return
The expression of the addition operation. 
#### Parameters
other 
the matrix evaluated from the tensor expression to which the scalar value is added.