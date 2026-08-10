# Color4 | PICO Spatial SDK

foundation / com.pico.spatial.core.math / Color4 
# Color4
```kotlin
class Color4
```
Represents a gamma color with red, green, blue, and alpha components. Component values are typically in the range 0, 1, though this is not strictly enforced. 
Members 
## Constructors
Color4 
```kotlin
constructor(red: Float, green: Float, blue: Float, alpha: Float)
```
Constructs a new  Color4  instance with the specified red, green, blue, and alpha components. 
```kotlin
constructor(another: Color4)
```
The constructor to initialize from another  Color4  instance. 
```kotlin
constructor(vector4: Vector4)
```
The constructor to initialize from a  Vector4  instance. 
```kotlin
constructor(vector3: Vector3)
```
The constructor to initialize from a  Vector3  instance, the default alpha value will be use 1f. 
## Types
Companion 
```kotlin
object Companion
```
The companion object of  Color4 . 
## Properties
alpha 
```kotlin
val alpha: Float
```
The alpha component (opacity) of the color. 
blue 
```kotlin
val blue: Float
```
The blue component of the color. 
green 
```kotlin
val green: Float
```
The green component of the color. 
red 
```kotlin
val red: Float
```
The red component of the color. 
## Functions
adjust Brightness 
```kotlin
fun adjustBrightness(factor: Float): Color4
```
Adjusts the brightness of the color by multiplying it with a factor. 
blend With 
```kotlin
fun blendWith(other: Color4, ratio: Float): Color4
```
Blends this color with another color based on a given ratio. 
div 
```kotlin
operator fun div(other: Color4): Color4
```
Divides by another  Color4  instance. 
```kotlin
operator fun div(scalar: Float): Color4
```
Divides by a scalar value. 
equals 
```kotlin
open operator override fun equals(other: Any?): Boolean
```hash Code 
```kotlin
open override fun hashCode(): Int
```minus 
```kotlin
operator fun minus(other: Color4): Color4
```
Subtracts the given  Color4  from this instance and returns the result as a new  Color4 . 
plus 
```kotlin
operator fun plus(other: Color4): Color4
```
Adds the given  Color4  to this instance and returns the result as a new  Color4 . 
times 
```kotlin
operator fun times(other: Color4): Color4
```
Multiplies by another  Color4  instance. 
```kotlin
operator fun times(scalar: Float): Color4
```
Multiplies by a scalar value. 
to Hex 
```kotlin
fun toHex(): String
```
Converts  Color4  to sRGB Hex. 
to HSV 
```kotlin
fun toHSV(): Vector3
```
Converts  Color4  to HSV (Hue, Saturation, Value). 
to Linear Color 
```kotlin
fun toLinearColor(): Vector4
```
Decodes this  Color4  from sRGB/gamma-encoded 0..1 channels into linear RGB. 
to Linear Hex 
```kotlin
fun toLinearHex(): String
```
Converts  Color4  to Linear Hex. 
to SRGBByte 
```kotlin
fun toSRGBByte(): Vector4
```
Converts this  Color4  (sRGB/gamma-encoded channels in the 0..1 range) into 8-bit-per-channel sRGB (RGBA8) values. 
to String 
```kotlin
open override fun toString(): String
```
Returns a string representation of the  Color4  object.