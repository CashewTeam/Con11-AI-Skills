# sinh | PICO Spatial SDK

spatialml:securemr / com.pico.spatial.ml.securemr / PipelineArithmeticScope / sinh 
# sinh
```kotlin
fun sinh(value: Tensor): PipelineArithmeticScope.TensorArithmetic
```
Hyperbolic sine operation. Computes the elementwise hyperbolic sine of a matrix. 
#### Return
The expression of the hyperbolic sine operation. 
#### Parameters
value 
the tensor to compute hyperbolic sine for. 
#### Throws
Spatial MLException 
If the tensor is not a matrix. 
```kotlin
fun sinh(value: PipelineArithmeticScope.TensorArithmetic): PipelineArithmeticScope.TensorArithmetic
```
Hyperbolic sine operation. Computes the elementwise hyperbolic sine of a matrix evaluated from the matrix expression. 
#### Return
The expression of the hyperbolic sine operation. 
#### Parameters
value 
the matrix evaluated from the tensor arithmetic expression to compute hyperbolic sine for.