# WindowContainerConstraintsScope | PICO Spatial SDK

ui:platform / com.pico.spatial.ui.platform.resize / WindowContainerConstraintsScope 
# WindowContainerConstraintsScope
```kotlin
interface WindowContainerConstraintsScope
```
Interface representing the scope of constraints for the WindowContainer. 
#### Inheritors
WindowContainerScope Members 
## Functions
window Constraints 
```kotlin
abstract fun Modifier.windowConstraints(width: Dp, height: Dp, depth: Dp = Dp.Unspecified): Modifier
```
Constraint the width, height, and depth of the window to be equal to the maximum and minimum values. When the  ContainerResizeType  is CONTENT_SIZE, you can directly control the size of the WindowContainer 
```kotlin
abstract fun Modifier.windowConstraints(minWidth: Dp = Dp.Hairline, minHeight: Dp = Dp.Hairline, maxWidth: Dp = Dp.Infinity, maxHeight: Dp = Dp.Infinity, minDepth: Dp = Dp.Hairline, maxDepth: Dp = Dp.Infinity): Modifier
```
This constraint not only constrains the window, but also constrains the content. When constraining the content, it is equivalent to  Modifier.sizeIn , and it can only take effect when used by the first child node under the root node. It Constrain the width of the content to be between  minWidth dp and  maxWidth dp and the height of the content to be between  minHeight dp and  maxHeight dp and the depth of the content to be between  minDepth dp and  maxDepth dp as permitted by the incoming measurement  Constraints . If the incoming constraints are more restrictive the requested size will obey the incoming constraints and attempt to be as close as possible to the preferred size.