# distanceBias | PICO Spatial SDK

core / com.pico.spatial.core.ecs / SortAsUIElementComponent / distanceBias 
# distanceBias
```kotlin
var distanceBias: Float
```
A bias (in meters) applied to the view-independent reference distance used for sorting. 
A positive value increases the sort order (rendered later, on top); a negative value decreases it (rendered earlier, behind). This value only affects sorting and does not change the entity's spatial position.