# JavaScriptIO | PICO Spatial SDK

spatialml:securemr / com.pico.spatial.ml.securemr / Pipeline / JavaScriptIO 
# JavaScriptIO
```kotlin
class JavaScriptIO
```
Defining the relationship between a  Tensor , and undefined JS  val  in the JavaScript script to be executed by  Pipeline.runJavaScript . 
You can define the the relationship using: 
- 
tensor into "name" : which will copy the tensor's content into the JavaScript  val name  during execution of JavaScript, but the update of the JavaScript  val name  will not be written back to the  tensor . 
- 
tensor outFrom "name" : which will write the JavaScript  val name  after the JavaScript execution is finished, but the  val name  does not have the original  tensor 's content at initialization. 
- 
tensor inToAndOutFrom "name" : a combination of the above two: the tensor's content will be given to the JavaScript  val name , and the content updates to the  val name  by the JavaScript codes will be reflected in the  tensor  after execution. 
#### See also
Pipeline. into Pipeline. outFrom Pipeline. into And Out From