# Stepper | PICO Spatial SDK

ui:design / com.pico.spatial.ui.design / Stepper 
# Stepper
```kotlin
@Composable
```fun  Stepper ( value :  String ,  onStep :  ( step :  Int )  ->  Unit ,  modifier :  Modifier  =  Modifier ,  decreaseIcon :  @ Composable ( )  ->  Unit  =  StepperIconStyle.MinusAndAdd.iconDecrease() ,  increaseIcon :  @ Composable ( )  ->  Unit  =  StepperIconStyle.MinusAndAdd.iconIncrease() ,  stepLength :  Int  =  1 ,  increasable :  Boolean  =  true ,  decreasable :  Boolean  =  true ,  onEdited :  ( newValue :  String )  ->  Unit ?  =  null ,  editable :  Boolean  =  onEdited != null ,  textStyle :  TextStyle  =  PicoTheme.typography.titleMedium.copy(fontWeight = FontWeight.Normal) ,  textColor :  Color  =  PicoTheme.colorScheme.labelPrimary ,  paddingValues :  PaddingValues  =  PaddingValues(defaultPadding) ,  backgroundShape :  Shape  =  RoundedCornerShape(10.dp) ,  backgroundColor :  Color  =  PicoTheme.colorScheme.fillTertiary ,  cursorBrush :  Brush  =  SolidColor(PicoTheme.colorScheme.fillPrimary) ,  keyboardOptions :  KeyboardOptions  =  KeyboardOptions.Default ) 
Basic implement of a stepper. 
#### Parameters
value 
current value 
on Step 
callback when  increaseIcon / decreaseIcon  is triggered 
modifier 
modifier 
decrease Icon 
config icon for decrease, see also  StepperIconStyle 
increase Icon 
config icon for increase, see also  StepperIconStyle 
step Length 
step length for increase or decrease 
increasable 
the enable state of  increaseIcon 
decreasable 
the enable state of  decreaseIcon 
on Edited 
the callback when user has editable input 
editable 
editable if true. 
text Style 
The text style of the stepper. 
text Color 
The text color of the stepper. 
padding Values 
The padding of the stepper. 
background Shape 
The background shape of the stepper. 
background Color 
The background color of the stepper. 
cursor Brush 
The cursor brush color of the stepper. 
keyboard Options 
The keyboard options for the stepper. 
#### Samples
```
import androidx.compose.foundation.layout.Column
import androidx.compose.runtime.Composable
import androidx.compose.runtime.derivedStateOf
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableIntStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.tooling.preview.Preview
import com.pico.spatial.ui.design.Stepper
import com.pico.spatial.ui.design.StepperIconStyle
import com.pico.spatial.ui.design.Text

fun main() { 
   //sampleStart 
   var number by remember { mutableIntStateOf(value = 0) }
Stepper(value = "$number", onStep = { number += it }) 
   //sampleEnd
}
```
```
import androidx.compose.foundation.layout.Column
import androidx.compose.runtime.Composable
import androidx.compose.runtime.derivedStateOf
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableIntStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.tooling.preview.Preview
import com.pico.spatial.ui.design.Stepper
import com.pico.spatial.ui.design.StepperIconStyle
import com.pico.spatial.ui.design.Text

fun main() { 
   //sampleStart 
   Column {
    var month by remember { mutableIntStateOf(1) }
    val increasable by remember { derivedStateOf { month < December } }
    val decreasable by remember { derivedStateOf { month > January } }
    val monthText = "$month Month"
    Text(text = "Current Month is: $monthText ")
    // stepper
    Stepper(
        value = monthText,
        onStep = { stepLength ->
            val newMonth = month + stepLength
            if (newMonth <= December || newMonth >= January) {
                month = newMonth
            }
        },
        increaseIcon = StepperIconStyle.Arrow.iconIncrease(),
        decreaseIcon = StepperIconStyle.Arrow.iconDecrease(),
        increasable = increasable,
        decreasable = decreasable,
    )
} 
   //sampleEnd
}
```