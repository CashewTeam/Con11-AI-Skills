# animation | PICO Spatial SDK

ui:foundation / com.pico.spatial.ui.foundation.hover / SpatialHoverEffectRootScope / animation 
# animation
```kotlin
abstract fun animation(animation: SpatialHoverAnimation = tween(), block: SpatialHoverEffectScope.() -> Unit)
```
Specify the  animation  for sub-scope effects 
In the following example, activating effects will use FastOutSlowInEasing, deactivating effects will use LinearEasing. 

```
animation(tween(easing = if (isActive) FastOutSlowInEasing else LinearEasing )) {        //effects ...}
```
#### Parameters
animation 
the animation for the  block 
block 
sub-scope of  animation