# radianToDegree | PICO Spatial SDK

foundation / com.pico.spatial.core.math / EulerAngles / Companion / radianToDegree 
# radianToDegree
```kotlin
@JvmStatic
```fun  radianToDegree ( radian :  Float ) :  Float 
Converts an angle from radians to degrees using a pre-calculated conversion factor. 
The input  radian  value must be a finite floating-point number. The conversion factor  RAD_TO_DEG_FACTOR  is  (180.0 / PI)  cast to a  Float . 
#### Return
The angle converted to degrees, as a  Float . 
#### Parameters
radian 
The angle in radians. Must be a finite number. 
#### Throws
Illegal Argument Exception 
If radian is not a finite number (that is, NaN or Infinity).