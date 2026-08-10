# tensor | PICO Spatial SDK

spatialml:securemr / com.pico.spatial.ml.securemr / Pipeline / tensor 
# tensor
```kotlin
val Point.tensor: PipelineTensor
```
A helper getter to create a new local tensor in-place for a android  android.graphics.Point . The X and Y values of the provided point will be set as the tensor's content automatically. 
The getter returns the newly created local tensor, whose lifecycle is bound to this pipeline. The tensor will be created with  Point2ArrayInitInfo  creation info with  DataType.INT32  datatype, and use the X, Y values in the given  android.graphics.Point  as its init values. 
#### See also
Pipeline Tensor Local Pipeline. new Local Tensor 
#### Throws
Spatial MLException 
If the usage is not allowed by the SpatialML run-time Framework, or if the framework encounters internal error and cannot perform the requested behavior. 
```kotlin
val Color.tensor: PipelineTensor
```
A helper getter to create a new local tensor in-place for an android  android.graphics.Color . The R, G, B, and A values of the provided color will be set as the tensor's content automatically. 
The getter returns the newly created local tensor, whose lifecycle is bound to this pipeline. The tensor will be created with  ColorArrayInitInfo  creation info with  ColorType.R32G32B32A32_FLOAT  color format, and use the R, G, B, A values in the given  android.graphics.Color  as its init values. 
#### See also
Pipeline Tensor Local Pipeline. new Local Tensor 
#### Throws
Spatial MLException 
If the usage is not allowed by the SpatialML run-time Framework, or if the framework encounters internal error and cannot perform the requested behavior. 
```kotlin
val Array<Point>.tensor: PipelineTensor
```
A helper getter to create a new local tensor in-place for an array of android  android.graphics.Point . The X and Y values of the provided points will be set as the tensor's content automatically. 
The getter returns the newly created local tensor, whose lifecycle is bound to this pipeline. The tensor will be created with  Point2ArrayInitInfo  creation info with  DataType.INT32  datatype, and use the X, Y values in the given  android.graphics.Point  array as its init values. 
#### See also
Pipeline Tensor Local Pipeline. new Local Tensor 
#### Throws
Spatial MLException 
If the usage is not allowed by the SpatialML run-time Framework, or if the framework encounters internal error and cannot perform the requested behavior. 
```kotlin
val Array<Color>.tensor: PipelineTensor
```
A helper getter to create a new local tensor in-place for an array of  android.graphics.Color . The R, G, B, and A values of the provided colors will be set as the tensor's content automatically. 
The getter returns the newly created local tensor, whose lifecycle is bound to this pipeline. The tensor will be created with  ColorArrayInitInfo  creation info with  ColorType.R32G32B32A32_FLOAT  color format, and use the R, G, B, A values in the given  android.graphics.Color  array as its init values. 
#### See also
Pipeline Tensor Local Pipeline. new Local Tensor 
#### Throws
Spatial MLException 
If the usage is not allowed by the SpatialML run-time Framework, or if the framework encounters internal error and cannot perform the requested behavior. 
```kotlin
val Double.tensor: PipelineTensor
```
A helper getter to create a new local tensor in-place for a single double scalar. 
This returns a scalar array  PipelineTensor  of  size = 1 ,  dataType = DataType.FLOAT64 , i.e, a tensor containing only one double value, which will be initialized to this double. 
#### See also
Pipeline Tensor Local Pipeline. new Local Tensor 
#### Throws
Spatial MLException 
If the usage is not allowed by the SpatialML run-time Framework, or if the framework encounters internal error and cannot perform the requested behavior. 
```kotlin
val DoubleArray.tensor: PipelineTensor
```
A helper getter to create a new local tensor in-place for double array 
This returns a scalar array  PipelineTensor  of the same size as the double array, and  dataType = DataType.FLOAT64 , i.e, a tensor containing only one double value, which will be initialized to this double. 
#### See also
Pipeline Tensor Local Pipeline. new Local Tensor 
#### Throws
Spatial MLException 
If the usage is not allowed by the SpatialML run-time Framework, or if the framework encounters internal error and cannot perform the requested behavior. 
```kotlin
val Float.tensor: PipelineTensor
```
A helper getter to create a new local tensor in-place for a single float scalar. 
This returns a scalar array  PipelineTensor  of  size = 1 ,  dataType = DataType.FLOAT32 , i.e, a tensor containing only one float value, which will be initialized to this float. 
#### See also
Pipeline Tensor Local Pipeline. new Local Tensor 
#### Throws
Spatial MLException 
If the usage is not allowed by the SpatialML run-time Framework, or if the framework encounters internal error and cannot perform the requested behavior. 
```kotlin
val FloatArray.tensor: PipelineTensor
```
A helper getter to create a new local tensor in-place for a float array. 
This returns a scalar array  PipelineTensor  of the same size as the float array, and  dataType = DataType.FLOAT32 , i.e, a tensor initialized to this float array. 
#### See also
Pipeline Tensor Local Pipeline. new Local Tensor 
#### Throws
Spatial MLException 
If the usage is not allowed by the SpatialML run-time Framework, or if the framework encounters internal error and cannot perform the requested behavior. 
```kotlin
val Int.tensor: PipelineTensor
```
A helper getter to create a new local tensor in-place for a single int scalar. 
This returns a scalar array  PipelineTensor  of  size = 1 ,  dataType = DataType.INT32 , i.e, a tensor containing only one double value, which will be initialized to this int. 
#### See also
Pipeline Tensor Local Pipeline. new Local Tensor 
#### Throws
Spatial MLException 
If the usage is not allowed by the SpatialML run-time Framework, or if the framework encounters internal error and cannot perform the requested behavior. 
```kotlin
val IntArray.tensor: PipelineTensor
```
A helper getter to create a new local tensor in-place for an int array. 
This returns a scalar array  PipelineTensor  of the same size as the int array, and  dataType = DataType.INT32 , i.e, a tensor containing initialized to this int array. 
#### See also
Pipeline Tensor Local Pipeline. new Local Tensor 
#### Throws
Spatial MLException 
If the usage is not allowed by the SpatialML run-time Framework, or if the framework encounters internal error and cannot perform the requested behavior. 
```kotlin
val Short.tensor: PipelineTensor
```
A helper getter to create a new local tensor in-place for a single short scalar. 
This returns a scalar array  PipelineTensor  of  size = 1 ,  dataType = DataType.INT16 , i.e, a tensor containing only one short value, which will be initialized to this short. 
#### See also
Pipeline Tensor Local Pipeline. new Local Tensor 
#### Throws
Spatial MLException 
If the usage is not allowed by the SpatialML run-time Framework, or if the framework encounters internal error and cannot perform the requested behavior. 
```kotlin
val ShortArray.tensor: PipelineTensor
```
A helper getter to create a new local tensor in-place for a short array. 
This returns a scalar array  PipelineTensor  of the same size as the short array, and  dataType = DataType.INT16 , i.e, a tensor initialized to this short array. 
#### See also
Pipeline Tensor Local Pipeline. new Local Tensor 
#### Throws
Spatial MLException 
If the usage is not allowed by the SpatialML run-time Framework, or if the framework encounters internal error and cannot perform the requested behavior. 
```kotlin
val Byte.tensor: PipelineTensor
```
A helper getter to create a new local tensor in-place for a single byte scalar. 
This returns a scalar array  PipelineTensor  of  size = 1 ,  dataType = DataType.INT8 , i.e, a tensor containing only one byte value (treated as signed), which will be initialized to this byte. 
#### See also
Pipeline Tensor Local Pipeline. new Local Tensor 
#### Throws
Spatial MLException 
If the usage is not allowed by the SpatialML run-time Framework, or if the framework encounters internal error and cannot perform the requested behavior. 
```kotlin
val String.tensor: PipelineTensor
```
A helper getter to create a new local tensor in-place for a string. 
This returns a scalar array  PipelineTensor  of with  dataType  =  DataType.UINT8 . Its size of the returned tensor will be same as the parameter this string's number of bytes with UTF-8 encoding. Internally, the given string is converted to byte array with UTF-8 encoding, with which the returned tensor is initialized. 
#### See also
Pipeline Tensor Local Pipeline. new Local Tensor 
#### Throws
Spatial MLException 
If the usage is not allowed by the SpatialML run-time Framework, or if the framework encounters internal error and cannot perform the requested behavior.