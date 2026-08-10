# windowConstraints | PICO Spatial SDK

ui:platform / com.pico.spatial.ui.platform.resize / WindowContainerConstraintsScope / windowConstraints 
# windowConstraints
```kotlin
abstract fun Modifier.windowConstraints(minWidth: Dp = Dp.Hairline, minHeight: Dp = Dp.Hairline, maxWidth: Dp = Dp.Infinity, maxHeight: Dp = Dp.Infinity, minDepth: Dp = Dp.Hairline, maxDepth: Dp = Dp.Infinity): Modifier
```
This constraint not only constrains the window, but also constrains the content. When constraining the content, it is equivalent to  Modifier.sizeIn , and it can only take effect when used by the first child node under the root node. It Constrain the width of the content to be between  minWidth dp and  maxWidth dp and the height of the content to be between  minHeight dp and  maxHeight dp and the depth of the content to be between  minDepth dp and  maxDepth dp as permitted by the incoming measurement  Constraints . If the incoming constraints are more restrictive the requested size will obey the incoming constraints and attempt to be as close as possible to the preferred size. 
#### Return
The  Modifier  that applies the resize constraints to the content and WindowContainer. 
#### Parameters
min Width 
The minimum width of the content. 
min Height 
The minimum height of the content. 
max Width 
The maximum width of the content. 
max Height 
The maximum height of the content. 
min Depth 
The minimum depth of the content. 
max Depth 
The maximum depth of the content. 
#### Samples
```
import androidx.compose.foundation.layout.Box
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp
import com.pico.spatial.ui.foundation.dsl.SpatialAppScope
import com.pico.spatial.ui.foundation.dsl.WindowContainer
import com.pico.spatial.ui.platform.resize.ContainerResizeType

fun main() { 
   //sampleStart 
   WindowContainer(id = "ResizeSample", resizeType = ContainerResizeType.ContentSize) {
    Box(
        modifier =
            Modifier.windowConstraints(
                minWidth = 500.dp,
                minHeight = 500.dp,
                minDepth = 500.dp,
                maxWidth = 1500.dp,
                maxHeight = 1500.dp,
                maxDepth = 1500.dp,
            )
    ) {}
} 
   //sampleEnd
}
```
```kotlin
abstract fun Modifier.windowConstraints(width: Dp, height: Dp, depth: Dp = Dp.Unspecified): Modifier
```
Constraint the width, height, and depth of the window to be equal to the maximum and minimum values. When the  ContainerResizeType  is CONTENT_SIZE, you can directly control the size of the WindowContainer 
#### Return
the  Modifier  that applies the resize constraints to the content and WindowContainer. 
#### Parameters
width 
The width of the content. 
height 
The height of the content. 
depth 
The depth of the content. 
#### Samples
```
import androidx.compose.foundation.layout.Box
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp
import com.pico.spatial.ui.foundation.dsl.SpatialAppScope
import com.pico.spatial.ui.foundation.dsl.WindowContainer
import com.pico.spatial.ui.platform.resize.ContainerResizeType

fun main() { 
   //sampleStart 
   WindowContainer(id = "ResizeSample", resizeType = ContainerResizeType.ContentSize) {
    Box(
        modifier = Modifier.windowConstraints(width = 500.dp, height = 700.dp, depth = 300.dp)
    ) {}
} 
   //sampleEnd
}
```