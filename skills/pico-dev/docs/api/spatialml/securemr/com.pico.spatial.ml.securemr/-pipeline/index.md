# Pipeline | PICO Spatial SDK

spatialml:securemr / com.pico.spatial.ml.securemr / Pipeline 
# Pipeline
```kotlin
@RequiresApi(value = 27)
```class  Pipeline  :  BaseHandle 
SpatialML pipeline. 
Each pipeline defines a computation graph of tensors. A pipeline will not be run until it is submitted, and each submission will schedule one execution of the whole pipeline. One submitted execution will be put onto one thread in the backend, so that multiple submitted pipelines can be run concurrently. 
#### Throws
Spatial MLException 
If the usage is not allowed by the SpatialML run-time Framework, or if the framework encounters internal error and cannot perform the requested behavior. 
Members 
## Types
Color Conversion 
```kotlin
enum ColorConversion : Enum<Pipeline.ColorConversion>
```
Color conversion types. 
Java Script IO 
```kotlin
class JavaScriptIO
```
Defining the relationship between a  Tensor , and undefined JS  val  in the JavaScript script to be executed by  Pipeline.runJavaScript . 
Model Inference Type 
```kotlin
enum ModelInferenceType : Enum<Pipeline.ModelInferenceType>
```
LiteRT / TensorFlow Lite model inference backend used to accelerate model inference. 
Model Node Encoding 
```kotlin
class ModelNodeEncoding(val nodeName: String, val tensor: Tensor)
```
The association of a node in a model (TFLite, etc.) computation graph and a pipeline tensor. 
Normalize Type 
```kotlin
enum NormalizeType : Enum<Pipeline.NormalizeType>
```
Normalization type for  normalize . 
Norm Type 
```kotlin
enum NormType : Enum<Pipeline.NormType>
```
Norm type for  norm . 
Run Task 
```kotlin
class RunTask(pipeline: Pipeline, placeholderMap: Map<PipelineTensorPlaceholder, GlobalTensor>, condition: GlobalTensor?, waitFor: Pipeline.RunTask?)
```
The handle to one submitted pipeline run task. 
Sort Type 
```kotlin
enum SortType : Enum<Pipeline.SortType>
```
Enum to determine how a matrix will be sorted. 
Text Horizontal Alignment 
```kotlin
enum TextHorizontalAlignment : Enum<Pipeline.TextHorizontalAlignment>
```
Horizontal alignment that can be used to update  SceneGraphProperty.Text.HorizontalAlignment . 
Text Vertical Alignment 
```kotlin
enum TextVerticalAlignment : Enum<Pipeline.TextVerticalAlignment>
```
Vertical alignment that can be used to update  SceneGraphProperty.Text.VerticalAlignment . 
## Properties
destructor 
```kotlin
open override val destructor: BaseHandle.HandleDestructor
```
The  BaseHandle 's implementation's destructor. 
tensor 
```kotlin
val Color.tensor: PipelineTensor
```
A helper getter to create a new local tensor in-place for an android  android.graphics.Color . The R, G, B, and A values of the provided color will be set as the tensor's content automatically. 
```kotlin
val Point.tensor: PipelineTensor
```
A helper getter to create a new local tensor in-place for a android  android.graphics.Point . The X and Y values of the provided point will be set as the tensor's content automatically. 
```kotlin
val Array<Color>.tensor: PipelineTensor
```
A helper getter to create a new local tensor in-place for an array of  android.graphics.Color . The R, G, B, and A values of the provided colors will be set as the tensor's content automatically. 
```kotlin
val Array<Point>.tensor: PipelineTensor
```
A helper getter to create a new local tensor in-place for an array of android  android.graphics.Point . The X and Y values of the provided points will be set as the tensor's content automatically. 
```kotlin
val Byte.tensor: PipelineTensor
```
A helper getter to create a new local tensor in-place for a single byte scalar. 
```kotlin
val Double.tensor: PipelineTensor
```
A helper getter to create a new local tensor in-place for a single double scalar. 
```kotlin
val DoubleArray.tensor: PipelineTensor
```
A helper getter to create a new local tensor in-place for double array 
```kotlin
val Float.tensor: PipelineTensor
```
A helper getter to create a new local tensor in-place for a single float scalar. 
```kotlin
val FloatArray.tensor: PipelineTensor
```
A helper getter to create a new local tensor in-place for a float array. 
```kotlin
val Int.tensor: PipelineTensor
```
A helper getter to create a new local tensor in-place for a single int scalar. 
```kotlin
val IntArray.tensor: PipelineTensor
```
A helper getter to create a new local tensor in-place for an int array. 
```kotlin
val Short.tensor: PipelineTensor
```
A helper getter to create a new local tensor in-place for a single short scalar. 
```kotlin
val ShortArray.tensor: PipelineTensor
```
A helper getter to create a new local tensor in-place for a short array. 
```kotlin
val String.tensor: PipelineTensor
```
A helper getter to create a new local tensor in-place for a string. 
## Functions
apply Affine 
```kotlin
fun applyAffine(affineMatrix: Tensor, srcImage: Tensor, affinedImage: Tensor)
```
Apply the affine transform on 2D image. 
apply Affine Point 
```kotlin
fun applyAffinePoint(affineMatrix: Tensor, srcPoints: Tensor, affinedPoints: Tensor)
```
Apply the affine transform on 2D points rather than 2D images. 
argmax 
```kotlin
fun argmax(source: Tensor, result: Tensor)
```
Compute argmax operation on tensor, giving the indices of max element of the input tensor. 
arithmetic 
```kotlin
fun arithmetic(result: Tensor, arithmeticOperations: PipelineArithmeticScope.() -> PipelineArithmeticScope.TensorArithmetic)
```
Defines an arithmetic operator to the pipeline. The operator allows you to define complex operations between tensors. Different from the above overload which is defined by a string expression, this overload allows you to define the arithmetic operations directly, hence providing operand validations and type checks. 
```kotlin
fun arithmetic(expression: String, operands: Array<Tensor>, result: Tensor)
```
Defines an arithmetic operator to the pipeline. An arithmetic operator takes in an array of  PipelineTensor  (size of which must be no more than 10), and write the arithmetic result into  result . The arithmetic expression to be executed is defined by  expression . 
bitwise And 
```kotlin
fun bitwiseAnd(tensor1: Tensor, tensor2: Tensor, result: Tensor)
```
Perform an bitwise-and of two input tensors. 
bitwise Or 
```kotlin
fun bitwiseOr(tensor1: Tensor, tensor2: Tensor, result: Tensor)
```
Perform an bitwise-or of two input tensors. 
bytewise All 
```kotlin
fun bytewiseAll(operand: Tensor, result: Tensor)
```
Perform a byte-wise all on all the values constituting the tensor. 
bytewise Any 
```kotlin
fun bytewiseAny(operand: Tensor, result: Tensor)
```
Perform a byte-wise any on all the values constituting the tensor. 
capture Microphone 
```kotlin
fun captureMicrophone(sampleRate: Int, stereoTrackResult: Tensor, timestampResult: Tensor? = null)
```
Captures microphone stereo-audio track into tensors, encoded in compatible PCM format. 
```kotlin
fun captureMicrophone(sampleRate: Int, leftTrackResult: Tensor? = null, rightTrackResult: Tensor? = null, timestampResult: Tensor? = null)
```
Captures microphone left and right audio track into separated tensors, encoded in compatible PCM format.  Note:  at least one of the  leftTrackResult  and the  rightTrackResult  must be present. 
convert Color 
```kotlin
fun convertColor(conversionType: Pipeline.ColorConversion, source: Tensor, result: Tensor)
```
```kotlin
fun convertColor(opencvConvertStr: String, source: Tensor, result: Tensor)
```
Convert the color, e.g. RGB-to-Grayscale, RGB-to-BGR, etc. 
copy 
```kotlin
fun copy(src: PipelineTensorSlice, dst: PipelineTensorSlice)
```
Copy from a slice of one pipeline tensor to a slice of another tensor. The slice of the copy source must contain the same number of values as the total number of values in the copy destination. 
```kotlin
fun copy(src: PipelineTensorSlice, dst: Tensor)
```
Copy from one slice of a pipeline tensor to another. The slice of the copy source must contain the same number of values as the total number of values in the copy destination. 
```kotlin
fun copy(src: Tensor, dst: PipelineTensorSlice)
```
Copy from one pipeline tensor to a slice of another tensor. The slice of the copy source must contain the same number of values as the total number of values in the copy destination. 
```kotlin
fun copy(src: Tensor, dst: Tensor)
```
Copy from one pipeline tensor to another. The two pipeline tensors, respectively denoted as  src  and  dst , must have the same number of values. 
elementwise Max 
```kotlin
fun elementwiseMax(tensor1: Tensor, tensor2: Tensor, result: Tensor)
```
Perform an elementwise-max of two input tensors. 
elementwise Min 
```kotlin
fun elementwiseMin(tensor1: Tensor, tensor2: Tensor, result: Tensor)
```
Perform an elementwise-min of two input tensors. 
elementwise Multiply 
```kotlin
fun elementwiseMultiply(tensor1: Tensor, tensor2: Tensor, result: Tensor)
```
Perform an elementwise-multiplication of two input tensors. 
equal 
```kotlin
fun equal(tensor1: Tensor, tensor2: Tensor, result: Tensor)
```
Perform an elementwise-equal comparison of two input tensors. 
get 
```kotlin
operator fun GlobalTensor.get(indices: PipelineTensor): PipelineTensorSlice
```
Convenient method to directly create a slice of a GlobalTensor using bracket operators from a tensor. This operator overload allows SpatialML framework users to apply tensors output from previous steps as a  dynamic  slices. 
```kotlin
operator fun GlobalTensor.get(vararg indexAndSkips: IntProgression): PipelineTensorSlice
```
Convenient method to directly create a slice of a GlobalTensor using bracket operators from  IntProgression . Different from the overloaded method that uses  IntRange  as inputs,  IntProgression  allows skip and backward iteration. Similarly, there must be the same number of  IntProgression  inputs as the number of this tensor's dimensions 
```kotlin
operator fun GlobalTensor.get(vararg indices: IntRange): PipelineTensorSlice
```
Convenient method to directly create a slice of a GlobalTensor using bracket operators from  IntRange s like  0..5, 1..2 . 
```kotlin
operator fun PipelineTensorSlice.get(channelSliceTensor: Tensor): PipelineTensorSlice
```
Create a slice on channels using bracket operators from a slice tensor. 
get Affine 
```kotlin
fun getAffine(srcPoints: Tensor, affinedPoints: Tensor, affineMatrixResult: Tensor)
```
Compute the 2D affine transform between two triangles. 
get Depth Map 
```kotlin
fun getDepthMap(depthMapResult: Tensor)
```
Using PICO's depth sensor to get the depth map. The depth map's FOV is fixed at 90 degrees vertically, 109 degrees horizontally. 
into 
```kotlin
infix fun Tensor.into(jsVarName: String): Pipeline.JavaScriptIO
```
Define a relationship between a  Tensor  and a JS  var  in the JavaScript script to be executed by  Pipeline.runJavaScript  that: will copy the tensor's content into the JavaScript  var name  during execution of JavaScript, but the update of the JavaScript  var name  will not be written back to the  tensor . 
into And Out From 
```kotlin
infix fun Tensor.intoAndOutFrom(jsVarName: String): Pipeline.JavaScriptIO
```
Define a relationship between a  Tensor  and a JS  var  in the JavaScript script to be executed by  Pipeline.runJavaScript  that: will copy the tensor's content into the JavaScript  var name  during execution of JavaScript, and the update of the JavaScript  var name  will be written back to the  tensor  after the execution of JavaScript. 
inversion 
```kotlin
fun inversion(source: Tensor, result: Tensor)
```
Compute the matrix inversion. 
larger Equal 
```kotlin
fun largerEqual(tensor1: Tensor, tensor2: Tensor, result: Tensor)
```
Perform an elementwise-large-equal comparison of two input tensors. 
larger Than 
```kotlin
fun largerThan(tensor1: Tensor, tensor2: Tensor, result: Tensor)
```
Perform an elementwise-large-than comparison of two input tensors. 
make Transform 
```kotlin
fun makeTransform(rotationVec: Tensor?, translationVec: Tensor?, scaleVec: Tensor?, result: Tensor)
```
Compute the 4x4 transform matrix for translation, rotation and scale. 
new Local Tensor 
```kotlin
fun newLocalTensor(color: Color): PipelineTensorLocal
```
A helper function to create a new local tensor in-place for an android  android.graphics.Color . The R, G, B, and A values of the provided color will be set as the tensor's content automatically. 
```kotlin
fun newLocalTensor(point2: Point): PipelineTensorLocal
```
A helper function to create a new local tensor in-place for a android  android.graphics.Point . The X and Y values of the provided point will be set as the tensor's content automatically. 
```kotlin
fun newLocalTensor(config: Tensor.InitInfo): PipelineTensor
```
Create a new local tensor inside this pipeline. The tensor have memory allocated local to the pipeline. 
```kotlin
fun newLocalTensor(colorArray: Array<Color>): PipelineTensorLocal
```
A helper function to create a new local tensor in-place for an array of  android.graphics.Color . The R, G, B, and A values of the provided colors will be set as the tensor's content automatically. 
```kotlin
fun newLocalTensor(point2Array: Array<Point>): PipelineTensorLocal
```
A helper function to create a new local tensor in-place for an array of android  android.graphics.Point . The X and Y values of the provided points will be set as the tensor's content automatically. 
```kotlin
fun newLocalTensor(char: Byte): PipelineTensorLocal
```
A helper function to create a new local tensor in-place for a single character. 
```kotlin
fun newLocalTensor(doubleVal: Double): PipelineTensorLocal
```
A helper function to create a new local tensor in-place for a single double scalar. 
```kotlin
fun newLocalTensor(doubleVal: DoubleArray): PipelineTensorLocal
```
A helper function to create a new local tensor in-place for a double array. 
```kotlin
fun newLocalTensor(floatVal: Float): PipelineTensorLocal
```
A helper function to create a new local tensor in-place for a single float scalar. 
```kotlin
fun newLocalTensor(floatVal: FloatArray): PipelineTensorLocal
```
A helper function to create a new local tensor in-place for a float array. 
```kotlin
fun newLocalTensor(intVal: Int): PipelineTensorLocal
```
A helper function to create a new local tensor in-place for a single int scalar. 
```kotlin
fun newLocalTensor(intVal: IntArray): PipelineTensorLocal
```
A helper function to create a new local tensor in-place for an int array. 
```kotlin
fun newLocalTensor(shortVal: Short): PipelineTensorLocal
```
A helper function to create a new local tensor in-place for a single short scalar. 
```kotlin
fun newLocalTensor(shortVal: ShortArray): PipelineTensorLocal
```
A helper function to create a new local tensor in-place for a short array. 
```kotlin
fun newLocalTensor(string: String): PipelineTensorLocal
```
A helper function to create a new local tensor in-place for a string. 
new Placeholder 
```kotlin
fun newPlaceholder(config: Tensor.InitInfo): PipelineTensorPlaceholder
```
Create a new placeholder tensor inside this pipeline. Different from a local tensor, a placeholder tensor has  no  local memory allocated in the pipeline's scope; on the contrary, the placeholder must refer to a compatible global tensor when the pipeline is submitted for execution. 
new Placeholder Like 
```kotlin
fun newPlaceholderLike(globalTensor: GlobalTensor): PipelineTensorPlaceholder
```
Create a new placeholder tensor inside this pipeline with guarantee compatibility with the a  GlobalTensor , i.e., the newly created placeholder share the same configuration with the  GlobalTensor .  Note:  a placeholder tensor has  no  local memory allocated in the pipeline's scope; on the contrary, the placeholder must refer to a compatible global tensor when the pipeline is submitted for execution. 
new Scene From GLTF 
```kotlin
fun newSceneFromGLTF(gltfSceneMemory: SharedMemory): PipelineTensor
```
Create an SpatialML scene from a glTF file already loaded into SharedMemory. Similar to  SpatialMLSession.newSceneFromGLTF  but that one creates a global scene graph handle, so that multiple pipelines can share, whereas this method creates one scene graph local to the pipeline only. 
non Maximum Suppression 
```kotlin
fun nonMaximumSuppression(iou: Float, scores: Tensor, boxes: Tensor, scoresResult: Tensor? = null, boxesResult: Tensor? = null, indicesResult: Tensor? = null)
```
Run non-maximum-suppression (NMS) on 2D bounding boxes. 
norm 
```kotlin
fun norm(type: Pipeline.NormType, srcTensor: Tensor, result: Tensor)
```
Compute the norm of a tensor. 
normalize 
```kotlin
fun normalize(type: Pipeline.NormalizeType, source: Tensor, alphaBeta: Tensor?, result: Tensor)
```
Normalize a tensor. 
not Equal 
```kotlin
fun notEqual(tensor1: Tensor, tensor2: Tensor, result: Tensor)
```
Perform an elementwise-not-equal comparison of two input tensors. 
out From 
```kotlin
infix fun Tensor.outFrom(jsVarName: String): Pipeline.JavaScriptIO
```
Define a relationship between a  Tensor  and a JS  var  in the JavaScript script to be executed by  Pipeline.runJavaScript  that: will write the content of the specified JS  var  to the tensor after the JavaScript's execution is done. The JS  var  will be initialized as an all-zero JS array of the corresponding datatype, with length = the total count of elements in the Tensor. 
output Sounds 
```kotlin
fun outputSounds(sampleRate: Int, audioTrack: Tensor)
```
Play sounds from an audio track. The audio track must be encoded in PCM format. 
rectified VSTAccess 
```kotlin
fun rectifiedVSTAccess(rightImageResult: Tensor?, leftImageResult: Tensor?, timestampResult: Tensor?, cameraMatrixResult: Tensor?)
```
Obtain the latest camera images. The images will be rectified internal against len distortion. 
run Java Script 
```kotlin
fun runJavaScript(script: String, jsVarIO: List<Pipeline.JavaScriptIO>)
```
Put a JS script into the SpatialML pipeline for execution. 
run Model Inference 
```kotlin
fun runModelInference(modelName: String, modelType: Pipeline.ModelInferenceType, modelBinary: SharedMemory, inputs: Array<Pipeline.ModelNodeEncoding>, outputs: Array<Pipeline.ModelNodeEncoding>)
```
Run the inference of an algorithm model provided in binary package. 
singular Value Decomposition 
```kotlin
fun singularValueDecomposition(source: Tensor, wResult: Tensor?, uResult: Tensor?, vtResult: Tensor?)
```
Perform singular value decomposition of a matrix. 
smaller Equal 
```kotlin
fun smallerEqual(tensor1: Tensor, tensor2: Tensor, result: Tensor)
```
Perform an elementwise-smaller-equal comparison of two input tensors. 
smaller Than 
```kotlin
fun smallerThan(tensor1: Tensor, tensor2: Tensor, result: Tensor)
```
Perform an elementwise-smaller-than comparison of two input tensors. 
solve Pn P 
```kotlin
fun solvePnP(objPoints: Tensor, imgPoints: Tensor, camMatrix: Tensor, rotationVecResult: Tensor? = null, translationVecResult: Tensor? = null)
```
Run the OpenCV solve PnP algorithm. Solve PnP reverses the camera projection procedure: given the projected result (2D points) of the vertices of a mesh, and the original 3D coordinates of the mesh vertices corresponding to the mesh's local space, inferring the most likely pose of the mesh corresponding to the camera space. 
sort Matrix 
```kotlin
fun sortMatrix(sortType: Pipeline.SortType, source: Tensor, sortedResult: Tensor?, indexResult: Tensor?)
```
Sort a matrix, column-by-column or row-by-row. 
sort Vec 
```kotlin
fun sortVec(source: Tensor, sortedResult: Tensor?, indexResult: Tensor?)
```
Sort a scalar array. 
submit 
```kotlin
fun submit(parameters: Map<PipelineTensorPlaceholder, GlobalTensor>, condition: GlobalTensor?, waitFor: Pipeline.RunTask?): Pipeline.RunTask
```
Submit the pipeline for  one  run. Note: the method only submits the run as a task, and SpatialML framework will schedule the task based on its  waitFor  task, the  GlobalTensor  it will access, and the current computation resource availability. 
switch CHWAnd HWC 
```kotlin
fun switchCHWAndHWC(source: Tensor, result: Tensor)
```
Switch tensor content between a CHW and HWC format. A tensor of CHW format means it is a multi-dimensional tensor of datatype =  Tensor.DataType , and 3 dimensions:  C x H x W . A tensor of HWC format means it is a multi-dimensional tensor of 2 dimensions:  H x W , with datatype =  Tensor.DataType.Image . 
switch Scene Visibility 
```kotlin
fun switchSceneVisibility(sceneEntity: Tensor, visible: Tensor)
```
Control the visibility of an already-loaded scene graph tensor. 
update Scene Graph Property 
```kotlin
fun updateSceneGraphProperty(sceneEntity: Tensor, entityPath: String, targetProperty: SceneGraphProperty, data: Tensor)
```
Update data of a specified component property in the scene graph, using the values from a tensor. 
update Scene Graph Text Content 
```kotlin
fun updateSceneGraphTextContent(sceneEntity: Tensor, entityPath: String, text: String)
```
Update data of text content of a text component in the scene graph using a text String. 
update Scene Graph Text Horizontal Alignment 
```kotlin
fun updateSceneGraphTextHorizontalAlignment(sceneEntity: Tensor, entityPath: String, horizontalAlignment: Pipeline.TextHorizontalAlignment)
```
Update data of horizontal alignment of a text component in the scene graph using the alignment enum defined in  TextHorizontalAlignment . 
update Scene Graph Text Vertical Alignment 
```kotlin
fun updateSceneGraphTextVerticalAlignment(sceneEntity: Tensor, entityPath: String, verticalAlignment: Pipeline.TextVerticalAlignment)
```
Update data of vertical alignment of a text component in the scene graph using the alignment enum defined in  TextVerticalAlignment . 
uv To3DIn Camera Space 
```kotlin
fun uvTo3DInCameraSpace(uv: Tensor, timestamp: Tensor, camMatrix: Tensor, leftImage: Tensor, rightImage: Tensor, point3Result: Tensor)
```
Using PICO's depth sensor and stereo view RGB images, estimate the 3D coordinates of 2D points on camera output.