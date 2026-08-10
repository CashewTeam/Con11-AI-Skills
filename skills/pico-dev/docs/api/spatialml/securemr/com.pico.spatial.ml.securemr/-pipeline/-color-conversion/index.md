# ColorConversion | PICO Spatial SDK

spatialml:securemr / com.pico.spatial.ml.securemr / Pipeline / ColorConversion 
# ColorConversion
```kotlin
enum ColorConversion : Enum<Pipeline.ColorConversion>
```
Color conversion types. 
Members Entries 
## Entries
BGR_TO_BGRA 
```kotlin
BGR_TO_BGRA
```
Conversion from BGR color space to BGRA. 
RGB_TO_RGBA 
```kotlin
RGB_TO_RGBA
```
Conversion from RGB color space to RGBA. 
BGRA_TO_BGR 
```kotlin
BGRA_TO_BGR
```
Conversion from BGRA color space to BGR. 
RGBA_TO_RGB 
```kotlin
RGBA_TO_RGB
```
Conversion from RGBA color space to RGB. 
BGR_TO_RGBA 
```kotlin
BGR_TO_RGBA
```
Conversion from BGR color space to RGBA. 
RGB_TO_BGRA 
```kotlin
RGB_TO_BGRA
```
Conversion from RGB color space to BGRA. 
RGBA_TO_BGR 
```kotlin
RGBA_TO_BGR
```
Conversion from RGBA color space to BGR. 
BGRA_TO_RGB 
```kotlin
BGRA_TO_RGB
```
Conversion from BGRA color space to RGB. 
BGR_TO_RGB 
```kotlin
BGR_TO_RGB
```
Conversion from BGR color space to RGB. 
RGB_TO_BGR 
```kotlin
RGB_TO_BGR
```
Conversion from RGB color space to BGR. 
BGRA_TO_RGBA 
```kotlin
BGRA_TO_RGBA
```
Conversion from BGRA color space to RGBA. 
RGBA_TO_BGRA 
```kotlin
RGBA_TO_BGRA
```
Conversion from RGBA color space to BGRA. 
BGR_TO_GRAY 
```kotlin
BGR_TO_GRAY
```
Conversion from BGR color space to gray scale. 
RGB_TO_GRAY 
```kotlin
RGB_TO_GRAY
```
Conversion from RGB color space to gray scale. 
GRAY_TO_BGR 
```kotlin
GRAY_TO_BGR
```
Conversion from gray scale to BGR color space, using  OpenCV's conversion algorithm  for color recovery. 
GRAY_TO_RGB 
```kotlin
GRAY_TO_RGB
```
Conversion from gray scale to RGB color space, using  OpenCV's conversion algorithm  for color recovery. 
GRAY_TO_BGRA 
```kotlin
GRAY_TO_BGRA
```
Conversion from gray scale to BGRA color space, using  OpenCV's conversion algorithm  for color recovery. 
GRAY_TO_RGBA 
```kotlin
GRAY_TO_RGBA
```
Conversion from gray scale to RGBA color space, using  OpenCV's conversion algorithm  for color recovery. 
BGRA_TO_GRAY 
```kotlin
BGRA_TO_GRAY
```
Conversion from BGRA color space to gray scale. 
RGBA_TO_GRAY 
```kotlin
RGBA_TO_GRAY
```
Conversion from RGBA color space to gray scale. 
BGR_TO_XYZ 
```kotlin
BGR_TO_XYZ
```
Conversion from BGR to CIE-1931 XYZ color space. 
RGB_TO_XYZ 
```kotlin
RGB_TO_XYZ
```
Conversion from RGB to CIE-1931 XYZ color space. 
XYZ_TO_BGR 
```kotlin
XYZ_TO_BGR
```
Conversion from CIE-1931 XYZ to BGR color space. 
XYZ_TO_RGB 
```kotlin
XYZ_TO_RGB
```
Conversion from CIE-1931 XYZ to RGB color space. 
BGR_TO_HSV 
```kotlin
BGR_TO_HSV
```
Conversion from BGR to HSV color space using the same  color conversion formula  as OpenCV's  cvtColor . 
RGB_TO_HSV 
```kotlin
RGB_TO_HSV
```
Conversion from RGB to HSV color space using the same  color conversion formula  as OpenCV's  cvtColor . 
HSV_TO_BGR 
```kotlin
HSV_TO_BGR
```
Conversion from HSV to BGR color space using the same  color conversion formula  as OpenCV's  cvtColor . 
HSV_TO_RGB 
```kotlin
HSV_TO_RGB
```
Conversion from HSV to RGB color space using the same  color conversion formula  as OpenCV's  cvtColor . 
BGR_TO_HLS 
```kotlin
BGR_TO_HLS
```
Conversion from BGR to HLS color space using the same  color conversion formula as OpenCV's  cvtColor  as OpenCV's  cvtColor . 
RGB_TO_HLS 
```kotlin
RGB_TO_HLS
```
Conversion from RGB to HLS color space using the same  color conversion formula as OpenCV's  cvtColor  as OpenCV's  cvtColor . 
HLS_TO_BGR 
```kotlin
HLS_TO_BGR
```
Conversion from HLS to BGR color space using the same  color conversion formula as OpenCV's  cvtColor  as OpenCV's  cvtColor . 
HLS_TO_RGB 
```kotlin
HLS_TO_RGB
```
Conversion from HLS to RGB color space using the same  color conversion formula as OpenCV's  cvtColor  as OpenCV's  cvtColor . 
## Properties
entries 
```kotlin
val entries: EnumEntries<Pipeline.ColorConversion>
```
Returns a representation of an immutable list of all enum entries, in the order they're declared. 
## Functions
value Of 
```kotlin
fun valueOf(value: String): Pipeline.ColorConversion
```
Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.) 
values 
```kotlin
fun values(): Array<Pipeline.ColorConversion>
```
Returns an array containing the constants of this enum type, in the order they're declared.