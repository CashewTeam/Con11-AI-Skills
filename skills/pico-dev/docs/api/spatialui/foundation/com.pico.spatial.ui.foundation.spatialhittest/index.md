# com.pico.spatial.ui.foundation.spatialhittest | PICO Spatial SDK

ui:foundation / com.pico.spatial.ui.foundation.spatialhittest 
# Package-level declarations
Functions 
## Functions
enable Spatial Hittest Provider 
```kotlin
fun Modifier.enableSpatialHittestProvider(enable: Boolean = true): Modifier
```
Declares the spatial hittest intent for the descendant subtree, to be picked up by the nearest ancestor  SpatialPropertyConsumerNode  that registers  SpatialHittestProviderNode.TraverseKey  (e.g.  Modifier.spaceAnchorConsumer()  or  Modifier.backgroundMaterial() ).