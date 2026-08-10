# makeTransform | PICO Spatial SDK

spatialml:securemr / com.pico.spatial.ml.securemr / Pipeline / makeTransform 
# makeTransform
```kotlin
fun makeTransform(rotationVec: Tensor?, translationVec: Tensor?, scaleVec: Tensor?, result: Tensor)
```
Compute the 4x4 transform matrix for translation, rotation and scale. 
#### Parameters
rotation Vec 
an optional input, for the rotation part of the transform. The rotation is expressed as a rotation vector. Hence, it must be a multi-dimensional tensor with dimensions = 1x3 or 3x1. If provided, the data type should be  DataType.FLOAT32  or  DataType.FLOAT64 . Alternatively,  DataType.Image.R_FLOAT ,  DataType.Image.R_DOUBLE  or  DataType.Image.R_FLOAT_DYNAMIC  are also acceptable but not recommended. 
translation Vec 
an optional input, for the translation part of the transform. It must be a multi-dimensional tensor with dimensions = 1x3 or 3x1. If provided, the data type should be  DataType.FLOAT32  or  DataType.FLOAT64 . Alternatively,  DataType.Image.R_FLOAT ,  DataType.Image.R_DOUBLE  or  DataType.Image.R_FLOAT_DYNAMIC  are also acceptable but not recommended. 
scale Vec 
an optional input, for the scale part of the transform. It must be a multi-dimensional tensor with dimensions = 1x3 or 3x1. If provided, the data type should be  DataType.FLOAT32  or  DataType.FLOAT64 . Alternatively,  DataType.Image.R_FLOAT ,  DataType.Image.R_DOUBLE  or  DataType.Image.R_FLOAT_DYNAMIC  are also acceptable but not recommended. 
result 
the required result to store transform matrix. It must be a multi-dimensional tensor of exactly 2 dimensions: 4x4. The data type must be  DataType.FLOAT32  or  DataType.FLOAT64 . Alternatively,  DataType.Image.R_FLOAT ,  DataType.Image.R_DOUBLE  or  DataType.Image.R_FLOAT_DYNAMIC  are also acceptable but not recommended. 
#### Throws
Spatial MLException 
If the usage is not allowed by the SpatialML run-time Framework, or if the framework encounters internal error and cannot perform the requested behavior.