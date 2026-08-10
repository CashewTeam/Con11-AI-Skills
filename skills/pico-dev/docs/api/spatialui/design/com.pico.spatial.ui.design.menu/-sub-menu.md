# SubMenu | PICO Spatial SDK

ui:design / com.pico.spatial.ui.design.menu / SubMenu 
# SubMenu
```kotlin
@Composable
```fun  SubMenu ( onDismissRequest :  ( )  ->  Unit ,  modifier :  Modifier  =  Modifier ,  positionProvider :  PopupPositionProvider  =  rememberSubMenuPositionProvider() ,  scrollState :  ScrollState  =  rememberScrollState() ,  properties :  PopupProperties  =  MenuDefaults.DefaultPopupProperties ,  padding :  PaddingValues  =  MenuDefaults.DefaultMenuPadding ,  cornerRadius :  Dp  =  MenuDefaults.DefaultMenuCornerRadius ,  hasScrollIndicator :  Boolean  =  false ,  content :  @ Composable ColumnScope . ( )  ->  Unit ) 
A submenu is a compact way of displaying multiple choices of  Menu . 
#### Parameters
on Dismiss Request 
called when the user requests to dismiss the menu, such as by tapping outside the menu's bounds. 
modifier 
Modifier  to be applied to the menu's content. 
position Provider 
a position provider to determine where to place the sub menu, by default it's  rememberSubMenuPositionProvider . 
scroll State 
a  ScrollState  to used by the menu's content for items vertical scrolling. 
properties 
PopupProperties  for further customization of this popup's behavior. 
padding 
the padding value of the menu panel, default is  MenuDefaults.DefaultMenuPadding . 
corner Radius 
the corner radius used to clip this menu. 
has Scroll Indicator 
Whether this menu has a scroll indicator or not. Default is false. 
content 
the content of this dropdown menu, typically a  MenuItem . 
#### See also
Menu Item Menu 
#### Samples
```
import androidx.compose.foundation.layout.Box
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.tooling.preview.Preview
import androidx.compose.ui.unit.dp
import com.pico.spatial.ui.design.Button
import com.pico.spatial.ui.design.Divider
import com.pico.spatial.ui.design.Text
import com.pico.spatial.ui.design.menu.Menu
import com.pico.spatial.ui.design.menu.MenuItem
import com.pico.spatial.ui.design.menu.SubMenu
import com.pico.spatial.ui.design.menu.rememberMenuPositionProvider
import com.pico.spatial.ui.design.windows.popup.HorizontalPlacement
import com.pico.spatial.ui.design.windows.popup.VerticalPlacement

fun main() { 
   //sampleStart 
   // declare show state
var showMenu by remember { mutableStateOf(false) }
Box {
    // declare a dropdown menu
    if (showMenu) {
        Menu(
            onDismissRequest = {
                // dismiss menu
                showMenu = false
            }
        ) {
            var showSubMenu by remember { mutableStateOf(false) }
            // add menu item here
            MenuItem(
                title = { Text("Menu1") },
                onClick = {
                    // show sub menu
                    showSubMenu = true
                },
                subMenu = {
                    if (showSubMenu) {
                        SubMenu(
                            onDismissRequest = {
                                // dismiss submenu
                                showSubMenu = false
                            }
                        ) {
                            // add menu item to submenu
                            MenuItem(title = { Text("I am submenu 1") })
                            MenuItem(title = { Text("I am submenu 2") })
                        }
                    }
                },
            )
            // ... more menu item
        }
    }
    // use Button as menu anchor
    Button(
        onClick = {
            // show menu
            showMenu = true
        }
    ) {
        Text("show menu")
    }
} 
   //sampleEnd
}
```