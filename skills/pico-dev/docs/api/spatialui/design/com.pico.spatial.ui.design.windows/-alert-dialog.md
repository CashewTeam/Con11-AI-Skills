# AlertDialog | PICO Spatial SDK

ui:design / com.pico.spatial.ui.design.windows / AlertDialog 
# AlertDialog
```kotlin
@Composable
```fun  AlertDialog ( modifier :  Modifier  =  Modifier ,  cornerRadius :  Dp  =  AlertDialogDefaults.DialogCornerRadius ,  properties :  DialogProperties  =  AlertDialogDefaults.DefaultAlertDialogProperties ,  onDismissRequest :  ( )  ->  Unit ?  =  null ,  icon :  @ Composable ( )  ->  Unit ?  =  null ,  title :  @ Composable ( )  ->  Unit ?  =  null ,  content :  @ Composable ( )  ->  Unit ?  =  null ,  buttons :  @ Composable ( )  ->  Unit ?  =  null ,  orientation :  Orientation  =  Orientation.Horizontal ,  padding :  PaddingValues  =  AlertDialogDefaults.DialogPadding ,  followViewpoints :  Set < ViewPoint >  =  ViewPoint.All ) 
Dialogs provide important prompts in a user flow. They can require an action, communicate information, or help users accomplish a task. 
Displays an alert dialog with customizable components. This dialog can include an icon, title, custom content, and buttons. 
#### Parameters
modifier 
The  Modifier  to be applied to the dialog. 
corner Radius 
The corner radius of the dialog, defaulting to  AlertDialogDefaults.DialogCornerRadius . 
properties 
Platform-specific properties used to further configure the dialog, defaulting to  AlertDialogDefaults.DefaultAlertDialogProperties . 
on Dismiss Request 
A callback invoked when the user attempts to dismiss the dialog by clicking outside or pressing the back button. 
icon 
An optional composable for the icon, which will be displayed above the title. 
title 
An optional composable for the title, used to explain the purpose of the dialog. 
content 
An optional composable for custom content, displayed below the title. 
buttons 
An optional composable for the buttons, typically used for actions like "OK" or "Cancel". 
orientation 
The orientation of the dialog, defaulting to  Orientation.Horizontal . 
padding 
The padding for the entire dialog, defaulting to  AlertDialogDefaults.DialogPadding . 
follow Viewpoints 
The viewpoints to follow, defaulting to  ViewPoint.All . 
#### Samples
```
import androidx.compose.foundation.gestures.Orientation
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.res.painterResource
import androidx.compose.ui.tooling.preview.Preview
import androidx.compose.ui.unit.dp
import androidx.compose.ui.window.DialogProperties
import com.pico.spatial.ui.design.Button
import com.pico.spatial.ui.design.ButtonDefaults
import com.pico.spatial.ui.design.CircularProgressIndicator
import com.pico.spatial.ui.design.Icon
import com.pico.spatial.ui.design.ListItem
import com.pico.spatial.ui.design.PicoTheme
import com.pico.spatial.ui.design.Text
import com.pico.spatial.ui.design.windows.AlertDialog

fun main() { 
   //sampleStart 
   var show by remember { mutableStateOf(false) }
if (show) {
    AlertDialog(
        onDismissRequest = { show = false },
        buttons = {
            Row(
                modifier = Modifier.fillMaxWidth(),
                horizontalArrangement = Arrangement.spacedBy(15.dp, Alignment.End),
            ) {
                Button(onClick = { show = false }) { Text(text = "Cancel") }
            }
        },
        title = { Text(text = "Dialog Alert") },
    )
}
Button(onClick = { show = true }) { Text(text = "show simple dialog") } 
   //sampleEnd
}
```
```
import androidx.compose.foundation.gestures.Orientation
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.res.painterResource
import androidx.compose.ui.tooling.preview.Preview
import androidx.compose.ui.unit.dp
import androidx.compose.ui.window.DialogProperties
import com.pico.spatial.ui.design.Button
import com.pico.spatial.ui.design.ButtonDefaults
import com.pico.spatial.ui.design.CircularProgressIndicator
import com.pico.spatial.ui.design.Icon
import com.pico.spatial.ui.design.ListItem
import com.pico.spatial.ui.design.PicoTheme
import com.pico.spatial.ui.design.Text
import com.pico.spatial.ui.design.windows.AlertDialog

fun main() { 
   //sampleStart 
   var show by remember { mutableStateOf(false) }
if (show) {
    AlertDialog(
        onDismissRequest = { show = false },
        buttons = {
            Row(
                modifier = Modifier.fillMaxWidth(),
                horizontalArrangement = Arrangement.spacedBy(8.dp, Alignment.End),
            ) {
                Button(
                    modifier = Modifier.weight(1f),
                    onClick = { show = false },
                    colors =
                        ButtonDefaults.buttonColors(
                            containerColor = Color.LightGray,
                            contentColor = Color(color = 0xFF000000),
                        ),
                ) {
                    Text(text = "Cancel")
                }
                Button(modifier = Modifier.weight(1f), onClick = { show = false }) {
                    Text(text = "Action")
                }
            }
        },
        icon = {
            Icon(
                modifier = Modifier.size(28.dp),
                painter = painterResource(id = R.drawable.ic_sample_listitem_leading),
                contentDescription = null,
            )
        },
        title = { Text(text = "Dialog Alert") },
        content = {
            Text(text = AlertContent, style = PicoTheme.typography.bodyMediumMultiline)
        },
    )
}
Button(onClick = { show = true }) { Text(text = "show dialog") } 
   //sampleEnd
}
```
```
import androidx.compose.foundation.gestures.Orientation
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.res.painterResource
import androidx.compose.ui.tooling.preview.Preview
import androidx.compose.ui.unit.dp
import androidx.compose.ui.window.DialogProperties
import com.pico.spatial.ui.design.Button
import com.pico.spatial.ui.design.ButtonDefaults
import com.pico.spatial.ui.design.CircularProgressIndicator
import com.pico.spatial.ui.design.Icon
import com.pico.spatial.ui.design.ListItem
import com.pico.spatial.ui.design.PicoTheme
import com.pico.spatial.ui.design.Text
import com.pico.spatial.ui.design.windows.AlertDialog

fun main() { 
   //sampleStart 
   var show by remember { mutableStateOf(false) }
if (show) {
    AlertDialog(
        onDismissRequest = { show = false },
        title = { Text(text = "Title") },
        content = {
            LazyColumn(
                modifier = Modifier.fillMaxWidth().height(350.dp),
                verticalArrangement = Arrangement.spacedBy(10.dp),
            ) {
                items(count = 100) {
                    ListItem(
                        headlineContent = { Text(text = "Item $it") },
                        leadingContent = {
                            Icon(
                                painter =
                                    painterResource(
                                        id = R.drawable.ic_sample_listitem_lite_icon
                                    ),
                                contentDescription = null,
                            )
                        },
                    )
                }
            }
        },
        buttons = {
            Button(modifier = Modifier.fillMaxWidth(), onClick = { show = false }) {
                Text(text = "Button")
            }
        },
    )
}
Button(onClick = { show = true }) { Text(text = "show dialog with custom content") } 
   //sampleEnd
}
```