# Menu | PICO Spatial SDK

ui:design / com.pico.spatial.ui.design.menu / Menu 
# Menu
```kotlin
@Composable
```fun  Menu ( onDismissRequest :  ( )  ->  Unit ,  modifier :  Modifier  =  Modifier ,  positionProvider :  PopupPositionProvider  =  rememberMenuPositionProvider() ,  scrollState :  ScrollState  =  rememberScrollState() ,  properties :  PopupProperties  =  MenuDefaults.DefaultPopupProperties ,  padding :  PaddingValues  =  MenuDefaults.DefaultMenuPadding ,  cornerRadius :  Dp  =  MenuDefaults.DefaultMenuCornerRadius ,  hasScrollIndicator :  Boolean  =  false ,  content :  @ Composable ColumnScope . ( )  ->  Unit ) 
A dropdown menu is a compact way of displaying multiple choices. It appears upon interaction with an element (such as an icon or button) or when users perform a specific action. 
A  Menu  behaves similarly to a  Popup , and will use the position of the parent layout to position itself on screen. Commonly a  Menu  will be placed in a  Box  with a sibling that will be used as the 'anchor'. Note that a  Menu  by itself will not take up any space in a layout, as the menu is displayed in a separate window, on top of other content. 
The  content  of a  Menu  will typically be  MenuItem s, as well as custom content. Using  MenuItem s will result in a menu that matches the Material specification for menus. Also note that if  scrollState  is not null, the  content  will be placed inside a scrollable  Column . So using a  androidx.compose.foundation.lazy.LazyColumn  as the root layout inside  content  is unsupported in that case. By default, the content container  Column  is not scrollable. 
onDismissRequest  will be called when the menu should close - for example when there is a tap outside the menu, or when the back key is pressed. 
Menu  changes its positioning depending on the available space, always trying to be fully visible. It will try to expand horizontally, depending on layout direction, to the end of its parent, then to the start of its parent, and then screen end-aligned. Vertically, it will try to expand to the bottom of its parent, then from the top of its parent, and then screen top-aligned. 
#### Parameters
on Dismiss Request 
called when the user requests to dismiss the menu, such as by tapping outside the menu's bounds 
modifier 
Modifier  To be applied to the menu's content. 
position Provider 
a position provider to determine where to place the menu, by default it's  rememberMenuPositionProvider 
scroll State 
a  ScrollState  to used by the menu's content for items vertical scrolling 
properties 
PopupProperties  for further customization of this popup's behavior 
padding 
the padding value of the menu panel, default is  MenuDefaults.DefaultMenuPadding 
corner Radius 
the corner radius used to clip this menu 
has Scroll Indicator 
Whether this menu has a scroll indicator or not. Default is false. 
content 
the content of this dropdown menu, typically a  MenuItem . 
#### See also
Sub Menu Menu Item 
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
            // add menu items here
            MenuItem(title = { Text("Menu1") })
            // add divider, or custom composable function
            Divider()
            MenuItem(title = { Text("Menu2") })
        }
    }
    // us Button as dropdown anchor
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
            },
            // set custom position
            positionProvider =
                rememberMenuPositionProvider(
                    horizontalPlacement = HorizontalPlacement.alignStart(),
                    verticalPlacement = VerticalPlacement.above(offset = 10.dp),
                ),
        ) {
            // add menu items here
            MenuItem(title = { Text("Menu1") })
        }
    }
    // us Button as dropdown anchor
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