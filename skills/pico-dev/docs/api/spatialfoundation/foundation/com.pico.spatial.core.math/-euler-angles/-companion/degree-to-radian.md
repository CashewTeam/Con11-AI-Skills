# degreeToRadian | PICO Spatial SDK

foundation / com.pico.spatial.core.math / EulerAngles / Companion / degreeToRadian 
# degreeToRadian
```kotlin
@JvmStatic
```fun  degreeToRadian ( degree :  Float ) :  Float 
Converts an angle from degrees to radians using a pre-calculated conversion factor. 
The input  degree  value must be a finite floating-point number. The conversion factor  DEG_TO_RAD_FACTOR is  (PI / 180.0) cast to a  Float`. 
#### Return
The angle converted to radians, as a  Float . 
#### Parameters
degree 
The angle in degrees. 
#### Throws
Illegal Argument Exception 
if  degree  is not a finite number (that is, NaN or Infinity).