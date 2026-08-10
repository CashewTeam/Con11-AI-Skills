# atan | PICO Spatial SDK

spatialml:securemr / com.pico.spatial.ml.securemr / PipelineArithmeticScope / atan 
# atan
```kotlin
fun atan(value: Tensor): PipelineArithmeticScope.TensorArithmetic
```
Inverse trigonometric arctangent operation. Computes the elementwise arctangent of a matrix. 
#### Return
The expression of the arctangent operation. 
#### Parameters
value 
the tensor to compute arctangent for. 
#### Throws
Spatial MLException 
If the tensor is not a matrix. 
```kotlin
fun atan(value: PipelineArithmeticScope.TensorArithmetic): PipelineArithmeticScope.TensorArithmetic
```
Inverse trigonometric arctangent operation. Computes the elementwise arctangent of a matrix evaluated from the matrix expression. 
#### Return
The expression of the arctangent operation. 
#### Parameters
value 
the matrix evaluated from the tensor arithmetic expression to compute arctangent for.