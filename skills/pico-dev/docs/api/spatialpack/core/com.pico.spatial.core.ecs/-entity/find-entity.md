# findEntity | PICO Spatial SDK

core / com.pico.spatial.core.ecs / Entity / findEntity 
# findEntity
```kotlin
@MainThread
```fun  findEntity ( name :  String ) :  Entity ? 
Searches for an entity by its name within the entire depth of its tree structure, including the entity itself. If there are multiple entities with the same name, only the first matching entity encountered will be returned. 
#### Return
The first entity with the specified name if found, or null if no such entity exists. 
#### Parameters
name 
The name of the entity to search for.