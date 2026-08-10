# ListItem | PICO Spatial SDK

ui:design / com.pico.spatial.ui.design / ListItem 
# ListItem
```kotlin
@Composable
```fun  ListItem ( headlineContent :  @ Composable ( )  ->  Unit ,  modifier :  Modifier  =  Modifier ,  supportingContent :  @ Composable ( )  ->  Unit ?  =  null ,  leadingContent :  @ Composable BoxScope . ( )  ->  Unit ?  =  null ,  trailingContent :  @ Composable BoxScope . ( )  ->  Unit ?  =  null ,  colors :  ListItemColors  =  ListItemDefaults.listItemColors() ,  padding :  PaddingValues  =  ListItemDefaults.DefaultPadding ,  shape :  Shape  =  ListItemDefaults.shape ) 
This component can be used to achieve the list item templates existing in the spec. 
#### Parameters
headline Content 
the headline content of the list item 
modifier 
Modifier  to be applied to the list item 
supporting Content 
the supporting content of the list item 
leading Content 
the leading content of the list item 
trailing Content 
the trailing meta text, icon, switch or checkbox 
colors 
ListItemColors  that will be used to resolve the background and content color for this list item in different states. See  ListItemDefaults.listItemColors 
padding 
the padding values surrounding the content 
shape 
background shape of the list item. Color  ListItemColors.backgroundColor 
#### Samples
```
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.res.painterResource
import androidx.compose.ui.tooling.preview.Preview
import com.pico.spatial.ui.design.Icon
import com.pico.spatial.ui.design.ListItem
import com.pico.spatial.ui.design.Text

fun main() { 
   //sampleStart 
   ListItem(headlineContent = { Text(text = "Item") }) 
   //sampleEnd
}
```
```
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.res.painterResource
import androidx.compose.ui.tooling.preview.Preview
import com.pico.spatial.ui.design.Icon
import com.pico.spatial.ui.design.ListItem
import com.pico.spatial.ui.design.Text

fun main() { 
   //sampleStart 
   ListItem(
    headlineContent = { Text(text = "Headline content") },
    leadingContent = {
        Icon(
            painter = painterResource(R.drawable.ic_sample_placeholder),
            contentDescription = null,
        )
    },
    supportingContent = { Text(text = "Supporting content") },
    trailingContent = {
        Icon(
            painter = painterResource(id = R.drawable.ic_sample_listitem_check),
            contentDescription = null,
        )
    },
) 
   //sampleEnd
}
```