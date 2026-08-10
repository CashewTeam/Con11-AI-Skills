# acos | PICO Spatial SDK

spatialml:securemr / com.pico.spatial.ml.securemr / PipelineArithmeticScope / acos 
# acos
```kotlin
fun acos(value: Tensor): PipelineArithmeticScope.TensorArithmetic
```
Inverse trigonometric arccosine operation. Computes the elementwise arccosine of a matrix. 
#### Return
The expression of the arccosine operation. 
#### Parameters
value 
the tensor to compute arccosine for. 
#### Throws
Spatial MLException 
If the tensor is not a matrix. 
```kotlin
fun acos(value: PipelineArithmeticScope.TensorArithmetic): PipelineArithmeticScope.TensorArithmetic
```
Inverse trigonometric arccosine operation. Computes the elementwise arccosine of a matrix evaluated from the matrix expression. 
#### Return
The expression of the arccosine operation. 
#### Parameters
value 
the matrix evaluated from the tensor arithmetic expression to compute arccosine for.