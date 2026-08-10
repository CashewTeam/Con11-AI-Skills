# Link | PICO Spatial SDK

ui:design / com.pico.spatial.ui.design / Link 
# Link
```kotlin
@Composable
```fun  Link ( onClick :  ( )  ->  Unit ,  modifier :  Modifier  =  Modifier ,  enabled :  Boolean  =  true ,  size :  ButtonSize  =  LinkDefaults.Regular ,  shape :  Shape  =  size.shapeForLink() ,  colors :  ButtonColors  =  LinkDefaults.defaultColors() ,  trailingIcon :  @ Composable ( )  ->  Unit ?  =  null ,  semanticsContent :  String ?  =  null ,  contentPadding :  PaddingValues  =  size.paddingForLink(trailingIcon != null) ,  interactionSource :  MutableInteractionSource  =  remember { MutableInteractionSource() } ,  content :  @ Composable BoxScope . ( )  ->  Unit ) 
A  Link  is a text button with a optional trailing icon. 
#### Parameters
on Click 
the callback to be invoked when this link is clicked. 
modifier 
the  Modifier  to be applied to this link. 
enabled 
whether this link is enabled. 
size 
the size of this link. 
shape 
the shape of this link. 
colors 
the  ButtonColors  used by this link to resolve background color and content color. 
trailing Icon 
a trailing icon after the content, typically an  Icon , default tint is  ButtonColors.contentColor 
semantics Content 
the semantic content of this link. 
content Padding 
the padding of this link. 
interaction Source 
the  MutableInteractionSource  representing the stream of Interactions for this link 
content 
the content of this link. typically a  Text 
#### Samples
```
import androidx.compose.runtime.Composable
import androidx.compose.ui.tooling.preview.Preview
import androidx.compose.ui.unit.dp
import com.pico.spatial.ui.design.Link
import com.pico.spatial.ui.design.Text

fun main() { 
   //sampleStart 
   Link(onClick = {}) { Text("Link style button") } 
   //sampleEnd
}
```