# enableSpatialHittestProvider | PICO Spatial SDK

ui:foundation / com.pico.spatial.ui.foundation.spatialhittest / enableSpatialHittestProvider 
# enableSpatialHittestProvider
```kotlin
fun Modifier.enableSpatialHittestProvider(enable: Boolean = true): Modifier
```
Declares the spatial hittest intent for the descendant subtree, to be picked up by the nearest ancestor  SpatialPropertyConsumerNode  that registers  SpatialHittestProviderNode.TraverseKey  (e.g.  Modifier.spaceAnchorConsumer()  or  Modifier.backgroundMaterial() ). 
## Behavior
- 
This modifier does  not  create an independent graphics layer by itself; it only contributes a property that the ancestor consumer reads during measure/layout. 
- 
When  enable  changes, the ancestor consumer is notified and re-measured automatically. 
- 
When multiple  enableSpatialHittestProvider  modifiers nest in the same subtree, the one closest to the ancestor consumer wins (default  overrideDescendants == true ). 
- 
If no matching consumer exists in the ancestor chain, this modifier has no visual effect. 
## Example

```
Box(    Modifier        .spaceAnchorConsumer()        .size(200.dp)) {    Box(        Modifier            .enableSpatialHittestProvider(enable = true)            .fillMaxSize()    )}
```
#### Return
The chained  Modifier . 
#### Parameters
enable 
true  to opt the subtree into spatial hittest;  false  to opt out. Default  true .