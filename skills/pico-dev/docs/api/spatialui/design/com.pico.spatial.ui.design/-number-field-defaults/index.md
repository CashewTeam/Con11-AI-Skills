# NumberFieldDefaults | PICO Spatial SDK

ui:design / com.pico.spatial.ui.design / NumberFieldDefaults 
# NumberFieldDefaults
```kotlin
object NumberFieldDefaults
```
Object that containing default values for  NumberField . 
Members 
## Functions
default Decrease Icon 
```kotlin
fun defaultDecreaseIcon(): @Composable () -> Unit
```default Increase Icon 
```kotlin
fun defaultIncreaseIcon(): @Composable () -> Unit
```default Size 
```kotlin
fun defaultSize(): NumberFieldSize
```number Field Colors 
```kotlin
@Composable
```fun  numberFieldColors ( ) :  NumberFieldColors 
```kotlin
@Composable
```fun  numberFieldColors ( contentColor :  Color  =  Color.Unspecified ,  backgroundColor :  Color  =  Color.Unspecified ,  focusedColor :  Color  =  Color.Unspecified ,  errorColor :  Color  =  Color.Unspecified ) :  NumberFieldColors 
The custom colors for  NumberField . 
size 
```kotlin
fun size(height: Dp): NumberFieldSize
```small Size 
```kotlin
fun smallSize(): NumberFieldSize
```