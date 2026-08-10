# padding3D | PICO Spatial SDK

ui:foundation / com.pico.spatial.ui.foundation.layout / padding3D 
# padding3D
```kotlin
@Stable
```fun  Modifier . padding3D ( start :  Dp  =  0.dp ,  top :  Dp  =  0.dp ,  end :  Dp  =  0.dp ,  bottom :  Dp  =  0.dp ,  back :  Dp  =  0.dp ,  front :  Dp  =  0.dp ) :  Modifier 
Apply additional space along each edge of the content in Dp: start, top, end, bottom, back, and front. The start and end edges will be determined by the current LayoutDirection. Padding is applied before content measurement and takes precedence; content may only be as large as the remaining space. Negative padding is not permitted — it will cause IllegalArgumentException. See Modifier.offset. 
#### Return
The  Modifier  with expected offset value. 
#### Samples
```
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.text.BasicText
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.tooling.preview.Preview
import androidx.compose.ui.unit.dp
import com.pico.spatial.ui.foundation.layout.padding3D

fun main() { 
   //sampleStart 
   Column {
    Box(modifier = Modifier.padding3D(10.dp)) {
        BasicText(text = "padding3D all", color = { Color.Yellow })
    }

    Box(modifier = Modifier.padding3D(thicknessPadding = 10.dp)) {
        BasicText(text = "padding3D thicknessPadding 10dp", color = { Color.Yellow })
    }

    Box(modifier = Modifier.padding3D(back = 20.dp, front = 20.dp)) {
        BasicText(text = "padding3D back 20dp front 20dp", color = { Color.Yellow })
    }
} 
   //sampleEnd
}
```
```kotlin
@Stable
```fun  Modifier . padding3D ( horizontal :  Dp  =  0.dp ,  vertical :  Dp  =  0.dp ,  thicknessPadding :  Dp  =  0.dp ) :  Modifier 
Apply  horizontal  dp space along the left and right edges of the content, and  vertical  dp space along the top and bottom edges, and  thicknessPadding  dp space along the back and front edges. 
Negative padding is not permitted — it will cause IllegalArgumentException. See Modifier.offset. 
#### Return
The  Modifier  with expected offset value. 
#### Samples
```
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.text.BasicText
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.tooling.preview.Preview
import androidx.compose.ui.unit.dp
import com.pico.spatial.ui.foundation.layout.padding3D

fun main() { 
   //sampleStart 
   Column {
    Box(modifier = Modifier.padding3D(10.dp)) {
        BasicText(text = "padding3D all", color = { Color.Yellow })
    }

    Box(modifier = Modifier.padding3D(thicknessPadding = 10.dp)) {
        BasicText(text = "padding3D thicknessPadding 10dp", color = { Color.Yellow })
    }

    Box(modifier = Modifier.padding3D(back = 20.dp, front = 20.dp)) {
        BasicText(text = "padding3D back 20dp front 20dp", color = { Color.Yellow })
    }
} 
   //sampleEnd
}
```
```kotlin
@Stable
```fun  Modifier . padding3D ( all :  Dp ) :  Modifier 
Apply  all  dp of additional space along each edge of the content, left, top, right, bottom, back and front. Padding is applied before content measurement and takes precedence; content may only be as large as the remaining space. Negative padding is not permitted — it will cause IllegalArgumentException. See Modifier.offset. 
#### Return
The  Modifier  with expected offset value. 
#### Samples
```
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.text.BasicText
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.tooling.preview.Preview
import androidx.compose.ui.unit.dp
import com.pico.spatial.ui.foundation.layout.padding3D

fun main() { 
   //sampleStart 
   Column {
    Box(modifier = Modifier.padding3D(10.dp)) {
        BasicText(text = "padding3D all", color = { Color.Yellow })
    }

    Box(modifier = Modifier.padding3D(thicknessPadding = 10.dp)) {
        BasicText(text = "padding3D thicknessPadding 10dp", color = { Color.Yellow })
    }

    Box(modifier = Modifier.padding3D(back = 20.dp, front = 20.dp)) {
        BasicText(text = "padding3D back 20dp front 20dp", color = { Color.Yellow })
    }
} 
   //sampleEnd
}
```