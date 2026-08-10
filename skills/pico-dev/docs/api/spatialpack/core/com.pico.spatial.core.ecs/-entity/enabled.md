# enabled | PICO Spatial SDK

core / com.pico.spatial.core.ecs / Entity / enabled 
# enabled
```kotlin
@get:JvmName(name = "isEnabled")
```@get: MainThread @set: MainThread var  enabled :  Boolean 
Gets or sets the current entity's enabled state. The default enabled state is  true . 
If the entity itself is enabled but its parent is disabled, this property returns  false . When an entity is disabled, it is not rendered and will not be visible in the  Scene , but it will still remain in  EntityQueryCondition .