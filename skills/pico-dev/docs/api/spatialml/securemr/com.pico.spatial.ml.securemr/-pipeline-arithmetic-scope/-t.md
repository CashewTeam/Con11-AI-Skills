# T | PICO Spatial SDK

spatialml:securemr / com.pico.spatial.ml.securemr / PipelineArithmeticScope / T 
# T
```kotlin
fun Tensor.T(): PipelineArithmeticScope.TensorArithmetic
```
Matrix transpose operation. Computes the transpose of a matrix. 
#### Return
The expression of the transpose operation. 
#### Throws
Spatial MLException 
If this tensor is not a matrix. 
```kotlin
fun PipelineArithmeticScope.TensorArithmetic.T(): PipelineArithmeticScope.TensorArithmetic
```
Matrix transpose operation. Computes the transpose of a matrix evaluated from the matrix expression. 
#### Return
The expression of the transpose operation.