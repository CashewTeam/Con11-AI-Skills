# MenuItem | PICO Spatial SDK

ui:design / com.pico.spatial.ui.design.menu / MenuItem 
# MenuItem
```kotlin
@Composable
```fun  MenuItem ( title :  @ Composable ( )  ->  Unit ,  modifier :  Modifier  =  Modifier ,  subMenu :  @ Composable ( )  ->  Unit ?  =  null ,  onClick :  ( )  ->  Unit ?  =  null ,  subtitle :  @ Composable ( )  ->  Unit ?  =  null ,  leadingIcon :  @ Composable ( )  ->  Unit ?  =  null ,  trailingIcon :  @ Composable ( )  ->  Unit ?  =  null ,  contentColors :  MenuItemColors  =  MenuItemDefaults.menuItemColors() ,  paddings :  PaddingValues  =  MenuItemDefaults.DefaultPadding ,  cornerSize :  Dp  =  MenuItemDefaults.RoundRadius ,  interactionSource :  MutableInteractionSource  =  remember { MutableInteractionSource() } ) 
Standard menuItem for  Menu / SubMenu . Some slot was provide for developers to fastly build standard menu, such as  title , subtitle ,  leadingIcon ,  trailingIcon . 
#### Parameters
title 
title content, use Text 
modifier 
Modifier  to be applied to the item 
sub Menu 
place your  SubMenu  in this function 
on Click 
The onClick callback of this  MenuItem . 
subtitle 
the subtitle content of this item. 
leading Icon 
the icon on left side. Usually place Icon or other composable content 
trailing Icon 
the icon on right side. Usually place Icon or other composable content 
content Colors 
The content color of this  MenuItem . 
paddings 
The surrounding padding of this  MenuItem . 
corner Size 
The size of corner 
interaction Source 
The  MutableInteractionSource  representing the stream of Interactions for this  MenuItem . You can create and pass in your own remembered  MutableInteractionSource  if you custom click behavior through  Modifier.clickable . 
#### See also
Menu Sub Menu Basic Menu Item 
#### Samples
```
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.layout.width
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.res.painterResource
import androidx.compose.ui.tooling.preview.Preview
import androidx.compose.ui.unit.dp
import com.pico.spatial.ui.design.Icon
import com.pico.spatial.ui.design.Text
import com.pico.spatial.ui.design.menu.MenuItem

fun main() { 
   //sampleStart 
   MenuItem(
    title = { Text("Action") },
    onClick = {
        // action here
    },
) 
   //sampleEnd
}
```
```
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.layout.width
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.res.painterResource
import androidx.compose.ui.tooling.preview.Preview
import androidx.compose.ui.unit.dp
import com.pico.spatial.ui.design.Icon
import com.pico.spatial.ui.design.Text
import com.pico.spatial.ui.design.menu.MenuItem

fun main() { 
   //sampleStart 
   MenuItem(title = { Text("Title") }, subtitle = { Text("Message") }) 
   //sampleEnd
}
```
```
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.layout.width
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.res.painterResource
import androidx.compose.ui.tooling.preview.Preview
import androidx.compose.ui.unit.dp
import com.pico.spatial.ui.design.Icon
import com.pico.spatial.ui.design.Text
import com.pico.spatial.ui.design.menu.MenuItem

fun main() { 
   //sampleStart 
   MenuItem(
    title = { Text("Option") },
    subtitle = { Text("Message") },
    trailingIcon = {
        Icon(
            painter =
                painterResource(
                    id =
                        com.pico.spatial.ui.design.R.drawable.ic_sui_settinglistitem_trail_arrow
                ),
            contentDescription = null,
        )
    },
) 
   //sampleEnd
}
```
```
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.layout.width
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.res.painterResource
import androidx.compose.ui.tooling.preview.Preview
import androidx.compose.ui.unit.dp
import com.pico.spatial.ui.design.Icon
import com.pico.spatial.ui.design.Text
import com.pico.spatial.ui.design.menu.MenuItem

fun main() { 
   //sampleStart 
   MenuItem(
    title = { Text("Option") },
    subtitle = { Text("Message") },
    leadingIcon = {
        Icon(
            painter = painterResource(id = R.drawable.ic_sample_listitem_lite_icon),
            contentDescription = null,
            modifier = Modifier.size(20.dp),
        )
    },
    trailingIcon = {
        Icon(
            painter =
                painterResource(
                    id =
                        com.pico.spatial.ui.design.R.drawable.ic_sui_settinglistitem_trail_arrow
                ),
            contentDescription = null,
        )
    },
) 
   //sampleEnd
}
```
```
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.layout.width
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.res.painterResource
import androidx.compose.ui.tooling.preview.Preview
import androidx.compose.ui.unit.dp
import com.pico.spatial.ui.design.Icon
import com.pico.spatial.ui.design.Text
import com.pico.spatial.ui.design.menu.MenuItem

fun main() { 
   //sampleStart 
   MenuItem(
    title = { Text("Option") },
    subtitle = { Text("Message") },
    leadingIcon = {
        Icon(
            painter = painterResource(id = R.drawable.ic_sample_listitem_check),
            contentDescription = null,
            modifier = Modifier.size(20.dp),
        )
    },
) 
   //sampleEnd
}
```