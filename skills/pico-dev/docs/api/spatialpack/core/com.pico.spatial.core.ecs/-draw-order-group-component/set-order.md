# setOrder | PICO Spatial SDK

core / com.pico.spatial.core.ecs / DrawOrderGroupComponent / setOrder 
# setOrder
```kotlin
fun setOrder(drawOrderGroup: DrawOrderGroup, order: Int)
```
Sets the drawing group and sorting priority for the entity's visual components. 
By calling this method, the entity is assigned to a specific  DrawOrderGroup , and its rendering sequence within that group is determined by the provided  order . This ensures that the entity's model and particle components are layered correctly relative to other entities within the same group. 
This is the primary mechanism for resolving depth-sorting issues and managing complex rendering hierarchies. 
#### Parameters
draw Order Group 
The identifier used to categorize the entity for rendering management. 
order 
The rendering order index. Typically, components with higher values are rendered on top of those with lower values.