# Toolbar | PICO Spatial SDK

ui:design / com.pico.spatial.ui.design.windows / Toolbar 
# Toolbar
```kotlin
@Composable
```fun  Toolbar ( cornerSize :  Dp  =  ToolbarDefaults.CornerRadius ,  followViewpoints :  Set < ViewPoint >  =  ViewPoint.All ,  focusable :  Boolean  =  true ,  content :  @ Composable RowScope . ( )  ->  Unit ) 
Toolbar is floating window will be placed at center bottom of WindowContainer. 
This overload is the legacy single-segment toolbar. 
#### Parameters
corner Size 
Control the corner radius of the Toolbar. Default is 16 dp. 
follow Viewpoints 
The  ViewPoint s that the toolbar will follow. 
focusable 
Whether the toolbar is focusable. When a  Toolbar  is not focusable, it can not receive input events, such as text input and accessibility events. 
content 
The content of the toolbar. 
#### Samples
```
import androidx.compose.foundation.layout.Box
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.unit.dp
import com.pico.spatial.ui.design.IconButton
import com.pico.spatial.ui.design.IconButtonDefaults
import com.pico.spatial.ui.design.windows.Toolbar
import com.pico.spatial.ui.design.windows.ToolbarDefaults

fun main() { 
   //sampleStart 
   Toolbar(cornerSize = 200.dp) {
    repeat(5) {
        var showMenu by remember { mutableStateOf(false) }
        Box {
            IconButton(
                onClick = { showMenu = true },
                colors = IconButtonDefaults.iconButtonColors(containerColor = Color.Transparent),
            ) {
                AnyIcon(iconSize = 20.dp)
            }
            if (showMenu) {
                val onDismissRequest = {
                    // dismiss menu
                    showMenu = false
                }
                SimpleMenu(onDismissRequest)
            }
        }
    }
} 
   //sampleEnd
}
```
```kotlin
@Composable
```fun  Toolbar ( followViewpoints :  Set < ViewPoint >  =  ViewPoint.All ,  focusable :  Boolean  =  true ,  contentConfiguration :  ToolbarSegmentConfiguration  =  ToolbarDefaults.contentConfiguration() ,  supportingConfiguration :  ToolbarSegmentConfiguration  =  ToolbarDefaults.supportingConfiguration() ,  supportingContent :  @ Composable RowScope . ( )  ->  Unit ?  =  null ,  content :  @ Composable RowScope . ( )  ->  Unit ) 
Segmented Toolbar overload. 
This overload supports rendering  content  and optional  supportingContent  as two independent segments. Each segment renders its own material/color background, padding and corner radius. The gap between segments is fixed to  ToolbarDefaults.SegmentGap . 
Note: to avoid call ambiguity with the legacy  Toolbar { ... }  overload, callers should use the named argument form  Toolbar(content = { ... }) . 
#### Parameters
follow Viewpoints 
The  ViewPoint s that the toolbar will follow. 
focusable 
Whether the toolbar is focusable. When a  Toolbar  is not focusable, it can not receive input events, such as text input and accessibility events. 
content Configuration 
The configuration of the content segment. 
supporting Configuration 
The configuration of the supporting segment. 
supporting Content 
The supporting content of the toolbar. 
content 
The content of the toolbar. 
#### Samples
```
import androidx.compose.foundation.layout.Box
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.unit.dp
import com.pico.spatial.ui.design.IconButton
import com.pico.spatial.ui.design.IconButtonDefaults
import com.pico.spatial.ui.design.windows.Toolbar
import com.pico.spatial.ui.design.windows.ToolbarDefaults

fun main() { 
   //sampleStart 
   Toolbar(
    content = {
        repeat(3) {
            IconButton(
                onClick = {},
                colors = IconButtonDefaults.iconButtonColors(containerColor = Color.Transparent),
            ) {
                AnyIcon(iconSize = 20.dp)
            }
        }
    },
    supportingContent = {
        repeat(2) {
            IconButton(
                onClick = {},
                colors = IconButtonDefaults.iconButtonColors(containerColor = Color.Transparent),
            ) {
                AnyIcon(iconSize = 20.dp)
            }
        }
    },
    supportingConfiguration =
        ToolbarDefaults.supportingConfiguration(
            enableMaterial = false,
            backgroundColor = Color.Red,
            itemGap = 8.dp,
        ),
) 
   //sampleEnd
}
```