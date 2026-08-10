# Subwindow | PICO Spatial SDK

ui:design / com.pico.spatial.ui.design.windows / Subwindow 
# Subwindow
```kotlin
@Composable
```fun  Subwindow ( rotation3D :  Rotation3D ?  =  null ,  followViewpoints :  Set < ViewPoint >  =  ViewPoint.All ,  placement :  SubwindowPlacement  =  SubwindowPlacement.Default ,  offset :  DpOffset3D  =  getGap(getLayoutDirection(placement)) ,  focusable :  Boolean  =  true ,  content :  @ Composable BoxScope . ( )  ->  Unit ) 
Subwindow is a component shown at left or right side of the window container. and it's height always fill the height of the window container. 
#### Parameters
rotation3D 
The rotation of the subwindow. the  Rotation3D.pivot 'z will be ignored 
follow Viewpoints 
The  ViewPoint s that the subwindow will follow. 
placement 
Determines the placement of the subwindow. see  SubwindowPlacement 
offset 
The offset of the subwindow. 
focusable 
Whether the subwindow is focusable. When an  Subwindow  is not focusable, it can not receive input events, such as text input and accessibility events. 
content 
The content of the subwindow. 
#### Samples
```
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Modifier
import androidx.compose.ui.platform.LocalLayoutDirection
import androidx.compose.ui.unit.LayoutDirection
import com.pico.spatial.ui.design.Text
import com.pico.spatial.ui.design.TextField
import com.pico.spatial.ui.design.windows.Subwindow
import com.pico.spatial.ui.foundation.geometry.NormalizedPoint3D
import com.pico.spatial.ui.foundation.geometry.Rotation3D
import com.pico.spatial.ui.foundation.geometry.RotationAxis3D

fun main() { 
   //sampleStart 
   // a message list alongside the main window with a little rotation
val axis =
    when (LocalLayoutDirection.current) {
        LayoutDirection.Ltr -> -RotationAxis3D.Y
        LayoutDirection.Rtl -> RotationAxis3D.Y
    }

val pivot =
    when (LocalLayoutDirection.current) {
        LayoutDirection.Ltr -> NormalizedPoint3D.Left
        LayoutDirection.Rtl -> NormalizedPoint3D.Right
    }
Subwindow(rotation3D = Rotation3D(degree = 45f, axis, pivot)) {
    LazyColumn(Modifier.fillMaxSize()) {
        item { Headers() }
        items(count = 100) { Text("messageItem-${it}") }
    }
} 
   //sampleEnd
}
```