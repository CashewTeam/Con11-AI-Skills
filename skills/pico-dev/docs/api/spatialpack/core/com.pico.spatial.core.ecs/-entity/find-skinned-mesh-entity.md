# findSkinnedMeshEntity | PICO Spatial SDK

core / com.pico.spatial.core.ecs / Entity / findSkinnedMeshEntity 
# findSkinnedMeshEntity
```kotlin
@MainThread
```fun  findSkinnedMeshEntity ( includeDisabled :  Boolean  =  false ) :  Array < Entity > 
Finds all entities with a skinned mesh component within this entity and its children. The search traverses the entire entity hierarchy starting from the current entity. 
#### Return
An array of entities containing a skinned mesh component, collected from the entity hierarchy. 
#### Parameters
include Disabled 
Whether to include disabled entities in the search. 
- 
true : returns both enabled and disabled entities with skinned meshes. 
- 
false : returns only enabled entities.