# transpose | PICO Spatial SDK

spatialml:securemr / com.pico.spatial.ml.securemr / PipelineArithmeticScope / transpose 
# transpose
```kotlin
fun transpose(value: Tensor): PipelineArithmeticScope.TensorArithmetic
```
Matrix transpose operation. Computes the transpose of a matrix. 
#### Return
The expression of the transpose operation. 
#### Parameters
value 
the tensor to transpose. 
#### Throws
Spatial MLException 
If the tensor is not a matrix. 
```kotlin
fun transpose(value: PipelineArithmeticScope.TensorArithmetic): PipelineArithmeticScope.TensorArithmetic
```
Matrix transpose operation. Computes the transpose of a matrix evaluated from the matrix expression. 
#### Return
The expression of the transpose operation. 
#### Parameters
value 
the matrix evaluated from the tensor arithmetic expression to transpose.