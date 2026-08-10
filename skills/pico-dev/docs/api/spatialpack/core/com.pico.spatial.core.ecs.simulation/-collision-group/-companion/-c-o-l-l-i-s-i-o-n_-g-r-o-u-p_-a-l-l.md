# COLLISION_GROUP_ALL | PICO Spatial SDK

core / com.pico.spatial.core.ecs.simulation / CollisionGroup / Companion / COLLISION_GROUP_ALL 
# COLLISION_GROUP_ALL
```kotlin
const val COLLISION_GROUP_ALL: UInt
```
The collision group that represents all 32 categories (0xFFFFFFFF). 
When used as a group, it means the entity belongs to all categories. When used as a mask, it ensures interaction with any entity that has at least one bit set in its group, satisfying the  (Mask AND Group) != 0  logic.