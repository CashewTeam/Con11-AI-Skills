# cosh | PICO Spatial SDK

spatialml:securemr / com.pico.spatial.ml.securemr / PipelineArithmeticScope / cosh 
# cosh
```kotlin
fun cosh(value: Tensor): PipelineArithmeticScope.TensorArithmetic
```
Hyperbolic cosine operation. Computes the elementwise hyperbolic cosine of a matrix. 
#### Return
The expression of the hyperbolic cosine operation. 
#### Parameters
value 
the tensor to compute hyperbolic cosine for. 
#### Throws
Spatial MLException 
If the tensor is not a matrix. 
```kotlin
fun cosh(value: PipelineArithmeticScope.TensorArithmetic): PipelineArithmeticScope.TensorArithmetic
```
Hyperbolic cosine operation. Computes the elementwise hyperbolic cosine of a matrix evaluated from the matrix expression. 
#### Return
The expression of the hyperbolic cosine operation. 
#### Parameters
value 
the matrix evaluated from the tensor arithmetic expression to compute hyperbolic cosine for.