# SearchField | PICO Spatial SDK

ui:design / com.pico.spatial.ui.design / SearchField 
# SearchField
```kotlin
@Composable
```fun  SearchField ( value :  String ,  onValueChange :  ( String )  ->  Unit ,  onSearch :  ( String )  ->  Unit ,  modifier :  Modifier  =  Modifier ,  placeholder :  @ Composable ( )  ->  Unit ?  =  null ,  leadingContent :  @ Composable ( )  ->  Unit  =  SearchFieldDefaults.searchIcon() ,  enabled :  Boolean  =  true ,  textStyle :  TextStyle  =  SearchFieldDefaults.DefaultTextStyle ,  interactionSource :  MutableInteractionSource  =  remember { MutableInteractionSource() } ,  cornerRadius :  Dp  =  100.dp ,  colors :  TextFieldColors  =  SearchFieldDefaults.searchFieldColors() ) 
Search field allows users to input text, and trigger a search action either by pressing the search button on the keyboard or other means. 
#### Parameters
value 
The current text value in the search field. 
on Value Change 
The callback function that is invoked when the text in the search field changes. It takes the new text value as a parameter. 
on Search 
The callback that is triggered when user click search button on software     * keyboard. 
modifier 
A  Modifier  to be applied to the search field. 
placeholder 
An optional composable function to display a placeholder text when the search field is empty. 
leading Content 
A composable function to display content at the beginning of the search field. Defaults to a search icon provided by  SearchFieldDefaults.searchIcon . 
enabled 
A boolean value indicating whether the search field is enabled. If set to false, the search field will be neither editable nor focusable. 
text Style 
The text style to be applied to the input text in the search field. Defaults to the style defined in  SearchFieldDefaults.DefaultTextStyle . 
interaction Source 
A  MutableInteractionSource  representing the stream of  Interaction s for this search field. Defaults to a newly created  MutableInteractionSource . 
corner Radius 
The corner radius of the search field. Defaults to 100.dp. 
colors 
The  TextFieldColors  to be used for the search field. Defaults to the colors defined in  SearchFieldDefaults.searchFieldColors . 
#### Samples
```
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.rememberCoroutineScope
import androidx.compose.runtime.setValue
import androidx.compose.ui.res.painterResource
import androidx.compose.ui.tooling.preview.Preview
import com.pico.spatial.ui.design.Icon
import com.pico.spatial.ui.design.SearchField
import com.pico.spatial.ui.design.Text
import com.pico.spatial.ui.design.windows.LocalSnackbarHostState
import kotlinx.coroutines.launch

fun main() { 
   //sampleStart 
   var value by remember { mutableStateOf("") }
val scope = rememberCoroutineScope()
val snackHostState = LocalSnackbarHostState.current
SearchField(
    value = value,
    onValueChange = { value = it },
    placeholder = { Text(text = "Search") },
    onSearch = {
        scope.launch {
            // invoke when user click action button on keyboard
            snackHostState.show(message = "searchFor：$it")
        }
    },
) 
   //sampleEnd
}
```
```
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.rememberCoroutineScope
import androidx.compose.runtime.setValue
import androidx.compose.ui.res.painterResource
import androidx.compose.ui.tooling.preview.Preview
import com.pico.spatial.ui.design.Icon
import com.pico.spatial.ui.design.SearchField
import com.pico.spatial.ui.design.Text
import com.pico.spatial.ui.design.windows.LocalSnackbarHostState
import kotlinx.coroutines.launch

fun main() { 
   //sampleStart 
   var value by remember { mutableStateOf("") }
SearchField(
    value = value,
    onValueChange = { value = it },
    placeholder = { Text(text = "Search") },
    onSearch = {},
    leadingContent = { Icon(painter = painterResource(R.drawable.ic_sameple_voice), null) },
) 
   //sampleEnd
}
```