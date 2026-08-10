# convertColor | PICO Spatial SDK

spatialml:securemr / com.pico.spatial.ml.securemr / Pipeline / convertColor 
# convertColor
```kotlin
fun convertColor(opencvConvertStr: String, source: Tensor, result: Tensor)
```
Convert the color, e.g. RGB-to-Grayscale, RGB-to-BGR, etc. 
The method is provided only for the convenience of migration of OpenCV codes. It is recommended to use other overloads. 
#### Parameters
opencv Convert Str 
the OpenCV's  cv::ColorConversionCodes  enum values, converted to string. For example, if you want to convert an RGBA image to a grayscale image, you may enter  "11" , because  cv::COLOR_RGBA2GRAY  enum is defined as  11  in  OpenCV's specification . 
source 
the tensor to be converted. It must be a multi-dimensional tensor, whose number of channels must match the expectation implied by the  opencvConvertStr  conversion string. For example, if the string is  "11  ( cv::COLOR_RGBA2GRAY ), the  source  must be of 4 channels. The number of dimensions must be 2. 
result 
the required result to store conversion outcome. It must be a multi-dimensional tensor, whose number of channels must match the expectation implied by  opencvConvertStr . For example, if the string is  "11  ( cv::COLOR_RGBA2GRAY ), the  result  must be of 1 channel. Its dimensions must be the same as those of  source . 
#### Throws
Spatial MLException 
If the usage is not allowed by the SpatialML run-time Framework, or if the framework encounters internal error and cannot perform the requested behavior. 
```kotlin
fun convertColor(conversionType: Pipeline.ColorConversion, source: Tensor, result: Tensor)
```
Convert the color, e.g. RGB-to-Grayscale, RGB-to-BGR, etc. 
#### Parameters
conversion Type 
the type of conversion you want to carry out. 
source 
the tensor to be converted. It must be a multi-dimensional tensor, whose number of channels must match the expectation implied by the  conversionType  conversion string. For example, if the string is  ColorConversion.RGBA_TO_GRAY , the  source  must be of 4 channels. The number of dimensions must be 2. 
result 
the required result to store conversion outcome. It must be a multi-dimensional tensor, whose number of channels must match the expectation implied by  conversionType . For example, if the string is  ColorConversion.RGB_TO_GRAY  must be of 1 channel. Its dimensions must be the same as those of  source . 
#### Throws
Spatial MLException 
If the usage is not allowed by the SpatialML run-time Framework, or if the framework encounters internal error and cannot perform the requested behavior.