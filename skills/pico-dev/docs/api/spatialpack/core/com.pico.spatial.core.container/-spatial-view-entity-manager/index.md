# SpatialViewEntityManager | PICO Spatial SDK

core / com.pico.spatial.core.container / SpatialViewEntityManager 
# SpatialViewEntityManager
```kotlin
interface SpatialViewEntityManager
```
Interface to define content of  SpatialView  and operations about the content. 
#### Inheritors
SpatialViewContent Members 
## Properties
entities 
```kotlin
abstract val entities: SpatialViewEntityCollection
```
The  SpatialViewEntityCollection  that contains and manages all the  Entity  instances in current SpatialView. 
## Functions
add Entity 
```kotlin
abstract fun addEntity(entity: Entity)
```
Add  Entity  to this content. 
remove Entity 
```kotlin
abstract fun removeEntity(entity: Entity)
```
Remove  Entity  from this content, if present.