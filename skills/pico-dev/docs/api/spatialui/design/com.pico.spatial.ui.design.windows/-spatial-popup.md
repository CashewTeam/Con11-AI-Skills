# SpatialPopup | PICO Spatial SDK

ui:design / com.pico.spatial.ui.design.windows / SpatialPopup 
# SpatialPopup
```kotlin
@Composable
```fun  SpatialPopup ( onDismissRequest :  ( )  ->  Unit ? ,  modifier :  Modifier  =  Modifier ,  popupPositionProvider :  PopupPositionProvider  =  rememberSpatialPopupPositionProvider() ,  cornerRadius :  Dp  =  SpatialPopupDefaults.CornerRadius ,  defaultMinWidth :  Dp  =  SpatialPopupDefaults.DefaultWidth ,  defaultMinHeight :  Dp  =  SpatialPopupDefaults.DefaultHeight ,  properties :  PopupProperties  =  SpatialPopupDefaults.DefaultPopupProperties ,  content :  @ Composable BoxScope . ( )  ->  Unit ) 
Opens a popup with the given content. 
A popup is a floating container that appears on top of the current window with a fixed spatial z offset. It is especially useful for non-modal UI surfaces that remain hidden until they are needed, for example floating widgets like Cut/Copy/Paste. 
The popup is positioned relative to its anchor view, using the  popupPositionProvider . You can use  rememberSpatialPopupPositionProvider  to create a  PopupPositionProvider  that places the popup relative to it's anchor view. 
#### Parameters
on Dismiss Request 
Executes when the user clicks outside of the popup. 
modifier 
Modifier for the popup. 
popup Position Provider 
Provides the screen position of the popup, see  rememberSpatialPopupPositionProvider . 
corner Radius 
The corner radius of the popup. 
default Min Width 
The minimum width of the popup. Use  Dp.Unspecified  to wrap content size. 
default Min Height 
The minimum height of the popup. Use  Dp.Unspecified  to wrap content size. 
properties 
PopupProperties  for further customization of this popup's behavior. 
content 
The content to be displayed inside the popup. 
#### Samples
```
import androidx.compose.foundation.layout.Box
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.Dp
import androidx.compose.ui.unit.dp
import com.pico.spatial.ui.design.Button
import com.pico.spatial.ui.design.Text
import com.pico.spatial.ui.design.windows.SpatialPopup
import com.pico.spatial.ui.design.windows.popup.HorizontalPlacement
import com.pico.spatial.ui.design.windows.popup.VerticalPlacement
import com.pico.spatial.ui.design.windows.rememberSpatialPopupPositionProvider

fun main() { 
   //sampleStart 
   // declare show state
var showPopup by remember { mutableStateOf(false) }
Box {
    // declare a popup
    if (showPopup) {
        SpatialPopup(
            onDismissRequest = {
                // dismiss popup
                showPopup = false
            }
        ) {
            // popup content
            Text(text = "SpatialPopup", modifier = Modifier.align(Alignment.Center))
        }
    }
    // use Button as anchor
    Button(
        onClick = {
            // show popup
            showPopup = true
        }
    ) {
        Text("show popup")
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
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.Dp
import androidx.compose.ui.unit.dp
import com.pico.spatial.ui.design.Button
import com.pico.spatial.ui.design.Text
import com.pico.spatial.ui.design.windows.SpatialPopup
import com.pico.spatial.ui.design.windows.popup.HorizontalPlacement
import com.pico.spatial.ui.design.windows.popup.VerticalPlacement
import com.pico.spatial.ui.design.windows.rememberSpatialPopupPositionProvider

fun main() { 
   //sampleStart 
   var showPopup by remember { mutableStateOf(false) }
Box {
    if (showPopup) {
        SpatialPopup(
            // use Dp.Unspecified to wrap content size
            defaultMinHeight = Dp.Unspecified,
            defaultMinWidth = Dp.Unspecified,
            onDismissRequest = { showPopup = false },
        ) {
            Text(text = "SpatialPopup", modifier = Modifier.align(Alignment.Center))
        }
    }
    Button(onClick = { showPopup = true }) { Text("show popup") }
} 
   //sampleEnd
}
```