# Companion | PICO Spatial SDK

foundation / com.pico.spatial.core.math / Color4 / Companion 
# Companion
```kotlin
object Companion
```
The companion object of  Color4 . 
Members 
## Properties
BLACK 
```kotlin
@JvmField
```val  BLACK :  Color4 
Default black data. 
BLUE 
```kotlin
@JvmField
```val  BLUE :  Color4 
Default blue data. 
GREEN 
```kotlin
@JvmField
```val  GREEN :  Color4 
Default green data. 
RED 
```kotlin
@JvmField
```val  RED :  Color4 
Default red data. 
TRANSPARENT 
```kotlin
@JvmField
```val  TRANSPARENT :  Color4 
Default transparent data. 
WHITE 
```kotlin
@JvmField
```val  WHITE :  Color4 
Default white data. 
## Functions
from HSV 
```kotlin
@JvmStatic
```fun  fromHSV ( hsv :  Vector3 ,  alpha :  Float  =  1.0f ) :  Color4 
Converts a color from HSV (Hue, Saturation, Value) color space to  Color4  with an optional alpha value. 
from Linear Color 
```kotlin
@JvmStatic
```fun  fromLinearColor ( linearColor :  Vector4 ) :  Color4 
Creates a  Color4  from a linear-light RGBA color. 
from Linear Hex 
```kotlin
@JvmStatic
```fun  fromLinearHex ( hex :  String ) :  Color4 
Converts a color from a linear hexadecimal representation to  Color4 . 
from SRGBHex 
```kotlin
@JvmStatic
```fun  fromSRGBHex ( hex :  String ) :  Color4 
Converts a color from an sRGB hexadecimal representation to Color4.