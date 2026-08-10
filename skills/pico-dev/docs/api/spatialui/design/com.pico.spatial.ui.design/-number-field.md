# NumberField | PICO Spatial SDK

ui:design / com.pico.spatial.ui.design / NumberField 
# NumberField
```kotlin
@Composable
```fun  NumberField ( value :  Int ,  onValueChange :  ( Int )  ->  Unit ,  modifier :  Modifier  =  Modifier ,  increaseIcon :  @ Composable ( )  ->  Unit  =  NumberFieldDefaults.defaultIncreaseIcon() ,  decreaseIcon :  @ Composable ( )  ->  Unit  =  NumberFieldDefaults.defaultDecreaseIcon() ,  stepLength :  Int  =  1 ,  valueRange :  IntRange  =  NumberFieldDefaults.DefaultRange ,  colors :  NumberFieldColors  =  NumberFieldDefaults.numberFieldColors() ,  size :  NumberFieldSize  =  NumberFieldDefaults.defaultSize() ,  cornerSize :  Dp  =  size.height.cornerSize() ,  gap :  Dp  =  NumberFieldDefaults.DefaultGap ,  enabled :  Boolean  =  true ,  editable :  Boolean  =  true ,  textStyle :  TextStyle  =  NumberFieldDefaults.defaultTextStyle(size.height) ,  keyboardOptions :  KeyboardOptions  =  NumberFieldDefaults.DefaultKeyboardOptions ,  unit :  String ?  =  null ,  spacerWidth :  Dp  =  NumberFieldDefaults.DefaultSpacerWidth ) 
NumberField  is used to create a number input field with increase and decrease buttons. 
#### Parameters
value 
The current value of the number field. 
on Value Change 
The callback that is triggered when the value changes. 
modifier 
The  Modifier  to be applied to the number field. 
increase Icon 
The icon to be displayed for the increase button. 
decrease Icon 
The icon to be displayed for the decrease button. 
step Length 
The step length for increasing or decreasing the value. 
value Range 
The range of valid values for the number field. 
colors 
The colors for the number field. 
size 
The size of the number field. 
corner Size 
The corner size of the number field. 
gap 
The gap between the text and buttons 
enabled 
Whether the number field is enabled. 
editable 
Whether the number field is editable. 
text Style 
The text style for the number field. 
keyboard Options 
The keyboard options for the number field. 
unit 
The unit text to be displayed after the number. 
spacer Width 
The width of the spacer between the number and the unit. 
#### Samples
```
import androidx.compose.foundation.layout.width
import androidx.compose.foundation.text.KeyboardOptions
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableDoubleStateOf
import androidx.compose.runtime.mutableFloatStateOf
import androidx.compose.runtime.mutableIntStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Modifier
import androidx.compose.ui.text.input.ImeAction
import androidx.compose.ui.text.input.KeyboardType
import androidx.compose.ui.unit.dp
import com.pico.spatial.ui.design.NumberField
import com.pico.spatial.ui.design.NumberFieldDefaults

fun main() { 
   //sampleStart 
   var value by remember { mutableIntStateOf(0) }
NumberField(value = value, onValueChange = { value = it }) 
   //sampleEnd
}
```
```
import androidx.compose.foundation.layout.width
import androidx.compose.foundation.text.KeyboardOptions
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableDoubleStateOf
import androidx.compose.runtime.mutableFloatStateOf
import androidx.compose.runtime.mutableIntStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Modifier
import androidx.compose.ui.text.input.ImeAction
import androidx.compose.ui.text.input.KeyboardType
import androidx.compose.ui.unit.dp
import com.pico.spatial.ui.design.NumberField
import com.pico.spatial.ui.design.NumberFieldDefaults

fun main() { 
   //sampleStart 
   var value by remember { mutableIntStateOf(0) }
NumberField(
    value = value,
    onValueChange = { value = it },
    size = NumberFieldDefaults.smallSize(),
) 
   //sampleEnd
}
```
```
import androidx.compose.foundation.layout.width
import androidx.compose.foundation.text.KeyboardOptions
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableDoubleStateOf
import androidx.compose.runtime.mutableFloatStateOf
import androidx.compose.runtime.mutableIntStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Modifier
import androidx.compose.ui.text.input.ImeAction
import androidx.compose.ui.text.input.KeyboardType
import androidx.compose.ui.unit.dp
import com.pico.spatial.ui.design.NumberField
import com.pico.spatial.ui.design.NumberFieldDefaults

fun main() { 
   //sampleStart 
   var value by remember { mutableIntStateOf(0) }
NumberField(value = value, onValueChange = { value = it }, valueRange = -100..100) 
   //sampleEnd
}
```
```
import androidx.compose.foundation.layout.width
import androidx.compose.foundation.text.KeyboardOptions
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableDoubleStateOf
import androidx.compose.runtime.mutableFloatStateOf
import androidx.compose.runtime.mutableIntStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Modifier
import androidx.compose.ui.text.input.ImeAction
import androidx.compose.ui.text.input.KeyboardType
import androidx.compose.ui.unit.dp
import com.pico.spatial.ui.design.NumberField
import com.pico.spatial.ui.design.NumberFieldDefaults

fun main() { 
   //sampleStart 
   var value by remember { mutableIntStateOf(0) }
NumberField(value = value, onValueChange = { value = it }, stepLength = 2) 
   //sampleEnd
}
```
```
import androidx.compose.foundation.layout.width
import androidx.compose.foundation.text.KeyboardOptions
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableDoubleStateOf
import androidx.compose.runtime.mutableFloatStateOf
import androidx.compose.runtime.mutableIntStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Modifier
import androidx.compose.ui.text.input.ImeAction
import androidx.compose.ui.text.input.KeyboardType
import androidx.compose.ui.unit.dp
import com.pico.spatial.ui.design.NumberField
import com.pico.spatial.ui.design.NumberFieldDefaults

fun main() { 
   //sampleStart 
   var value by remember { mutableIntStateOf(0) }
NumberField(value = value, onValueChange = { value = it }, editable = false) 
   //sampleEnd
}
```
```
import androidx.compose.foundation.layout.width
import androidx.compose.foundation.text.KeyboardOptions
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableDoubleStateOf
import androidx.compose.runtime.mutableFloatStateOf
import androidx.compose.runtime.mutableIntStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Modifier
import androidx.compose.ui.text.input.ImeAction
import androidx.compose.ui.text.input.KeyboardType
import androidx.compose.ui.unit.dp
import com.pico.spatial.ui.design.NumberField
import com.pico.spatial.ui.design.NumberFieldDefaults

fun main() { 
   //sampleStart 
   var value by remember { mutableIntStateOf(0) }
NumberField(value = value, onValueChange = { value = it }, enabled = false) 
   //sampleEnd
}
```
```
import androidx.compose.foundation.layout.width
import androidx.compose.foundation.text.KeyboardOptions
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableDoubleStateOf
import androidx.compose.runtime.mutableFloatStateOf
import androidx.compose.runtime.mutableIntStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Modifier
import androidx.compose.ui.text.input.ImeAction
import androidx.compose.ui.text.input.KeyboardType
import androidx.compose.ui.unit.dp
import com.pico.spatial.ui.design.NumberField
import com.pico.spatial.ui.design.NumberFieldDefaults

fun main() { 
   //sampleStart 
   var value by remember { mutableIntStateOf(0) }
NumberField(value = value, onValueChange = { value = it }, unit = "kg") 
   //sampleEnd
}
```
```
import androidx.compose.foundation.layout.width
import androidx.compose.foundation.text.KeyboardOptions
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableDoubleStateOf
import androidx.compose.runtime.mutableFloatStateOf
import androidx.compose.runtime.mutableIntStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Modifier
import androidx.compose.ui.text.input.ImeAction
import androidx.compose.ui.text.input.KeyboardType
import androidx.compose.ui.unit.dp
import com.pico.spatial.ui.design.NumberField
import com.pico.spatial.ui.design.NumberFieldDefaults

fun main() { 
   //sampleStart 
   var value by remember { mutableIntStateOf(0) }
NumberField(value = value, onValueChange = { value = it }, unit = "kkkkkkkkkkkg") 
   //sampleEnd
}
```
```
import androidx.compose.foundation.layout.width
import androidx.compose.foundation.text.KeyboardOptions
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableDoubleStateOf
import androidx.compose.runtime.mutableFloatStateOf
import androidx.compose.runtime.mutableIntStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Modifier
import androidx.compose.ui.text.input.ImeAction
import androidx.compose.ui.text.input.KeyboardType
import androidx.compose.ui.unit.dp
import com.pico.spatial.ui.design.NumberField
import com.pico.spatial.ui.design.NumberFieldDefaults

fun main() { 
   //sampleStart 
   var value by remember { mutableIntStateOf(0) }
NumberField(value = value, onValueChange = { value = it }, unit = "kg", spacerWidth = 20.dp) 
   //sampleEnd
}
```
```kotlin
@Composable
```fun  NumberField ( value :  Double ,  onValueChange :  ( Double )  ->  Unit ,  modifier :  Modifier  =  Modifier ,  increaseIcon :  @ Composable ( )  ->  Unit  =  NumberFieldDefaults.defaultIncreaseIcon() ,  decreaseIcon :  @ Composable ( )  ->  Unit  =  NumberFieldDefaults.defaultDecreaseIcon() ,  stepLength :  Double  =  1.0 ,  valueRange :  ClosedFloatingPointRange < Double >  =  NumberFieldDefaults.DefaultDoubleRange ,  colors :  NumberFieldColors  =  NumberFieldDefaults.numberFieldColors() ,  size :  NumberFieldSize  =  NumberFieldDefaults.defaultSize() ,  cornerSize :  Dp  =  size.height.cornerSize() ,  gap :  Dp  =  NumberFieldDefaults.DefaultGap ,  enabled :  Boolean  =  true ,  editable :  Boolean  =  true ,  textStyle :  TextStyle  =  NumberFieldDefaults.defaultTextStyle(size.height) ,  keyboardOptions :  KeyboardOptions  =  NumberFieldDefaults.DefaultKeyboardOptions ,  unit :  String ?  =  null ,  spacerWidth :  Dp  =  NumberFieldDefaults.DefaultSpacerWidth ,  fractionDigits :  Int  =  1 ) 
NumberField  is used to create a number input field with increase and decrease buttons. 
#### Parameters
value 
The current value of the number field. 
on Value Change 
The callback that is triggered when the value changes. 
modifier 
The  Modifier  to be applied to the number field. 
increase Icon 
The icon to be displayed for the increase button. 
decrease Icon 
The icon to be displayed for the decrease button. 
step Length 
The step length for increasing or decreasing the value. 
value Range 
The range of valid values for the number field. 
colors 
The colors for the number field. 
size 
The size of the number field. 
corner Size 
The corner size of the number field. 
gap 
The gap between the text and buttons 
enabled 
Whether the number field is enabled. 
editable 
Whether the number field is editable. 
text Style 
The text style for the number field. 
keyboard Options 
The keyboard options for the number field. 
unit 
The unit text to be displayed after the number. 
spacer Width 
The width of the spacer between the number and the unit. 
fraction Digits 
The number of digits to display after the decimal point. 
#### Samples
```
import androidx.compose.foundation.layout.width
import androidx.compose.foundation.text.KeyboardOptions
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableDoubleStateOf
import androidx.compose.runtime.mutableFloatStateOf
import androidx.compose.runtime.mutableIntStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Modifier
import androidx.compose.ui.text.input.ImeAction
import androidx.compose.ui.text.input.KeyboardType
import androidx.compose.ui.unit.dp
import com.pico.spatial.ui.design.NumberField
import com.pico.spatial.ui.design.NumberFieldDefaults

fun main() { 
   //sampleStart 
   var value by remember { mutableDoubleStateOf(0.0) }
NumberField(value = value, onValueChange = { value = it }) 
   //sampleEnd
}
```
```
import androidx.compose.foundation.layout.width
import androidx.compose.foundation.text.KeyboardOptions
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableDoubleStateOf
import androidx.compose.runtime.mutableFloatStateOf
import androidx.compose.runtime.mutableIntStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Modifier
import androidx.compose.ui.text.input.ImeAction
import androidx.compose.ui.text.input.KeyboardType
import androidx.compose.ui.unit.dp
import com.pico.spatial.ui.design.NumberField
import com.pico.spatial.ui.design.NumberFieldDefaults

fun main() { 
   //sampleStart 
   var value by remember { mutableDoubleStateOf(0.0) }
NumberField(value = value, onValueChange = { value = it }, fractionDigits = 2) 
   //sampleEnd
}
```
```
import androidx.compose.foundation.layout.width
import androidx.compose.foundation.text.KeyboardOptions
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableDoubleStateOf
import androidx.compose.runtime.mutableFloatStateOf
import androidx.compose.runtime.mutableIntStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Modifier
import androidx.compose.ui.text.input.ImeAction
import androidx.compose.ui.text.input.KeyboardType
import androidx.compose.ui.unit.dp
import com.pico.spatial.ui.design.NumberField
import com.pico.spatial.ui.design.NumberFieldDefaults

fun main() { 
   //sampleStart 
   var value by remember { mutableDoubleStateOf(0.0) }
NumberField(value = value, onValueChange = { value = it }, valueRange = -10.2..33.0) 
   //sampleEnd
}
```
```
import androidx.compose.foundation.layout.width
import androidx.compose.foundation.text.KeyboardOptions
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableDoubleStateOf
import androidx.compose.runtime.mutableFloatStateOf
import androidx.compose.runtime.mutableIntStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Modifier
import androidx.compose.ui.text.input.ImeAction
import androidx.compose.ui.text.input.KeyboardType
import androidx.compose.ui.unit.dp
import com.pico.spatial.ui.design.NumberField
import com.pico.spatial.ui.design.NumberFieldDefaults

fun main() { 
   //sampleStart 
   var value by remember { mutableDoubleStateOf(0.0) }
NumberField(value = value, onValueChange = { value = it }, stepLength = 3.3) 
   //sampleEnd
}
```
```
import androidx.compose.foundation.layout.width
import androidx.compose.foundation.text.KeyboardOptions
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableDoubleStateOf
import androidx.compose.runtime.mutableFloatStateOf
import androidx.compose.runtime.mutableIntStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Modifier
import androidx.compose.ui.text.input.ImeAction
import androidx.compose.ui.text.input.KeyboardType
import androidx.compose.ui.unit.dp
import com.pico.spatial.ui.design.NumberField
import com.pico.spatial.ui.design.NumberFieldDefaults

fun main() { 
   //sampleStart 
   var value by remember { mutableDoubleStateOf(0.0) }
NumberField(value = value, onValueChange = { value = it }, unit = "s") 
   //sampleEnd
}
```
```
import androidx.compose.foundation.layout.width
import androidx.compose.foundation.text.KeyboardOptions
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableDoubleStateOf
import androidx.compose.runtime.mutableFloatStateOf
import androidx.compose.runtime.mutableIntStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Modifier
import androidx.compose.ui.text.input.ImeAction
import androidx.compose.ui.text.input.KeyboardType
import androidx.compose.ui.unit.dp
import com.pico.spatial.ui.design.NumberField
import com.pico.spatial.ui.design.NumberFieldDefaults

fun main() { 
   //sampleStart 
   var value by remember { mutableDoubleStateOf(0.0) }
NumberField(value = value, onValueChange = { value = it }, unit = "dp") 
   //sampleEnd
}
```
```
import androidx.compose.foundation.layout.width
import androidx.compose.foundation.text.KeyboardOptions
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableDoubleStateOf
import androidx.compose.runtime.mutableFloatStateOf
import androidx.compose.runtime.mutableIntStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Modifier
import androidx.compose.ui.text.input.ImeAction
import androidx.compose.ui.text.input.KeyboardType
import androidx.compose.ui.unit.dp
import com.pico.spatial.ui.design.NumberField
import com.pico.spatial.ui.design.NumberFieldDefaults

fun main() { 
   //sampleStart 
   var value by remember { mutableDoubleStateOf(0.0) }
NumberField(
    value = value,
    onValueChange = { value = it },
    unit = "meter",
    keyboardOptions =
        KeyboardOptions(keyboardType = KeyboardType.Ascii, imeAction = ImeAction.Done),
) 
   //sampleEnd
}
```
```kotlin
@Composable
```fun  NumberField ( value :  Float ,  onValueChange :  ( Float )  ->  Unit ,  modifier :  Modifier  =  Modifier ,  increaseIcon :  @ Composable ( )  ->  Unit  =  NumberFieldDefaults.defaultIncreaseIcon() ,  decreaseIcon :  @ Composable ( )  ->  Unit  =  NumberFieldDefaults.defaultDecreaseIcon() ,  stepLength :  Float  =  1.0f ,  valueRange :  ClosedFloatingPointRange < Float >  =  NumberFieldDefaults.DefaultFloatRange ,  colors :  NumberFieldColors  =  NumberFieldDefaults.numberFieldColors() ,  size :  NumberFieldSize  =  NumberFieldDefaults.defaultSize() ,  cornerSize :  Dp  =  size.height.cornerSize() ,  gap :  Dp  =  NumberFieldDefaults.DefaultGap ,  enabled :  Boolean  =  true ,  editable :  Boolean  =  true ,  textStyle :  TextStyle  =  NumberFieldDefaults.defaultTextStyle(size.height) ,  keyboardOptions :  KeyboardOptions  =  NumberFieldDefaults.DefaultKeyboardOptions ,  unit :  String ?  =  null ,  spacerWidth :  Dp  =  NumberFieldDefaults.DefaultSpacerWidth ,  fractionDigits :  Int  =  1 ) 
NumberField  is used to create a number input field with increase and decrease buttons. 
#### Parameters
value 
The current value of the number field. 
on Value Change 
The callback that is triggered when the value changes. 
modifier 
The  Modifier  to be applied to the number field. 
increase Icon 
The icon to be displayed for the increase button. 
decrease Icon 
The icon to be displayed for the decrease button. 
step Length 
The step length for increasing or decreasing the value. 
value Range 
The range of valid values for the number field. 
colors 
The colors for the number field. 
size 
The size of the number field. 
corner Size 
The corner size of the number field. 
gap 
The gap between the text and buttons 
enabled 
Whether the number field is enabled. 
editable 
Whether the number field is editable. 
text Style 
The text style for the number field. 
keyboard Options 
The keyboard options for the number field. 
unit 
The unit text to be displayed after the number. 
spacer Width 
The width of the spacer between the number and the unit. 
fraction Digits 
The number of digits to display after the decimal point. 
#### Samples
```
import androidx.compose.foundation.layout.width
import androidx.compose.foundation.text.KeyboardOptions
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableDoubleStateOf
import androidx.compose.runtime.mutableFloatStateOf
import androidx.compose.runtime.mutableIntStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Modifier
import androidx.compose.ui.text.input.ImeAction
import androidx.compose.ui.text.input.KeyboardType
import androidx.compose.ui.unit.dp
import com.pico.spatial.ui.design.NumberField
import com.pico.spatial.ui.design.NumberFieldDefaults

fun main() { 
   //sampleStart 
   var value by remember { mutableFloatStateOf(0.0f) }
NumberField(
    value = value,
    onValueChange = { value = it },
    unit = "meter",
    keyboardOptions =
        KeyboardOptions(keyboardType = KeyboardType.Ascii, imeAction = ImeAction.Next),
) 
   //sampleEnd
}
```