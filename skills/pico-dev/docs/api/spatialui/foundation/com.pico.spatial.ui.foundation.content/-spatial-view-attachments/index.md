# SpatialViewAttachments | PICO Spatial SDK

ui:foundation / com.pico.spatial.ui.foundation.content / SpatialViewAttachments 
# SpatialViewAttachments
```kotlin
interface SpatialViewAttachments
```
The attachments belong to a  SpatialView 
You can retrieve the attachment entity by the same id that you set in  SpatialView  attachments 
Members 
## Functions
entity 
```kotlin
abstract fun entity(id: Any): Entity?
```
Gets the identified attachment as an entity, if the attachment with that identifier exists.