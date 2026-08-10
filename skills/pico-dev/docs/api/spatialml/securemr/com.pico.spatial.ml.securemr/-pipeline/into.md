# into | PICO Spatial SDK

spatialml:securemr / com.pico.spatial.ml.securemr / Pipeline / into 
# into
```kotlin
infix fun Tensor.into(jsVarName: String): Pipeline.JavaScriptIO
```
Define a relationship between a  Tensor  and a JS  var  in the JavaScript script to be executed by  Pipeline.runJavaScript  that: will copy the tensor's content into the JavaScript  var name  during execution of JavaScript, but the update of the JavaScript  var name  will not be written back to the  tensor . 
#### Return
A  JavaScriptIO  describing the relationship that the tensor's data will initialized the JavaScript  var jsVarName  and the former's content will be copied  into  the later. 
#### Parameters
js Var Name 
the name of the JS  var  in the JavaScript script to be executed by  Pipeline.runJavaScript . The JS  var jsVarName  will be initialized as a JS Array of floats, of length equal to the total count of elements in this tensor, whose content will be initialized with the content of this tensor's content at run time. 
Note  the JS  var  must not be initialized in the script. The JS  var  will be initialized by the SpatialML based on the datatype and the total count of elements in this tensor at run time. For example, if you: 

```
var tensor1 = newLocalTensor(MultiDimensionalInitInfo(DataType.FLOAT32, intArrayOf(2, 3)))tensor1 into "my_js_var"
```
The JS  var  called  my_js_var  will be initialized as a JS Array of floats, of length 6, because the  tensor1  is an FLOAT32 tensor of 2x3 = 6 elements in total. If the 
The following JavaScript codes are wrong, because it initializes the JS  var  in the script, conflicting with the relationship defined above. 
```
var my_js_var = [1.0, 2.0, 3.0];
```
Instead, your JavaScript codes should be: 

```
var my_js_var;my_js_var[0] = 2.0;...
```
Because the  my_js_var  will be initialized with the  tensor1  at runtime.