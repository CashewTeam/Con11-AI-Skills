# spatialHoverEffectGroup | PICO Spatial SDK

ui:foundation / com.pico.spatial.ui.foundation.hover / spatialHoverEffectGroup 
# spatialHoverEffectGroup
```kotlin
fun Modifier.spatialHoverEffectGroup(group: SpatialHoverEffectGroup, enable: Boolean = true): Modifier
```
Adds a HoverEffectGroup to all effects defined on descendant views, and activates the group whenever this view or any descendant views are hovered. 
#### Return
Modifier  with spatialHoverEffectGroup 
#### Parameters
group 
The spatial hover effect group to associate with this view hierarchy. 
enable 
Controls whether the current view's group ID association is active 
Important note about  enable  parameter behavior: 
- 
When set to  false ,  only disables the group specifically set on this view . 
- 
Has no effect on groups inherited from parent views in the hierarchy. 
- 
Use this to opt-out of a group association at the current view level only. 
Example: 

```
// This disables ONLY the group set at this levelval myGroup = SpatialHoverEffectGroup.obtain()Button(    modifier = Modifier        .spatialHoverEffectGroup(group = myGroup, enable = false),    onClick = {}) {}// This does NOT disable inherited groups from parent viewsval groupFromParent = SpatialHoverEffectGroup.obtain()Box(modifier = Modifier        .spatialHoverEffectGroup(group = groupFromParent)) {    Button(        modifier = Modifier            .spatialHoverEffectGroup(group = groupFromParent, enable = false),        onClick = {}    ) {}}
```
```kotlin
fun Modifier.spatialHoverEffectGroup(): Modifier
```
Adds a default HoverEffectGroup to all effects defined on descendant views, and activates the group whenever this view or any descendant views are hovered. 
Important behavior: 
- 
Each view that calls this function will receive a  unique group 
- 
Different views calling this function will not share the same hover effect group 
- 
This provides isolated hover effects per view without requiring explicit group management 
Example: 

```
// Two buttons using separate groups by defaultColumn {    Button(        modifier = Modifier.spatialHoverEffectGroup(),        onClick = { /* action1 */}    )    Button(        modifier = Modifier.spatialHoverEffectGroup(),        onClick = { /* action2 */}    )}
```
In this example, hovering over each button triggers only its own hover effect. 
#### Return
Modifier  with spatialHoverEffectGroup