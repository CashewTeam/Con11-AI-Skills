# PhysicalLengthConverter | PICO Spatial SDK

ui:platform / com.pico.spatial.ui.platform / PhysicalLengthConverter 
# PhysicalLengthConverter
```kotlin
interface PhysicalLengthConverter : Density
```
Interface for converting length between physical lengthUnit and Dp 
Members 
## Functions
dp To Length 
```kotlin
abstract fun dpToLength(dp: Dp, lengthUnit: LengthUnit): Float
```
Converts an  Int  Dp value to  LengthUnit . 
length To Dp 
```kotlin
abstract fun lengthToDp(length: Float, lengthUnit: LengthUnit): Dp
```
Converts a  Float  LengthUnit value to  Dp .