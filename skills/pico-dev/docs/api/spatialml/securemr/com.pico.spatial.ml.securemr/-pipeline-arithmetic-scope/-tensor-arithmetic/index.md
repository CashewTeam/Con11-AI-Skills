# TensorArithmetic | PICO Spatial SDK

spatialml:securemr / com.pico.spatial.ml.securemr / PipelineArithmeticScope / TensorArithmetic 
# TensorArithmetic
```kotlin
class TensorArithmetic
```
The interim results of arithmetic operations of tensors, which represents an expression tree of tensors involved in the arithmetic operations. In such a tree, each leaf node is a  Tensor , where as a non-leaf node denote an arithmetic op. 
Tensor  at each leaf node  must  be a matrix, i.e., a multi-dimensional tensor (see  Tensor.MultiDimensionalInitInfo ) of 2 dimensions. 
#### Parameters
op Char 
The top arithmetic op in the tree. 
left Exp 
The left-hand-side subtree of the top arithmetic op. 
right Exp 
The right-hand-side subtree of the top arithmetic op. 
current Shape 
The expected shape of the matrix output from the tree. 
Members 
## Functions
to String 
```kotlin
open override fun toString(): String
```