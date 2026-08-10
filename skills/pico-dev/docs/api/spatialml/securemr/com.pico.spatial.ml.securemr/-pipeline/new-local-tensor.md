# newLocalTensor | PICO Spatial SDK

spatialml:securemr / com.pico.spatial.ml.securemr / Pipeline / newLocalTensor 
# newLocalTensor
```kotlin
fun newLocalTensor(config: Tensor.InitInfo): PipelineTensor
```
Create a new local tensor inside this pipeline. The tensor have memory allocated local to the pipeline. 
#### Return
the newly created local tensor, whose lifecycle is bound to this pipeline. 
#### Parameters
config 
the configuration of the local tensor. 
#### See also
Pipeline Tensor Local 
#### Throws
Spatial MLException 
If the usage is not allowed by the SpatialML run-time Framework, or if the framework encounters internal error and cannot perform the requested behavior. 
```kotlin
fun newLocalTensor(point2: Point): PipelineTensorLocal
```
A helper function to create a new local tensor in-place for a android  android.graphics.Point . The X and Y values of the provided point will be set as the tensor's content automatically. 
#### Return
the newly created local tensor, whose lifecycle is bound to this pipeline. The tensor will be created with  Point2ArrayInitInfo  creation info with  DataType.INT32  datatype, and use the X, Y values in the given  android.graphics.Point  as its init values. 
#### Parameters
point2 
the  Point  whose values will be set to the newly-created tensor. 
#### See also
Pipeline Tensor Local 
#### Throws
Spatial MLException 
If the usage is not allowed by the SpatialML run-time Framework, or if the framework encounters internal error and cannot perform the requested behavior. 
```kotlin
fun newLocalTensor(point2Array: Array<Point>): PipelineTensorLocal
```
A helper function to create a new local tensor in-place for an array of android  android.graphics.Point . The X and Y values of the provided points will be set as the tensor's content automatically. 
#### Return
the newly created local tensor, whose lifecycle is bound to this pipeline. The tensor will be created with  Point2ArrayInitInfo  creation info with  DataType.INT32  datatype, and use the X, Y values in the given  android.graphics.Point  array as its init values. 
#### Parameters
point2Array 
the  Point  array whose values will be set to the newly-created tensor. 
#### See also
Pipeline Tensor Local 
#### Throws
Spatial MLException 
If the usage is not allowed by the SpatialML run-time Framework, or if the framework encounters internal error and cannot perform the requested behavior. 
```kotlin
fun newLocalTensor(color: Color): PipelineTensorLocal
```
A helper function to create a new local tensor in-place for an android  android.graphics.Color . The R, G, B, and A values of the provided color will be set as the tensor's content automatically. 
#### Return
the newly created local tensor, whose lifecycle is bound to this pipeline. The tensor will be created with  ColorArrayInitInfo  creation info with  ColorType.R32G32B32A32_FLOAT  color format, and use the R, G, B, A values in the given  android.graphics.Color  as its init values. 
#### Parameters
color 
the  Color  whose values will be set to the newly-created tensor. 
#### See also
Pipeline Tensor Local 
#### Throws
Spatial MLException 
If the usage is not allowed by the SpatialML run-time Framework, or if the framework encounters internal error and cannot perform the requested behavior. 
```kotlin
fun newLocalTensor(colorArray: Array<Color>): PipelineTensorLocal
```
A helper function to create a new local tensor in-place for an array of  android.graphics.Color . The R, G, B, and A values of the provided colors will be set as the tensor's content automatically. 
#### Return
the newly created local tensor, whose lifecycle is bound to this pipeline. The tensor will be created with  ColorArrayInitInfo  creation info with  ColorType.R32G32B32A32_FLOAT  color format, and use the R, G, B, A values in the given  android.graphics.Color  array as its init values. 
#### Parameters
color Array 
the  Color  array whose values will be set to the newly-created tensor. 
#### See also
Pipeline Tensor Local 
#### Throws
Spatial MLException 
If the usage is not allowed by the SpatialML run-time Framework, or if the framework encounters internal error and cannot perform the requested behavior. 
```kotlin
fun newLocalTensor(doubleVal: Double): PipelineTensorLocal
```
A helper function to create a new local tensor in-place for a single double scalar. 
#### Return
A scalar array  PipelineTensor  of  size = 1 ,  dataType = DataType.FLOAT64 , i.e, a tensor containing only one double value, which will be initialized to the given  doubleVal . 
#### Parameters
double Val 
The double value to be set as the initial value of the tensor. 
#### Throws
Spatial MLException 
If the usage is not allowed by the SpatialML run-time Framework, or if the framework encounters internal error and cannot perform the requested behavior. 
```kotlin
fun newLocalTensor(doubleVal: DoubleArray): PipelineTensorLocal
```
A helper function to create a new local tensor in-place for a double array. 
#### Return
A scalar array  PipelineTensor  of the same size as the double array,  dataType = DataType.FLOAT64 , i.e, a tensor containing which will be initialized to the given  doubleVal . 
#### Parameters
double Val 
The double array to be set as the initial value of the tensor. 
#### Throws
Spatial MLException 
If the usage is not allowed by the SpatialML run-time Framework, or if the framework encounters internal error and cannot perform the requested behavior. 
```kotlin
fun newLocalTensor(floatVal: Float): PipelineTensorLocal
```
A helper function to create a new local tensor in-place for a single float scalar. 
#### Return
A scalar array  PipelineTensor  of the same size as the float array,  dataType = DataType.FLOAT32 , i.e, a tensor containing only one float value, which will be initialized to the given  floatVal . 
#### Parameters
float Val 
The float value to be set as the initial value of the tensor. 
#### Throws
Spatial MLException 
If the usage is not allowed by the SpatialML run-time Framework, or if the framework encounters internal error and cannot perform the requested behavior. 
```kotlin
fun newLocalTensor(floatVal: FloatArray): PipelineTensorLocal
```
A helper function to create a new local tensor in-place for a float array. 
#### Return
A scalar array  PipelineTensor  of the same  size  as the array,  dataType = DataType.FLOAT32 , i.e, a tensor which will be initialized to the given  floatVal . 
#### Parameters
float Val 
The float array to be set as the initial value of the tensor. 
#### Throws
Spatial MLException 
If the usage is not allowed by the SpatialML run-time Framework, or if the framework encounters internal error and cannot perform the requested behavior. 
```kotlin
fun newLocalTensor(intVal: Int): PipelineTensorLocal
```
A helper function to create a new local tensor in-place for a single int scalar. 
#### Return
A scalar array  PipelineTensor  of  size = 1 ,  dataType = DataType.INT32 , i.e, a tensor containing only one int value, which will be initialized to the given  intVal . 
#### Parameters
int Val 
The int value to be set as the initial value of the tensor. 
#### Throws
Spatial MLException 
If the usage is not allowed by the SpatialML run-time Framework, or if the framework encounters internal error and cannot perform the requested behavior. 
```kotlin
fun newLocalTensor(intVal: IntArray): PipelineTensorLocal
```
A helper function to create a new local tensor in-place for an int array. 
#### Return
A scalar array  PipelineTensor  of the same size as the int array,  dataType = DataType.FLOAT32 , i.e, a tensor which will be initialized to the given  intVal . 
#### Parameters
int Val 
The int array to be set as the initial value of the tensor. 
#### Throws
Spatial MLException 
If the usage is not allowed by the SpatialML run-time Framework, or if the framework encounters internal error and cannot perform the requested behavior. 
```kotlin
fun newLocalTensor(shortVal: Short): PipelineTensorLocal
```
A helper function to create a new local tensor in-place for a single short scalar. 
#### Return
A scalar array  PipelineTensor  of  size = 1 ,  dataType = DataType.INT16 , i.e, a tensor containing only one short value, which will be initialized to the given  shortVal . 
#### Parameters
short Val 
The short value to be set as the initial value of the tensor. 
#### Throws
Spatial MLException 
If the usage is not allowed by the SpatialML run-time Framework, or if the framework encounters internal error and cannot perform the requested behavior. 
```kotlin
fun newLocalTensor(shortVal: ShortArray): PipelineTensorLocal
```
A helper function to create a new local tensor in-place for a short array. 
#### Return
A scalar array  PipelineTensor  of the same size as the short array,  dataType = DataType.INT16 , i.e, a tensor which will be initialized to the given  shortVal . 
#### Parameters
short Val 
The short array to be set as the initial value of the tensor. 
#### Throws
Spatial MLException 
If the usage is not allowed by the SpatialML run-time Framework, or if the framework encounters internal error and cannot perform the requested behavior. 
```kotlin
fun newLocalTensor(char: Byte): PipelineTensorLocal
```
A helper function to create a new local tensor in-place for a single character. 
#### Return
A scalar array  PipelineTensor  of  size = 1 ,  dataType = DataType.UINT8 , i.e, a tensor containing only one UINT8 value, which will be initialized to the given  char . 
#### Parameters
char 
The single character to be set as the initial value of the tensor. 
#### Throws
Spatial MLException 
If the usage is not allowed by the SpatialML run-time Framework, or if the framework encounters internal error and cannot perform the requested behavior. 
```kotlin
fun newLocalTensor(string: String): PipelineTensorLocal
```
A helper function to create a new local tensor in-place for a string. 
#### Return
A scalar array  PipelineTensor  of with  dataType  =  DataType.UINT8 . The array size of the returned tensor will be same as the parameter  string 's number of bytes with UTF-8 encoding. Internally, the given  string  is converted to byte array with UTF-8 encoding, with which the returned tensor is initialized. 
#### Parameters
string 
The string to be set as the initial value of the tensor. 
#### Throws
Spatial MLException 
If the usage is not allowed by the SpatialML run-time Framework, or if the framework encounters internal error and cannot perform the requested behavior.