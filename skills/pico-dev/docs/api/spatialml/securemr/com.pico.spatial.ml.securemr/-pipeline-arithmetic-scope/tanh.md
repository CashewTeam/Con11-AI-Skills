# tanh | PICO Spatial SDK

spatialml:securemr / com.pico.spatial.ml.securemr / PipelineArithmeticScope / tanh 
# tanh
```kotlin
fun tanh(value: Tensor): PipelineArithmeticScope.TensorArithmetic
```
Hyperbolic tangent operation. Computes the elementwise hyperbolic tangent of a matrix. 
#### Return
The expression of the hyperbolic tangent operation. 
#### Parameters
value 
the tensor to compute hyperbolic tangent for. 
#### Throws
Spatial MLException 
If the tensor is not a matrix. 
```kotlin
fun tanh(value: PipelineArithmeticScope.TensorArithmetic): PipelineArithmeticScope.TensorArithmetic
```
Hyperbolic tangent operation. Computes the elementwise hyperbolic tangent of a matrix evaluated from the matrix expression. 
#### Return
The expression of the hyperbolic tangent operation. 
#### Parameters
value 
the matrix evaluated from the tensor arithmetic expression to compute hyperbolic tangent for.