# TextField | PICO Spatial SDK

ui:design / com.pico.spatial.ui.design / TextField 
# TextField
```kotlin
@Composable
```fun  TextField ( value :  String ,  onValueChange :  ( String )  ->  Unit ,  modifier :  Modifier  =  Modifier ,  placeholder :  @ Composable ( )  ->  Unit ?  =  null ,  leadingContent :  @ Composable ( )  ->  Unit ?  =  null ,  trailingContent :  @ Composable ( )  ->  Unit ?  =  null ,  supportingText :  @ Composable ( )  ->  Unit ?  =  null ,  enabled :  Boolean  =  true ,  readOnly :  Boolean  =  false ,  textStyle :  TextStyle  =  TextFieldDefaults.DefaultTextStyle ,  isError :  Boolean  =  false ,  visualTransformation :  VisualTransformation  =  VisualTransformation.None ,  keyboardOptions :  KeyboardOptions  =  KeyboardOptions.Default ,  keyboardActions :  KeyboardActions  =  KeyboardActions.Default ,  singleLine :  Boolean  =  true ,  maxLines :  Int  =  if (singleLine) 1 else Int.MAX_VALUE ,  minLines :  Int  =  1 ,  showScrollIndicator :  Boolean  =  false ,  interactionSource :  MutableInteractionSource  =  remember { MutableInteractionSource() } ,  cornerRadius :  Dp  =  TextFieldDefaults.CornerRadius ,  colors :  TextFieldColors  =  TextFieldDefaults.textFieldColors() ,  clearable :  Boolean  =  true ) 
Text fields allow users to enter text into a UI. 
If you only need to observe plain text changes, prefer the overload that takes a  String . Use this overload when you also need to track cursor position, selection range, or IME composition via  TextFieldValue . 
#### Parameters
value 
The input text to be shown in the text field. 
on Value Change 
The callback that is triggered when the input service updates the text. An updated text comes as a parameter of the callback. 
modifier 
A  Modifier  for this text field. 
placeholder 
The optional placeholder to be displayed when the input text is empty. 
leading Content 
The optional leading icon to be displayed at the beginning of the text field container 
trailing Content 
The optional trailing icon to be displayed at the end of the text field container 
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
single Line 
A boolean that controls whether the text field is single line or multi line. When  true , the text field will be single line. When  false , the text field will be multi line. 
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
TextFieldColors  that will be used to resolve color of the text, content (including label, placeholder, leading and trailing icons, indicator line) and background for this text field in different states. See  TextFieldDefaults.textFieldColors 
clearable 
controls whether to display a clear button when text is present and the field is focused. This only applies if  trailingContent  is null. 
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
TextField(
    value = text,
    onValueChange = { newValue -> text = newValue },
    modifier = Modifier.width(350.dp),
    placeholder = { Text(text = "fix width 350dp") },
    singleLine = true,
) 
   //sampleEnd
}
```
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
TextField(
    value = text,
    onValueChange = { newValue -> text = newValue },
    modifier = Modifier.width(200.dp),
    placeholder = { Text(text = "fix width 200dp") },
) 
   //sampleEnd
}
```
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
var error by remember { mutableStateOf(false) }
TextField(
    value = text,
    onValueChange = { newValue ->
        text = newValue
        error = text.contains("9")
    },
    placeholder = { Text(text = "press 9 to show error") },
    leadingContent = {
        Icon(
            painter = painterResource(id = R.drawable.ic_sample_search),
            contentDescription = null,
            modifier =
                Modifier.clickable {
                    // do something
                },
        )
    },
    trailingContent = {
        Icon(
            painter =
                painterResource(
                    id = com.pico.spatial.ui.design.R.drawable.ic_sui_dropdown_trigger_down
                ),
            contentDescription = null,
            tint = Color(color = 0x59FFFFFF),
            modifier =
                Modifier.clickable {
                    // do something
                },
        )
    },
    isError = error,
    supportingText = {
        Text(text = "supporting text supporting text supporting text supporting text")
    },
) 
   //sampleEnd
}
```
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
var showPassword by rememberSaveable { mutableStateOf(false) }
var isError by remember { mutableStateOf(false) }
TextField(
    value = text,
    onValueChange = { newValue ->
        text = newValue
        isError = newValue.length > 6
    },
    placeholder = { Text(text = "Input password") },
    trailingContent = {
        IconButton(
            onClick = { showPassword = !showPassword },
            colors = IconButtonDefaults.iconButtonColors(containerColor = Color.Transparent),
        ) {
            if (showPassword) {
                Icon(
                    painterResource(R.drawable.ic_sample_visible),
                    null,
                    tint = Color.Unspecified,
                )
            } else {
                Icon(
                    painterResource(R.drawable.ic_sample_visible_off),
                    null,
                    tint = Color.Unspecified,
                )
            }
        }
    },
    isError = isError,
    visualTransformation =
        if (showPassword) {
            VisualTransformation.None
        } else {
            PasswordVisualTransformation(mask = '☻')
        },
    keyboardOptions = KeyboardOptions(keyboardType = KeyboardType.Password),
    supportingText =
        if (isError) {
            { Text(text = "Invalid input!") }
        } else {
            null
        },
) 
   //sampleEnd
}
```
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
var showMenu by remember { mutableStateOf(false) }
Box {
    // text field
    TextField(
        value = text,
        onValueChange = { newValue -> text = newValue },
        placeholder = { Text(text = "click to dropdown") },
        trailingContent = {
            Icon(
                painter =
                    painterResource(
                        id = com.pico.spatial.ui.design.R.drawable.ic_sui_dropdown_trigger_down
                    ),
                contentDescription = null,
                tint = Color(color = 0x59FFFFFF),
                modifier =
                    Modifier.clickable {
                        // show menu
                        showMenu = true
                    },
            )
        },
        singleLine = true,
    )
    // menu
    if (showMenu) {
        Menu(onDismissRequest = { showMenu = false }) {
            repeat(times = 5) {
                val menuText = "option $it"
                MenuItem(
                    title = { Text(menuText) },
                    onClick = {
                        // set text to text field
                        text = menuText
                        // dismiss menu
                        showMenu = false
                    },
                )
            }
        }
    }
} 
   //sampleEnd
}
```
```kotlin
@Composable
```fun  TextField ( value :  TextFieldValue ,  onValueChange :  ( TextFieldValue )  ->  Unit ,  modifier :  Modifier  =  Modifier ,  placeholder :  @ Composable ( )  ->  Unit ?  =  null ,  leadingContent :  @ Composable ( )  ->  Unit ?  =  null ,  trailingContent :  @ Composable ( )  ->  Unit ?  =  null ,  supportingText :  @ Composable ( )  ->  Unit ?  =  null ,  enabled :  Boolean  =  true ,  readOnly :  Boolean  =  false ,  textStyle :  TextStyle  =  TextFieldDefaults.DefaultTextStyle ,  isError :  Boolean  =  false ,  visualTransformation :  VisualTransformation  =  VisualTransformation.None ,  keyboardOptions :  KeyboardOptions  =  KeyboardOptions.Default ,  keyboardActions :  KeyboardActions  =  KeyboardActions.Default ,  singleLine :  Boolean  =  true ,  maxLines :  Int  =  if (singleLine) 1 else Int.MAX_VALUE ,  minLines :  Int  =  1 ,  showScrollIndicator :  Boolean  =  false ,  interactionSource :  MutableInteractionSource  =  remember { MutableInteractionSource() } ,  cornerRadius :  Dp  =  TextFieldDefaults.CornerRadius ,  colors :  TextFieldColors  =  TextFieldDefaults.textFieldColors() ,  clearable :  Boolean  =  true ) 
Text fields allow users to enter text into a UI. 
If apart from input text change you also want to observe the cursor location, selection range, or IME composition use the TextField overload with the  TextFieldValue  parameter instead. 
#### Parameters
value 
The input  TextFieldValue  to be shown in the text field. 
on Value Change 
The callback that is triggered when the input service updates the text. An updated text comes as a parameter of the callback. 
modifier 
A  Modifier  for this text field. 
placeholder 
The optional placeholder to be displayed when the input text is empty. 
leading Content 
The optional leading icon to be displayed at the beginning of the text field container 
trailing Content 
The optional trailing icon to be displayed at the end of the text field container 
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
single Line 
A boolean that controls whether the text field is single line or multi line. When  true , the text field will be single line. When  false , the text field will be multi line. 
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
TextFieldColors  that will be used to resolve color of the text, content (including label, placeholder, leading and trailing icons, indicator line) and background for this text field in different states. See  TextFieldDefaults.textFieldColors 
clearable 
controls whether to display a clear button when text is present and the field is focused. This only applies if  trailingContent  is null. 
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
   var text by remember {
    mutableStateOf(
        TextFieldValue(
            "hello world!",
            selection = TextRange(start = 0, end = 3),
            composition = TextRange(start = 4, end = 6),
        )
    )
}
TextField(
    value = text,
    onValueChange = { newValue -> text = newValue },
    placeholder = { Text(text = "hint text") },
    singleLine = true,
) 
   //sampleEnd
}
```