# arithmetic | PICO Spatial SDK

spatialml:securemr / com.pico.spatial.ml.securemr / Pipeline / arithmetic 
# arithmetic
```kotlin
fun arithmetic(result: Tensor, arithmeticOperations: PipelineArithmeticScope.() -> PipelineArithmeticScope.TensorArithmetic)
```
Defines an arithmetic operator to the pipeline. The operator allows you to define complex operations between tensors. Different from the above overload which is defined by a string expression, this overload allows you to define the arithmetic operations directly, hence providing operand validations and type checks. 
#### Parameters
result 
the tensor to store the result of the arithmetic operation. 
arithmetic Operations 
the arithmetic operations you would like apply onto  Tensor s. The last line of this closure will be taken as the result and assigned to  result  tensor.  Note  there are several requirements on the operand tensors involved in the arithmetic operations defined in this closure: 
- 
The arithmetic operations defined in one closure must not involve more than 10  Tensor s.     Please split into multiple arithmetic calls if you need to do so. 
- 
All the tensors involved in this closure must be matrices, i.e., must be multi-dimensional     tensor (see Tensor.MultiDimensionalInitInfo) of exactly 2 dimensions. 
- 
All the tensors involved in the closure must have floating-point datatype, and its     datatype must not be multi-dimensional pixel types, e.g., Tensor.DataType.Image.RG_FLOAT     is not allowed. 
#### See also
Pipeline Arithmetic Scope 
#### Throws
Spatial MLException 
If the usage is not allowed by the SpatialML run-time Framework, or if the framework encounters internal error and cannot perform the requested behavior. 
```kotlin
fun arithmetic(expression: String, operands: Array<Tensor>, result: Tensor)
```
### Deprecated
Directly defining arithmetic expressions in String skips the validation of the compatibility and type of operand tensors. Consider using other overloads of Pipeline.arithmetic to define the arithmetic expressions. 
#### Replace with
```
arithmetic(result){ /*Expression*/ }
```
Defines an arithmetic operator to the pipeline. An arithmetic operator takes in an array of  PipelineTensor  (size of which must be no more than 10), and write the arithmetic result into  result . The arithmetic expression to be executed is defined by  expression . 
Note  It is not recommended to use this method. Instead, please consider use the other overloads, because this method does not provide validation nor type checks of the operand tensors involved in the arithmetic expression. If you are confident to use it, you will need to explicitly  OptIn . 

```
@OptIn(AvoidArithmeticExpressionAsString::class)pipeline.arithmetic("{0} + {1} * {3}", ...)
```
#### Parameters
expression 
The arithmetic expression to be executed. It has the following requirements: 
- 
Use {IDX} to refer to the No. IDX input tensor, where IDX is the index among the     operands parameter. 
- 
The following arithmetic symbols are allowed:  + ,  - ,  *  (matrix multiplication),      / (elementwise division),  ^ (power, the right operand to which must be a constant or 1x1     tensor),  sin ,  cos ,  tan ,  asin ,  acos ,  atan ,  sinh ,  cosh ,  tanh  and  inv  (     matrix inverse, for matrix division). Parentheses  (  and  )  are also supported. 
- 
Constants are allowed in the expression, but they cannot appear on both sides of the     arithmetic symbols listed above, such as  5.0 + 1.0  is not valid, because the callers are     required to pre-compute these arithmetic operations between constants. i.e., don't call     the method with  expression  =  {0} * (5.0 + 1.0) , but  {0} * 6.0  instead. 
- 
In terms of the computation priority ambiguity between trigonometry functions and power,     we make the following rules:  sin {0} ^ 2  means the sine of {0} ^ 2, whereas  (sin {0}) ^     2  means the power 2 of sine of operand 0. 
Valid examples are: 
- 
{0} + {1} * 2 , 
- 
sin (( {0} * 3.1415926 ) / 180) , 
- 
{0} * {1} note  this is matrix multiplication, 
- 
{0} * inv {1} . 
operands 
the input operand to the arithmetic  expression . The tensor indexed IDX in this array will replace the symbol  {IDX}  in expression. The size of this array must not exceed 10. All the tensors in this array must: 
- 
be created use  Tensor.MultiDimensionalInitInfo  as initialization config, i.e., must be     multi-dimensional tensor with no special usage; 
- 
have exactly two dimensions (current limitation, we will support multi-dimensional     arithmetic operations shortly afterwards). 
result 
the tensor to store the result of the arithmetic operation. 
#### See also
Pipeline Arithmetic Scope 
#### Throws
Spatial MLException 
If the usage is not allowed by the SpatialML run-time Framework, or if the framework encounters internal error and cannot perform the requested behavior.