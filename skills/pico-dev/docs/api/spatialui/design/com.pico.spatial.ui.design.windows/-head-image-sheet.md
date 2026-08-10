# HeadImageSheet | PICO Spatial SDK

ui:design / com.pico.spatial.ui.design.windows / HeadImageSheet 
# HeadImageSheet
```kotlin
@Composable
```fun  HeadImageSheet ( headerImage :  @ Composable ( )  ->  Unit ,  modifier :  Modifier  =  Modifier ,  properties :  DialogProperties  =  SheetDefaults.DefaultSheetsProperties ,  onDismissRequest :  ( )  ->  Unit ?  =  null ,  cornerRadius :  Dp  =  SheetDefaults.CornerRadius ,  followViewpoints :  Set < ViewPoint >  =  ViewPoint.All ,  contentPadding :  PaddingValues  =  SheetDefaults.ContentPadding ,  contentSpace :  Dp  =  SheetDefaults.ContentSpace ,  closeIcon :  @ Composable ( )  ->  Unit  =  {
        HeadImageSheetCloseIconButton { onDismissRequest?.invoke() }
    } ,  title :  @ Composable ( )  ->  Unit ?  =  null ,  bottom :  @ Composable ( )  ->  Unit ?  =  null ,  content :  @ Composable ( )  ->  Unit ) 
A sheet. It includes a head image, a title, a content body, and a bottom area. Only provides basic layout, you can customize it by passing  headerImage ,  title ,  content  and  bottom . The  headerImage  will be shown at the top, the  title  will be shown at the bottom of head image, the  content  will be shown in the middle of sheet, the  bottom  will be shown at the bottom of sheet. The  closeIcon  will be shown at top leading corner of sheet. 
#### Parameters
header Image 
The component will be shown at the top 
modifier 
The modifier to be applied to the content. 
properties 
see  DialogProperties . 
on Dismiss Request 
Executes when the user clicks outside the sheet. 
corner Radius 
The corner radius of the sheet. 
follow Viewpoints 
The viewpoints that the sheet will follow. By default, it is  ViewPoint.All . 
content Padding 
The padding of content body. 
content Space 
The space between content items. 
close Icon 
The component shown at top left corner of  HeadImageSheet . Default is  HeadImageSheetCloseIconButton 
title 
The component shown as title on bottom of head image, expected to be  Text 
bottom 
The component shown at bottom of  HeadImageSheet 
content 
The content of sheet 
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
    HeadImageSheet(
        headerImage = {
            Image(
                painter = painterResource(id = R.drawable.img_sample_headimage),
                contentDescription = "description of image",
                modifier = Modifier.fillMaxWidth(),
                contentScale = ContentScale.Crop,
            )
        },
        title = { Text("Sheet Title") },
        onDismissRequest = { isShow = false },
    ) {
        Box(
            modifier =
                Modifier.fillMaxWidth()
                    .height(132.dp)
                    .background(ContentBackgroundColor)
                    .padding(16.dp)
        ) {
            Text("Sheet body", style = PicoTheme.typography.titleMedium)
        }
    }
}
Button(onClick = { isShow = true }) { Text("Show Head Image Sheet") } 
   //sampleEnd
}
```