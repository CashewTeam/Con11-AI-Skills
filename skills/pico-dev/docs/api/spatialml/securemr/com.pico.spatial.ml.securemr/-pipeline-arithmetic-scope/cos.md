# cos | PICO Spatial SDK

spatialml:securemr / com.pico.spatial.ml.securemr / PipelineArithmeticScope / cos 
# cos
```kotlin
fun cos(value: Tensor): PipelineArithmeticScope.TensorArithmetic
```
Trigonometric cosine operation. Computes the elementwise cosine of a matrix. 
#### Return
The expression of the cosine operation. 
#### Parameters
value 
the tensor to compute cosine for. 
#### Throws
Spatial MLException 
If the tensor is not a matrix. 
```kotlin
fun cos(value: PipelineArithmeticScope.TensorArithmetic): PipelineArithmeticScope.TensorArithmetic
```
Trigonometric cosine operation. Computes the elementwise cosine of a matrix evaluated from the matrix expression. 
#### Return
The expression of the cosine operation. 
#### Parameters
value 
the matrix evaluated from the tensor arithmetic expression to compute cosine for.