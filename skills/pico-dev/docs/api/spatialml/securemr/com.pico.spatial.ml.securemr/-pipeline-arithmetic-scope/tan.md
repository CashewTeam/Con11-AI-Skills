# tan | PICO Spatial SDK

spatialml:securemr / com.pico.spatial.ml.securemr / PipelineArithmeticScope / tan 
# tan
```kotlin
fun tan(value: Tensor): PipelineArithmeticScope.TensorArithmetic
```
Trigonometric tangent operation. Computes the elementwise tangent of a matrix. 
#### Return
The expression of the tangent operation. 
#### Parameters
value 
the tensor to compute tangent for. 
#### Throws
Spatial MLException 
If the tensor is not a matrix. 
```kotlin
fun tan(value: PipelineArithmeticScope.TensorArithmetic): PipelineArithmeticScope.TensorArithmetic
```
Trigonometric tangent operation. Computes the elementwise tangent of a matrix evaluated from the matrix expression. 
#### Return
The expression of the tangent operation. 
#### Parameters
value 
the matrix evaluated from the tensor arithmetic expression to compute tangent for.