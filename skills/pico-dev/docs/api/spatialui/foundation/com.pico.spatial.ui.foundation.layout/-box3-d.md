# Box3D | PICO Spatial SDK

ui:foundation / com.pico.spatial.ui.foundation.layout / Box3D 
# Box3D
```kotlin
@Composable
```fun  Box3D ( modifier :  Modifier  =  Modifier ,  depthAlignment :  DepthAlignment  =  DepthAlignment.DepthCenter ,  propagateMinConstraints :  Boolean  =  false ,  content :  @ Composable Box3DScope . ( )  ->  Unit ) 
A layout composable that arranges its children in a 3D space. The  Box3D  will size itself to fit the content, subject to the incoming constraints. For the alignments of the children layouts in the xy plane, you need to use the  Box3DScope.align  modifier. By default, the content will be measured without the  Box3D 's incoming min constraints, unless  propagateMinConstraints  is  true . As an example, setting  propagateMinConstraints  to  true  can be useful when the  Box3D  has content on which modifiers cannot be specified directly and setting a min size on the content of the  Box3D  is needed. If  propagateMinConstraints  is set to  true , the min size set on the  Box3D  will also be applied to the content, whereas otherwise the min size will only apply to the  Box3D . When the content has more than one layout child, the layout children will be stacked one on top of the other (positioned as explained above) in the composition order. 
#### Parameters
modifier 
the  Modifier  to be applied to this layout 
depth Alignment 
the depth alignment of the children within the layout 
propagate Min Constraints 
whether to propagate min constraints to the children 
content 
the content of the layout 
#### Samples
```
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.size
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp
import com.pico.spatial.ui.foundation.layout.Box3D
import com.pico.spatial.ui.foundation.layout.DepthAlignment
import com.pico.spatial.ui.foundation.layout.depth

fun main() { 
   //sampleStart 
   Box3D(depthAlignment = DepthAlignment.DepthCenter) {
    repeat(3) { Box(modifier = Modifier.size(20.dp).depth(20.dp)) }
} 
   //sampleEnd
}
```