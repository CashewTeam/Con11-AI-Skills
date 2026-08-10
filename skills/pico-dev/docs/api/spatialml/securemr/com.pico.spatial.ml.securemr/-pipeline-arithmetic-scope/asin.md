# asin | PICO Spatial SDK

spatialml:securemr / com.pico.spatial.ml.securemr / PipelineArithmeticScope / asin 
# asin
```kotlin
fun asin(value: Tensor): PipelineArithmeticScope.TensorArithmetic
```
Inverse trigonometric arcsine operation. Computes the elementwise arcsine of a matrix. 
#### Return
The expression of the arcsine operation. 
#### Parameters
value 
the tensor to compute arcsine for. 
#### Throws
Spatial MLException 
If the tensor is not a matrix. 
```kotlin
fun asin(value: PipelineArithmeticScope.TensorArithmetic): PipelineArithmeticScope.TensorArithmetic
```
Inverse trigonometric arcsine operation. Computes the elementwise arcsine of a matrix evaluated from the matrix expression. 
#### Return
The expression of the arcsine operation. 
#### Parameters
value 
the matrix evaluated from the tensor arithmetic expression to compute arcsine for.