# Sheet | PICO Spatial SDK

ui:design / com.pico.spatial.ui.design.windows / Sheet 
# Sheet
```kotlin
@Composable
```fun  Sheet ( modifier :  Modifier  =  Modifier ,  properties :  DialogProperties  =  SheetDefaults.DefaultSheetsProperties ,  onDismissRequest :  ( )  ->  Unit ?  =  null ,  cornerRadius :  Dp  =  SheetDefaults.CornerRadius ,  followViewpoints :  Set < ViewPoint >  =  ViewPoint.All ,  contentPadding :  PaddingValues  =  SheetDefaults.ContentPadding ,  contentSpace :  Dp  =  SheetDefaults.ContentSpace ,  title :  @ Composable ( )  ->  Unit ?  =  null ,  leadingAction :  @ Composable ( )  ->  Unit ?  =  {
        DefaultCloseIconButton(onClick = { onDismissRequest?.invoke() })
    } ,  trailingAction :  @ Composable ( )  ->  Unit ?  =  null ,  bottom :  @ Composable ( )  ->  Unit ?  =  null ,  content :  @ Composable ( )  ->  Unit ) 
A sheet. It includes a title, a content body, and a bottom area. Only provides basic layout, you can customize it by passing  title ,  content  and  bottom . In the title area, you can customize the leading action and trailing action. 
#### Parameters
modifier 
The modifier to be applied to the content. 
properties 
see  DialogProperties . 
on Dismiss Request 
Executes when the user clicks outside the popup. 
corner Radius 
The corner radius of the sheet. 
follow Viewpoints 
The viewpoints that the sheet will follow. By default, it is  ViewPoint.All . 
content Padding 
The padding of content body. 
content Space 
The space between content items. 
title 
The component shown as title, typically  Text 
leading Action 
The component shown at top leading corner of  Sheet 
trailing Action 
The component shown at top trailing corner  Sheet 
bottom 
The component shown at bottom of  BasicSheet 
content 
will be passed to  LazyColumn 's content 
#### Samples
```
import androidx.compose.foundation.Image
import androidx.compose.foundation.background
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.layout.ContentScale
import androidx.compose.ui.res.painterResource
import androidx.compose.ui.tooling.preview.Preview
import androidx.compose.ui.unit.dp
import androidx.compose.ui.window.DialogProperties
import com.pico.spatial.ui.design.Button
import com.pico.spatial.ui.design.ButtonDefaults
import com.pico.spatial.ui.design.PicoTheme
import com.pico.spatial.ui.design.Text
import com.pico.spatial.ui.design.windows.HeadImageSheet
import com.pico.spatial.ui.design.windows.Sheet

fun main() { 
   //sampleStart 
   var isShow by remember { mutableStateOf(false) }
if (isShow) {
    Sheet(
        onDismissRequest = { isShow = false },
        title = { Text("Title") },
        bottom = {
            Column(
                modifier = Modifier.fillMaxWidth(),
                horizontalAlignment = Alignment.CenterHorizontally,
            ) {
                Button(
                    modifier = Modifier.fillMaxWidth().height(48.dp),
                    onClick = { isShow = false },
                    shape = RoundedCornerShape(24.dp),
                ) {
                    Text("OK")
                }
            }
        },
    ) {
        Text("Message")
    }
}
Button(onClick = { isShow = true }) { Text("Show Simple Sheet") } 
   //sampleEnd
}
```
```
import androidx.compose.foundation.Image
import androidx.compose.foundation.background
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.layout.ContentScale
import androidx.compose.ui.res.painterResource
import androidx.compose.ui.tooling.preview.Preview
import androidx.compose.ui.unit.dp
import androidx.compose.ui.window.DialogProperties
import com.pico.spatial.ui.design.Button
import com.pico.spatial.ui.design.ButtonDefaults
import com.pico.spatial.ui.design.PicoTheme
import com.pico.spatial.ui.design.Text
import com.pico.spatial.ui.design.windows.HeadImageSheet
import com.pico.spatial.ui.design.windows.Sheet

fun main() { 
   //sampleStart 
   var isShow by remember { mutableStateOf(false) }
if (isShow) {
    Sheet(
        onDismissRequest = { isShow = false },
        title = { Text("Title") },
        trailingAction = {
            Button(
                onClick = { isShow = false },
                size = ButtonDefaults.buttonSize(width = 69.dp, height = 40.dp),
                shape = RoundedCornerShape(20.dp),
            ) {
                Text("OK", style = PicoTheme.typography.titleSmall)
            }
        },
        bottom = {
            Row(
                modifier = Modifier.fillMaxWidth(),
                verticalAlignment = Alignment.CenterVertically,
                horizontalArrangement =
                    Arrangement.spacedBy(space = 8.dp, alignment = Alignment.End),
            ) {
                Button(
                    onClick = { isShow = false },
                    size = ButtonDefaults.buttonSize(width = 113.dp, height = 48.dp),
                    colors =
                        ButtonDefaults.buttonColors(
                            containerColor = ButtonContainerColor,
                            contentColor = ButtonContentColor,
                        ),
                    shape = RoundedCornerShape(24.dp),
                ) {
                    Text("Cancel")
                }
                Button(
                    onClick = { isShow = false },
                    size = ButtonDefaults.buttonSize(width = 113.dp, height = 48.dp),
                    shape = RoundedCornerShape(24.dp),
                ) {
                    Text("Confirm")
                }
            }
        },
    ) {
        Text("Message")
    }
}
Button(onClick = { isShow = true }) { Text("Show Title Sheet") } 
   //sampleEnd
}
```
```
import androidx.compose.foundation.Image
import androidx.compose.foundation.background
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.layout.ContentScale
import androidx.compose.ui.res.painterResource
import androidx.compose.ui.tooling.preview.Preview
import androidx.compose.ui.unit.dp
import androidx.compose.ui.window.DialogProperties
import com.pico.spatial.ui.design.Button
import com.pico.spatial.ui.design.ButtonDefaults
import com.pico.spatial.ui.design.PicoTheme
import com.pico.spatial.ui.design.Text
import com.pico.spatial.ui.design.windows.HeadImageSheet
import com.pico.spatial.ui.design.windows.Sheet

fun main() { 
   //sampleStart 
   var isShow by remember { mutableStateOf(false) }
if (isShow) {
    Sheet(
        onDismissRequest = { isShow = false },
        leadingAction = null,
        properties = DialogProperties(dismissOnClickOutside = true),
    ) {
        Box(modifier = Modifier.height(200.dp), contentAlignment = Alignment.Center) {
            Text("No Title Sheet")
        }
    }
}
Button(onClick = { isShow = true }) { Text("Show No Title Sheet") } 
   //sampleEnd
}
```