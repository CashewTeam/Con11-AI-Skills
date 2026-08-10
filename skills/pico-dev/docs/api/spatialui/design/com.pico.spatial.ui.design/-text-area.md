# TextArea | PICO Spatial SDK

ui:design / com.pico.spatial.ui.design / TextArea 
# TextArea
```kotlin
@Composable
```fun  TextArea ( value :  String ,  onValueChange :  ( String )  ->  Unit ,  modifier :  Modifier  =  Modifier ,  placeholder :  @ Composable ( )  ->  Unit ?  =  null ,  supportingText :  @ Composable ( )  ->  Unit ?  =  null ,  enabled :  Boolean  =  true ,  readOnly :  Boolean  =  false ,  textStyle :  TextStyle  =  TextFieldDefaults.DefaultTextStyle ,  isError :  Boolean  =  false ,  visualTransformation :  VisualTransformation  =  VisualTransformation.None ,  keyboardOptions :  KeyboardOptions  =  KeyboardOptions.Default ,  keyboardActions :  KeyboardActions  =  KeyboardActions.Default ,  maxLines :  Int  =  Int.MAX_VALUE ,  minLines :  Int  =  1 ,  showScrollIndicator :  Boolean  =  false ,  interactionSource :  MutableInteractionSource  =  remember { MutableInteractionSource() } ,  cornerRadius :  Dp  =  TextFieldDefaults.CornerRadius ,  colors :  TextFieldColors  =  TextFieldDefaults.textFieldColors() ) 
Multi-line text input 
If apart from input text change you also want to observe the cursor location, selection range, or IME composition, use  TextFieldValue . 
#### Parameters
value 
The input text to be shown in the text field. 
on Value Change 
The callback that is triggered when the input service updates the text. An updated text comes as a parameter of the callback. 
modifier 
A  Modifier  for this text field. 
placeholder 
The optional placeholder to be displayed when the input text is empty. 
supporting Text 
The optional supporting text to be displayed below the text field container. 
enabled 
controls the enabled state of this text field. When  false , this component does not respond to user input, and it appears visually disabled to accessibility services. 
read Only 
controls the editable state of the text field. When  true , the text field cannot be modified. However, a user can focus it and copy text from it. Read-only text fields are usually used to display pre-filled forms that a user cannot edit. 
text Style 
The style to be applied to the input text. The default  textStyle  uses the  LocalTextStyle  defined by the theme. 
is Error 
A boolean that controls the error state of the  TextField . When  true , the text field is highlighted with the error color. 
visual Transformation 
A  VisualTransformation  that is applied to the input text. The default  visualTransformation  is  VisualTransformation.None . 
keyboard Options 
A  KeyboardOptions  that is applied to the input text. The default  keyboardOptions  is  KeyboardOptions.Default . 
keyboard Actions 
A  KeyboardActions  that is applied to the input text. The default  keyboardActions  is  KeyboardActions.Default . 
max Lines 
The maximum number of lines to be displayed in the text field. The default  maxLines  is  Int.MAX_VALUE . 
min Lines 
The minimum number of lines to be displayed in the text field. The default  minLines  is 1. 
show Scroll Indicator 
A boolean that controls whether to show the scroll indicator. The default  showScrollIndicator  is false. 
interaction Source 
The  MutableInteractionSource  representing the stream of  Interaction s for this TextField. You can create and pass in your own remembered  MutableInteractionSource  if you want to observe  Interaction s and customize the appearance / behavior of this TextField in different  Interaction s. 
corner Radius 
The corner radius of the text field. 
colors 
TextFieldColors  that will be used to resolve the color of the text, content (including label, placeholder, leading and trailing icons, indicator line) and background for this text field in different states. See  TextFieldDefaults.textFieldColors . 
#### Samples
```
import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.layout.width
import androidx.compose.foundation.text.KeyboardOptions
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.saveable.rememberSaveable
import androidx.compose.runtime.setValue
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.res.painterResource
import androidx.compose.ui.text.TextRange
import androidx.compose.ui.text.input.KeyboardType
import androidx.compose.ui.text.input.PasswordVisualTransformation
import androidx.compose.ui.text.input.TextFieldValue
import androidx.compose.ui.text.input.VisualTransformation
import androidx.compose.ui.tooling.preview.Preview
import androidx.compose.ui.unit.dp
import com.pico.spatial.ui.design.Icon
import com.pico.spatial.ui.design.IconButton
import com.pico.spatial.ui.design.IconButtonDefaults
import com.pico.spatial.ui.design.Text
import com.pico.spatial.ui.design.TextArea
import com.pico.spatial.ui.design.TextField
import com.pico.spatial.ui.design.menu.Menu
import com.pico.spatial.ui.design.menu.MenuItem

fun main() { 
   //sampleStart 
   var text by remember { mutableStateOf("") }
TextArea(
    value = text,
    onValueChange = { newValue -> text = newValue },
    placeholder = { Text(text = "hint text") },
    modifier = Modifier.size(width = 200.dp, height = 200.dp),
    maxLines = 2,
) 
   //sampleEnd
}
```
```kotlin
@Composable
```fun  TextArea ( value :  TextFieldValue ,  onValueChange :  ( TextFieldValue )  ->  Unit ,  modifier :  Modifier  =  Modifier ,  placeholder :  @ Composable ( )  ->  Unit ?  =  null ,  supportingText :  @ Composable ( )  ->  Unit ?  =  null ,  enabled :  Boolean  =  true ,  readOnly :  Boolean  =  false ,  textStyle :  TextStyle  =  TextFieldDefaults.DefaultTextStyle ,  isError :  Boolean  =  false ,  visualTransformation :  VisualTransformation  =  VisualTransformation.None ,  keyboardOptions :  KeyboardOptions  =  KeyboardOptions.Default ,  keyboardActions :  KeyboardActions  =  KeyboardActions.Default ,  maxLines :  Int  =  Int.MAX_VALUE ,  minLines :  Int  =  1 ,  showScrollIndicator :  Boolean  =  false ,  interactionSource :  MutableInteractionSource  =  remember { MutableInteractionSource() } ,  cornerRadius :  Dp  =  TextFieldDefaults.CornerRadius ,  colors :  TextFieldColors  =  TextFieldDefaults.textFieldColors() ) 
Multi line text input 
#### Parameters
value 
The input  TextFieldValue  to be shown in the text field. 
on Value Change 
The callback that is triggered when the input service updates the text. An updated text comes as a parameter of the callback. 
modifier 
A  Modifier  for this text field. 
placeholder 
The optional placeholder to be displayed when the input text is empty. 
supporting Text 
The optional supporting text to be displayed below the text field container. 
enabled 
controls the enabled state of this text field. When  false , this component does not respond to user input, and it appears visually disabled to accessibility services. 
read Only 
controls the editable state of the text field. When  true , the text field cannot be modified. However, a user can focus it and copy text from it. Read-only text fields are usually used to display pre-filled forms that a user cannot edit. 
text Style 
The style to be applied to the input text. The default  textStyle  uses the  LocalTextStyle  defined by the theme. 
is Error 
A boolean that controls the error state of the  TextField . When  true , the text field is highlighted with the error color. 
visual Transformation 
A  VisualTransformation  that is applied to the input text. The default  visualTransformation  is  VisualTransformation.None . 
keyboard Options 
A  KeyboardOptions  that is applied to the input text. The default  keyboardOptions  is  KeyboardOptions.Default . 
keyboard Actions 
A  KeyboardActions  that is applied to the input text. The default  keyboardActions  is  KeyboardActions.Default . 
max Lines 
The maximum number of lines to be displayed in the text field. The default  maxLines  is  Int.MAX_VALUE . 
min Lines 
The minimum number of lines to be displayed in the text field. The default  minLines  is 1. 
show Scroll Indicator 
A boolean that controls whether to show the scroll indicator. The default  showScrollIndicator  is false. 
interaction Source 
The  MutableInteractionSource  representing the stream of  Interaction s for this TextField. You can create and pass in your own remembered  MutableInteractionSource  if you want to observe  Interaction s and customize the appearance / behavior of this TextField in different  Interaction s. 
corner Radius 
The corner radius of the text field. 
colors 
TextFieldColors  that will be used to resolve the color of the text, content (including label, placeholder, leading and trailing icons, indicator line) and background for this text field in different states. See  TextFieldDefaults.textFieldColors . 
#### Samples
```
import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.layout.width
import androidx.compose.foundation.text.KeyboardOptions
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.saveable.rememberSaveable
import androidx.compose.runtime.setValue
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.res.painterResource
import androidx.compose.ui.text.TextRange
import androidx.compose.ui.text.input.KeyboardType
import androidx.compose.ui.text.input.PasswordVisualTransformation
import androidx.compose.ui.text.input.TextFieldValue
import androidx.compose.ui.text.input.VisualTransformation
import androidx.compose.ui.tooling.preview.Preview
import androidx.compose.ui.unit.dp
import com.pico.spatial.ui.design.Icon
import com.pico.spatial.ui.design.IconButton
import com.pico.spatial.ui.design.IconButtonDefaults
import com.pico.spatial.ui.design.Text
import com.pico.spatial.ui.design.TextArea
import com.pico.spatial.ui.design.TextField
import com.pico.spatial.ui.design.menu.Menu
import com.pico.spatial.ui.design.menu.MenuItem

fun main() { 
   //sampleStart 
   var text by remember { mutableStateOf("") }
TextArea(
    value = text,
    onValueChange = { newValue -> text = newValue },
    placeholder = { Text(text = "hint text") },
    modifier = Modifier.size(width = 200.dp, height = 200.dp),
    maxLines = 2,
) 
   //sampleEnd
}
```