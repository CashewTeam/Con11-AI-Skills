# runJavaScript | PICO Spatial SDK

spatialml:securemr / com.pico.spatial.ml.securemr / Pipeline / runJavaScript 
# runJavaScript
```kotlin
fun runJavaScript(script: String, jsVarIO: List<Pipeline.JavaScriptIO>)
```
Put a JS script into the SpatialML pipeline for execution. 
You can use data in a  Tensor  or write outputs to  Tensor  in the JavaScript codes. To do so, you will need declare a  var someName  in JavaScript, without providing the definition, and then create a tensor-to-JSvar relationship using  tensor into "someName" ,  tensor outFrom "someName" , or  tensor inToAndOutFrom "someName" . 
#### Parameters
script 
the JS script to be executed. 
js Var IO 
the tensors to be used as JS  val s in the script when being executed. For example: 

```
tensor1 = newLocalTensor(MultiDimensionalInitInfo(DataType.FLOAT32, intArrayOf(2, 3)))// tensor1 is a matrix of 2x3javaScript( "var a; a[0] = a[1] * a[3];", listOf(tensor1 into "a"), mapOf(...) ) }
```
In the JavaScript codes, the  var a  is left undefined. When the JavaScript is executed  var a  will be initialized based to an array of the same datatype as  tensor1 , i.e., an array of float, with length =  tensor1 's total amount of values. Hence,  var a  will be a float array of size 6. Since the relationship between  tensor1  and  var a  is defined as the  into , the content of  tensor1  will be copied to  var a  but the update of  var a 's content during execution will not be reflected to  tensor1 . 
#### See also
Pipeline. into Pipeline. outFrom Pipeline. into And Out From