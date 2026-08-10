# PipelineArithmeticScope | PICO Spatial SDK

spatialml:securemr / com.pico.spatial.ml.securemr / PipelineArithmeticScope 
# PipelineArithmeticScope
```kotlin
@RequiresApi(value = 27)
```class  PipelineArithmeticScope 
The scope for arithmetic operations between  Tensor  in  Pipeline . 
Note : each individual scope must not contain more than 10  Tensor s. 
Members 
## Constructors
Pipeline Arithmetic Scope 
```kotlin
constructor()
```
## Types
Tensor Arithmetic 
```kotlin
class TensorArithmetic
```
The interim results of arithmetic operations of tensors, which represents an expression tree of tensors involved in the arithmetic operations. In such a tree, each leaf node is a  Tensor , where as a non-leaf node denote an arithmetic op. 
## Functions
acos 
```kotlin
fun acos(value: PipelineArithmeticScope.TensorArithmetic): PipelineArithmeticScope.TensorArithmetic
```
Inverse trigonometric arccosine operation. Computes the elementwise arccosine of a matrix evaluated from the matrix expression. 
```kotlin
fun acos(value: Tensor): PipelineArithmeticScope.TensorArithmetic
```
Inverse trigonometric arccosine operation. Computes the elementwise arccosine of a matrix. 
asin 
```kotlin
fun asin(value: PipelineArithmeticScope.TensorArithmetic): PipelineArithmeticScope.TensorArithmetic
```
Inverse trigonometric arcsine operation. Computes the elementwise arcsine of a matrix evaluated from the matrix expression. 
```kotlin
fun asin(value: Tensor): PipelineArithmeticScope.TensorArithmetic
```
Inverse trigonometric arcsine operation. Computes the elementwise arcsine of a matrix. 
atan 
```kotlin
fun atan(value: PipelineArithmeticScope.TensorArithmetic): PipelineArithmeticScope.TensorArithmetic
```
Inverse trigonometric arctangent operation. Computes the elementwise arctangent of a matrix evaluated from the matrix expression. 
```kotlin
fun atan(value: Tensor): PipelineArithmeticScope.TensorArithmetic
```
Inverse trigonometric arctangent operation. Computes the elementwise arctangent of a matrix. 
cos 
```kotlin
fun cos(value: PipelineArithmeticScope.TensorArithmetic): PipelineArithmeticScope.TensorArithmetic
```
Trigonometric cosine operation. Computes the elementwise cosine of a matrix evaluated from the matrix expression. 
```kotlin
fun cos(value: Tensor): PipelineArithmeticScope.TensorArithmetic
```
Trigonometric cosine operation. Computes the elementwise cosine of a matrix. 
cosh 
```kotlin
fun cosh(value: PipelineArithmeticScope.TensorArithmetic): PipelineArithmeticScope.TensorArithmetic
```
Hyperbolic cosine operation. Computes the elementwise hyperbolic cosine of a matrix evaluated from the matrix expression. 
```kotlin
fun cosh(value: Tensor): PipelineArithmeticScope.TensorArithmetic
```
Hyperbolic cosine operation. Computes the elementwise hyperbolic cosine of a matrix. 
div 
```kotlin
operator fun PipelineArithmeticScope.TensorArithmetic.div(other: PipelineArithmeticScope.TensorArithmetic): PipelineArithmeticScope.TensorArithmetic
```
Elementwise division. The matrix evaluated from the left-hand-side expression will be divided by the matrix evaluated from the right-hand-side expression element-by-element. 
```kotlin
operator fun PipelineArithmeticScope.TensorArithmetic.div(other: Tensor): PipelineArithmeticScope.TensorArithmetic
```
Elementwise division. The matrix evaluated from the left-hand-side expression will be divided by the right-hand-side tensor element-by-element. 
```kotlin
operator fun PipelineArithmeticScope.TensorArithmetic.div(other: Double): PipelineArithmeticScope.TensorArithmetic
```
Scalar division. The matrix evaluated from the tensor expression will be divided element-by-element by a scalar value. 
```kotlin
operator fun Tensor.div(other: PipelineArithmeticScope.TensorArithmetic): PipelineArithmeticScope.TensorArithmetic
```
Elementwise division. The left-hand-side tensor will be divided by the matrix evaluated from the right-hand-side expression element-by-element. 
```kotlin
operator fun Tensor.div(other: Tensor): PipelineArithmeticScope.TensorArithmetic
```
Elementwise division. The left-hand-side tensor will be divided by the right-hand-side tensor element-by-element. 
```kotlin
operator fun Tensor.div(other: Double): PipelineArithmeticScope.TensorArithmetic
```
Scalar division. The tensor will be divided element-by-element by a scalar value. 
inv 
```kotlin
fun inv(value: PipelineArithmeticScope.TensorArithmetic): PipelineArithmeticScope.TensorArithmetic
```
Matrix inverse operation. Computes the inverse of a matrix evaluated from the square matrix expression. 
```kotlin
fun inv(value: Tensor): PipelineArithmeticScope.TensorArithmetic
```
Matrix inverse operation. Computes the inverse of a square matrix. 
minus 
```kotlin
operator fun PipelineArithmeticScope.TensorArithmetic.minus(other: PipelineArithmeticScope.TensorArithmetic): PipelineArithmeticScope.TensorArithmetic
```
Arithmetic subtraction. The matrix evaluated from the right-hand-side expression will be subtracted from the matrix evaluated from the left-hand-side expression element-by-element. 
```kotlin
operator fun PipelineArithmeticScope.TensorArithmetic.minus(other: Tensor): PipelineArithmeticScope.TensorArithmetic
```
Arithmetic subtraction. The right-hand-side tensor will be subtracted from the matrix evaluated from the left-hand-side expression element-by-element. 
```kotlin
operator fun PipelineArithmeticScope.TensorArithmetic.minus(other: Double): PipelineArithmeticScope.TensorArithmetic
```
Arithmetic subtraction. A scalar value will be subtracted from the matrix evaluated from the tensor expression element-by-element. 
```kotlin
operator fun Tensor.minus(other: PipelineArithmeticScope.TensorArithmetic): PipelineArithmeticScope.TensorArithmetic
```
Arithmetic subtraction. The matrix evaluated from the right-hand-side expression will be subtracted from the left-hand-side tensor element-by-element. 
```kotlin
operator fun Tensor.minus(other: Tensor): PipelineArithmeticScope.TensorArithmetic
```
Arithmetic subtraction. The right-hand-side tensor will be subtracted from the left-hand-side tensor element-by-element. 
```kotlin
operator fun Tensor.minus(other: Double): PipelineArithmeticScope.TensorArithmetic
```
Arithmetic subtraction. A scalar value will be subtracted from the tensor element-by-element. 
```kotlin
operator fun Double.minus(other: PipelineArithmeticScope.TensorArithmetic): PipelineArithmeticScope.TensorArithmetic
```
Arithmetic subtraction. The matrix evaluated from the tensor expression will be subtracted from a scalar value element-by-element. 
```kotlin
operator fun Double.minus(other: Tensor): PipelineArithmeticScope.TensorArithmetic
```
Arithmetic subtraction. The tensor will be subtracted from a scalar value element-by-element. 
plus 
```kotlin
operator fun PipelineArithmeticScope.TensorArithmetic.plus(other: PipelineArithmeticScope.TensorArithmetic): PipelineArithmeticScope.TensorArithmetic
```
Arithmetic addition. The matrices evaluated from the left-hand-side and the right-hand-side expressions will be added element-by-element. 
```kotlin
operator fun PipelineArithmeticScope.TensorArithmetic.plus(other: Tensor): PipelineArithmeticScope.TensorArithmetic
```
Arithmetic addition. The matrix evaluated from the left-hand-side expression and the right-hand-side tensor will be added element-by-element. 
```kotlin
operator fun PipelineArithmeticScope.TensorArithmetic.plus(other: Double): PipelineArithmeticScope.TensorArithmetic
```
Arithmetic addition. The matrix evaluated from the tensor expression will be added element-by-element with a scalar value. 
```kotlin
operator fun Tensor.plus(other: PipelineArithmeticScope.TensorArithmetic): PipelineArithmeticScope.TensorArithmetic
```
Arithmetic addition. The left-hand-side tensor and the matrix evaluated from the right-hand-side expression will be added element-by-element. 
```kotlin
operator fun Tensor.plus(other: Tensor): PipelineArithmeticScope.TensorArithmetic
```
Arithmetic addition. The left-hand-side and the right-hand-side will be added element-by-element. 
```kotlin
operator fun Tensor.plus(other: Double): PipelineArithmeticScope.TensorArithmetic
```
Arithmetic addition. The tensor will be added element-by-element with a scalar value. 
```kotlin
operator fun Double.plus(other: PipelineArithmeticScope.TensorArithmetic): PipelineArithmeticScope.TensorArithmetic
```
Arithmetic addition. A scalar value will be added element-by-element to the matrix evaluated from the tensor expression. 
```kotlin
operator fun Double.plus(other: Tensor): PipelineArithmeticScope.TensorArithmetic
```
Arithmetic addition. A scalar value will be added element-by-element to the tensor. 
power 
```kotlin
fun PipelineArithmeticScope.TensorArithmetic.power(exponent: PipelineArithmeticScope.TensorArithmetic): PipelineArithmeticScope.TensorArithmetic
```
Matrix power operation. The matrix evaluated from the tensor expression will be raised to the power of the matrix evaluated from the exponent expression element-by-element. 
```kotlin
fun PipelineArithmeticScope.TensorArithmetic.power(exponent: Tensor): PipelineArithmeticScope.TensorArithmetic
```
Matrix power operation. The matrix evaluated from the tensor expression will be raised to the power of the exponent tensor element-by-element. 
```kotlin
fun PipelineArithmeticScope.TensorArithmetic.power(other: Double): PipelineArithmeticScope.TensorArithmetic
```
Scalar power operation. The matrix evaluated from the tensor expression will be raised to the power of a scalar value element-by-element. 
```kotlin
fun Tensor.power(exponent: PipelineArithmeticScope.TensorArithmetic): PipelineArithmeticScope.TensorArithmetic
```
Matrix power operation. The tensor will be raised to the power of the matrix evaluated from the exponent expression element-by-element. 
```kotlin
fun Tensor.power(exponent: Tensor): PipelineArithmeticScope.TensorArithmetic
```
Matrix power operation. The tensor will be raised to the power of the exponent tensor. 
```kotlin
fun Tensor.power(other: Double): PipelineArithmeticScope.TensorArithmetic
```
Scalar power operation. The tensor will be raised to the power of a scalar value element-by-element. 
```kotlin
fun Double.power(exponent: PipelineArithmeticScope.TensorArithmetic): PipelineArithmeticScope.TensorArithmetic
```
Scalar power operation. A scalar value will be raised to the power of the matrix evaluated from the exponent expression. 
```kotlin
fun Double.power(exponent: Tensor): PipelineArithmeticScope.TensorArithmetic
```
Scalar power operation. A scalar value will be raised to the power of the exponent tensor. 
sin 
```kotlin
fun sin(value: PipelineArithmeticScope.TensorArithmetic): PipelineArithmeticScope.TensorArithmetic
```
Trigonometric sine operation. Computes the elementwise sine of a matrix evaluated from the matrix expression. 
```kotlin
fun sin(value: Tensor): PipelineArithmeticScope.TensorArithmetic
```
Trigonometric sine operation. Computes the elementwise sine of a matrix. 
sinh 
```kotlin
fun sinh(value: PipelineArithmeticScope.TensorArithmetic): PipelineArithmeticScope.TensorArithmetic
```
Hyperbolic sine operation. Computes the elementwise hyperbolic sine of a matrix evaluated from the matrix expression. 
```kotlin
fun sinh(value: Tensor): PipelineArithmeticScope.TensorArithmetic
```
Hyperbolic sine operation. Computes the elementwise hyperbolic sine of a matrix. 
T 
```kotlin
fun PipelineArithmeticScope.TensorArithmetic.T(): PipelineArithmeticScope.TensorArithmetic
```
Matrix transpose operation. Computes the transpose of a matrix evaluated from the matrix expression. 
```kotlin
fun Tensor.T(): PipelineArithmeticScope.TensorArithmetic
```
Matrix transpose operation. Computes the transpose of a matrix. 
tan 
```kotlin
fun tan(value: PipelineArithmeticScope.TensorArithmetic): PipelineArithmeticScope.TensorArithmetic
```
Trigonometric tangent operation. Computes the elementwise tangent of a matrix evaluated from the matrix expression. 
```kotlin
fun tan(value: Tensor): PipelineArithmeticScope.TensorArithmetic
```
Trigonometric tangent operation. Computes the elementwise tangent of a matrix. 
tanh 
```kotlin
fun tanh(value: PipelineArithmeticScope.TensorArithmetic): PipelineArithmeticScope.TensorArithmetic
```
Hyperbolic tangent operation. Computes the elementwise hyperbolic tangent of a matrix evaluated from the matrix expression. 
```kotlin
fun tanh(value: Tensor): PipelineArithmeticScope.TensorArithmetic
```
Hyperbolic tangent operation. Computes the elementwise hyperbolic tangent of a matrix. 
times 
```kotlin
operator fun PipelineArithmeticScope.TensorArithmetic.times(other: PipelineArithmeticScope.TensorArithmetic): PipelineArithmeticScope.TensorArithmetic
```
Matrix multiplication. The matrices evaluated from the left-hand-side and the right-hand-side expressions will be multiplied using matrix multiplication. 
```kotlin
operator fun PipelineArithmeticScope.TensorArithmetic.times(other: Tensor): PipelineArithmeticScope.TensorArithmetic
```
Matrix multiplication. The matrix evaluated from the left-hand-side expression and the right-hand-side tensor will be multiplied using matrix multiplication. 
```kotlin
operator fun PipelineArithmeticScope.TensorArithmetic.times(other: Double): PipelineArithmeticScope.TensorArithmetic
```
Scalar multiplication. The matrix evaluated from the tensor expression will be multiplied element-by-element with a scalar value. 
```kotlin
operator fun Tensor.times(other: PipelineArithmeticScope.TensorArithmetic): PipelineArithmeticScope.TensorArithmetic
```
Matrix multiplication. The left-hand-side tensor and the matrix evaluated from the right-hand-side expression will be multiplied using matrix multiplication rules. 
```kotlin
operator fun Tensor.times(other: Tensor): PipelineArithmeticScope.TensorArithmetic
```
Matrix multiplication. The left-hand-side and the right-hand-side tensors will be multiplied using matrix multiplication rules. 
```kotlin
operator fun Tensor.times(other: Double): PipelineArithmeticScope.TensorArithmetic
```
Scalar multiplication. The tensor will be multiplied element-by-element with a scalar value. 
```kotlin
operator fun Double.times(other: PipelineArithmeticScope.TensorArithmetic): PipelineArithmeticScope.TensorArithmetic
```
Scalar multiplication. A scalar value will be multiplied element-by-element with the matrix evaluated from the tensor expression. 
```kotlin
operator fun Double.times(other: Tensor): PipelineArithmeticScope.TensorArithmetic
```
Scalar multiplication. A scalar value will be multiplied element-by-element with the tensor. 
transpose 
```kotlin
fun transpose(value: PipelineArithmeticScope.TensorArithmetic): PipelineArithmeticScope.TensorArithmetic
```
Matrix transpose operation. Computes the transpose of a matrix evaluated from the matrix expression. 
```kotlin
fun transpose(value: Tensor): PipelineArithmeticScope.TensorArithmetic
```
Matrix transpose operation. Computes the transpose of a matrix.