# Augment | PICO Spatial SDK

ui:foundation / com.pico.spatial.ui.foundation.window / Augment 
# Augment
```kotlin
@Composable
```fun  Augment ( anchor :  NormalizedPoint3D ,  alignment :  AugmentContentAlignment ,  offset :  IntOffset3D ,  rotation3D :  Rotation3D ?  =  null ,  followViewpoints :  Set < ViewPoint >  =  ViewPoint.All ,  cornerRadius :  Dp  =  AugmentDefaults.defaultCornerRadius ,  enableMaterialBackground :  Boolean  =  true ,  focusable :  Boolean  =  true ,  windowSizeBehaviors :  WindowSizeBehaviors  =  WindowSizeBehaviors.Adaptive ,  content :  @ Composable ( )  ->  Unit ) 
A Augment is a container that can be placed around the main window. 
#### Parameters
anchor 
The anchor point, which is a normalized point relative to the top-left corner of the WindowContainer. (0,0,0) refers to the top-left-back corner, and (1,1,1) refers to the bottom-right-front corner. 
alignment 
A normalized 2D point, representing a point relative to the Augment itself, which will be aligned with the anchor. 
offset 
The absolute offset will be applied after anchor and alignment. 
rotation3D 
The rotation of the Augment relative to itself. 
follow Viewpoints 
The viewpoints to follow. By default, it is empty, which means that the Augment will not follow any viewpoints. (Equivalent to only following Front) 
corner Radius 
The corner radius of the Augment. 
enable Material Background 
Whether to enable the material background. 
focusable 
Whether the Augment is focusable. When an  Augment  is not focusable, it can not receive input events, such as text input and accessibility events. 
window Size Behaviors 
The window size behaviors. By default, it is  WindowSizeBehaviors.Adaptive . If it is  WindowSizeBehaviors.MatchContainerWidth , the Augment and content will match the container width, and height is adaptive to the content. If it is  WindowSizeBehaviors.MatchContainerHeight , the Augment and content will match the container height, and width is adaptive to the content. 
content 
The content of the Augment. 
#### Samples
```
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.width
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.platform.LocalDensity
import androidx.compose.ui.platform.LocalWindowInfo
import androidx.compose.ui.unit.dp
import com.pico.spatial.ui.foundation.geometry.NormalizedPoint3D
import com.pico.spatial.ui.foundation.window.Augment
import com.pico.spatial.ui.foundation.window.AugmentContentAlignment

fun main() { 
   //sampleStart 
   // A floating title bar above the window
Augment(anchor = NormalizedPoint3D.TopFront, alignment = AugmentContentAlignment.BottomCenter) {
    val containerWidth =
        with(LocalDensity.current) { LocalWindowInfo.current.containerSize.width.toDp() }
    Row(Modifier.width(containerWidth).height(64.dp)) {
        // some buttons
    }
} 
   //sampleEnd
}
```
```kotlin
@Composable
```fun  Augment ( anchor :  NormalizedPoint3D ,  alignment :  AugmentContentAlignment ,  offset :  DpOffset3D  =  DpOffset3D.Zero ,  rotation3D :  Rotation3D ?  =  null ,  followViewpoints :  Set < ViewPoint >  =  ViewPoint.All ,  cornerRadius :  Dp  =  AugmentDefaults.defaultCornerRadius ,  enableMaterialBackground :  Boolean  =  true ,  focusable :  Boolean  =  true ,  windowSizeBehaviors :  WindowSizeBehaviors  =  WindowSizeBehaviors.Adaptive ,  content :  @ Composable ( )  ->  Unit ) 
A Augment is a container that can be placed around the main window. 
#### Parameters
anchor 
The anchor point, which is a normalized point relative to the top-left corner of the WindowContainer. (0,0,0) refers to the top-left-back corner, and (1,1,1) refers to the bottom-right-front corner. 
alignment 
A normalized 2D point, representing a point relative to the Augment itself, which will be aligned with the anchor. 
offset 
The absolute offset will be applied after anchor and alignment. 
rotation3D 
The rotation of the subwindow. the  Rotation3D.pivot 'z will be ignored 
follow Viewpoints 
The viewpoints to follow.Default is  ViewPoint.All . 
corner Radius 
The corner radius of the Augment. 
enable Material Background 
Whether to enable the material background. 
focusable 
Whether the Augment is focusable. When an  Augment  is not focusable, it can receive input events, such as text input and accessibility events. 
window Size Behaviors 
The window size behaviors. By default, it is  WindowSizeBehaviors.Adaptive . If it is  WindowSizeBehaviors.MatchContainerWidth , the Augment and content will match the container width, and height is adaptive to the content. If it is  WindowSizeBehaviors.MatchContainerHeight , the Augment and content will match the container height, and width is adaptive to the content. 
content 
The content of the Augment. 
#### Samples
```
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.width
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.platform.LocalDensity
import androidx.compose.ui.platform.LocalWindowInfo
import androidx.compose.ui.unit.dp
import com.pico.spatial.ui.foundation.geometry.NormalizedPoint3D
import com.pico.spatial.ui.foundation.window.Augment
import com.pico.spatial.ui.foundation.window.AugmentContentAlignment

fun main() { 
   //sampleStart 
   // A floating title bar above the window
Augment(anchor = NormalizedPoint3D.TopFront, alignment = AugmentContentAlignment.BottomCenter) {
    val containerWidth =
        with(LocalDensity.current) { LocalWindowInfo.current.containerSize.width.toDp() }
    Row(Modifier.width(containerWidth).height(64.dp)) {
        // some buttons
    }
} 
   //sampleEnd
}
```