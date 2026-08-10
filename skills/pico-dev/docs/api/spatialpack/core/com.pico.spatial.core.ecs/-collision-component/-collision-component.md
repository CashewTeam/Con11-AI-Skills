# CollisionComponent | PICO Spatial SDK

core / com.pico.spatial.core.ecs / CollisionComponent / CollisionComponent 
# CollisionComponent
```kotlin
constructor(collisionShape: List<ShapeResource>, physicsMaterial: PhysicsMaterialResource, collisionResponseMode: CollisionResponseMode = COLLIDER_FULL, collisionFilter: CollisionFilter = CollisionFilter.COLLISION_FILTER_DEFAULT, collisionInfoDetailLevel: CollisionInfoDetailLevel = CollisionInfoDetailLevel.BRIEF)
```
Creates a new  CollisionComponent  instance. 
#### Parameters
collision Shape 
A list of  ShapeResource  objects representing the shapes used for collision detection. 
physics Material 
The physics material properties used for physics simulation. 
collision Response Mode 
The collision response mode that determines how the component interacts with other objects. Default value is  CollisionResponseMode.COLLIDER_FULL . 
collision Filter 
The filter settings to define which objects this component can collide with. Default value is  CollisionFilter.COLLISION_FILTER_DEFAULT . 
collision Info Detail Level 
The options for collision reporting, specifying how collisions are reported or handled. Default value is  CollisionInfoDetailLevel.BRIEF .