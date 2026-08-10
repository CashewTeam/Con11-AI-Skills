# sin | PICO Spatial SDK

spatialml:securemr / com.pico.spatial.ml.securemr / PipelineArithmeticScope / sin 
# sin
```kotlin
fun sin(value: Tensor): PipelineArithmeticScope.TensorArithmetic
```
Trigonometric sine operation. Computes the elementwise sine of a matrix. 
#### Return
The expression of the sine operation. 
#### Parameters
value 
the tensor to compute sine for. 
#### Throws
Spatial MLException 
If the tensor is not a matrix. 
```kotlin
fun sin(value: PipelineArithmeticScope.TensorArithmetic): PipelineArithmeticScope.TensorArithmetic
```
Trigonometric sine operation. Computes the elementwise sine of a matrix evaluated from the matrix expression. 
#### Return
The expression of the sine operation. 
#### Parameters
value 
the matrix evaluated from the tensor arithmetic expression to compute sine for.